#!/usr/bin/env python3
"""Generate test-fit gauges for the perforated enclosure panel.

Two unknowns have to be separated:
  * hole pitch, measured at 3/16 in (4.7625 mm) from the second, flatter photo
  * hole size,  bracketed by test print at 2.6 to 2.8 mm

peg_size_gauge  isolates hole size: one peg per tab, five widths, insert one at a time.
pitch_gauge_*   isolates pitch: a 4x4 grid of deliberately undersized pegs, so only the
                pitch can bind. Errors accumulate across the grid, which is the point:
                over three spans a pitch error of d shows up as 3d at the far corner.

Geometry is emitted as a union of closed solids. Overlapping closed volumes are resolved
by the slicer at slice time, and because every primitive is individually watertight the
whole file stays manifold (every edge used exactly twice).

Everything prints flat on the bed, pegs up, no supports.
"""
import struct
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "models" / "test_gauges"

# ---------------------------------------------------------------- primitives

def _quad(v0, v1, v2, v3, outward):
    """Two triangles for a quad, wound so the normal points along `outward`."""
    ax, ay, az = (v1[0]-v0[0], v1[1]-v0[1], v1[2]-v0[2])
    bx, by, bz = (v2[0]-v0[0], v2[1]-v0[1], v2[2]-v0[2])
    n = (ay*bz-az*by, az*bx-ax*bz, ax*by-ay*bx)
    if sum(a*b for a, b in zip(n, outward)) < 0:
        v0, v1, v2, v3 = v3, v2, v1, v0
        ax, ay, az = (v1[0]-v0[0], v1[1]-v0[1], v1[2]-v0[2])
        bx, by, bz = (v2[0]-v0[0], v2[1]-v0[1], v2[2]-v0[2])
        n = (ay*bz-az*by, az*bx-ax*bz, ax*by-ay*bx)
    L = max((n[0]**2+n[1]**2+n[2]**2) ** 0.5, 1e-12)
    n = (n[0]/L, n[1]/L, n[2]/L)
    return [(n, v0, v1, v2), (n, v0, v2, v3)]


def frustum(cx, cy, z0, z1, s0, s1):
    """Square frustum: half-size s0 at z0 tapering to s1 at z1. s0 == s1 gives a box."""
    b = [(cx-s0, cy-s0, z0), (cx+s0, cy-s0, z0), (cx+s0, cy+s0, z0), (cx-s0, cy+s0, z0)]
    t = [(cx-s1, cy-s1, z1), (cx+s1, cy-s1, z1), (cx+s1, cy+s1, z1), (cx-s1, cy+s1, z1)]
    tris = []
    tris += _quad(*b, (0, 0, -1))
    tris += _quad(*t, (0, 0, 1))
    for i in range(4):
        j = (i+1) % 4
        mid = ((b[i][0]+b[j][0])/2 - cx, (b[i][1]+b[j][1])/2 - cy, 0)
        tris += _quad(b[i], b[j], t[j], t[i], mid)
    return tris


def box(x0, y0, z0, x1, y1, z1):
    return frustum((x0+x1)/2, (y0+y1)/2, z0, z1, (x1-x0)/2, (y1-y0)/2) \
        if abs((x1-x0)-(y1-y0)) < 1e-9 else _rect(x0, y0, z0, x1, y1, z1)


def _rect(x0, y0, z0, x1, y1, z1):
    b = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)]
    t = [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    tris = []
    tris += _quad(*b, (0, 0, -1))
    tris += _quad(*t, (0, 0, 1))
    cx, cy = (x0+x1)/2, (y0+y1)/2
    for i in range(4):
        j = (i+1) % 4
        mid = ((b[i][0]+b[j][0])/2 - cx, (b[i][1]+b[j][1])/2 - cy, 0)
        tris += _quad(b[i], b[j], t[j], t[i], mid)
    return tris

# ---------------------------------------------------------------- 7-segment text

SEG = {
    "0": "abcdef", "1": "bc", "2": "abged", "3": "abgcd", "4": "fgbc",
    "5": "afgcd", "6": "afgedc", "7": "abc", "8": "abcdefg", "9": "abfgcd",
}
GW, GH, GT = 3.0, 5.0, 0.8          # glyph width, height, stroke
GAP, DOTW = 1.0, 0.9


def glyph_rects(ch, x, y):
    if ch == ".":
        return [(x, y, x+DOTW, y+DOTW)], DOTW
    r = []
    s = SEG[ch]
    if "a" in s: r.append((x,        y+GH-GT,       x+GW,    y+GH))
    if "d" in s: r.append((x,        y,             x+GW,    y+GT))
    if "g" in s: r.append((x,        y+(GH-GT)/2,   x+GW,    y+(GH+GT)/2))
    if "f" in s: r.append((x,        y+GH/2,        x+GT,    y+GH))
    if "b" in s: r.append((x+GW-GT,  y+GH/2,        x+GW,    y+GH))
    if "e" in s: r.append((x,        y,             x+GT,    y+GH/2))
    if "c" in s: r.append((x+GW-GT,  y,             x+GW,    y+GH/2))
    return r, GW


def text_width(s):
    w = 0.0
    for i, ch in enumerate(s):
        w += DOTW if ch == "." else GW
        if i < len(s)-1:
            w += GAP
    return w


def text(s, x, y, z0, z1):
    tris, cx = [], x
    for ch in s:
        rects, w = glyph_rects(ch, cx, y)
        for (a, b, c, d) in rects:
            tris += _rect(a, b, z0, c, d, z1)
        cx += w + GAP
    return tris, cx - x - GAP

# ---------------------------------------------------------------- STL

def write_stl(path, tris, header=b"gauge"):
    with open(path, "wb") as f:
        f.write(header.ljust(80, b" ")[:80])
        f.write(struct.pack("<I", len(tris)))
        for n, a, b, c in tris:
            f.write(struct.pack("<12fH", *n, *a, *b, *c, 0))

# ---------------------------------------------------------------- parts

PLATE_T   = 1.6      # plate thickness
PEG_H     = 3.5      # peg height above the plate
TIP       = 1.0      # tapered lead-in length
LABEL_Z   = 0.6      # embossed text height


SINK = 0.3           # sink pegs/text into the plate so solids overlap, never merely touch
DEBOSS = 0.6         # depth of the label recessed into the bed face


def plate_with_recess(W, Hgt, cuts):
    """Plate 0..PLATE_T, with `cuts` (axis-aligned rects) recessed into the bed face.

    The recessed layer is tiled by subdividing on every cut edge and emitting a box for
    each cell that is not inside a cut. Exact for axis-aligned rectangles, and keeps
    everything a union of closed boxes so the result stays manifold.
    """
    tris = _rect(0, 0, DEBOSS, W, Hgt, PLATE_T)          # main body
    xs = sorted({0.0, W} | {c[0] for c in cuts} | {c[2] for c in cuts})
    ys = sorted({0.0, Hgt} | {c[1] for c in cuts} | {c[3] for c in cuts})
    for i in range(len(xs)-1):
        for j in range(len(ys)-1):
            x0, x1, y0, y1 = xs[i], xs[i+1], ys[j], ys[j+1]
            if x1-x0 < 1e-9 or y1-y0 < 1e-9:
                continue
            mx, my = (x0+x1)/2, (y0+y1)/2
            if any(c[0] < mx < c[2] and c[1] < my < c[3] for c in cuts):
                continue                                  # inside a letter: leave void
            tris += _rect(x0, y0, 0.0, x1, y1, DEBOSS+1e-6)
    return tris


def label_cuts(s, x, y):
    """Digit rects for `s`, mirrored in x about its own centre so the recess reads
    correctly when the part is flipped over and pushed into the panel."""
    rects, cx = [], x
    for ch in s:
        r, w = glyph_rects(ch, cx, y)
        rects += r
        cx += w + GAP
    x0 = min(r[0] for r in rects); x1 = max(r[2] for r in rects)
    return [(x0+x1-r[2], r[1], x0+x1-r[0], r[3]) for r in rects]


def peg(cx, cy, width):
    h = width/2
    t = []
    t += frustum(cx, cy, PLATE_T-SINK, PLATE_T+PEG_H-TIP, h, h)
    t += frustum(cx, cy, PLATE_T+PEG_H-TIP, PLATE_T+PEG_H, h, h*0.68)
    return t


def pitch_gauge(pitch, n=3, peg_w=2.1, label=None):
    span = (n-1)*pitch
    grid_x0, grid_y0 = 3.0, 3.0
    label = label if label is not None else f"{pitch:.2f}"
    lw = text_width(label)
    W = grid_x0 + span + 3.0 + 3.0 + lw + 3.0
    Hgt = max(span + 6.0, GH + 6.0)
    tx = grid_x0 + span + 6.0
    ty = (Hgt-GH)/2
    tris = plate_with_recess(W, Hgt, label_cuts(label, tx, ty))
    cy0 = (Hgt - span)/2
    for i in range(n):
        for j in range(n):
            tris += peg(grid_x0 + i*pitch, cy0 + j*pitch, peg_w)
    t, _ = text(label, tx, ty, PLATE_T-SINK, PLATE_T+LABEL_Z)
    return tris + t, (W, Hgt)


def peg_size_gauge(widths=(2.0, 2.2, 2.4, 2.6, 2.8)):
    tabs, y = [], 0.0
    TW, TH, GAPY = 24.0, 10.0, 3.0
    for w in widths:
        lbl, lx, ly = f"{w:.1f}", 10.0, y+(TH-GH)/2
        sub = plate_with_recess(TW, TH, [(a, b-y, c, d-y) for a, b, c, d in label_cuts(lbl, lx, ly)])
        tabs += [(nn, (ax, ay+y, az), (bx, by+y, bz), (cx_, cy_+y, cz))
                 for nn, (ax, ay, az), (bx, by, bz), (cx_, cy_, cz) in sub]
        tabs += peg(5.0, y+TH/2, w)
        t, _ = text(lbl, lx, ly, PLATE_T-SINK, PLATE_T+LABEL_Z)
        tabs += t
        y += TH + GAPY
    return tabs, (TW, y-GAPY)





# ---------------------------------------------------------------- round studs

import math as _math


def _tri(v0, v1, v2, outward):
    """One triangle wound so its normal points along `outward`."""
    ax, ay, az = (v1[0]-v0[0], v1[1]-v0[1], v1[2]-v0[2])
    bx, by, bz = (v2[0]-v0[0], v2[1]-v0[1], v2[2]-v0[2])
    n = (ay*bz-az*by, az*bx-ax*bz, ax*by-ay*bx)
    if sum(a*b for a, b in zip(n, outward)) < 0:
        v1, v2 = v2, v1
        ax, ay, az = (v1[0]-v0[0], v1[1]-v0[1], v1[2]-v0[2])
        bx, by, bz = (v2[0]-v0[0], v2[1]-v0[1], v2[2]-v0[2])
        n = (ay*bz-az*by, az*bx-ax*bz, ax*by-ay*bx)
    L = max((n[0]**2+n[1]**2+n[2]**2) ** 0.5, 1e-12)
    return [((n[0]/L, n[1]/L, n[2]/L), v0, v1, v2)]


def round_frustum(cx, cy, z0, z1, r0, r1, n=28):
    """Circular frustum as a closed solid. r0 at z0 tapering to r1 at z1.

    Caps are triangle fans from vertex 0; the side wall is quads. Every edge is
    used exactly twice, so the solid is watertight.
    """
    b = [(cx + r0*_math.cos(2*_math.pi*i/n), cy + r0*_math.sin(2*_math.pi*i/n), z0)
         for i in range(n)]
    t = [(cx + r1*_math.cos(2*_math.pi*i/n), cy + r1*_math.sin(2*_math.pi*i/n), z1)
         for i in range(n)]
    tris = []
    for i in range(1, n-1):
        tris += _tri(b[0], b[i], b[i+1], (0, 0, -1))
        tris += _tri(t[0], t[i], t[i+1], (0, 0, 1))
    for i in range(n):
        j = (i+1) % n
        mid = ((b[i][0]+b[j][0])/2 - cx, (b[i][1]+b[j][1])/2 - cy, 0)
        tris += _quad(b[i], b[j], t[j], t[i], mid)
    return tris


def stud(cx, cy, z0, head_d, neck_d, neck_len=4.0, head_t=2.0):
    """A printed 'screw head': neck standing off the plate, then a wider head.

    Hangs a keyhole: the head passes the big hole, the neck slides up the slot,
    and the head traps the wall behind it. Head top is chamfered so it starts
    into the keyhole without fighting.
    """
    t = []
    t += round_frustum(cx, cy, z0-0.3, z0+neck_len, neck_d/2, neck_d/2)
    t += round_frustum(cx, cy, z0+neck_len, z0+neck_len+head_t-0.5, head_d/2, head_d/2)
    t += round_frustum(cx, cy, z0+neck_len+head_t-0.5, z0+neck_len+head_t,
                       head_d/2, head_d/2-0.5)
    return t


def stud_gauge(sizes=((5.4, 2.4), (5.8, 2.6), (6.2, 2.8))):
    """One stud per tab so each can be offered up to a keyhole on its own."""
    out, y = [], 0.0
    TW, TH, GAPY = 34.0, 14.0, 3.0
    for head_d, neck_d in sizes:
        lbl = f"{head_d:.1f}"
        lx, ly = 15.0, y + (TH-GH)/2
        sub = plate_with_recess(TW, TH, [(a, b-y, c, d-y)
                                         for a, b, c, d in label_cuts(lbl, lx, ly)])
        out += [(nn, (ax, ay+y, az), (bx, by+y, bz), (cx_, cy_+y, cz))
                for nn, (ax, ay, az), (bx, by, bz), (cx_, cy_, cz) in sub]
        out += stud(7.0, y + TH/2, PLATE_T, head_d, neck_d)
        t, _ = text(lbl, lx, ly, PLATE_T-SINK, PLATE_T+LABEL_Z)
        out += t
        y += TH + GAPY
    return out, (TW, y-GAPY)


def strip_hanger_test(spacing=65.40, head_d=5.8, neck_d=2.6):
    """Two studs at the measured keyhole spacing. Hold it against the strip's
    back and check both keyholes engage and it hangs square. No panel posts:
    this tests the keyhole side only.

    The bulge sits mid-slot (measured at 49-52% down), so the keyhole hangs either
    way up and the studs sit at the bulge centres, i.e. at the keyhole centre
    spacing of 65.40 mm rather than at a slot end.

    Head 5.8 clears the 6.71 mm bulge by 0.9 mm; neck 2.6 passes any slot wider
    than about 2.8 mm while the head blocks any slot narrower than about 5.5 mm.
    That spans the whole plausible range for a 6.71 mm bulge, so the slot width
    never has to be measured."""
    MARG, H = 12.0, 16.0
    W = spacing + 2*MARG
    tris = _rect(0, 0, 0, W, H, PLATE_T)
    for cx in (MARG, MARG + spacing):
        tris += stud(cx, H/2, PLATE_T, head_d, neck_d)
    return tris, (W, H)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    made = []
    # Panel measured at 3/16 in (4.7625 mm). Bracket it, and keep 5.00 as the
    # metric alternative in case the imperial read is wrong.
    for p in (4.60, 4.70, 4.7625, 4.83, 4.90, 5.00):
        lab = "4.76" if abs(p-4.7625) < 1e-6 else f"{p:.2f}"
        tris, size = pitch_gauge(p, label=lab)
        f = OUT / f"pitch_gauge_{lab}mm.stl"
        write_stl(f, tris, f"pitch gauge {p:.4f}mm 3x3".encode())
        made.append((f, len(tris), size))
    # Post-size fit gauges: pitch now known (3/16 in), so vary post width instead.
    # Nine snug posts entering at once is a much harder tolerance stack than the one
    # post of peg_size_gauge, so the usable post size for a real plate is smaller
    # than the largest single peg that fits.
    for w in (2.30, 2.40, 2.50, 2.60):
        lab = f"{w:.1f}"
        tris, size = pitch_gauge(4.7625, n=3, peg_w=w, label=lab)
        f = OUT / f"fit_gauge_post{lab}mm.stl"
        write_stl(f, tris, f"fit gauge 3x3 @4.7625mm post {w:.2f}mm".encode())
        made.append((f, len(tris), size))

    tris, size = stud_gauge()
    f = OUT.parent / "strip_mount" / "stud_gauge.stl"
    f.parent.mkdir(parents=True, exist_ok=True)
    write_stl(f, tris, b"stud gauge heads 5.4/6.2/7.4mm")
    made.append((f, len(tris), size))
    tris, size = strip_hanger_test()
    f = OUT.parent / "strip_mount" / "strip_hanger_test.stl"
    write_stl(f, tris, b"strip hanger test 65.27mm spacing")
    made.append((f, len(tris), size))

    tris, size = peg_size_gauge()
    f = OUT / "peg_size_gauge.stl"
    write_stl(f, tris, b"peg size gauge 2.0-2.8mm")
    made.append((f, len(tris), size))
    for f, n, s in made:
        print(f"{f.name:28s} {n:5d} tris   {s[0]:.1f} x {s[1]:.1f} mm")
