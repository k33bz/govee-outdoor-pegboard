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

## Cross-width pair, and why FOUR studs

Calipers give 21.18 mm between the insides and 35.83 mm across the outsides, so
centre-to-centre is **28.50 mm**. Deriving it from the 6.71 mm bulge instead gives 27.89 and
29.12, mean 28.50.

**A two-stud version was built first and failed in use: the strip twisted and levered the
posts out of the panel.** The reasoning behind it was wrong. A stud sitting in a vertical
keyhole slot is a **slider, not a point** -- it is free to travel along the slot. Two sliders
on one horizontal line do not constrain rotation at all, so the strip simply rocks one stud
up and the other down until it prises the plate off.

The over-constraint argument used to justify two studs was wrong for the same reason, because
the two axes are nowhere near equally tight:

| axis | spacing | held by | play |
|---|---|---|---|
| horizontal | 65.20 mm | slot **width** | a few tenths, tight |
| vertical | 28.50 mm | slot **length** | about +/-5.0 mm, loose |

So the second row costs almost nothing in tolerance. The 28.50 mm figure can be out by
millimetres and every stud still engages, each simply sitting at its own height in its own
slot. Treating all four constraints as equally tight was the mistake.

The second row is also what reacts the tip-out moment, as a couple across the rows rather
than by levering posts out of the panel.

## Panel geometry -- SETTLED

A 1200 dpi flatbed scan of the small enclosure's panel, lattice-fit over 21 hole centres
with both axes agreeing to 0.1 um:

    pitch  4.9643 mm     hole  2.879 x 2.858 mm     web  2.086 mm

That is a 5.00 mm tool less 0.71 per cent, ordinary ABS moulding shrinkage, so the grid was
cut metric. Calipers confirm independently: 47.5 mm across ten holes outer wall to outer
wall is `9 x pitch + 1 hole`, giving 4.958 to 4.967 depending on which hole figure is used.

`pitchspan_4.96mm`, sixteen spans with deliberately loose 2.0 mm posts, **seats**. That is
the pitch confirmed on a printed part rather than only in a measurement, and it bounds the
combined panel-and-printer error at **0.0275 mm per pitch**.

Earlier photograph-derived figures of 5.4, 4.2 and 4.7625 were all wrong. Photographs kept
failing because perspective, lens distortion and tilt all bias scale; a scan has none of
them and settled it in one shot.

## `strip_plate.stl` + `strip_stud.stl` -- the actual part

**Two pieces, because the features have to be on opposite faces.** Posts enter the panel;
studs must face the other way to hold the strip. A single part with features on both faces
cannot print flat, so the studs are separate and drop into square sockets in the plate. Both
pieces print flat, posts up and spigot down respectively, with no supports.

The sockets are square so the stud cannot rotate. The spigot is 3.9 mm into a 4.0 mm socket
and is exactly the plate thickness, so it finishes flush with the panel side; once the plate
is on the panel, the panel itself traps the studs. Glue is optional, not structural.

| part | size | mass | print |
|---|---|---|---|
| `strip_plate.stl` | 87.2 x 41.5 x 5.9 mm | 11.3 g | 1 off, posts up |
| `strip_stud.stl` | 5.8 mm head, 8.4 mm tall | 0.13 g | **4 off**, spigot down |

**Posts are graded, 2.53 mm at the middle down to 2.10 mm at the ends.** Cumulative pitch
error is zero at the plate centre and worst at the extremes, so a uniform post is either
slack everywhere or binds at the tips. Grading puts a firm locating fit where error cannot
accumulate and generous clearance where it can: the middle posts hold the plate, the end
posts only carry shear, which they do at any fit.

Misalignment at a post `n` pitches from centre is `n x delta`, so each post sets its own
limit:

| post | width | play | pitches from centre | max delta | margin |
|---|---|---|---|---|---|
| end | 2.10 mm | 0.389 mm | 7 | 0.0556 | **2.0x** |
| | 2.24 mm | 0.319 mm | 5 | 0.0639 | 2.3x |
| | 2.39 mm | 0.244 mm | 3 | 0.0815 | 3.0x |
| centre | 2.53 mm | 0.175 mm | 1 | 0.1747 | 6.4x |

The binding case is the end post at 0.0556 against a proven 0.0275: two times the margin. A
uniform 2.5 mm plate would need 0.0271, 0.99x proven, on the edge and not actually covered.
That is why the posts are graded rather than simply loosened.

## Assembly

1. Drop a stud into each of the **four** sockets from the flat face, heads pointing away
   from the posts.
2. Push the plate onto the panel, posts first. The panel now traps both studs.
3. Hang the strip: heads through the keyhole bulges, then let it drop about 5 mm so the
   necks sit in the slots.

`tools/gen_strip_mount.py` takes `w_centre` and `w_end`; raise them together for a firmer
fit once this one is confirmed.
