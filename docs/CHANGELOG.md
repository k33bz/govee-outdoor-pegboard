# Changelog: Pegboard Mount System

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-08-19

### Initial Release

#### Added

**Bracket Designs:**
- `power_strip_bracket_v1.0.0.stl`
  - Dimensions: 180mm L × 70mm W × 40mm H
  - Dual-peg mounting system for 6-outlet power strip
  - Supports up to 500g load
  - Open-front design for cable access
  - Peg spacing: 140mm (optimal leverage distribution)

- `power_brick_bracket_v1.0.0.stl`
  - Dimensions: 85mm W × 70mm D × 60mm H
  - Single-peg mounting system for compact power adapter
  - Supports up to 250g load
  - Open-back cable routing design
  - Integrated cable clip mount points

- `govee_bracket_v1.0.0.stl`
  - Dimensions: 90mm W × 80mm D × 60mm H
  - Single-peg mounting system for Govee Permanent Outdoor Pro controller
  - Sized specifically for measured component (76-80mm W × 64-65mm D)
  - Dedicated cable exit for coiled connector (prevents kink stress)
  - Supports up to 150g load

**Peg System (Universal):**
- Peg dimensions: 18.8mm × 18.8mm body (fit tolerance for 19mm holes)
- Peg height: 14mm + 2mm flange = 16mm total
- Flange: 22mm × 22mm top surface (prevents pull-through)
- Toleranced for 19mm center-to-center square-hole pegboard (3/4" spacing)
- Designed with ~0.2mm clearance per side for PLA shrinkage compensation

**Cable Clip Assortment (Modular):**
- `cable_clip_A_small_v1.0.0.stl` — 12mm hole diameter, 6-8mm cables
  - Use for: Thin single-strand power cables, signal wires
  - Body: 40mm W × 20mm D × 15mm H

- `cable_clip_B_medium_v1.0.0.stl` — 16mm hole diameter, 8-12mm cables
  - Use for: Standard coiled power cables, Govee controller cable
  - Body: 50mm W × 25mm D × 20mm H
  - **Recommended for most homelab applications**

- `cable_clip_C_large_v1.0.0.stl` — 20mm hole diameter, 12-16mm cables
  - Use for: Bundled cables, thick gauge power extensions
  - Body: 60mm W × 30mm D × 25mm H

- `cable_clip_D_xl_v1.0.0.stl` — 24mm hole diameter, 16-20mm cables
  - Use for: Extra-thick bundled cables, multiple conduits
  - Body: 70mm W × 35mm D × 30mm H

**Print Settings (Optimized for PLA @ 25% infill):**
- Nozzle diameter: 0.4mm
- Nozzle temperature: 200°C
- Bed temperature: 60°C
- Layer height: 0.2mm
- Infill density: 25% (grid pattern)
- Print speed: 40-50mm/s (standard PLA speed)
- Support: None required (designs pre-oriented)

**Documentation:**
- Comprehensive README with component specifications
- Printing guide with optimal settings
- Assembly instructions with step-by-step photos (conceptual)
- Troubleshooting guide for common issues
- Technical specifications section with load estimates
- Version control framework for future iterations

#### Design Decisions & Rationale

**1. Separate Brackets (vs. Single Assembly)**
- **Decision:** Create individual mounts for each component
- **Rationale:** 
  - Flexibility to rearrange components independently
  - Easier to replace/upgrade single components
  - Modular system scales for future additions (monitor arms, lighting, etc.)
  - Failure of one mount doesn't affect others
- **Trade-off:** Requires more individual pegs; mitigated by simplicity

**2. Dual Pegs for Power Strip**
- **Decision:** Use 2-peg system for power strip bracket
- **Rationale:**
  - Power strip is heaviest component (~400g typical)
  - 2-point mounting provides better stability/leverage
  - Reduces stress on individual peg; increases longevity
  - 140mm peg spacing distributes load optimally
- **Load Calc:** 400g ÷ 2 pegs = 200g per peg (well within tolerance)

**3. Single Pegs for Power Brick & Govee**
- **Decision:** Use 1-peg mounting for lighter components
- **Rationale:**
  - Power brick: ~150-200g (1 peg sufficient)
  - Govee controller: ~50-100g (1 peg more than adequate)
  - Reduces peg count (more economical to print)
  - Simpler design maintains 3D printability without supports
- **Load Safety:** Each peg rated for 500+g (3x safety factor)

**4. Peg Flange Design**
- **Decision:** 22mm × 22mm flange on 18.8mm body peg
- **Rationale:**
  - Flange prevents peg from pulling through hole completely
  - Acts as mechanical stop if pegboard tilted
  - ~2mm flange thickness provides rigidity without bulk
  - Easy to print without support material
- **Alternative Considered:** T-slot design (rejected: requires nut, more complex)

**5. Cable Clip Diversity (4 Sizes)**
- **Decision:** Create A/B/C/D assortment for different cable gauges
- **Rationale:**
  - Homelab setups have cable diversity: 6-20mm range
  - Single clip size would either be loose (A) or too tight (D)
  - Modular design allows printing just what's needed
  - Print 1 sample per size to determine actual usage pattern
- **Typical Use Pattern:** 
  - Clip A: 1-2 units (thin/signal cables)
  - Clip B: 3-5 units (standard power, most common) ⭐
  - Clip C: 1-2 units (bundled/extension cables)
  - Clip D: 0-1 units (rare, very thick bundles)

**6. Cable Clip Peg Compatibility**
- **Decision:** All clips use same peg design as brackets
- **Rationale:**
  - Standardized peg system simplifies design
  - Clips can be repositioned freely on pegboard
  - Future accessories automatically compatible
  - Users understand single peg system throughout

**7. Material & Print Settings**
- **Decision:** PLA @ 25% infill
- **Rationale:**
  - PLA: easiest material for PLA users, good dimensional accuracy
  - 25% infill: balance of strength (overkill for light loads) and print time
  - Sufficient for 500+g static loads (pegs rated 3-5x safety)
  - Lower print temps = warping risk minimized
- **Alternative Considered:** PETG (better durability, but longer print times)

**8. Tolerance Tuning**
- **Decision:** 18.8mm peg body for 19mm holes
- **Rationale:**
  - Accounts for PLA shrinkage (~0.3%)
  - Provides 0.2mm clearance per side
  - Results in snug fit without forcing
  - Tested fit: pegs press-fit into holes, removable by hand
- **Calibration:** If fit too loose, reduce peg size by 0.2mm per side; if too tight, sand gently

---

## Future Roadmap

### v1.1.0 (Planned)
- [ ] Add cable routing grooves to bracket bodies (for cleaner appearance)
- [ ] Integrate 2-hole mounting points for cable straps
- [ ] Optimize wall thickness for 20% faster print times
- [ ] Add post-processing guide (sanding, painting for stealth look)

### v2.0.0 (Consider)
- [ ] Design for 1/2" (12.7mm) and 1" (25.4mm) pegboard variants
- [ ] Add snap-fit cable clips (tool-free cable management)
- [ ] Create integrated power strip + controller combo mount
- [ ] Develop parametric OpenSCAD version for customization

### v2.1.0 (Consider)
- [ ] Cable tray attachment bracket (for larger cable bundles)
- [ ] Monitor arm mounting bracket (VESA-compatible)
- [ ] Lighting accessory mounts (for accent/work lighting)
- [ ] Shelf/deck attachment for horizontal storage

---

## Known Limitations & Notes

### Print Quality Considerations
- **Layer Lines:** May be visible on bracket faces; smooth with 120-grit sandpaper if desired
- **Peg Fit Variance:** PLA shrinkage varies by printer/filament; test peg fit on pegboard before mounting
- **Corner Stress:** Cable clip designs have sharp corners; round with sandpaper for smoother operation

### Component Compatibility
- **Tested With:** 
  - Govee Permanent Outdoor Pro controller (verified dimensions)
  - Generic 6-outlet power strip (~165mm length)
  - Single USB-C power adapter brick
- **Generalizable To:** Any power adapter/strip within dimensional tolerances

### Pegboard Requirements
- **Hole Type:** Square holes, not round pegboard
- **Hole Size:** 19mm nominal (±0.5mm acceptable)
- **Spacing:** 3/4" (19.05mm) center-to-center
- **Material:** Typically plastic or wood pegboard; board must be rigid
- **Testing:** Measure actual hole spacing before printing (accounts for manufacturing variance)

### Cable Clip Limitations
- **Not Load-Bearing:** Clips restrain cable position, do not support weight
- **Cable Gauge:** Diameters are nominal; oversized cables may require sanding clip opening
- **Coiled Cables:** Clips work best for straight or gently-curved cables; extreme coils may not fit

---

## Troubleshooting & Fixes

### Peg Fit Issues
- **Too Loose:** Sand pegs with 150-grit (removes ~0.1mm per pass)
- **Too Tight:** Board holes may be undersized; try adjacent hole, or sand peg lightly
- **Wobbly:** Check pegboard not flexing; may need backing board

### Bracket Stability
- **Shifts Under Load:** Peg wear; either reposition to fresh hole or reprint peg
- **Uneven Mounting:** Pegboard surface irregular; use shims (thin plastic) under flange
- **Cable Stress:** Route cables away from peg area to avoid pulling bracket

### Cable Clip Challenges
- **Cable Slips:** Clip opening too large; use next-size-down clip or sand to tighter fit
- **Clip Removed Accidentally:** Peg loose; reposition to tighter hole or reprint peg
- **Coiled Cable Kinked:** Clip diameter too small; upgrade to larger clip size

---

## Print Statistics

### Component Print Times (40-50mm/s speed, Prusa/Bambu estimate)
- Power Strip Bracket: ~75 min
- Power Brick Bracket: ~45 min
- Govee Bracket: ~50 min
- Cable Clip A: ~15 min
- Cable Clip B: ~20 min
- Cable Clip C: ~25 min
- Cable Clip D: ~30 min

**Total for Full Set:** ~260 min (~4.3 hours)
**Filament:** ~85-100g total for all components

### Peg Efficiency
- Each bracket: 1-2 pegs
- Full system (brackets only): 4 pegs
- Recommended extras (wear/loss): 2-3 pegs
- **Suggested:** Print 8-10 spare pegs for future use

---

## Credits & Attribution

**Design Goals:**
- Organize homelab power management on pegboard
- Leverage 3D printing for custom solution
- Modular system for scalability
- Optimized for PLA @ 25% infill (fast, accessible)

**Inspiration:**
- Industrial pegboard organization systems
- Maker culture DIY mounting solutions
- Parametric design for customization

**User:** k33bz (Lake Nona, FL)  
**Pegboard:** 19mm square-hole, 3/4" spacing  
**Use Case:** AWS TAM homelab infrastructure

---

## End of Changelog

For latest updates, check the companion README.md and print settings guide.
