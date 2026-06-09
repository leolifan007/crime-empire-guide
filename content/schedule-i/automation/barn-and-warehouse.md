---
title: "Barn and Warehouse Setup: Best AFK Production Lines Per Property"
date: 2026-06-09T01:00:00+08:00
draft: false
game: schedule-i
tag: AUTOMATION
weight: 4
---

{{< callout "info" >}}
**Short answer:** The Barn ($25K) supports 10 employees and is the best mid-game automation property. The Docks Warehouse ($50K) supports 12 employees and is the endgame automation hub. Each property needs a different layout: Barn uses a 2-floor vertical chain, Warehouse uses a horizontal U-shape. Cocaine 8-mix at the Warehouse yields $305 net per unit with full automation.
{{< /callout >}}

{{< diagram "diagrams/barn-warehouse-layout.svg" "Barn vs Warehouse Layout Comparison" "760" >}}

{{< section "Barn Setup (10 Employees)" >}}

The Barn is the first property where full automation becomes viable. Buy it from Ray's Realty for $25,000 once you reach Dealer rank.

**Optimal Employee Allocation:**

| Zone | Employees | Task |
|------|-----------|------|
| Ground floor - south | 1 Botanist | 5 pots growing base strain |
| Ground floor - center | 2 Chemist | 4 Mixing Stations (daisy chain) |
| Ground floor - north | 3 Handler | Shelf restocking + inter-zone moves |
| Upper floor | 1 Handler + 1 Packer | Output bagging + loading bay |
| Utility | 1 Botanist + 1 Handler | Drying rack management |

**Layout Blueprint for Meth 4-Mix:**

1. Place 4 shelves near the ground floor loading bay. Whitelist 2 ingredients per shelf.
2. Set 4 Mixing Stations in a straight line along the center wall. Station 1 output to Station 2, and so on.
3. Run a Handler route: Loading bay -> each shelf. Whitelist by ingredient type.
4. Run a second Handler route: Station 4 output -> stairwell box.
5. On the upper floor: Packer bags from the stairwell box. Handler moves bags to upper loading bay.

{{< insight >}}The Barn's 2-floor layout introduces a common failure: Handlers get stuck on stairs with large loads. Keep stairwell boxes small (1 shelf, not a rack) and limit each Handler to 4 routes max instead of 6 inside the Barn.{{< /insight >}}

{{< section "Docks Warehouse Setup (12 Employees)" >}}

The Docks Warehouse ($50,000, Hoodlum V rank unlock, 6PM-6AM access) is the largest automation property before the Manor.

**Optimal Employee Allocation:**

| Zone | Employees | Task |
|------|-----------|------|
| Main floor - east | 2 Botanist | 10 pots of coca base |
| Main floor - center | 4 Chemist | 8 Mixing Stations (two 4-chains) |
| Main floor - west | 4 Handler | Full logistics coverage |
| Loading bay | 2 Packer | Dual output bagging |

**Layout Blueprint for Cocaine 8-Mix:**

1. Place 6 shelves along the east wall, 3 per side. Whitelist ingredients for 8-mix: OG Kush base + Battery + Horse Semen + Mega Bean + Cuke + Paracetamol + Gasoline + Motor Oil.
2. Set 8 Mixing Stations in two parallel 4-station chains. Chain A processes ingredients 1-4, Chain B processes 5-8.
3. Use clipboard to merge Chain B output into Chain A's final station for the complete 8-mix.
4. Two Packer stations at the west loading bay, each bagging different product sizes ($50 and $100 bags).
5. Three Handlers on routes: Loading bay <-> Shelves, Shelves <-> Stations, Stations <-> Packer.

| Metric | Barn (Meth 4-mix, approx.) | Warehouse (Coke 8-mix, approx.) |
|--------|-------------------|----------------------|
| Setup cost | $25K property + $5K equipment | $50K property + $12K equipment |
| Daily employee cost | ~$490 | ~$790 |
| Units per day | ~120 | ~240 |
| Profit per unit (estimated) | $100-130 (Meth) | $250-350 (Cocaine) |
| Daily gross (estimated) | $12K-$18K | $60K-$85K |
| Days to recoup setup | ~2-3 days | ~1 day |

{{< section "Automation Priority Order" >}}

1. **Bungalow ($6K):** Semi-auto, 4 employees. Best for starting Peddler III OG Kush production.
2. **Barn ($25K):** First true automation. Upgrade at Dealer I rank when daily revenue exceeds $10K.
3. **Docks Warehouse ($50K):** Endgame automation. Upgrade when you can sustain $20K/day in ingredient costs.
4. **Skip the Manor** ($250K) unless you are at Kingpin rank with Cocaine 9-mix demand.

<div class="resource-section">
  <h2>Community Verification and Resources</h2>
  <p>Layouts vary by patch version. Cross-check your property-specific setup against:</p>
  <div class="resource-grid">
    <a href="https://www.youtube.com/watch?v=s93o84TUkxo" class="resource-card" target="_blank" rel="noopener">
      <span class="resource-icon"></span>
      <span class="resource-name">Max Production Barn/Warehouse Video</span>
      <span class="resource-desc">Endgame production line walkthrough</span>
    </a>
    <a href="https://www.reddit.com/r/Schedule_I/comments/1jyowf2/automated_8mix_coke_docks_warehouse_layout/" class="resource-card" target="_blank" rel="noopener">
      <span class="resource-icon"></span>
      <span class="resource-name">8-Mix Coke Warehouse Layout (Reddit)</span>
      <span class="resource-desc">Community-tested docks warehouse blueprint</span>
    </a>
    <a href="https://scalacube.com/blog/schedule-1/best-barn-setup-in-schedule-1" class="resource-card" target="_blank" rel="noopener">
      <span class="resource-icon"></span>
      <span class="resource-name">Best Barn Setup (ScalaCube)</span>
      <span class="resource-desc">Step-by-step barn layout guide</span>
    </a>
  </div>
</div>

See also: [Mixing Station Automation Setup](/schedule-i/automation/workshop/) for the full guide on configuring Chemist, Handler and Packer routes.
