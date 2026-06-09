---
title: "DDS2 Employee Roles: Best Assignments for Each Staff Type"
date: 2026-06-09T10:00:00+08:00
draft: false
game: dds2
tag: STAFF
weight: 2
---

{{< callout "info" >}}
Not all staff assignments are created equal. A Cook assigned to quality processing generates 15% more revenue but misses the volume bonus of mass production. A Runner on black market deals makes 25% more per order but has 3x arrest risk. Here is the data-driven assignment strategy.

{{< /callout >}}

{{< section "Cook Assignment: Quality vs. Mass Production" >}}

| Factor | Quality Processing | Mass Production |
|--------|-------------------|-----------------|
| Output/hr | 2 batches | 4 batches |
| Sell price | +15% | Base |
| Revenue/hr (meth, base $600/batch) | $1,380 | $2,400 |
| Ingredient cost/hr | $300 | $600 |
| Net profit/hr | $1,080 | $1,800 |

**Verdict:** Mass production wins by $720/hr. Quality processing only makes sense if ingredient supply is constrained (early game, limited pharmacy access).

{{< insight >}}The community discovered that quality processing becomes better at Cook skill 8+. At skill 8, the quality bonus increases to +25%, making the math: 2 x $750 = $1,500 vs 4 x $600 = $2,400. Still mass production wins, but by a smaller margin. At skill 10 quality (+30%): 2 x $780 = $1,560. Mass production still leads. Never use quality processing unless the player is manually controlling every batch.{{< /insight >}}

{{< section "Runner Route Optimization" >}}

Runners make decisions based on range vs. payout. The optimal zone is:

| Delivery Distance | Payout | Time | Per-Hour Earnings |
|------------------|--------|------|-------------------|
| Zone 1 (same district) | $80-120 | 5 min | $1,200 |
| Zone 2 (adjacent) | $150-250 | 12 min | $1,000 |
| Zone 3 (2 zones away) | $300-500 | 25 min | $960 |
| Zone 4 (cross-map) | $600-1,000 | 45 min | $800 |

**Optimization:** Set runners to Zone 1-2 only. The per-hour earnings drop steeply past Zone 2. Save Zone 3-4 deliveries for yourself when you have bribe cash, or assign to a Driver instead.

{{< section "Guard Assignment Priority" >}}

Not every hideout needs a guard. Assign guards by this priority:

| Guard Priority | Hideout Type | Reason |
|---------------|-------------|--------|
| 1st guard | Main processing lab | Highest value location |
| 2nd guard | Distribution hub | Second highest value |
| 3rd guard | High-activity stash | Active hideout = higher raid chance |
| 4th+ guard | Raw material storage | Lowest priority |

A single guard at the right hideout is worth more than 3 guards spread thin. Concentrate protection on your highest-value asset.

{{< section "Manager Benefits Breakdown" >}}

The manager is the most misunderstood staff member. They do not produce anything directly. Instead they:

1. Auto-assign tasks to idle staff (saves you 3 min per day)
2. Reduce staff stress by 20% (increases effective loyalty)
3. Negotiate supply discounts (5-10% off raw materials)
4. Alert you to staff loyalty drops (24 hr early warning)

| Staff Count | Manager Worth It? | Reason |
|------------|-------------------|--------|
| 1-3 | No | Not enough staff to coordinate |
| 4-5 | Maybe | Borderline, depends on staff quality |
| 6+ | Yes | Auto-assignment saves significant time |

{{< section "Specialist Assignments (Late Game)" >}}

At rank 5+, unlock these specialist roles:

| Specialist | Base Staff Type | Effect | Unlock Cost |
|------------|-----------------|--------|-------------|
| Chemist | Cook | +10% yield on all batches | $10k |
| Scout | Runner | Reveals delivery zone police heat | $5k |
| Enforcer | Guard | Can retrieve stolen goods | $15k |
| Fixer | Driver | Covers up failed deals (bribe police) | $20k |

Specialists require the base staff member to have Skill 6+ in their role. You cannot train a Cook into a Chemist instantly -- they need 3 in-game days of "specialization training" during which they do nothing.

{{< section "Quick Reference: Best Staff Setup by Play Stage" >}}

| Stage | Staff Setup | Daily Cost | Daily Revenue |
|-------|------------|------------|---------------|
| Early ($5-20k) | 1 Runner | $50 | $400-800 |
| Mid ($20-100k) | 1 Runner + 1 Cook + 1 Guard | $230 | $1,800-3,000 |
| Late ($100-500k) | 2 Runners + 2 Cooks + 2 Guards + 1 Driver | $710 | $5,000-9,000 |
| Endgame ($500k+) | 3 Runners + 3 Cooks + 3 Guards + 1 Driver + 1 Manager | $1,280 | $10,000-18,000 |

<div class="resource-section">
  <h2>Community Resources</h2>
  {{< resourcegrid >}}
    {{< resourcecard name="DDS2 Staff Guide Thread" url="https://steamcommunity.com/app/1708850/guides" desc="Curated community staff guides" >}}
    {{< resourcecard name="Economy Deep Dive" url="https://steamcommunity.com/sharedfiles/filedetails/?id=3412205678" desc="Data-driven staff economy analysis" >}}
  {{< /resourcegrid >}}
</div>
