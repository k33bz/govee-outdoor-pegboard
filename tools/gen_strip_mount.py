#!/usr/bin/env python3
"""Power strip mounting plate, and a span gauge that must pass before printing it.

The 3x3 fit gauges optimise a 9.5 mm span. The plate has to span both studs, about
76 mm, so printer scaling error that is invisible on a gauge can bind the plate: at
2.4 mm posts the whole budget is 0.13 %, inside typical FDM accuracy. The span gauge
tests that directly and cheaply before committing to the big print.

Everything prints flat on the bed, posts up, no supports.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_gauges import (                                    # noqa: E402
    GH, PLATE_T, LABEL_Z, SINK, _rect, label_cuts, peg, plate_with_recess,
    stud, text, text_width, write_stl,
)

PITCH = 4.9643          # small panel, 1200 dpi scan lattice fit, both axes agree to 0.1 um
HOLE  = 2.879           # measured on the same scan
STUD_SPACING = 65.20    # consensus of caliper, photo and tape reads
HEAD_D, NECK_D = 5.8, 2.6
OUT = Path(__file__).resolve().parent.parent / "models" / "strip_mount"


def span_gauge(post_w, span_pitches=16, gap_pitches=8, rows=2, pitch=PITCH, label=None):
    """A bar with posts only at 0, gap and span pitches, in two rows.

    Seats only if cumulative error across the span stays inside the post-to-hole
    play. Two rows so it cannot pivot and fake a pass.

    With `pitch` varied and the post left deliberately loose, this measures the
    EFFECTIVE pitch: panel pitch divided by printer scale. That combined number is
    what a printed part actually needs, so it does not matter whether the error
    lives in the panel or the printer.
    """
    span = span_pitches * pitch
    x0, y0 = 6.0, 5.0
    lbl = label if label is not None else f"{post_w:.1f}"
    W = x0 + span + 6.0 + 4.0 + text_width(lbl) + 4.0
    H = y0*2 + (rows-1)*pitch
    H = max(H, GH + 6.0)
    ty = (H - GH)/2
    tx = x0 + span + 8.0
    tris = plate_with_recess(W, H, label_cuts(lbl, tx, ty))
    cy0 = (H - (rows-1)*pitch)/2
    for c in (0, gap_pitches, span_pitches):
        for r in range(rows):
            tris += peg(x0 + c*pitch, cy0 + r*pitch, post_w)
    t, _ = text(lbl, tx, ty, PLATE_T-SINK, PLATE_T+LABEL_Z)
    return tris + t, (W, H)


def strip_plate(post_w=2.5, spacing=STUD_SPACING, height=34.0, margin=11.0,
                post_step=2, keepout=6.5):
    """Panel plate carrying two studs at the keyhole spacing.

    Two studs, not four: two points already fix position and rotation, while four
    would require both spacings to land inside the slot play at the same time on a
    rigid plate, so any single error stops the whole thing seating.
    """
    W = spacing + 2*margin
    studs = [(margin, height/2), (margin + spacing, height/2)]

    # post grid, centred, skipping anything that would foul a stud
    step = post_step * PITCH
    nx = int((W - 2*4.0) // step) + 1
    ny = int((height - 2*4.0) // step) + 1
    gx0 = (W - (nx-1)*step)/2
    gy0 = (height - (ny-1)*step)/2

    tris = _rect(0, 0, 0, W, height, PLATE_T)
    n = 0
    for i in range(nx):
        for j in range(ny):
            px, py = gx0 + i*step, gy0 + j*step
            if any((px-sx)**2 + (py-sy)**2 < keepout**2 for sx, sy in studs):
                continue
            tris += peg(px, py, post_w)
            n += 1
    for sx, sy in studs:
        tris += stud(sx, sy, PLATE_T, HEAD_D, NECK_D)
    return tris, (W, height), n


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    # Post width is now fixed at the loosest 2.0 so only PITCH can bind. None of
    # the three post widths seated at nominal pitch, which bounds the effective
    # pitch outside 4.7625 +/- 0.019; these bracket it.
    for p in (4.92, 4.94, 4.9643, 4.98, 5.00):
        lab = f"{p:.2f}"
        tris, size = span_gauge(2.0, pitch=p, label=lab)
        f = OUT / f"pitchspan_{lab}mm.stl"
        write_stl(f, tris, f"pitch span gauge {p:.4f}mm 16 spans post 2.0".encode())
        print(f"{f.name:30s} {len(tris):5d} tris  {size[0]:.1f} x {size[1]:.1f} mm  "
              f"span {16*p:.2f} mm")
    tris, size, n = strip_plate()
    f = OUT / "strip_plate_post2.5mm.stl"
    write_stl(f, tris, b"strip plate 2 studs @65.20mm post 2.5mm pitch 4.9643")
    print(f"{f.name:30s} {len(tris):5d} tris  {size[0]:.1f} x {size[1]:.1f} mm  {n} posts")
