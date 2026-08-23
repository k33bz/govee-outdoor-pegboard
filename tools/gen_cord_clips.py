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
from gen_gauges import _rect, round_frustum, write_stl                 # noqa: E402
from gen_strip_mount import PANEL_T, PITCH, barbed_post                # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "models" / "cord_clips"

BRIDGE_T = 2.0          # bridge thickness
SHOULDER = 3.6          # standoff section, wider than the 2.929 hole so it stops there
POST_W   = 2.6          # octagonal post across flats, into the panel


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


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"{'file':26s} {'legs':>5} {'gap':>7} {'standoff':>9} {'size mm':>18}")
    for d in (4, 6, 8, 10, 13):
        tris, (L, W, H, sp, gap, so) = cord_staple(d)
        f = OUT / f"cord_staple_{d:02d}mm.stl"
        write_stl(f, tris, f"cord staple {d}mm: {sp} pitch legs, {so:.1f} standoff".encode())
        print(f"{f.name:26s} {sp:5d} {gap:7.2f} {so:9.2f} "
              f"{L:6.1f} x {W:.1f} x {H:.1f}")
