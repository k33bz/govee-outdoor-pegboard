# Cord staples

A bridge over the cord with barbed legs into the panel. Lay the cord on the panel, push the
staple down over it.

| file | legs | clear gap | standoff | size | mass |
|---|---|---|---|---|---|
| `cord_staple_04mm` | 2 pitches | 6.33 mm | 4.30 mm | 15.5 x 6.0 x 12.6 | 0.42 g |
| `cord_staple_06mm` | 3 pitches | 11.29 mm | 6.30 mm | 20.5 x 6.0 x 14.6 | 0.55 g |
| `cord_staple_08mm` | 3 pitches | 11.29 mm | 8.30 mm | 20.5 x 6.0 x 16.6 | 0.60 g |
| `cord_staple_10mm` | 3 pitches | 11.29 mm | 10.30 mm | 20.5 x 6.0 x 18.6 | 0.65 g |
| `cord_staple_13mm` | 4 pitches | 16.26 mm | 13.30 mm | 25.5 x 6.0 x 21.6 | 0.81 g |

**10 mm is the measured power cord.** Leg spacing is always a whole number of panel pitches,
so the legs land on real holes; the smallest spacing that leaves the cord room is chosen
automatically.

## Why a staple and not a clip

The first attempt was a two-piece C-clip: a base plate with posts, and a separate clip that
socketed into it. A staple is better on every count.

**One piece, no supports, no glue.** A C-clip has to hold the cord in *front* of the plate
while the posts point *into* the panel, so the features land on opposite faces and no single
part can print flat. That forces either a two-piece assembly with a glue joint, or supports
under the whole plate underside, which measured at about 56 per cent overhead in material. A
staple puts the legs and the cord on the same side, so it prints bridge-down with the legs up
and has no overhang anywhere in it.

**Nothing has to flex.** A C-clip's arms must spread by roughly an eighth of the cord diameter
to admit it. Arm length scales with the cord but wall thickness does not, so the small sizes
are the ones that break: a 6 mm C-clip with a 1.5 mm wall runs past PLA yield. A staple flexes
nothing at all; it goes on over the cord.

**The standoff is set by geometry, not by feel.** The shoulder is 3.6 mm across, wider than
the 2.929 mm hole, so it bottoms on the panel face. The gap under the bridge is what was
designed rather than however far it happened to get pushed.

## Two legs is enough here

The strip mount needed four studs because a stud sitting in a keyhole **slot** is a slider,
free to travel along the slot, so two of them on one line formed a hinge and the strip twisted
off. That does not apply here: these are octagonal posts in **square holes**, and each one
constrains rotation on its own. Two legs do not form a hinge.

## Shared with the strip mount

Same panel numbers throughout: 4.9643 mm pitch, 2.929 mm holes with 0.698 mm corner radii,
2.9 mm panel. Legs use the same octagonal section, so the hole's corner radii do not limit
them, and the same christmas-tree barb with three ledges at 2.9 / 3.5 / 4.1 mm, which grips
any panel from 2.3 to 4.1 mm.

## Two options, and they are not the same job

| | staple | cradle |
|---|---|---|
| cord | **captive** | **lays in, lifts out** |
| to reroute | pull the staple out of the panel | just lift the cord |
| mass | 0.42 - 0.81 g | 1.4 - 1.7 g |
| supports | none | none |
| glue | none | none |

**Use a staple where the run is settled** and you want it to stay put: the strip's
power cord, anything crossing a busy area.

**Use a cradle where you expect to change things**: a bundle you add to, a lead you
unplug, anything you would rather not dismantle a mount to move.

## `cord_cradle_06 / 10 / 13mm.stl`

Open-top cradle on a back pad with four legs. Prints cradle-up.

Both of your ideas are in this one. **The flat bottom** is what makes it printable
cradle-up: a U resting on its curve touches the bed on a line, whereas flattened it has
real first-layer area. **The arms curl 22 degrees past the horizontal** so they rise above
the cord's centreline and it cannot roll out, while staying well inside 45 degrees of
inward lean so every layer is still self-supporting.

**On supports:** the answer is yes it works, but it does not need them. Opening up and
legs into the panel are *perpendicular*, not opposite, so one piece is possible. That
leaves the legs as horizontal cantilevers, which normally print badly. Rotating the
octagonal leg so a **vertex points down** makes it self-support at 45 degrees, and because
an octagon's fit is set by its inscribed circle, rotating it does not change the hole fit
at all. Printing legs-up instead would hang the cradle under the plate and cost about
56 per cent of the part mass in support.

Four legs in two rows, not two: the cord's weight acts on a lever arm out from the panel,
and a single row would let the cradle rock. Two rows react it as a couple.

## Print settings

```
Material      PLA
Nozzle        0.4 mm
Layer         0.2 mm
Perimeters    3
Infill        20 %
Supports      none
Orientation   as-is, bridge on the bed, legs up
```

Regenerate any size with `tools/gen_cord_clips.py`; `cord_staple()` takes the cord diameter,
and optionally the leg spacing in pitches and the bridge width.
