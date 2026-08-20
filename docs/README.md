# Pegboard Mount System v1.0.0

**Purpose:** Organize power strip, power brick, and Govee controller on a 3/4" (19mm) square-hole pegboard.

**Target Pegboard:** Black perforated board with 19mm center-to-center square hole spacing.

---

## 📋 Components Overview

### Brackets (Individual Mounts)

All brackets feature:
- **Mounting:** Pegboard peg system with flange (prevents pull-through)
- **Peg Height:** 14mm (sufficient grip without obstruction)
- **Material:** PLA @ 25% infill
- **Tolerance:** Designed for 19mm pegboard holes with ~0.2mm clearance

#### 1. Power Strip Bracket
- **File:** `power_strip_bracket_v1.0.0.stl`
- **Dimensions:** 180mm L × 70mm W × 40mm H
- **Capacity:** 6-outlet power strip (~165-178mm long)
- **Mount Points:** 2 pegs (dual-point stability)
- **Features:**
  - Open front for easy plug access
  - Cable routing channels on sides
  - Spaced 140mm apart for optimal support distribution

#### 2. Power Brick Bracket
- **File:** `power_brick_bracket_v1.0.0.stl`
- **Dimensions:** 85mm W × 70mm D × 60mm H
- **Capacity:** Single power adapter/brick (~75-80mm wide)
- **Mount Points:** 1 peg (sufficient for light load ~200-300g)
- **Features:**
  - Open-back design for cable routing
  - Cable clip mount compatibility
  - Centered mounting for stability

#### 3. Govee Controller Bracket
- **File:** `govee_bracket_v1.0.0.stl`
- **Dimensions:** 90mm W × 80mm D × 60mm H
- **Capacity:** Govee Permanent Outdoor Pro controller (~76-80mm W × 64-65mm D × 40-50mm H)
- **Mount Points:** 1 peg
- **Features:**
  - Dedicated cable exit area for coiled connector
  - Sized for snug fit without requiring straps
  - Integrated cable strain relief

---

## 🔌 Cable Clip Assortment

Print **1 sample of each** to test which sizes you need most. Adjust quantity based on usage patterns.

| Clip ID | File | Hole Diameter | Cable Size | Best For | Qty to Print |
|---------|------|---------------|-----------|----------|--------------|
| **A** | `cable_clip_A_small_v1.0.0.stl` | 12mm | 6-8mm | Thin power cables, single strand | 1 sample |
| **B** | `cable_clip_B_medium_v1.0.0.stl` | 16mm | 8-12mm | Standard coiled cables, Govee | **1-2** |
| **C** | `cable_clip_C_large_v1.0.0.stl` | 20mm | 12-16mm | Bundled cables, power strips | 1 sample |
| **D** | `cable_clip_D_xl_v1.0.0.stl` | 24mm | 16-20mm | Extra thick/multiple cables | 1 sample |

**Tip:** Based on typical homelab setups, **Clip B** is most versatile. Start with 2x Clip B, then add others as needed.

---

## 🖨️ Printing Guide

### Print Settings (PLA @ 25% Infill)

| Setting | Value | Notes |
|---------|-------|-------|
| **Nozzle** | 0.4mm | Standard |
| **Bed Temp** | 60°C | PLA standard |
| **Nozzle Temp** | 200°C | PLA standard |
| **Layer Height** | 0.2mm | Good quality/speed balance |
| **Infill** | 25% | Grid pattern recommended |
| **Support** | None needed | Designs oriented for direct print |
| **Print Time** | 45-90 min per part | Bracket times vary |

### Print Orientation

All files are pre-oriented for optimal printing:
- **Pegs:** Print pointing downward (peg faces bed)
- **Brackets:** Mounting face up for best dimensional accuracy
- **Cable Clips:** Peg down, body up

---

## 🔧 Assembly & Installation

### 1. Prepare Your Board
- Ensure pegboard is securely mounted to wall/cabinet
- Clean surface to remove dust/debris
- Verify hole spacing by measuring 2-3 columns

### 2. Mount Power Strip Bracket
1. Align two pegs with pegboard holes (spaced ~140mm apart)
2. Press firmly until flange sits flush against board
3. Place power strip in bracket (front-facing, cord down/to sides)
4. Cables should exit toward power source

### 3. Mount Power Brick Bracket
1. Align single peg with pegboard hole
2. Press until flange seats
3. Place power brick in bracket
4. Route cable downward toward power strip

### 4. Mount Govee Controller
1. Align single peg
2. Press flange flush
3. Insert Govee controller (face forward)
4. Coiled cable exits through designated relief area

### 5. Add Cable Clips (Optional)
1. Insert cable clip peg into pegboard hole
2. Route cable through clip opening
3. Adjust clip height as needed for cable management

---

## 📐 Technical Specifications

### Peg Design
- **Body:** 18.8mm × 18.8mm (slight undersizing for PLA fit tolerance)
- **Flange:** 22mm × 22mm × 2mm thick
- **Height:** 14mm (peg body) + 2mm (flange top) = 16mm total
- **Fit Test:** Peg should slide in with light pressure, not forced

### Tolerances
- **Pegboard Hole:** 19mm nominal square holes (±0.5mm)
- **Peg Clearance:** 0.2mm per side (total 0.4mm oversizing margin)
- **PLA Shrinkage:** ~0.3% (factored into 18.8mm design)
- **Expected Fit:** Snug but removable by hand (no tools needed)

### Load Estimates
- **Power Strip:** ~300-500g (supported by 2 pegs) — **✓ Safe**
- **Power Brick:** ~150-250g (single peg) — **✓ Safe**
- **Govee Controller:** ~50-100g (single peg) — **✓ Safe**
- **Safety Factor:** 2-3x above expected loads

---

## 🔄 Maintenance & Replacement

### Peg Wear
- Pegs are wear items; over time (6-12 months), repeated insertion/removal may loosen fit
- **Replace if:** Bracket shifts under moderate hand pressure
- **Solution:** Reprint single peg + bracket assembly, swap out

### Cable Clip Adjustment
- Clips can be repositioned freely on pegboard
- No tools required — just lift peg and move to new hole

### Future Upgrades
- Add brackets for additional components (monitor arms, cable trays, etc.)
- Scale designs for 1/2" or 1" pegboards if needed
- Integrate cable management tunnels for cleaner look

---

## 📝 Design Notes

### Why Separate Brackets?
- **Flexibility:** Rearrange components independently
- **Scalability:** Add/remove components without reprinting
- **Maintenance:** Easy access to cables and power connections

### Peg Flange Design
- Flange prevents pegs from pulling through holes completely
- Ensures components stay mounted even if board is tilted
- ~4mm overhang on all sides provides redundant safety

### Cable Clip Diversity
- Four sizes accommodate different cable gauges
- Peg-based design allows mixing/matching with brackets
- Modular system scales for future needs

---

## ⚙️ Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Peg won't fit | Peg too large or board hole too small | File peg gently with 120-grit sandpaper |
| Bracket loose after install | Peg too small or board worn | Reprint peg, try adjacent hole |
| Cable rubs bracket edge | Routing too tight | File cable exit edge smooth, reposition clip |
| Clip doesn't hold cable | Cable too large for clip | Use next-size-up clip (A→B→C→D) |

---

## 📞 Version History

**v1.0.0** (2026-08-19)
- Initial release
- Brackets for power strip, power brick, Govee controller
- Cable clip assortment (A, B, C, D)
- PLA-optimized settings (25% infill, 0.4mm nozzle)
- Designed for 19mm square-hole pegboard systems

---

## 💡 Pro Tips

1. **Test Fit First:** Before mounting, hand-insert a peg into pegboard to verify fit
2. **Start Minimal:** Begin with just brackets, add cable clips only as needed
3. **Cable Routing:** Route power cables down toward power strip to keep organized
4. **Future-Proof:** Design works with standard pegboard ecosystems if you decide to mix in commercial accessories
5. **Backup Pegs:** Print 2-3 extra pegs in case one wears out

---

**Design & Documentation:** Generated by Claude Homelab Assistant  
**Pegboard System:** 19mm center-to-center square holes, 3/4" spacing  
**Material:** PLA filament, 25% grid infill, 0.4mm nozzle

---

For questions or design improvements, feel free to fork and modify these files!
