---
title: "Barn vs Warehouse: Which Property Actually Runs Better for AFK"
date: 2026-06-15T12:15:00+08:00
draft: false
game: schedule-i
tag: AUTOMATION
weight: 4
---

{{< diagram "diagrams/barn-warehouse-layout.svg" "Barn vs Warehouse Layout Comparison" "760" >}}

I've tried automating both the Barn ($25K) and the Docks Warehouse ($50K). After running each for a few in-game days, here's what I found.

The Barn is the better deal. Two floors, 10 employees, 2 loading bays. You can fit a full OG Kush 4-mix or Meth line in there and still have room for a Botanist. I've seen other players say the Barn is the best value property in the game, and I agree.

The Warehouse has 12 employee slots and is bigger on paper, but the loading bay is at one end and your production has to stretch across the whole floor. That means more Handlers needed just for shuttle duty. Reddit threads mention the same thing -- people running 4 Handlers in the Warehouse just to keep shelves stocked, when the Barn could do it with 2.

Here's what I settled on after swapping between both:

**Barn layout that works:**

- Ground floor south: Botanist with 5 pots, drying rack
- Ground floor center: 4 Mixing Stations in a chain, 2 Chemists
- Ground floor north: 3 Shelves for ingredients, 1 Handler to shuttle bay-to-shelf
- Upper floor: Packing Station + Packer, output shelf
- Extra Handler shuttles between floors

The 2-floor trick is legit. I kept everything on one floor at first and Handler routes kept breaking. Splitting it vertically cut my route errors by more than half. A Reddit post from someone with 40+ hours claims the same thing -- 2-floor routing cuts errors by about 60%.

**Warehouse setup (when you need it):**

I only moved to the Warehouse when I wanted to run Cocaine 8-mix, which needs 8 Mixing Stations. The Barn can't fit that without getting cramped. Setup is:

- East wall: 6 shelves for ingredients
- Center: 8 Mixing Stations split into two parallel 4-chains
- West end: 2 Packing Stations
- 4 Handlers (yes, 4 -- the bay is far)

The Warehouse forces longer Handler routes. Reddit threads confirm a hard limit of 6 routes per Handler before errors spike. After the v0.3f patch changed route priority, I noticed the same thing. Keep each Handler at 4-5 routes max.

**Quick cost comparison (what I tracked):**

| | Barn (Meth 4-mix) | Warehouse (Coke 8-mix) |
|--|-------------------|----------------------|
| Property | $25K | $50K |
| Equipment | ~$5K | ~$12K |
| Daily wages | ~$2,000 | ~$5,000 |
| Units/day | ~120 | ~240 |
| Profit/day (rough) | $12K-$18K | $60K-$85K |

The numbers are estimates based on what I and a few other players have shared on Reddit. Your mileage will vary depending on what recipe you run and how good your route setup is.

**Known issues I've run into:**

- Barn staircase: Handlers sometimes freeze carrying large loads up the stairs. I keep a small transfer box at the bottom of the stairs to split the load. Not perfect but it helps.
- Warehouse bay distance: Dedicating one Handler to pure bay-to-shelf shuttle (only 2 routes) stops everything else from stalling. Multiple people on Steam Discussions suggest the same fix.
- MK2 Packing Station: I switched back to MK1 after noticing my Handler was way slower on MK2. Other players report the same -- the Fandom Wiki even notes it as a known behavior (flags it as a bug from v0.3.4f8 that wasn't fully fixed). I use MK2 for manual packing only now.

**When to upgrade:**

I'd skip the Manor ($250K) unless you're at Kingpin rank and already maxing out the Warehouse. Most players never need that much space. The Barn gets you through mid-game and the Warehouse covers endgame for 90% of players.

Check out the [Workshop Automation guide](/schedule-i/automation/workshop/) for the full breakdown on Chemist, Handler and Packer route setup.

{{< resourcegrid >}}
  {{< resourcecard name="8-Mix Coke Warehouse Layout (Reddit)" url="https://www.reddit.com/r/Schedule_I/comments/1jyowf2/automated_8mix_coke_docks_warehouse_layout/" desc="Community blueprints for docks warehouse" >}}
  {{< resourcecard name="Barn Setup (ScalaCube)" url="https://scalacube.com/blog/schedule-1/best-barn-setup-in-schedule-1" desc="Step-by-step barn layout" >}}
  {{< resourcecard name="Max Production Barn/Warehouse Video" url="https://www.youtube.com/watch?v=s93o84TUkxo" desc="Visual walkthrough of endgame setups" >}}
{{< /resourcegrid >}}
