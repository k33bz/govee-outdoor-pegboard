# Test-fit gauges

Print these before designing anything else. They settle the two numbers the whole mount
system depends on. Regenerate any variant with `tools/gen_gauges.py`.

## Current best numbers

| Quantity | Value | How it was established |
|---|---|---|
| Hole pitch | **3/16 in = 4.7625 mm** | measured off a flat reference photo, frame centre |
| Hole size | **2.6 to 2.8 mm square** | test print: 2.4 mm entered, 2.6 mm entered snugly |
| Web between holes | about 2.1 mm | pitch minus hole |

## Round 1 was wrong, and the failure was informative

The first gauge set bracketed 4.0 to 4.5 mm and **none of them would align**. That is not a
user error, it is the correct result for that set: at 4.2 mm pitch across a 4x4 grid the far
corner peg misses its hole by about 1.7 mm, roughly five times the available play, so pegs
1 and 16 can never both enter. No amount of wiggling fixes a pitch that is simply wrong.

The pitch came from a first photo where the tape sat well away from the region being
measured and the frame had a 19 % scale gradient. The replacement photo has the tape flat
against the panel and a much milder 4 % gradient, and it puts the pitch on 3/16 in to within
0.05 % at frame centre. See `../../MEASUREMENTS.md`.

## Print first: `peg_size_gauge.stl`

Five tabs, one peg each, at 2.0 / 2.2 / 2.4 / 2.6 / 2.8 mm. About 2.6 g, roughly 15 min.
Already run once: 2.4 entered, 2.6 entered more snugly. Reprint only if you want to check
2.8, or after changing filament or nozzle.

## Then: `pitch_gauge_4.60mm` through `pitch_gauge_5.00mm`

Six plates, each a **3x3** grid of 2.1 mm pegs. About 1.3 g and 10 min each. **Print all six
on one plate** so each layer has time to cool; the pegs are small and slump on a fast solo
print.

```
4.60  4.70  4.76  4.83  4.90     bracketing the measurement
5.00                             the metric alternative, in case the imperial read is wrong
```

`4.76` is 3/16 in exactly (4.7625 mm) and is the one expected to seat.

Three changes from round 1, all aimed at making these easier to insert:

- **3x3, not 4x4.** Two spans instead of three, so a given pitch error shows as 2d at the
  corner rather than 3d. Still resolves pitch to about 0.1 mm, which is the variant step,
  but it is far more forgiving to line up by hand.
- **2.1 mm pegs, not 1.9 mm.** The hole size is now known, so the pegs can be sized against
  a real number instead of a guess.
- **Two decimal labels**, because the interesting range is now finer than 0.1 mm.

Push each one in squarely without rocking. Expect one to seat flush and its neighbours to
bind at opposite corners. If two adjacent plates both seat, the true pitch is between them.

The pitch is embossed on the peg side and recessed into the flat side, so you can still read
it while the plate is sitting in the panel.

## Post-size fit gauges: `fit_gauge_post2.3mm` .. `post2.6mm`

**Pitch is now confirmed at 4.7625 mm (3/16 in).** These four fix the pitch and vary the
post width instead, and they are the last unknown before real mounting plates.

`peg_size_gauge` answered "what is the largest single peg that enters a hole" (2.6 mm).
That is not the same question as "what post width can a plate use", because a plate has to
enter nine holes at once and every printing and pitch tolerance stacks against you. Expect
the usable width to come out below 2.6 mm.

Print all four, insert each squarely, and pick by feel:

- **too loose** if the plate rattles or can be lifted off without resistance
- **right** if it needs a firm push, holds itself against the panel, and can be pulled off
  without tools
- **too tight** if it will not seat fully, or the panel flexes as you push

Whichever wins becomes the standard post for every mount. Report the winner and, if you can,
the panel thickness, and the mounting plates can be designed against real numbers.

## Print settings

```
Material      PLA
Nozzle        0.4 mm
Layer         0.2 mm
Perimeters    3
Infill        20 %
Supports      none
Orientation   as-is, flat on the bed, pegs up
```

## If nothing fits again

- **All six bind the same way.** The pitch is outside 4.60 to 5.00. Widen the tuple at the
  bottom of `gen_gauges.py` and reprint two or three probes rather than a full set.
- **Every plate seats loosely.** Raise `peg_w` toward 2.4 mm for a sharper result.
- **A plate seats on one axis but not the other.** The grid is not square. Say so and the
  generator can take separate x and y pitches.

## Why a grid and not one peg

The panel has roughly 2.1 mm webs and a single peg carrying real load would tear its hole.
Spreading load over 9 or more holes is the actual design, not just a measuring trick. Treat
a plate that seats well as the prototype footprint for the real mounts.
