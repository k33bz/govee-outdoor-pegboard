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
    GH, PEG_H, PLATE_T, LABEL_Z, SINK, TIP, _quad, _rect, frustum, label_cuts,
    peg, plate_with_recess, round_frustum, stud, text, text_width, write_stl,
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


PANEL_T  = 2.9          # measured panel thickness; sets shaft length and barb depth


def loft_rect(a, b, z0, z1):
    """Closed prism between rectangle a=(x0,y0,x1,y1) at z0 and b at z1."""
    A = [(a[0],a[1],z0),(a[2],a[1],z0),(a[2],a[3],z0),(a[0],a[3],z0)]
    B = [(b[0],b[1],z1),(b[2],b[1],z1),(b[2],b[3],z1),(b[0],b[3],z1)]
    tris = []
    tris += _quad(*A, (0,0,-1))
    tris += _quad(*B, (0,0,1))
    ca = ((a[0]+a[2])/2, (a[1]+a[3])/2)
    for k in range(4):
        m = (k+1) % 4
        mid = ((A[k][0]+A[m][0])/2 - ca[0], (A[k][1]+A[m][1])/2 - ca[1], 0)
        tris += _quad(A[k], A[m], B[m], B[k], mid)
    return tris


def barbed_post(cx, cy, z, w=2.5, slot=0.9, barb=3.4, tip=1.3,
                panel_t=PANEL_T, teeth=3, tooth=0.6, tip_len=1.0):
    """A split post with a CHRISTMAS-TREE barb, built as two independent legs.

    A single ledge set at exactly the panel thickness has zero margin: the first
    version put it dead on the 2.9 mm back face and it would not latch, because
    any under-seating, a slightly thick panel or a little under-extrusion is
    enough to keep it inside the hole. Simply lengthening the shaft trades that
    for the plate rattling by however much was added.

    Several ledges solve both. Whichever one clears the far face is the one that
    latches, so the post grips any panel from about 2.3 to 4.1 mm and does not
    care whether the plate seated perfectly.

    Longer legs come free with it: strain falls from 1.30 to 0.96 per cent and
    insertion force, going as 1/L^3, drops from about 30 N to 19 N for six posts.

    Only the OUTER face of each leg flares; the slot only permits movement in x,
    so flaring in y would engage more sides but could not compress. Each ledge is
    a square step rather than a chamfer, because a 45 degree undercut cams out
    under load while a 0.45 mm flat overhang bridges perfectly well.
    """
    tris = []
    for sgn in (-1, 1):
        inner  = cx + sgn*slot/2
        outer  = cx + sgn*w/2
        obarb  = cx + sgn*barb/2
        otip   = cx + sgn*tip/2
        lo, hi = min(inner, outer), max(inner, outer)
        blo, bhi = min(inner, obarb), max(inner, obarb)
        tlo, thi = min(inner, otip),  max(inner, otip)
        # shaft up to the first ledge
        zt = z + panel_t
        tris += _rect(lo, cy-w/2, z-SINK, hi, cy+w/2, zt)
        # sawtooth: each tooth steps out to the barb then tapers back to the shaft
        for k in range(teeth):
            zk = zt + k*tooth
            tris += loft_rect((blo, cy-w/2, bhi, cy+w/2),
                              (lo,  cy-w/2, hi,  cy+w/2), zk, zk+tooth)
        # lead-in tip
        ze = zt + teeth*tooth
        tris += loft_rect((lo,  cy-w/2, hi,  cy+w/2),
                          (tlo, cy-w/2, thi, cy+w/2), ze, ze+tip_len)
    return tris


PLATE_T2 = 2.4          # plate thickness for the strip mount; sets the spigot length
SOCKET   = 4.0          # square socket side; the stud spigot is 0.1 under


STUD_ROWS = 28.50       # cross-width keyhole spacing, calipers (21.18 inner, 35.83 outer)


def strip_plate(spacing=STUD_SPACING, rows=STUD_ROWS, margin=11.0, margin_y=6.5,
                post_step=2, keepout=6.5, w_centre=2.60, w_end=2.10, n_barbs=6):
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
    slots = []
    for i in range(nx):
        for j in range(ny):
            px, py = gx0 + i*step, gy0 + j*step
            if any((px-sx)**2 + (py-sy)**2 < keepout**2 for sx, sy in studs):
                continue
            slots.append((px, py))

    # barbs spread across the plate: nearest free post to each target
    targets = [(W*fx, height*fy) for fy in (0.5,) for fx in (0.18, 0.5, 0.82)] +               [(W*fx, height*fy) for fy in (0.12, 0.88) for fx in (0.34, 0.66)]
    barbed = set()
    for tx, ty in targets[:n_barbs]:
        best = min((q for q in slots if q not in barbed),
                   key=lambda q: (q[0]-tx)**2 + (q[1]-ty)**2)
        barbed.add(best)

    widths = []
    for px, py in slots:
        if (px, py) in barbed:
            tris += barbed_post(px, py, PLATE_T2)
            continue
        w = w_centre - (w_centre - w_end) * (abs(px - cx) / half)
        # full width through the whole panel, lead-in taper BEYOND the far face,
        # so the taper never eats into the engaged length
        # 0.5 mm past nominal panel thickness before the taper starts, so the
        # full width still fills the hole if the panel runs thick
        tris += frustum(px, py, PLATE_T2-SINK, PLATE_T2+PANEL_T+0.5, w/2, w/2)
        tris += frustum(px, py, PLATE_T2+PANEL_T+0.5, PLATE_T2+PANEL_T+1.1, w/2, w*0.34)
        widths.append(w)
    return tris, (W, height), widths, studs, sorted(barbed)


def strip_stud(head_d=6.2, neck_w=2.8, neck_l=5.5, neck_h=4.0, head_t=2.2,
               spigot=SOCKET-0.1):
    """One stud. Prints spigot down, so only one overhang: the head on the neck.

    The neck is a RECTANGLE, not a circle. It only has to be narrow across the
    slot; along the slot it has 16.80 mm to play with, so making it 2.8 x 5.5
    instead of 2.6 round is nearly three times the cross-section for no loss of
    fit. Its 6.17 mm diagonal still clears the 6.71 mm bulge on the way in.

    Head 6.2 and neck width 2.8 are the largest sizes actually proven on the
    stud gauge. The slot width W was never measured, so going beyond 2.8 would be
    guesswork.

    The neck's long axis runs along +Y, matching the slot direction when the strip
    hangs length-horizontal. The square spigot in the square socket is what fixes
    that orientation.
    """
    z0 = PLATE_T2
    tris = frustum(0, 0, 0.0, z0, spigot/2, spigot/2)
    tris += _rect(-neck_w/2, -neck_l/2, z0-0.01, neck_w/2, neck_l/2, z0+neck_h)
    tris += round_frustum(0, 0, z0+neck_h, z0+neck_h+head_t-0.5, head_d/2, head_d/2)
    tris += round_frustum(0, 0, z0+neck_h+head_t-0.5, z0+neck_h+head_t,
                          head_d/2, head_d/2-0.5)
    return tris, (neck_w, neck_l, head_d)


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
    tris, size, widths, studs, barbed = strip_plate()
    f = OUT / "strip_plate.stl"
    write_stl(f, tris, b"strip plate graded+barbed posts 4.9643, 4 stud sockets, panel 2.9")
    print(f"{f.name:30s} {len(tris):5d} tris  {size[0]:.1f} x {size[1]:.1f} mm  "
          f"{len(widths)} plain {min(widths):.2f}-{max(widths):.2f} + {len(barbed)} barbed, "
          f"{len(studs)} sockets")
    tris, size = strip_stud()
    f = OUT / "strip_stud.stl"
    write_stl(f, tris, b"strip stud: square spigot + 2.8x5.5 rect neck + 6.2 head")
    print(f"{f.name:30s} {len(tris):5d} tris  neck {size[0]}x{size[1]} mm, "
          f"head {size[2]} mm  (PRINT 4)")
