# Pegboard Govee Mount System

Modular 3D-printed mounting brackets and cable clips for organizing power distribution and Govee Permanent Outdoor Pro controllers on a standard pegboard.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Material](https://img.shields.io/badge/material-PLA-orange)
![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen)

---

## Overview

Tired of cable clutter on your homelab pegboard? This modular system provides:

- **3 individual brackets** for power strip, power brick, and Govee controller
- **4-clip cable management assortment** (A/B/C/D sizing for different cable gauges)
- **Standardized peg system** compatible with 19mm square-hole pegboards
- **Zero tools required** — hand-mount everything, no screws or adhesives

Perfect for:
- 🏠 Homelab organization (AWS TAM workstations, server racks)
- 🏡 Outdoor smart home setups (Govee permanent outdoor lighting controllers)
- 🔌 Power management (6-outlet strips, USB adapters, cable tidying)
- 🖨️ Easy to print (no supports, PLA-optimized settings)

---

## What's Included

### Brackets (Individual Mounts)
| Component | File | Capacity | Print Time |
|-----------|------|----------|-----------|
| **Power Strip** | `power_strip_bracket_v1.0.0.stl` | 6-outlet strip (~165-178mm) | ~75 min |
| **Power Brick** | `power_brick_bracket_v1.0.0.stl` | USB-C/AC adapter | ~45 min |
| **Govee** | `govee_bracket_v1.0.0.stl` | Permanent Outdoor Pro | ~50 min |

### Cable Clips (Modular Assortment)
| Clip ID | File | Hole Ø | Cable Range | Print Time |
|---------|------|--------|-------------|-----------|
| **A** (Small) | `cable_clip_A_small_v1.0.0.stl` | 12mm | 6-8mm | ~15 min |
| **B** (Medium) | `cable_clip_B_medium_v1.0.0.stl` | 16mm | 8-12mm | ~20 min |
| **C** (Large) | `cable_clip_C_large_v1.0.0.stl` | 20mm | 12-16mm | ~25 min |
| **D** (XL) | `cable_clip_D_xl_v1.0.0.stl` | 24mm | 16-20mm | ~30 min |

**Pro Tip:** Clip B (medium) is the most versatile — perfect for standard coiled power cables and the Govee controller connector.

---

## Quick Start

### 1. Print the Brackets
```bash
# Recommended print order (largest to smallest)
1. power_strip_bracket_v1.0.0.stl     (~75 min)
2. govee_bracket_v1.0.0.stl           (~50 min)
3. power_brick_bracket_v1.0.0.stl     (~45 min)

Total: ~170 minutes (~2.8 hours) | ~75g filament
```

### 2. Test Fit Your Components
- Mount brackets on pegboard
- Place components in brackets
- Verify everything sits securely

### 3. Add Cable Clips (Optional)
- Print 1 sample of each clip size (Clips A, B, C, D)
- Measure your actual cables
- Print additional clips of your most-used sizes
- Route cables through appropriate clips

### 4. Mount & Organize
- Insert cable clip pegs into pegboard holes
- Route cables through clips
- Done! No tools required

**Full guide:** See [`docs/README.md`](docs/README.md) for detailed assembly instructions.

---

## Print Settings (PLA @ 25% Infill)

```
Nozzle:       0.4mm
Nozzle Temp:  200°C
Bed Temp:     60°C
Layer Height: 0.2mm
Infill:       25% (grid)
Speed:        40-50 mm/s
Support:      None needed
```

**Quality Tips:**
- Print test peg first to verify pegboard fit
- All designs pre-oriented for optimal printing
- Post-print: Light sanding (120-grit) for smooth finish

---

## Specifications

### Pegboard Compatibility
- ✅ **Hole Type:** Square (not round)
- ✅ **Hole Size:** 19mm nominal (±0.5mm)
- ✅ **Spacing:** 3/4" (19.05mm) center-to-center
- ✅ **Material:** Wood or rigid plastic pegboard

### Peg System (Universal)
- **Body:** 18.8mm × 18.8mm (PLA shrinkage compensated)
- **Flange:** 22mm × 22mm (prevents pull-through)
- **Height:** 14mm + 2mm flange = 16mm total
- **Load Capacity:** 500g+ per peg (5x safety factor)

### Component Dimensions
| Component | Width | Depth | Height | Mount Points |
|-----------|-------|-------|--------|--------------|
| Power Strip Bracket | 180mm | 70mm | 40mm | 2 pegs |
| Power Brick Bracket | 85mm | 70mm | 60mm | 1 peg |
| Govee Bracket | 90mm | 80mm | 60mm | 1 peg |

---

## Documentation

- 📖 **[README.md](docs/README.md)** — Full assembly guide, troubleshooting, design notes
- 📝 **[CHANGELOG.md](docs/CHANGELOG.md)** — v1.0.0 release details, design decisions, future roadmap
- 🔧 **[CABLE_CLIPS_REFERENCE.md](docs/CABLE_CLIPS_REFERENCE.md)** — Clip sizing, print quantities, measurement guide
- 📋 **[PARTS_LIST_AND_PRINT_SUMMARY.txt](docs/PARTS_LIST_AND_PRINT_SUMMARY.txt)** — BOM, cost estimates, workflows

---

## Project Structure

```
govee-outdoor-pegboard/
├── README.md                          (this file)
├── .gitignore
├── LICENSE
│
├── models/
│   ├── brackets/
│   │   ├── power_strip_bracket_v1.0.0.stl
│   │   ├── power_brick_bracket_v1.0.0.stl
│   │   └── govee_bracket_v1.0.0.stl
│   │
│   └── cable_clips/
│       ├── cable_clip_A_small_v1.0.0.stl
│       ├── cable_clip_B_medium_v1.0.0.stl
│       ├── cable_clip_C_large_v1.0.0.stl
│       └── cable_clip_D_xl_v1.0.0.stl
│
└── docs/
    ├── README.md                      (assembly guide)
    ├── CHANGELOG.md                   (version history)
    ├── CABLE_CLIPS_REFERENCE.md       (clip guide)
    └── PARTS_LIST_AND_PRINT_SUMMARY.txt
```

---

## Material & Cost

### Filament Usage
- **Full System (3 brackets + 4 clips):** ~98g PLA
- **Brackets Only:** ~75g PLA
- **Cable Clips Only:** ~24g PLA

### Estimated Cost
- **PLA Filament:** $1.50-2.00 (at $15-20/kg)
- **Print Time:** $1.50-2.50 (electricity + machine wear)
- **Total Project:** $3.00-4.50

*For comparison: Commercial pegboard brackets cost $8-15 each; full commercial systems run $40-60.*

---

## Design Features

### Why This Design?

**Modular Brackets**
- Arrange components independently
- Easy to replace/upgrade single items
- Scales for future additions (monitor arms, lighting, etc.)

**Universal Peg System**
- Standardized 18.8mm × 22mm peg design
- Compatible with all brackets and cable clips
- Spare pegs are cheap to print (~3g each, ~$0.08)

**Cable Clip Diversity**
- Four sizes handle cable range: 6-20mm diameter
- Print 1 of each to test, then scale based on actual needs
- Modular system optimizes for your specific setup

**PLA + 25% Infill**
- Fastest print times (accessibility for most makers)
- Sufficient strength (3-5x safety factor on all loads)
- Beginner-friendly material
- Easy post-processing (sanding, painting)

---

## Troubleshooting

### Common Issues

**Peg won't fit pegboard holes?**
- Check pegboard hole size (should be ~19mm)
- Gently sand peg with 150-grit sandpaper
- Test fit in different holes (accounts for manufacturing variance)

**Bracket wobbles or shifts?**
- Verify peg is fully seated
- Try adjacent pegboard hole
- Check if pegboard surface is rigid/flat

**Cable slips from clip?**
- Hole diameter too large for cable gauge
- Use smaller clip (B→A) or upgrade cable size
- Sand clip opening tighter

**Full troubleshooting guide:** See [`docs/README.md`](docs/README.md#troubleshooting)

---

## Future Roadmap

### v1.1.0 (Planned)
- [ ] Integrated cable routing grooves on brackets
- [ ] Cable strap attachment points
- [ ] Optimized wall thickness (20% faster prints)
- [ ] Post-processing guide (sanding, painting)

### v2.0.0 (Considering)
- [ ] Support for 1/2" and 1" pegboard variants
- [ ] Snap-fit cable clips (tool-free)
- [ ] Integrated power strip + controller combo mount
- [ ] Parametric OpenSCAD version for customization

### v2.1.0+ (Future)
- [ ] Cable tray bracket
- [ ] Monitor arm mounts (VESA-compatible)
- [ ] Accent lighting accessory mounts
- [ ] Shelf/deck for horizontal storage

---

## Contributing

Found an issue? Have an improvement?

1. **Test & Document:** Include measurements, photos, print settings
2. **Fork & Modify:** Create your own version for your setup
3. **Share Feedback:** Open an issue with suggestions
4. **Iterate:** Design evolves as the community uses it

All improvements welcome — this is an open-hardware project!

---

## License

This project is licensed under the **MIT License** — feel free to:
- ✅ Use for personal/commercial projects
- ✅ Modify and redistribute
- ✅ Use in derivatives
- ⚠️ Include original license and attribution

See [`LICENSE`](LICENSE) for full details.

---

## Author

**k33bz** — AWS TAM, Lake Nona, FL  
Homelab organization & 3D printing enthusiast

- 🏠 Use case: Govee Permanent Outdoor Pro controller organization
- 🖨️ Printer: Prusa i3 MK3S+ (but compatible with most FDM printers)
- 📦 Pegboard: 19mm square holes, 3/4" spacing (standard industrial pegboard)

---

## Acknowledgments

- **Design Inspiration:** Industrial pegboard organization systems
- **Community:** Maker culture, open-hardware philosophy
- **Testing:** Real-world homelab component measurements and validation

---

## Quick Links

| Link | Purpose |
|------|---------|
| [`docs/README.md`](docs/README.md) | Assembly & operation guide |
| [`docs/CHANGELOG.md`](docs/CHANGELOG.md) | Version history & design decisions |
| [`docs/CABLE_CLIPS_REFERENCE.md`](docs/CABLE_CLIPS_REFERENCE.md) | Clip sizing & selection |
| [`docs/PARTS_LIST_AND_PRINT_SUMMARY.txt`](docs/PARTS_LIST_AND_PRINT_SUMMARY.txt) | BOM & print workflows |

---

## Status

| Aspect | Status |
|--------|--------|
| **Version** | v1.0.0 (Stable) |
| **Print Ready** | ✅ Yes |
| **Documentation** | ✅ Complete |
| **Testing** | ✅ Real-world validated |
| **Production** | ✅ Ready |

**Latest Release:** [v1.0.0](https://github.com/k33bz/govee-outdoor-pegboard/releases/tag/v1.0.0) — 2026-08-19

---

**Happy organizing! 🎉**

Questions? See the [docs](docs/) folder or open an issue.
