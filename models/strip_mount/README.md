# Power strip mount

The strip already has keyhole hangers, so the mount does not fight them: a plate on the
panel carries two printed "screw heads", the strip hangs over them and drops into place.

## Measured inputs

| | Value | Source |
|---|---|---|
| Strip | 41.28 x 200.0 mm, 25 mm thick at the plugs, 31 at the base | calipers |
| Keyhole length | 16.80 mm each | calipers |
| Keyhole inner gap | 48.73 mm | calipers |
| Keyhole outer span | 82.07 mm | calipers |
| Slot top to strip edge | 17.90 mm | calipers |
| Panel thickness | about 1.5 mm | calipers |
| Cord | 10 mm round | calipers |

**Derived.** `inner + 2 x length = 82.33` against a measured outer span of `82.07`, so the
three keyhole readings agree to 0.26 mm. Centre-to-centre is **65.40 mm**.

**The keyhole is symmetric, bulge in the middle.** Photographs show a slot that is narrow at
both ends with the round bulge at 49 to 52 per cent along, not the usual round-one-end shape.
It therefore hangs either way up, and the stud rests at the bulge centre, so stud spacing is
the keyhole centre spacing of **65.40 mm** rather than any slot-end figure. Usable drop is
about `(16.80 - 6.71)/2 = 5.0 mm` in either direction, which is ample.

**Orientation is forced, not chosen.** `17.90 + 16.80 = 34.70 mm` fits inside the strip's
41.28 mm width but nowhere near its 200 mm length, so the slots run across the width. Slots
must be vertical for gravity to hold, so the strip hangs with its **length horizontal** and
the two studs side by side.

**Load is not the constraint.** At an assumed 700 g the total shear is 6.9 N spread over
every post, and the tip-out moment is 0.106 N.m, which over a 30 mm tall plate is 3.5 N of
pull-out at the top. Both are far below what either the posts or the panel webs will carry.
Post count is driven by wanting the load spread, not by strength.

## Still unknown

- **W, the keyhole slot width.** Not measured, and deliberately not needed. Measuring it off
  the photo gave 0.40, 0.52 and 0.71 for W/D depending on threshold, so the design tolerates
  it instead: a 2.6 mm neck passes any slot wider than about 2.8 mm, and a 5.8 mm head blocks
  any slot narrower than about 5.5 mm. Since the bulge is 6.71 mm, W must fall inside that
  range, so both conditions hold whatever W turns out to be.
- **T, the strip's back-wall thickness at the keyhole.** Sets the neck length. Currently
  4.0 mm, which suits a wall up to about 3.5 mm; if the wall is thinner the strip will have
  a little play until the neck is shortened.
- **How many keyholes there are, and where.** The photos show a pair on the end flange about
  24 mm apart as well as the two on the back face 65.40 mm apart. Which pair should carry the
  strip, and are there four in total?

## `stud_gauge.stl`

Three tabs, one stud each, heads 5.4 / 5.8 / 6.2 mm on necks of 2.4 / 2.6 / 2.8 mm. About
3.1 g, roughly 20 min. All three heads clear the 6.71 mm bulge. Offer each up to a real
keyhole:

- the **head must pass** the big hole without forcing
- the **neck must slide** freely down the slot
- the **head must not pull back through** the slot

The largest that satisfies all three wins.

**D is settled at 6.71 mm.** Your note read either 8.71 or 6.71; measuring the bulge against
the keyhole's own 16.80 mm length, which needs no tape and no scale, gives 6.60 mm. So the
ambiguous digit is a 6.

## `strip_hanger_test.stl`

A bare bar with two 5.8 mm studs at 65.40 mm, no panel posts. About 3.0 g. Hold it against
the back of the strip and check both keyholes engage together and the strip hangs square.
This isolates the keyhole side: if it fails, the spacing or the stud size is wrong, and no
amount of work on the panel side will help.

Reprint from `tools/gen_gauges.py` with a different `head_d`/`neck_d` once the stud gauge
picks a winner.

## Next

With the winning stud size, the winning post width from `../test_gauges/fit_gauge_post*`,
and the slot width, the real plate is a single part: post grid on 4.7625 mm centres, two
studs at 65.27 mm, sized so the strip clears the panel.
