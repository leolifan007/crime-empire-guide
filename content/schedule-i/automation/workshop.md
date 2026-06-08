---
title: "Mixing Station Automation: Handler + Chemist + Packer Setup"
date: 2026-06-09T00:30:00+08:00
draft: false
game: schedule-i
tag: AUTOMATION
weight: 3
---

{{< callout "info" >}}
**Short answer:** Three employees automate mixing: the **Chemist** mixes ingredients at Mixing Stations, the **Handler** moves products between stations and shelves, and the **Packer** bags finished goods. Set up ingredient shelves feeding into daisy-chained Mixing Stations with the Handler on route, and your production runs AFK. Full auto requires 6+ Mixing Stations per recipe, 4+ shelves, and 2 Handlers minimum.
{{< /callout >}}

{{< diagram "diagrams/automation-flow.svg" "Automation Employee Flow Diagram" "760" >}}

{{< section "The Three Automation Roles" >}}

Schedule 1 has three employee types that form your automation pipeline. Each role handles a specific part of the production chain.

| Role | Hire Cost | Daily Wage | Unlock Rank | Does What | Capacity |
|------|-----------|------------|-------------|-----------|----------|
| {{< material "og_kush" >}} Botanist | $150 | $40/day | Hustler I | Harvests plants, moves to drying racks | 5 pots per Botanist |
| {{< material "battery" >}} Chemist | $200 | $60/day | Hustler II | Mixes ingredients at stations, auto-cooks | 2 stations per Chemist |
| {{< material "mega_bean" >}} Handler | $175 | $50/day | Hustler I | Moves items between shelves, stations, loading bay | 6 routes per Handler |
| {{< material "energy_drink" >}} Packer | $180 | $55/day | Hustler III | Bags finished product into packages | 4 output bins per Packer |

{{< insight >}}The Handler is the backbone of any automation setup. Without proper route configuration, your Chemist will run out of ingredients and your Packer will have nothing to bag. Spend time on Handler routes -- this is where most automation failures happen.{{< /insight >}}

{{< section "Step-by-Step: Automating a 4-Mix Recipe" >}}

<div class="upgrade-timeline">

<div class="upgrade-step">
  <div class="step-marker">
    <span class="step-dot">1</span>
    <div class="step-rail"></div>
  </div>
  <div class="step-panel">
    <div class="step-rank">
      <span class="rank-name">Place Ingredient Shelves</span>
      <span class="rank-badge">Foundation</span>
    </div>
    <p class="step-desc">Place 2-4 shelves near the loading bay. Set each shelf to whitelist 2 specific ingredients. For OG Kush 4-mix (Battery + Horse Semen + Mega Bean + OG Kush base), dedicate one shelf for each ingredient pair. Keep shelves within 3 tiles of the loading bay for fast Handler routes.</p>
  </div>
</div>

<div class="upgrade-step">
  <div class="step-marker">
    <span class="step-dot">2</span>
    <div class="step-rail"></div>
  </div>
  <div class="step-panel">
    <div class="step-rank">
      <span class="rank-name">Set Up Mixing Stations</span>
      <span class="rank-badge">Production</span>
    </div>
    <p class="step-desc">Place 4 Mixing Stations in a daisy chain. Station 1 pulls from shelf, output feeds to Station 2 input, and so on. Use the clipboard to configure each station's output destination to the next station. Station 4 output should go to a box or shelf for the Packer.</p>
  </div>
</div>

<div class="upgrade-step">
  <div class="step-marker">
    <span class="step-dot">3</span>
    <div class="step-rail"></div>
  </div>
  <div class="step-panel">
    <div class="step-rank">
      <span class="rank-name">Hire and Assign Chemist</span>
      <span class="rank-badge">Auto-Mix</span>
    </div>
    <p class="step-desc">Hire a Chemist ($200 + $60/day). Assign them to the Mixing Stations. The Chemist will automatically pull ingredients from the shelf, load them into each station, and advance the mix through the chain. One Chemist can handle up to 2 stations -- for a 4-station chain, hire 2 Chemists.</p>
  </div>
</div>

<div class="upgrade-step">
  <div class="step-marker">
    <span class="step-dot">4</span>
    <div class="step-rail"></div>
  </div>
  <div class="step-panel">
    <div class="step-rank">
      <span class="rank-name">Configure Handler Routes</span>
      <span class="rank-badge">Logistics</span>
    </div>
    <p class="step-desc">Hire 1-2 Handlers ($175 + $50/day). Route 1: Loading bay -> Ingredient shelf. Route 2: Station 4 output -> Packer input. Route 3: Packer output -> Loading bay. Set each route with whitelist filters so the Handler only moves the correct items. Test one route at a time to avoid configuration errors.</p>
  </div>
</div>

<div class="upgrade-step">
  <div class="step-marker end">
    <span class="step-dot">5</span>
  </div>
  <div class="step-panel">
    <div class="step-rank">
      <span class="rank-name">Packer and Delivery</span>
      <span class="rank-badge gold">AFK Money</span>
    </div>
    <p class="step-desc">Hire a Packer ($180 + $55/day). Assign it to the output box from Station 4. Set the Packer to bag in $50 or $100 quantities. Finished bags go to the loading bay where Handlers move them to the delivery drop-off. Check once per in-game day to restock ingredients and collect cash.</p>
  </div>
</div>

</div>

{{< section "Property-Specific Automation Tips" >}}

| Property | Max Employees | Best Setup | Bottleneck |
|----------|---------------|------------|------------|
| {{< material "og_kush" >}} Bungalow | 4 employees | 2 Chemist + 2 Handler | Floor space; fits only 4 stations max |
| {{< material "green_crack" >}} Barn | 10 employees | 3 Chemist + 4 Handler + 2 Packer + 1 Botanist | Shelf placement; 2-floor routing |
| {{< material "cocaine" >}} Docks Warehouse | 12 employees | 4 Chemist + 4 Handler + 2 Packer + 2 Botanist | Loading bay distance; long routes |
| {{< material "granddaddy_purple" >}} Hyland Manor | 16 employees | Full cocaine 9-mix production line | Start-up cost ($250K) |

{{< section "Common Automation Failures and Fixes" >}}

**Issue: Chemist not mixing**
- Check station has clipboard assignment
- Verify ingredients are on whitelisted shelf
- Confirm Chemist is assigned to correct stations

**Issue: Handler not moving items**
- Route destination must be reachable (no blocked paths)
- Whitelist/blacklist may be filtering everything out
- Handler capacity: 6 routes max, split across 2 if needed

**Issue: Packer not bagging**
- Output bin may be full -- add second bin
- Product must be finished (check station output)
- Bag quantity setting may not match product unit size

**Issue: Production stopped overnight**
- Ingredients ran out. Set up a shelf buffer with 2-3 days worth
- Use Dead Drop orders from suppliers for bulk restocking

{{< section "Related Guides" >}}

See also: [Best Drug Recipe Profit Rankings](/schedule-i/recipes/profit/) for which recipes to automate first based on profit per unit.

{{< resourcegrid >}}
  {{< resourcecard name="Mixing Station Automation Video" url="https://www.youtube.com/watch?v=2stFdafO7dw" desc="Complete walkthrough of Chemist + Handler setup" >}}
  {{< resourcecard name="7 Automation Tricks (Reddit)" url="https://www.reddit.com/r/Schedule_I/comments/1k4jp3c/7_most_important_automation_tricks_i_learned/" desc="Community-tested tips for smoother operations" >}}
  {{< resourcecard name="Steam Automation Discussion" url="https://steamcommunity.com/app/3164500/discussions/1/599655744453817131/" desc="Post-patch automation changes and fixes" >}}
{{< /resourcegrid >}}
