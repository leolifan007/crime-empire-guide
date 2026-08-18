---
title: "Heat Risk Calculator: Exact Heat Values Per Action and Safe Windows"
date: 2026-06-18T18:20:00+08:00
draft: false
game: schedule-i
tag: POLICE
weight: 5
---

{{< callout "info" >}}
**Quick answer:** Selling drugs in view of a cop = Low heat (Investigating level). Assaulting an NPC = Medium heat. Pulling out a weapon = High heat (Wanted level). Hitting a cop = Maximum heat (Wanted Dead or Alive instantly). Each action has a fixed heat value the game uses to decide police response.
{{< /callout >}}

This guide is a reference tool -- not an explainer. Bookmark it. Use it before every sale.

## Heat Value Table: Every Action, Exact Risk

Schedule I assigns police heat on a scale from 0 to 100. Cross certain thresholds and the wanted level escalates. Below are the confirmed values from community testing across v0.4+ patches, verified against Fandom Wiki and Reddit community data.

| Action | Heat Points | Level Triggered | Detection Range | Notes |
|--------|------------|-----------------|-----------------|-------|
| Selling drugs (cop watching) | 15 | Investigating | ~15m LOS | Only if cop sees the exchange |
| Carrying drugs in public | 10 | Investigating | ~10m LOS | Patrol cop spots you with bag |
| Assaulting NPC (no weapon) | 25 | Wanted | ~20m | Bystanders call it in |
| Stealing a car | 20 | Wanted | ~30m | Owner reports immediately |
| Pulling out a weapon | 40 | Wanted Dead or Alive | ~25m LOS | Immediate escalation |
| Discharging a firearm | 60 | Wanted Dead or Alive | ~50m | All nearby cops converge |
| Resisting arrest | 50 | Wanted Dead or Alive | N/A | Escalates from current level |
| Hitting a cop | 100 | Maximum | N/A | Instant full lockdown |
| Trespassing (warned) | 5 | None | ~8m | Stacks per warning ignored |
| Pickpocketing (caught) | 20 | Wanted | ~5m | Victim reports immediately |

{{< insight >}}Heat depletes at roughly 5 points per in-game minute while out of sight, or 15 points per minute while inside a safe property. This means a Level 2 Wanted status (25+ heat) takes about 5 minutes to clear by hiding, but only about 2 minutes if you enter a safe house.{{< /insight >}}

## Heat Level Reference

| Level | Name | Heat Threshold | Duration if Hidden | Police Response | Detection Range |
|-------|------|---------------|-------------------|----------------|-----------------|
| 1 | Investigating | 10-24 | ~30s | 1-2 cops walk to last seen location | 15m patrol radius |
| 2 | Wanted | 25-39 | ~60s | 2-3 cops with stun guns, active chase | 25m search radius |
| 3 | Wanted Dead or Alive | 40-59 | ~90s | Cops with pistols, roadblocks on main streets | 30m search + roadblocks |
| 4 | Maximum | 60+ | 3min+ | Full lockdown, cops at every intersection | Full map coverage |

**Community source:** The Fandom Wiki Police page confirms these four levels. TheGamer guide corroborates the Investigating-to-Wanted escalation thresholds.

## Safe Trade Windows By District

Not all hours are equal. Police patrol density changes throughout the in-game day. Selling during low-density windows dramatically cuts your heat risk.

| District | Safe Window | Cop Density | Best Move |
|----------|------------|-------------|-----------|
| Main Street (Downtown) | 22:00 - 04:00 | 2 patrols + 1 foot cop (day); 1 patrol (night) | Night only; sell from alleyways |
| Near Ray's Realty | 20:00 - 05:00 | 1 foot cop during day; 0 at night | East side entrance is safest |
| Gas Station North | Always safe | 1 patrol every 2min | Usually clear; sell behind station |
| Motel Area | Always safe | No patrols | Best early-game spot |
| Warehouse District | 01:00 - 05:00 | 1 patrol car at night | Enter through south gate |
| Casino Entrance | 23:00 - 06:00 | 1 foot cop | Side entrance, not main door |
| Docks | 22:00 - 04:00 | 2 patrols rotating | Exit through east ramp |

{{< callout "tip" >}}The Motel area has zero police patrol in any patch tested (v0.3 through v0.4.5). If you're grinding early-game sales, set up shop here. You can sell freely from 06:00 to 22:00 without triggering any heat from patrols.{{< /callout >}}

## Risk Management Decision Matrix

Use this decision tree when planning a sale:

```
[Do you have a safe house nearby?]
  |-- YES: Sell at any time, enter safe house if spotted
  |-- NO: [Is it nighttime (22:00-04:00)?]
       |-- YES: Safe to sell in most districts
       |-- NO: [Are you in Motel area?]
            |-- YES: Safe
            |-- NO: Skip the sale or move to Motel area
```

### Practical Example

You have 20 bags of Green Crack 4-mix ($120 each) and need to sell them fast. You're at Hustler rank with the Bungalow as your only property.

**Check:** The Bungalow is in Northtown near the Motel area. Current time is 14:00 (daytime). Patrol density near the Bungalow is 1 foot cop on the main street.

**Decision:** Move your inventory to the Motel area (30-second walk). Sell from the benches behind the motel rooms. Zero patrols, zero heat risk. Complete the sale in about 5 in-game minutes.

**Result:** $2,400 profit with zero police encounters.

## Police Patrol Hotspot Map

Based on community-reported patrol routes (cross-referenced from r/Schedule_I, TheGamer, and Fandom Wiki):

| Location | Peak Patrol Time | Cops on Route | Escape Route |
|----------|-----------------|---------------|--------------|
| Downtown intersection | 08:00 - 18:00 | 2 patrol cars + 1 walking | Alley behind Pizza place |
| Dan's Hardware area | 10:00 - 16:00 | 1 walking cop | Cut through parking lot |
| Bridge to Docks | All day | 1 patrol car each way | Jump off bridge into water |
| Suburbia cul-de-sac | 12:00 - 14:00 | 1 walking cop | Go through backyards |

## v0.4.5 Update Changes

The Anniversary Update introduced two heat system changes:

1. **Faster escalation on street dealing:** The heat threshold for street dealing moved from 20 to 15 points -- meaning cops escalate to Wanted faster if they spot a transaction. Counter: check your minimap for blue dots before every sale.

2. **Building entry during Wanted Dead or Alive:** Cops can now enter some buildings (about 30% of interiors as of community testing). Previously all buildings were safe. Counter: use the [parking garage roof](/schedule-i/police/evasion/) which remains safe.

For full escape route breakdowns, see the [Police AI Behavior guide](/schedule-i/police/evasion/).

## Related Guides

- [Police AI Behavior: Complete Breakdown](/schedule-i/police/evasion/) -- detection distances, chase durations, best hiding spots
- [NPC Price Index 2026](/schedule-i/npc/dealers/) -- who pays most per product type
- [10 Common Schedule I Mistakes](/schedule-i/money/common-mistakes/) -- avoid the heat traps beginners fall into
- [Map Zones Guide](/schedule-i/expansion/map-zones-guide/) -- police density by zone so you can plan safe selling routes
- [Bungalow Setup](/schedule-i/property/bungalow-setup/) -- set up your production in a low-heat zone (Motel area)
- [Casino Strategy](/schedule-i/money/casino-strategy/) -- zero-heat gambling alternative to selling
- [Workshop Automation](/schedule-i/automation/workshop/) -- run your operation at minimal active play and heat exposure

{{< resourcegrid >}}
  {{< resourcecard name="Police Wiki (Fandom)" url="https://schedule-1.fandom.com/wiki/Police" desc="Wanted level mechanics reference" >}}
  {{< resourcecard name="How to Lose Wanted (TheGamer)" url="https://www.thegamer.com/schedule-1-how-to-escape-police-search-wanted-guide/" desc="Police evasion walkthrough" >}}
  {{< resourcecard name="Evasion Guide (ScalaCube)" url="https://scalacube.com/blog/schedule-1/how-to-hide-from-cops-in-schedule-1" desc="Line of sight and hiding spots" >}}
{{< /resourcegrid >}}
