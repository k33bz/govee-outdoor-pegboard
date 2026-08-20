# Cable Clip Assortment Reference Guide v1.0.0

Quick reference for 4-clip system: Test print 1 of each, then scale based on actual needs.

---

## 📊 Clip Specifications at a Glance

### Clip A: SMALL
```
File:        cable_clip_A_small_v1.0.0.stl
Hole Ø:      12mm
Cable Range: 6-8mm diameter
Body Size:   40mm W × 20mm D × 15mm H
Print Time:  ~15 minutes
Use Cases:   • Thin power cables (2-pin)
             • Signal wires (audio/data)
             • Individual wire strands
             • Charger cords (thin profile)
Color Hint:  🟦 BLUE (cool/signal cables)
Qty First:   1 sample (→ may need 0-2 total)
```

**Best For:** Minimal cable runs, signal management, workspace isolation

---

### Clip B: MEDIUM ⭐ MOST USEFUL
```
File:        cable_clip_B_medium_v1.0.0.stl
Hole Ø:      16mm
Cable Range: 8-12mm diameter
Body Size:   50mm W × 25mm D × 20mm H
Print Time:  ~20 minutes
Use Cases:   • Govee controller coiled cable ✓ PRIMARY
             • Standard power strips (single cable)
             • USB extension cables (bundled)
             • Ethernet bundles (2-3 strands)
             • Most homelab component cables
Color Hint:  🟨 YELLOW (standard/common)
Qty First:   1-2 samples (→ likely need 3-5 total)
```

**Best For:** General-purpose cable management, most versatile size

**Govee Controller Specific:**
- Coiled connector measures ~10mm diameter when coiled
- Clip B provides comfortable fit without kinks
- Recommended: Mount 1 Clip B adjacent to Govee bracket
- Route coiled cable through clip for tension relief

---

### Clip C: LARGE
```
File:        cable_clip_C_large_v1.0.0.stl
Hole Ø:      20mm
Cable Range: 12-16mm diameter
Body Size:   60mm W × 30mm D × 25mm H
Print Time:  ~25 minutes
Use Cases:   • Bundled power cables (3+ wires)
             • Extension cord packs
             • Heavy-gauge power supplies
             • Cable sleeves (wrapped bundles)
             • Right-angle adapters (thick plugs)
Color Hint:  🟧 ORANGE (thick/industrial)
Qty First:   1 sample (→ may need 1-2 total)
```

**Best For:** Organizing bundled cables, power extensions, heavy components

---

### Clip D: EXTRA LARGE
```
File:        cable_clip_D_xl_v1.0.0.stl
Hole Ø:      24mm
Cable Range: 16-20mm diameter
Body Size:   70mm W × 35mm D × 30mm H
Print Time:  ~30 minutes
Use Cases:   • Multiple cables bundled together
             • Conduit/sleeve bundles
             • Right-angle power connector blocks
             • Heavy industrial extension cords
             • Future: cable trays/large accessories
Color Hint:  🔴 RED (extra/large/priority)
Qty First:   1 sample (→ may need 0-1 total, rare)
```

**Best For:** Unusual oversized cables, future accessories, bulk cable routing

---

## 🎯 Typical Homelab Print Plan

### Phase 1: Initial Testing (Print 1 of Each)
**Print Time: ~90 minutes | Filament: ~12-15g | Cost: ~$0.30-0.50**

```
Print Queue:
  □ cable_clip_A_small_v1.0.0.stl      [~15 min]  (test fit: thin cables)
  □ cable_clip_B_medium_v1.0.0.stl     [~20 min]  (test fit: Govee cable)
  □ cable_clip_C_large_v1.0.0.stl      [~25 min]  (test fit: bundled)
  □ cable_clip_D_xl_v1.0.0.stl         [~30 min]  (test fit: future)
```

**After Testing:** Determine actual usage pattern, proceed to Phase 2

---

### Phase 2: Production Printing (Recommended)

#### Scenario A: Minimal Setup (Govee Only)
```
Qty Needed:
  • Clip B: 2 units (1 for Govee controller, 1 for spare)
  
Print Time: ~40 min
Filament: ~6g
```

#### Scenario B: Standard Homelab (Recommended)
```
Qty Needed:
  • Clip A: 2 units (thin cables, spares)
  • Clip B: 4 units (Govee + 3 more for main cables)  ⭐ PRIMARY
  • Clip C: 2 units (bundled power)
  • Clip D: 1 unit (future/spare)
  
Print Time: ~175 min (~3 hours)
Filament: ~45-50g
Total Cost: ~$1.20-1.50
```

#### Scenario C: Elaborate Setup (Maximum Cable Management)
```
Qty Needed:
  • Clip A: 4 units (signal management)
  • Clip B: 8 units (main cables, extras)        ⭐ BULK
  • Clip C: 4 units (bundled/extensions)
  • Clip D: 2 units (future-proofing)
  
Print Time: ~360 min (~6 hours)
Filament: ~90-100g
Total Cost: ~$2.40-3.00
```

---

## 🔧 How to Measure Your Cables

Before deciding final quantities, measure your actual cables:

### Quick Measurement Guide
```
Use dial calipers or ruler:

Thin cables (Clip A):
  • iPhone charger: ~5-6mm
  • Single USB cable: ~6-7mm
  • Cat6 Ethernet: ~5-6mm
  ➜ Need Clip A?

Standard cables (Clip B):
  • Coiled power (Govee): ~10mm ✓ PERFECT FIT
  • Power strip plug: ~8-10mm ✓ GOOD FIT
  • Bundled 2-3 wires: ~10-12mm ✓ GOOD FIT
  ➜ Need Clip B? (most likely YES)

Thick cables (Clip C):
  • Right-angle power plug: ~12-14mm
  • Extension cord (heavy gauge): ~13-16mm
  • 4+ bundled wires: ~14mm+
  ➜ Need Clip C?

Extra thick (Clip D):
  • Conduit/sleeved bundle: ~16-20mm
  • Industrial extension: ~18-20mm+
  • Multiple power cables together: ~20mm+
  ➜ Need Clip D? (rare)
```

---

## 🎨 Clip Painting Guide (Optional)

For easier visual identification, paint clips by size:

| Clip | Suggested Color | Rationale |
|------|-----------------|-----------|
| A | 🔵 Blue | Cool/thin/delicate |
| B | 🟡 Yellow | Standard/common/primary |
| C | 🟠 Orange | Thick/heavy/industrial |
| D | 🔴 Red | Extra-large/rare |

**Application:** Spray paint after printing, use acrylic for PLA (or Plastidip for durability)

---

## 📦 Storage & Organization

After printing your clips:

```
Cabinet/Bin Organization:
┌─────────────────────────────────┐
│ Pegboard Clips Storage Box       │
├─────────────────────────────────┤
│ □ Clips A (small)      [Qty: __ ]│  🔵 Blue box
│ □ Clips B (medium)     [Qty: __ ]│  🟡 Yellow box (most)
│ □ Clips C (large)      [Qty: __ ]│  🟠 Orange box
│ □ Clips D (XL)         [Qty: __ ]│  🔴 Red box
│ □ Extra pegs           [Qty: __ ]│  ⚪ White box
├─────────────────────────────────┤
│ Inventory Last Updated: _______  │
└─────────────────────────────────┘
```

---

## 🚀 Advanced Usage: Clip Stacking

**Pro Tip:** Stack compatible clips for oversized cables!

### Stacking Strategy
```
Problem: Cable diameter 13-15mm (between Clip B and C?)

Solution: Stack two Clip B's vertically!
  • Mount first Clip B in pegboard hole
  • Mount second Clip B above (in hole ~19mm up)
  • Route 14mm cable through both
  • Double-clip provides better grip + visual interest

Advantages:
  ✓ Custom-sized solution without reprinting
  ✓ More secure grip for delicate routing
  ✓ Looks intentional/professional
  
Limitation:
  ✗ Uses two pegboard holes
  ✗ Cable must be accessible from front
```

---

## 📋 Installation Checklist

When adding cables clips to your board:

```
□ Measure cable diameter with calipers/ruler
□ Identify appropriate clip size (A/B/C/D)
□ Check if you have spare clip of that size
□ If not in inventory, print 1-2 units
□ After print, test fit cable in clip opening
□ Locate empty pegboard hole near cable path
□ Insert clip peg into hole (press until flush)
□ Route cable through clip opening
□ Verify cable seated comfortably (no pinching)
□ Check clip position: should prevent cable sag
□ Photograph setup (for documentation/reference)
□ Update inventory count in storage box
```

---

## 🔄 Replacement & Refresh Schedule

### Clip Maintenance
- **Frequency:** Check every 3-6 months
- **Signs of wear:** 
  - Peg loosens (wiggling)
  - Plastic cracks or breaks
  - Clip opening enlarged/deformed
- **Action:** Remove worn clip, reposition to fresh pegboard hole, or print replacement

### When to Restock Clips
- After 6 months, review usage pattern
- Identify which sizes are used most (likely Clip B)
- Print 2-3 of most-used size for contingency
- Retire old design when upgrading to v1.1.0

---

## 🎓 Learning Resources

### Related 3D Printing Topics
- **Cable Management in 3D Models:**
  - How to design clips with correct hole tolerances
  - Measuring cable diameter for accurate sizing
  
- **Pegboard Customization:**
  - Creating universal peg adapters
  - Designing brackets for specific components
  
- **Print Optimization:**
  - Orientation for minimal support material
  - Infill density for different loads

### Community Projects
- Look for "pegboard clip" on Thingiverse/Printables
- Compare design philosophy with similar projects
- Contribute improvements to open-source pegboard ecosystem

---

## 🐛 Troubleshooting Clips

| Problem | Cause | Solution |
|---------|-------|----------|
| Cable slips out | Hole too large | Use smaller clip (B→A) or sand opening tighter |
| Clip won't stay mounted | Peg too loose | Move clip to tighter hole or reprint peg |
| Cable kinked in clip | Clip too small | Upgrade to larger size (A→B→C) |
| Clip interferes with plug | Positioning poor | Reposition clip up/down to alternate hole |
| Plastic cracked | Overtightened cable | Use larger clip (B→C) to reduce stress |
| Multiple cable tangles | Too few clips | Print additional clips (scale up Phase 2) |

---

## 📞 Quick Reference Card

**For Printing Decisions:**

```
Q: How many cables do I need to manage?
A: If < 5 cables → Phase 1 only (test samples)
   If 5-10 cables → Phase 2A or 2B (standard)
   If > 10 cables → Phase 2C (elaborate)

Q: What's my cable diameter?
A: < 8mm → Clip A
   8-12mm → Clip B (most common!) ⭐
   12-16mm → Clip C
   > 16mm → Clip D

Q: I'm unsure about quantities?
A: START with 1 of each (Phase 1)
   THEN print in batches based on actual use
   This avoids waste and saves filament!
```

---

## 📝 Notes Section

**My Cable Summary (Fill in after measuring):**

```
Cable Type          Diameter    Qty    Best Clip
─────────────────────────────────────────────────
Govee coiled       ___ mm      1      Clip B ✓
Power strip plug   ___ mm      1      Clip __
USB extensions     ___ mm      __     Clip __
Ethernet           ___ mm      __     Clip __
Signal cables      ___ mm      __     Clip __
Custom: ________   ___ mm      __     Clip __
─────────────────────────────────────────────────

Total Clips Needed:
  • Clip A: __ units
  • Clip B: __ units (likely 2-5)
  • Clip C: __ units
  • Clip D: __ units
```

---

**Document Version:** 1.0.0  
**Last Updated:** 2026-08-19  
**Print Recommendation:** Start with Phase 1, scale based on measurements!
