# LED power brick mount

**Status: designed, not cut.** The brick has not been measured, so there are no STLs here
yet. Everything below is settled; only the numbers are missing.

The brick has no mounting features of its own, so it has to be trapped rather than fastened:
a shelf under it, a clip on each side, and a clip over the top.

## No back plate, and why that is the ventilated answer

The brief asked for vent holes in a back plate. The enclosure's own mounting panel is
**34.8 % open** already, 2.929 mm holes on a 4.9643 mm pitch, which is better than most
perforated sheet is rated at. Anything put behind the brick sits between it and that free
area, so a vented back plate does not add ventilation, it subtracts it. The best back plate
here is no back plate.

Instead the brick stands **4 mm off the panel** on the clips. That gap is what turns the
panel's existing holes into an air path: the enclosure has a thermostat and fan, so air is
moving, and the standoff lets it sweep the brick's back face and leave through the panel
rather than stagnating against it.

## One part, routed around the brick and not across it

The four clips are linked into a single part by a **perimeter frame** rather than left loose,
so the assembly installs as one unit and cannot be misaligned on the grid.

A frame, not a spine. A rib across the back of the brick would tie the clips together just as
well but would shadow roughly 12 % of the brick's footprint. Running the same link around the
brick's edge instead covers **none** of it, uses only grid holes that were outside the
brick's shadow anyway, and is stiffer, because a closed loop resists twist where a single rib
does not.

## Retention

| part | rigid or sprung | job |
|---|---|---|
| shelf | rigid | carries the weight in bearing, not friction |
| side clips x2 | rigid | hook the front corners, stop it coming forward |
| top clip | **sprung** | snaps over, stops it lifting; the only part that flexes |

The brick drops down into the rigid three and the top clip closes over it. Nothing has to
flex during normal service, and getting the brick out means popping one clip rather than
dismantling a mount off the panel.

## Two rows of posts, not one

By the rule in `models/cord_clips/README.md`: load sitting **on** the panel needs one row,
load standing **off** it needs two. The brick is a box held at a standoff, so its weight is
cantilevered exactly like the cord cradle's and every clip takes two rows.

## Print orientation

Features that hold something off a wall are necessarily on the opposite face from the posts
that go into the wall, which is what made the first cord clip attempt a two-piece assembly.
The fix here is the same one the cradle uses: print the frame **standing on the shelf's
ledge**, so the L of shelf-and-back lies with one leg on the bed and the other vertical, with
no overhang between them. That leaves the posts as horizontal cantilevers, which is fine
because an octagonal post rotated **vertex down** self-supports at 45 degrees, and an
octagon's fit is set by its inscribed circle so rotating it does not change the hole fit.

## Still needed before this can be cut

- brick length, width and depth
- which face the mains cord leaves from, and which face the DC lead leaves from
- whether the back face is flat, or ribbed or curved
