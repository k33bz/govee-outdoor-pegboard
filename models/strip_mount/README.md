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

The sockets are square so the stud cannot rotate, which also fixes the neck's orientation.
The spigot is 3.9 mm into a 4.0 mm socket and is exactly the plate thickness, so it finishes
flush with the panel side; once the plate is on the panel, the panel itself traps the studs.
Glue is optional, not structural.

### The neck is a rectangle, not a circle

A round 2.6 mm neck was structurally fine, roughly 60x margin even on layer adhesion, but it
looks and feels thin. It does not have to be round: the keyhole slot is **16.80 mm long and
only W wide**, so the neck only needs to be narrow *across* the slot and can be far longer
*along* it.

| neck | area | vs round 2.6 | diagonal | clears the 6.71 bulge |
|---|---|---|---|---|
| 2.6 round | 5.31 mm2 | 1.00x | 2.60 | yes |
| 2.8 round | 6.16 mm2 | 1.16x | 2.80 | yes |
| **2.8 x 5.5 rect** | **15.40 mm2** | **2.90x** | 6.17 | yes |
| 2.8 x 6.0 rect | 16.80 mm2 | 3.16x | 6.62 | too tight |

Adopted **2.8 x 5.5** with a **6.2 mm head**. Nearly three times the cross-section for no
loss of fit, and the 6.17 mm diagonal still passes the bulge going in.

Both figures are the largest actually **proven** on the stud gauge: heads 5.4, 5.8 and 6.2
all passed the bulge, and necks 2.4, 2.6 and 2.8 all slid the slot. W itself was never
measured, so anything wider than 2.8 would be guesswork.

The 5.5 mm neck is also wider than the 4.0 mm socket, so its shoulder bears on the plate
face and the stud cannot push through.

| part | size | mass | print |
|---|---|---|---|
| `strip_plate.stl` | 87.2 x 46.5 x 8.1 mm | 13.6 g | 1 off, posts up |
| `strip_stud.stl` | 6.2 mm head, 2.8 x 5.5 neck, 8.6 mm tall | 0.20 g | **4 off**, spigot down |

**Panel is 2.9 mm thick**, not the 1.5 mm first assumed. That is enough material to grab,
so six of the posts are barbed snap-fits and the other 22 are plain locators.

### Barbed posts -- christmas tree

Split down the middle so the legs pinch on the way through, then **three ledges** rather than
one.

A single ledge at exactly the panel thickness has zero margin, and the first version failed
that way: it sat dead on the 2.9 mm back face and would not latch, because any under-seating,
a slightly thick panel or a little under-extrusion keeps it inside the hole. Simply
lengthening the shaft trades that fault for the plate rattling by whatever was added.

Three ledges solve both. Whichever one clears the far face is the one that latches:

| ledge | at | grips a panel of |
|---|---|---|
| 1 | 2.9 mm | 2.3 to 2.9 mm |
| 2 | 3.5 mm | 2.9 to 3.5 mm |
| 3 | 4.1 mm | 3.5 to 4.1 mm |

So it holds anything from **2.3 to 4.1 mm** and does not care whether the plate seated
perfectly.

| | |
|---|---|
| post | 2.5 mm square, 0.9 mm slot, 0.8 mm legs |
| barb | 3.4 mm across each ledge, into a 2.879 mm hole |
| deflection | 0.26 mm per leg over 5.7 mm of free length |
| peak strain | **0.96 %**, against PLA yielding around 2 to 3 % |
| insertion | about 19 N for all six, roughly 2 kg |
| holding | 78 N per post, against 3.7 N of tip-out total |

The longer legs come free with the extra teeth: strain falls from 1.30 to 0.96 per cent and
insertion force, going as 1/L^3, from about 30 N to 19 N.

Only the **outer** face of each leg flares; the slot only permits movement in x, so flaring
in y would engage more sides but could not compress. Each ledge is a square step rather than
a chamfer, because a 45 degree undercut cams out under load while a 0.45 mm flat overhang
bridges perfectly well printed posts-up.

Barbs stand 2.8 mm proud of the far face, against 6 to 7 mm of clearance behind the panel.

### Plain posts: checkerboard lattice, graded width

Posts sit on a **checkerboard** of the panel lattice, every hole where `i+j` is even.
Nearest neighbours are `pitch x sqrt(2) = 7.02 mm` apart instead of 9.93, which is twice the
density for the same span, so the grading still covers cumulative error unchanged.

| pattern | nearest spacing | holes used | posts here |
|---|---|---|---|
| square, every 2nd hole (old) | 9.93 mm | 1 in 4 | 28 |
| **checkerboard** | **7.02 mm** | 1 in 2 | **62** |
| every hole | 4.96 mm | 1 in 1 | 112 |

The keepout around each socket was also wrong: a 4.0 mm socket and a 2.5 mm post clear once
their centres are 3.25 mm apart, and I had used 6.5, twice what was needed, deleting whole
rings of posts for nothing. Closest post to a socket is now 4.32 mm.

Rotating the posts 45 degrees into diamonds was considered and rejected: a diamond inscribed
in a 2.879 mm square hole has 2.04 mm sides, only 66 per cent of a 2.5 mm square post's
section. Nor can any lattice rotation put the sockets in the gaps, because the sockets sit
where the **strip's** keyholes dictate, 13.13 and 5.74 pitches apart, which are not lattice
positions at all.

Widths are graded 2.53 mm at the middle down to 2.10 mm at the ends, since cumulative pitch
error is zero at the plate centre and worst at the extremes. They run full width to 0.5 mm
past nominal panel thickness before tapering, so the hole stays filled if the panel runs
thick and the lead-in never eats into the engaged length.

`extra_bottom` adds rows below the lower stud row, currently one. Note the **top** matters
more mechanically: the strip's weight acts about 15 mm out from the panel, so the upper stud
row is pulled away from the panel while the lower is pushed into it. Rows above the top stud
row resist that tension directly, so raise `margin_y` rather than `extra_bottom` if the plate
ever needs more grip.

## Assembly

1. Drop a stud into each of the **four** sockets from the flat face, heads pointing away
   from the posts.
2. Push the plate onto the panel, posts first, pressing firmly until the six barbs
   snap through. The panel now traps all four studs.
3. Hang the strip: heads through the keyhole bulges, then let it drop about 5 mm so the
   necks sit in the slots.

`tools/gen_strip_mount.py` takes `w_centre` and `w_end`; raise them together for a firmer
fit once this one is confirmed.
