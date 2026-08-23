# Cord holders

Three ways to hold a cord against the panel. They are not variations on one idea; they
answer different questions about how much you want the cord pinned down.

| | staple | arch | cradle |
|---|---|---|---|
| holds the cord | on two sides, air at the flanks | **on three sides, wrapped** | in an open U |
| cord is | captive | captive | **lays in, lifts out** |
| to reroute | pull the mount out of the panel | pull the mount out of the panel | just lift the cord |
| mass | 0.42 - 0.81 g | **0.23 - 0.40 g** | 1.4 - 1.7 g |
| legs | 2 | 2 | 4 |
| supports | none | none | none |
| glue | none | none | none |

**Use the arch as the default.** It is the lightest of the three and the only one that
actually wraps the cord.

**Use a staple** where the cord is not round, or where a bundle has to pass under a
constant-height bridge.

**Use a cradle** where you expect to change things: a bundle you add to, a lead you
unplug, anything you would rather not dismantle a mount to move.

**10 mm is the measured power cord.**

## `cord_arch_06 / 08 / 10 / 13mm.stl`

This is the sketch: an arch hugging the cord, legs splaying down through the panel.

| file | legs | size | mass |
|---|---|---|---|
| `cord_arch_06mm` | 2 pitches | 12.5 x 6.0 x 13.3 | 0.23 g |
| `cord_arch_08mm` | 3 pitches | 17.5 x 6.0 x 15.2 | 0.29 g |
| `cord_arch_10mm` | 3 pitches | 17.5 x 6.0 x 17.1 | 0.33 g |
| `cord_arch_13mm` | 4 pitches | 22.5 x 6.0 x 19.9 | 0.40 g |

The inner surface is a circle of `cord_d/2 + 0.3` centred `cord_d/2` above the panel, so
it sits on the cord rather than clamping it.

**The arch cannot come straight down to the panel.** Carried to the panel face, an arch
that tight meets it only about 3.5 mm apart for a 10 mm cord. That is less than one
4.9643 mm pitch, so there is nowhere to put legs. The arch therefore stops 15 degrees
above the horizontal and straight struts splay out to legs that land on real holes.
Measured strut lean is 7.1 to 27.1 degrees from vertical across the four sizes, well
inside the 45 degree self-supporting limit.

**The crown carries a flat.** Printed crown-down it would otherwise balance on a curve
and touch the bed along a line. Clamping the outer surface at 90 per cent of full height
gives it real first-layer area. Watch for this if you regenerate: the part has to be
mirrored about the *flat*, not about the true crown, or it prints floating above the bed.

## `cord_staple_04 / 06 / 08 / 10 / 13mm.stl`

A flat bridge over the cord with barbed legs into the panel.

| file | legs | clear gap | standoff | size | mass |
|---|---|---|---|---|---|
| `cord_staple_04mm` | 2 pitches | 6.33 mm | 4.30 mm | 15.5 x 6.0 x 12.6 | 0.42 g |
| `cord_staple_06mm` | 3 pitches | 11.29 mm | 6.30 mm | 20.5 x 6.0 x 14.6 | 0.55 g |
| `cord_staple_08mm` | 3 pitches | 11.29 mm | 8.30 mm | 20.5 x 6.0 x 16.6 | 0.60 g |
| `cord_staple_10mm` | 3 pitches | 11.29 mm | 10.30 mm | 20.5 x 6.0 x 18.6 | 0.65 g |
| `cord_staple_13mm` | 4 pitches | 16.26 mm | 13.30 mm | 25.5 x 6.0 x 21.6 | 0.81 g |

**The standoff is set by geometry, not by feel.** The shoulder is 3.6 mm across, wider
than the 2.929 mm hole, so it bottoms on the panel face. The gap under the bridge is what
was designed rather than however far it happened to get pushed.

## `cord_cradle_06 / 10 / 13mm.stl`

Open-top cradle on a back pad with four legs. Prints cradle-up.

**The flat bottom** is what makes it printable cradle-up: a U resting on its curve touches
the bed on a line, whereas flattened it has real first-layer area. **The arms curl 22
degrees past the horizontal** so they rise above the cord's centreline and it cannot roll
out, while staying well inside 45 degrees of inward lean.

**On supports:** yes they would work, but the part does not need them. Opening up and legs
into the panel are *perpendicular*, not opposite, so one piece is possible. That leaves the
legs as horizontal cantilevers, which normally print badly. Rotating the octagonal leg so a
**vertex points down** makes it self-support at 45 degrees, and because an octagon's fit is
set by its inscribed circle, rotating it does not change the hole fit at all. Printing
legs-up instead would hang the cradle under the plate and cost about 56 per cent of the part
mass in support.

Four legs in two rows, not two: the cord's weight acts on a lever arm out from the panel,
and a single row would let the cradle rock. Two rows react it as a couple.

## Why none of these is a C-clip

The first attempt was a two-piece C-clip: a base plate with posts, and a separate clip that
socketed into it.

**One piece, no supports, no glue.** A C-clip has to hold the cord in *front* of the plate
while the posts point *into* the panel, so the features land on opposite faces and no single
part can print flat. That forces either a two-piece assembly with a glue joint, or supports
under the whole plate underside, about 56 per cent overhead in material.

**Nothing has to flex.** A C-clip's arms must spread by roughly an eighth of the cord
diameter to admit it. Arm length scales with the cord but wall thickness does not, so the
small sizes break first: a 6 mm C-clip with a 1.5 mm wall runs past PLA yield. None of the
three parts here flexes at all; the cord goes in from the open side or the mount goes on
over it.

## Two legs is enough on the staple and the arch

The strip mount needed four studs because a stud sitting in a keyhole **slot** is a slider,
free to travel along the slot, so two of them on one line formed a hinge and the strip
twisted off. That does not apply here: these are octagonal posts in **square holes**, and
each one constrains rotation on its own. Two legs do not form a hinge.

## Shared with the strip mount

Same panel numbers throughout: 4.9643 mm pitch, 2.929 mm holes with 0.698 mm corner radii,
2.9 mm panel. Legs use the same octagonal section, so the hole's corner radii do not limit
them, and the same christmas-tree barb with three ledges at 2.9 / 3.5 / 4.1 mm, which grips
any panel from 2.3 to 4.1 mm.

Leg spacing is always a whole number of panel pitches, so the legs land on real holes; the
smallest spacing that leaves the cord room is chosen automatically.

## Print settings

```
Material      PLA
Nozzle        0.4 mm
Layer         0.2 mm
Perimeters    3
Infill        20 %
Supports      none
Orientation   as-is
```

Regenerate any size with `tools/gen_cord_clips.py`. `cord_arch()`, `cord_staple()` and
`cord_cradle()` each take the cord diameter, and optionally the leg spacing in pitches and
the width.
