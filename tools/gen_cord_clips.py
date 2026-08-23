#!/usr/bin/env python3
"""Cord staples: a bridge over the cord with barbed legs into the panel.

This replaces an earlier two-piece C-clip design, which was worse in every way.
A C-clip has to hold the cord in FRONT of the plate while the posts point INTO
the panel, so the features land on opposite faces and no single part can print
flat. A staple puts the legs and the cord on the same side, so it is one piece,
prints bridge-down with the legs up, and needs neither supports nor glue.

It also removes the snap-strain problem entirely. A C-clip's arms must spread by
about an eighth of the cord diameter to let it in, and since arm length scales
with the cord while wall thickness does not, small clips are the ones that break:
a 6 mm C-clip with a 1.5 mm wall runs well past PLA yield. A staple flexes
nothing. You lay the cord on the panel and push the staple down over it.

The standoff is set by a shoulder that is wider than the panel hole, so it bottoms
on the panel face and the gap under the bridge is exactly what was designed rather
than however far it happened to be pushed.

Two legs is enough. Unlike the strip studs, which sit in SLOTS and are therefore
sliders free to travel, these are octagonal posts in square holes: each one
constrains rotation on its own, so two of them do not form a hinge.

Everything prints flat, no supports, no glue.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_gauges import _quad, _rect, round_frustum, write_stl           # noqa: E402
from gen_strip_mount import PANEL_T, PITCH, barbed_post                # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "models" / "cord_clips"

BRIDGE_T = 2.0          # bridge thickness
SHOULDER = 3.6          # standoff section, wider than the 2.929 hole so it stops there
POST_W   = 2.6          # octagonal post across flats, into the panel


def prism4(quad, z0, z1):
    """Closed solid from an arbitrary planar quad extruded in z. Needed because a
    U is not convex, so it cannot be one fan-triangulated cap; building it from
    angular segments keeps every primitive a closed solid."""
    A = [(x, y, z0) for x, y in quad]
    B = [(x, y, z1) for x, y in quad]
    cx = sum(p[0] for p in quad)/4
    cy = sum(p[1] for p in quad)/4
    tris = _quad(*A, (0, 0, -1)) + _quad(*B, (0, 0, 1))
    for k in range(4):
        m = (k+1) % 4
        mid = ((A[k][0]+A[m][0])/2 - cx, (A[k][1]+A[m][1])/2 - cy, 0)
        tris += _quad(A[k], A[m], B[m], B[k], mid)
    return tris


def octa(cx, cy, z0, z1, w0, w1=None):
    w1 = w0 if w1 is None else w1
    k = 1/(2*math.cos(math.pi/8))
    return round_frustum(cx, cy, z0, z1, w0*k, w1*k, 8, math.pi/8)


def cord_staple(cord_d, span_pitches=None, width=6.0, clearance=0.3):
    """One staple sized for `cord_d`.

    `span_pitches` is the leg spacing in panel pitches, so the legs always land
    on real holes. Chosen automatically as the smallest that leaves the cord room
    between the legs.
    """
    if span_pitches is None:
        span_pitches = 2
        while span_pitches*PITCH - SHOULDER < cord_d + 1.0:
            span_pitches += 1
    span = span_pitches * PITCH
    gap = span - SHOULDER
    standoff = cord_d + clearance

    x0, x1 = 0.0, span
    ov = SHOULDER/2 + 1.0
    tris = _rect(x0-ov, -width/2, 0.0, x1+ov, width/2, BRIDGE_T)

    z_sh = BRIDGE_T + standoff
    for cx in (x0, x1):
        # standoff shoulder: wider than the hole, so it bottoms on the panel face
        tris += octa(cx, 0.0, BRIDGE_T-0.01, z_sh, SHOULDER)
        # short lead from the shoulder down to post size, then the barbed post
        tris += octa(cx, 0.0, z_sh-0.01, z_sh+0.6, SHOULDER, POST_W)
        tris += barbed_post(cx, 0.0, z_sh+0.6)
    total = z_sh + 0.6 + PANEL_T + 3*0.6 + 1.0
    return tris, (x1-x0+2*ov, width, total, span_pitches, gap, standoff)



# ---------------------------------------------------------------- U-cradle

def prism4_y(quad_xz, y0, y1):
    """Closed solid from a quad given in (x, z), extruded along Y.

    prism4 takes an (x, y) profile and extrudes in Z; feeding it an (x, z)
    profile silently builds the part lying on its side, which is exactly the bug
    that produced a cradle 3 mm below the bed and 7 mm wide in the wrong axis.
    """
    A = [(x, y0, z) for x, z in quad_xz]
    B = [(x, y1, z) for x, z in quad_xz]
    cx = sum(p[0] for p in quad_xz)/4
    cz = sum(p[1] for p in quad_xz)/4
    tris = _quad(*A, (0, -1, 0)) + _quad(*B, (0, 1, 0))
    for k in range(4):
        m = (k+1) % 4
        mid = ((A[k][0]+A[m][0])/2 - cx, 0, (A[k][2]+A[m][2])/2 - cz)
        tris += _quad(A[k], A[m], B[m], B[k], mid)
    return tris


def octa_h(cx, cz, y0, y1, w, phase=0.0):
    """Octagonal prism along -Y, for a HORIZONTAL leg. `phase` rotates the
    section; 0 puts a VERTEX down so the leg self-supports at 45 degrees when
    printed lying on its side. An octagon's fit is set by its inscribed circle,
    which does not change with rotation, so the hole fit is unaffected."""
    k = 1/(2*math.cos(math.pi/8))
    r = w*k
    n = 8
    pts = [(cx + r*math.cos(2*math.pi*i/n + phase),
            cz + r*math.sin(2*math.pi*i/n + phase)) for i in range(n)]
    tris = []
    for i in range(1, n-1):
        tris += _tri3((pts[0][0], y0, pts[0][1]), (pts[i][0], y0, pts[i][1]),
                      (pts[i+1][0], y0, pts[i+1][1]), (0, -1, 0))
        tris += _tri3((pts[0][0], y1, pts[0][1]), (pts[i][0], y1, pts[i][1]),
                      (pts[i+1][0], y1, pts[i+1][1]), (0, 1, 0))
    for i in range(n):
        j = (i+1) % n
        mid = ((pts[i][0]+pts[j][0])/2 - cx, 0, (pts[i][1]+pts[j][1])/2 - cz)
        tris += _quad((pts[i][0], y0, pts[i][1]), (pts[j][0], y0, pts[j][1]),
                      (pts[j][0], y1, pts[j][1]), (pts[i][0], y1, pts[i][1]), mid)
    return tris


def _tri3(v0, v1, v2, outward):
    ax, ay, az = (v1[0]-v0[0], v1[1]-v0[1], v1[2]-v0[2])
    bx, by, bz = (v2[0]-v0[0], v2[1]-v0[1], v2[2]-v0[2])
    nn = (ay*bz-az*by, az*bx-ax*bz, ax*by-ay*bx)
    if sum(a*b for a, b in zip(nn, outward)) < 0:
        v1, v2 = v2, v1
        ax, ay, az = (v1[0]-v0[0], v1[1]-v0[1], v1[2]-v0[2])
        bx, by, bz = (v2[0]-v0[0], v2[1]-v0[1], v2[2]-v0[2])
        nn = (ay*bz-az*by, az*bx-ax*bz, ax*by-ay*bx)
    L = max((nn[0]**2+nn[1]**2+nn[2]**2) ** 0.5, 1e-12)
    return [((nn[0]/L, nn[1]/L, nn[2]/L), v0, v1, v2)]


def cord_cradle(cord_d, width=6.0, wall=2.0, span_pitches=3, rows_pitch=1,
                pad_t=2.6, seg=6.0, curl=22.0):
    """Open-top cradle: lay the cord in, lift it out, mount stays put.

    Prints cradle-up. The flat bottom gives it real first-layer area instead of
    balancing on an arc, and the legs are horizontal octagons rotated so a vertex
    points down, which self-supports at 45 degrees and needs no support material.

    Four legs in two rows, because the cord's weight acts on a lever arm out from
    the panel and a single row would let the cradle rock. Two rows react that as
    a couple.
    """
    ri = (cord_d + 0.6)/2
    ro = ri + wall
    flat = ro*0.55                      # half-width of the flat on the bottom
    zc = ro                             # cradle centre height above the bed
    # cradle profile: sweep the closed part, clamping the bottom flat
    tris = []
    # sweep past the horizontal by `curl` so the arms rise above the cord's
    # centreline and it cannot roll out. Staying under 45 degrees of inward lean
    # keeps every layer self-supporting, so this costs nothing to print.
    sweep = 180 + 2*curl
    n = max(12, int(sweep/seg))
    for k in range(n):
        t0 = math.radians(180 - curl + sweep*k/n)
        t1 = math.radians(180 - curl + sweep*(k+1)/n)
        def pt(r, t):
            x, z = r*math.cos(t), r*math.sin(t)
            return (x, max(z, -zc + (0.0 if abs(x) > flat else 0.0)))
        def clamp(r, t, floor):
            x, z = r*math.cos(t), r*math.sin(t)
            return (x, max(z, floor))
        qi0 = clamp(ri, t0, -ri*0.72); qi1 = clamp(ri, t1, -ri*0.72)
        qo0 = clamp(ro, t0, -ro);      qo1 = clamp(ro, t1, -ro)
        quad = [(qi0[0], qi0[1]+zc), (qo0[0], qo0[1]+zc),
                (qo1[0], qo1[1]+zc), (qi1[0], qi1[1]+zc)]
        if abs(quad[0][0]-quad[3][0]) < 1e-9 and abs(quad[1][0]-quad[2][0]) < 1e-9:
            continue
        tris += prism4_y(quad, -width/2, width/2)
    # back pad, standing in the XZ plane behind the cradle
    span = span_pitches*PITCH
    rows = rows_pitch*PITCH
    pw = span + 7.0
    ph = rows + 9.0
    y0 = -width/2 - pad_t
    tris += _rect(-pw/2, y0, 0.0, pw/2, -width/2 + 0.01, ph)
    # four legs, horizontal, vertex down, into the panel
    zc0 = (ph - rows)/2
    for dx in (-span/2, span/2):
        for dz in (0.0, rows):
            tris += octa_h(dx, zc0+dz, y0 - (PANEL_T + 3*0.6 + 1.0), y0 + 0.01, POST_W)
    return tris, (pw, ph, ro*2, width)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"{'file':26s} {'legs':>5} {'gap':>7} {'standoff':>9} {'size mm':>18}")
    for d in (4, 6, 8, 10, 13):
        tris, (L, W, H, sp, gap, so) = cord_staple(d)
        f = OUT / f"cord_staple_{d:02d}mm.stl"
        write_stl(f, tris, f"cord staple {d}mm: {sp} pitch legs, {so:.1f} standoff".encode())
        print(f"{f.name:26s} {sp:5d} {gap:7.2f} {so:9.2f} "
              f"{L:6.1f} x {W:.1f} x {H:.1f}")
    print()
    for d in (6, 10, 13):
        tris, (pw, ph, od, w) = cord_cradle(d)
        f = OUT / f"cord_cradle_{d:02d}mm.stl"
        write_stl(f, tris, f"cord cradle {d}mm open top, 4 legs".encode())
        print(f"{f.name:26s} pad {pw:.1f} x {ph:.1f}, cradle OD {od:.1f}, width {w:.0f}")
