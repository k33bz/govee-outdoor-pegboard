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
    GH, PEG_H, PLATE_T, LABEL_Z, SINK, TIP, _rect, frustum, label_cuts, peg,
    plate_with_recess, round_frustum, stud, text, text_width, write_stl,
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


def plate_with_holes(W, Hgt, holes, t=PLATE_T):
    """Plate 0..t with square through-holes. Tiled by subdividing on every hole
    edge and emitting a box per cell not inside a hole: exact for axis-aligned
    rectangles and keeps everything a union of closed boxes."""
    xs = sorted({0.0, W} | {h[0] for h in holes} | {h[2] for h in holes})
    ys = sorted({0.0, Hgt} | {h[1] for h in holes} | {h[3] for h in holes})
    tris = []
    for i in range(len(xs)-1):
        for j in range(len(ys)-1):
            x0, x1, y0, y1 = xs[i], xs[i+1], ys[j], ys[j+1]
            if x1-x0 < 1e-9 or y1-y0 < 1e-9:
                continue
            mx, my = (x0+x1)/2, (y0+y1)/2
            if any(h[0] < mx < h[2] and h[1] < my < h[3] for h in holes):
                continue
            tris += _rect(x0, y0, 0.0, x1, y1, t)
    return tris


PLATE_T2 = 2.4          # plate thickness for the strip mount; sets the spigot length
SOCKET   = 4.0          # square socket side; the stud spigot is 0.1 under


STUD_ROWS = 28.50       # cross-width keyhole spacing, calipers (21.18 inner, 35.83 outer)


def strip_plate(spacing=STUD_SPACING, rows=STUD_ROWS, margin=11.0, margin_y=6.5,
                post_step=2, keepout=6.5, w_centre=2.60, w_end=2.10):
    """Panel plate: posts on the +Z face, four square sockets for the studs.

    FOUR studs, in two rows. A stud sitting in a vertical keyhole slot is a
    SLIDER, not a point: it is free to move along the slot. Two sliders on one
    horizontal line therefore do not constrain rotation at all, and the strip
    rocks one stud up and the other down until it prises the posts out. An
    earlier two-stud version failed in exactly that way.

    Adding the second row costs almost nothing in tolerance, because the two axes
    are not equally tight. The horizontal spacing is held by the slot WIDTH, a few
    tenths of play. The vertical spacing is held by the slot LENGTH, about +/-5 mm
    of travel. So the 28.50 mm figure can be out by millimetres and every stud
    still engages, each simply sitting at its own height in its own slot.

    The second row is also what reacts the tip-out moment, as a couple across the
    rows rather than by levering the posts out of the panel.

    Posts are graded from `w_centre` at the middle to `w_end` at the extremes:
    cumulative pitch error is zero at the plate centre and worst at the ends.
    """
    W = spacing + 2*margin
    height = rows + 2*margin_y
    studs = [(margin + dx, margin_y + dy)
             for dx in (0.0, spacing) for dy in (0.0, rows)]
    h = SOCKET/2
    holes = [(sx-h, sy-h, sx+h, sy+h) for sx, sy in studs]
    tris = plate_with_holes(W, height, holes, PLATE_T2)

    step = post_step * PITCH
    nx = int((W - 2*4.0) // step) + 1
    ny = int((height - 2*4.0) // step) + 1
    gx0 = (W - (nx-1)*step)/2
    gy0 = (height - (ny-1)*step)/2
    cx = W/2
    half = max(abs(gx0 - cx), abs(gx0 + (nx-1)*step - cx))
    widths = []
    for i in range(nx):
        for j in range(ny):
            px, py = gx0 + i*step, gy0 + j*step
            if any((px-sx)**2 + (py-sy)**2 < keepout**2 for sx, sy in studs):
                continue
            w = w_centre - (w_centre - w_end) * (abs(px - cx) / half)
            tris += frustum(px, py, PLATE_T2-SINK, PLATE_T2+PEG_H-TIP, w/2, w/2)
            tris += frustum(px, py, PLATE_T2+PEG_H-TIP, PLATE_T2+PEG_H, w/2, w*0.34)
            widths.append(w)
    return tris, (W, height), widths, studs


def strip_stud(head_d=HEAD_D, neck_d=NECK_D, neck_len=4.0, head_t=2.0,
               spigot=SOCKET-0.1):
    """One stud. Prints spigot down: square spigot, then a step DOWN to the neck,
    then the head. Only one overhang, the same 1.6 mm one that printed fine on the
    stud gauge.

    The spigot is exactly the plate thickness, so it finishes flush with the panel
    side and the panel itself then traps the stud in place."""
    tris = frustum(0, 0, 0.0, PLATE_T2, spigot/2, spigot/2)
    tris += round_frustum(0, 0, PLATE_T2-0.01, PLATE_T2+neck_len, neck_d/2, neck_d/2)
    tris += round_frustum(0, 0, PLATE_T2+neck_len, PLATE_T2+neck_len+head_t-0.5,
                          head_d/2, head_d/2)
    tris += round_frustum(0, 0, PLATE_T2+neck_len+head_t-0.5, PLATE_T2+neck_len+head_t,
                          head_d/2, head_d/2-0.5)
    return tris, (spigot, spigot)


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
    tris, size, widths, studs = strip_plate()
    f = OUT / "strip_plate.stl"
    write_stl(f, tris, b"strip plate graded posts pitch 4.9643 + 4 stud sockets")
    print(f"{f.name:30s} {len(tris):5d} tris  {size[0]:.1f} x {size[1]:.1f} mm  "
          f"{len(widths)} posts {min(widths):.2f}-{max(widths):.2f}, {len(studs)} sockets")
    tris, size = strip_stud()
    f = OUT / "strip_stud.stl"
    write_stl(f, tris, b"strip stud: 3.9mm square spigot + 2.6 neck + 5.8 head")
    print(f"{f.name:30s} {len(tris):5d} tris  spigot {size[0]:.1f} mm  (PRINT 4)")
