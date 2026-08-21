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

**Three independent reads, spread 0.31 mm.**

| Method | Result |
|---|---|
| Calipers, `(inner + outer)/2` | 65.40 mm |
| Photo, grey box tops projected onto the tape axis | 65.21 mm |
| Direct tape read, `6 11/16 - 4 1/8 = 41/16 in` | 65.09 mm |

**Adopted: 65.20 mm.** The two direct tape reads agree to 0.12 mm and both sit below the
caliper figure, which is itself indirect: it comes from combining an inner gap, an outer span
and a keyhole length that were mutually inconsistent by 0.26 mm.

The tape reads also validate each other in a satisfying way. The photo method's absolute
readings sit a constant +0.180 and +0.175 in above the eyeball readings, which is the fixed
offset between a numeral's centroid and its inch tick. Being constant, it cancels entirely in
the difference, which is why the two methods land 0.12 mm apart despite disagreeing by nearly
0.18 in on each individual position.

Note the tape in that shot has a 21 per cent scale gradient end to end, which is why the
numerals are interpolated individually rather than averaged into one px-per-inch figure.

None of this precision actually matters: the slot play absorbs a few tenths. It is recorded
because three methods agreeing is what makes it safe to stop measuring.

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

## Cross-width pair

Calipers give 21.18 mm between the insides and 35.83 mm across the outsides, so
centre-to-centre is **28.50 mm**. Deriving it from the 6.71 mm bulge instead gives 27.89 and
29.12, mean 28.50, so the spacing is solid.

**The plate uses two studs, not four.** Two points already fix position and rotation. Four
would need both the 65.20 and the 28.50 spacings inside the slot play at once on a rigid
plate, so any single error stops the whole thing seating. At 6.9 N shear and 3.5 N pull-out
the load does not justify that risk.

## `pitchspan_4.72mm` .. `4.80mm` -- the current blocker

The three post-width span gauges (2.0, 2.2, 2.4 mm) **all failed to seat**. That is a real
result, not a bad print, and it bounds the answer.

Even the loosest, 2.0 mm posts with 0.299 mm of play per side, could not span 16 pitches, so
the effective pitch is off by more than `0.299 / 16 = 0.019 mm` per pitch, putting it outside
4.7438 to 4.7812.

**This does not contradict the 3x3 gauge seating at 4.76.** A 3x3 spans two pitches with
2.1 mm posts, so it only proves the pitch to within 0.124 mm per pitch, seven times looser
than a 16-span run needs. An error of 0.02 to 0.12 mm is invisible over two pitches and fatal
over sixteen. Both observations are consistent.

These five fix the post at the loosest 2.0 mm so **only pitch can bind**, and sweep it:

| file | pitch | span over 16 | drift vs nominal |
|---|---|---|---|
| `pitchspan_4.72mm` | 4.7200 | 75.52 mm | -0.68 mm |
| `pitchspan_4.74mm` | 4.7400 | 75.84 mm | -0.36 mm |
| `pitchspan_4.76mm` | 4.7625 | 76.20 mm | 0 |
| `pitchspan_4.78mm` | 4.7800 | 76.48 mm | +0.28 mm |
| `pitchspan_4.80mm` | 4.8000 | 76.80 mm | +0.60 mm |

About 3.3 g each. The one that seats gives the **effective pitch**: panel pitch divided by
printer scale. That combined figure is what a printed part actually needs, so the error does
not have to be attributed to panel or printer to be usable. Every later mount inherits it.

**Check for warp before concluding.** These bars are 108 x 15 x 1.6 mm, a shape prone to
curling at the ends, and a bowed bar tilts its end posts so they cannot enter regardless of
pitch. Use a brim and confirm the bar sits flat before judging. If none seats but the middle
cluster always does, suspect warp rather than pitch.

## `strip_plate_post2.2mm.stl`

87.2 x 34.0 mm, 23 posts on 9.525 mm centres, two 5.8 mm studs at 65.20 mm, about 6.6 g.
**Do not print it yet**: its post grid uses the nominal 4.7625 pitch, which the span gauges
have just shown is wrong over a long run. Regenerate once `pitchspan` picks a winner.

`tools/gen_strip_mount.py` takes the pitch as a parameter throughout.
