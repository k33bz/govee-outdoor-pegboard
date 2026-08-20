# Panel measurements from the reference photos

Derived from a reference photo of the panel with a tape measure laid across it. The photo
itself is not included in this repository.

## Result

| Quantity | Measured | v1.0.0 docs claim |
|---|---|---|
| Hole pitch | **4.2 mm** (0.167 in, 6 per inch) | 19.05 mm (3/4 in) |
| Hole size | **~2.5 mm square** (2.3 x 2.7) | 19 mm square |
| Web between holes | ~1.5 mm | n/a |
| Open area | ~35 % | n/a |

The published peg is 18.8 x 18.8 mm with a 22 mm flange. That peg is **4.4 hole pitches
wide** and roughly 7x the width of a single hole, so it cannot enter this panel at all.
This is not a tolerance problem, it is the wrong attachment concept.

## Method

A single global px-per-inch is wrong here: the panel is tilted relative to the sensor, so
scale varies across the frame. Fitting the tape edges gives a 1.9 to 2.5 degree tilt and
4.7 % foreshortening across the frame, and the measured 1/16 in tick spacing runs from
35.0 px on the left to 41.5 px on the right, a 19 % gradient.

1. Fit the tape's top and bottom edges, then resample the tape band to constant height to
   remove the tilt.
2. Detect graduation ticks and their lengths. Autocorrelating the tick-length sequence
   peaks at lag 16, with sub-peaks at 8 and 4, confirming the finest graduation is 1/16 in
   rather than 1/8 in.
3. Fit local 1/16 in spacing as s(x) = 0.002812x + 34.53 px (residual 0.44 px, 1.2 %).
   Cumulative inches are then I(x) = ln(s(x))/(16 * 0.002812).
4. Measure hole pitch by autocorrelation in patches, gated on correlation >= 0.5 to reject
   patches occluded by the cable and the white clip.
5. Compare hole pitch against tick spacing **at the same x and adjacent y**, using the
   pegboard immediately below the tape so nothing is extrapolated.

## Verification

Rendering the model's inch lines back over the tape puts them on the inch marks. Taking a
one-inch span next to the tape and marking hole columns inside it yields exactly 6, which
is 25.4 / 6 = 4.23 mm, independent of any fitted model.

## Correction

An earlier pass reported a pitch of about 5.4 mm. That figure was wrong. It assumed one
constant 608 px per inch across the whole frame, which accumulates error toward the right
of the image and lands the 3 to 4 inch interval visibly off by roughly 1/8 in. The
corrected value is 4.2 mm.
