# Test-fit gauges

Print these before designing anything else. They settle the two numbers the whole mount
system depends on. Regenerate any variant with `tools/gen_gauges.py`.

Measured from the reference photos: **pitch 4.23 mm**, **hole about 2.5 mm square**. The
pitch is good to roughly +/-0.1 mm, the hole size less so, which is exactly why these are
two separate gauges rather than one.

## Print first: `peg_size_gauge.stl`

Five tabs, one peg each, at 2.0 / 2.2 / 2.4 / 2.6 / 2.8 mm. About 2.6 g, roughly 15 min.

Push each peg into any single hole. The largest one that enters without forcing is your
hole size. Test one tab at a time; they are separate parts on purpose so a neighbouring
peg cannot foul the panel.

## Then: `pitch_gauge_4.0mm` through `pitch_gauge_4.5mm`

Six plates, 0.1 mm apart, each a 4x4 grid of 1.9 mm pegs. About 1.6 g and 10 min each, so
roughly an hour for all six. **Print all six on one plate** so each layer has time to cool
before the next; the pegs are small and will slump on a fast solo print.

The pegs are deliberately undersized so hole size cannot influence the result. Only pitch
can bind. A 4x4 grid spans three pitches, so an error of d shows as 3d at the far corner:
with about 0.3 mm of play, the grid resolves pitch to roughly +/-0.1 mm, which is why the
variants step by exactly that.

Push each one in squarely, without rocking. Expect one to seat flush and its neighbours to
bind at opposite corners. If two adjacent plates both seat, the true pitch is between them.

The pitch is embossed on the peg side and recessed into the flat side, so you can still
read it while the plate is sitting in the panel.

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

Leave horizontal expansion / XY compensation at your normal value. The pegs are drawn
undersized on the assumption that PLA prints posts about 0.1 mm oversize; if your printer
is dialled in differently, the peg size gauge will show it.

## If nothing fits

- **No pitch plate seats, and even the 2.0 mm peg is tight.** Holes are smaller than
  measured. Rerun `gen_gauges.py` with a smaller `peg_w` in `pitch_gauge()`.
- **Every pitch plate seats loosely.** Pegs are too far undersized to discriminate. Raise
  `peg_w` to just under the size the peg gauge reported and reprint.
- **True pitch is outside 4.0 to 4.5.** Widen the tuple at the bottom of `gen_gauges.py`.

## Why a grid and not one peg

The panel has roughly 1.5 mm webs between holes and about 35 % open area, so a single peg
carrying real load would tear its hole. Spreading load over 16 holes is the actual design,
not just a measuring trick. Treat a plate that seats well as the prototype footprint for
the real mounts.
