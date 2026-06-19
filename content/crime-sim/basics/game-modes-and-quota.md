---
title: "Crime Simulator Game Modes and Quota System Explained"
date: 2026-06-18
draft: false
game: crime-sim
tags: [mechanics, modes, quota, difficulty]
weight: 2
description: "Complete breakdown of Crime Simulator's three game modes -- Standard, Hardcore, Completionist -- plus the quota system mechanics, difficulty scaling, and which mode to pick for your playstyle."
---

Crime Simulator has three game modes. The differences are significant -- mode choice determines how punishing the quota is, whether you can die permanently, and how much time you have to explore. Pick the wrong mode and you will restart more than necessary.

## Mode Comparison

| Feature | Standard | Hardcore | Completionist |
|---------|:--------:|:--------:|:------------:|
| Permadeath | No | Yes | No |
| Difficulty | Normal | Master (locked) | Variable |
| Quota | Every 3 days | Every 3 days | No time limit |
| Quota penalty | Warning, then demote | Full reset | None |
| Police aggression | Normal | +50% (community estimate) | Normal |
| Fence prices | 100% | ~80% | 100% |
| Final score bonus | 1x | 2x | N/A |
| Best for | Learning the game | Challenge runs | Achievements |

## Standard Mode

Standard is the recommended starting mode. Difficulty is set to Normal. Quotas appear every 3 in-game days with a minimum dollar target. Fail the quota and you get a warning. Fail again and your rank decreases. Fail repeatedly and the game ends.

**Quota progression in Standard:**
- Quota 1: $500
- Quota 2: $1,000
- Quota 3: $2,000
- Quota 4: $3,500
- Quota 5-10: increases by $1,500-2,000 each step
- Quota 10+: $15,000+

{{< callout "tip" >}}
The first quota is $500. You can hit this by looting 2-3 small houses and selling everything. Do not waste time on a single high-value target early -- volume is faster in the first 30 minutes.
{{< /callout >}}

Dying in Standard sends you back to your hideout. You lose the loot you were carrying but keep your rank and upgrades. This makes it forgiving for learning map layouts, alarm patterns, and police response.

{{< insight >}}
Standard is the fastest way to learn the game. I spent my first 3 hours here and it saved me roughly 5 hours of Hardcore restarts. Learn the map in Standard, then switch to Hardcore once you can clear 3 houses without triggering a single alarm.
{{< /insight >}}

## Hardcore Mode

Hardcore locks difficulty to Master. Quotas are active with the same 3-day timer, but the penalties are absolute -- miss a single quota and your entire save is reset. Rank, money, upgrades, everything gone.

**What changes in Hardcore:**
- Police respond faster and patrol denser routes
- Alarm systems are more common and harder to disable
- Fence buy prices are roughly 20% lower (community consensus)
- Residents are more alert -- footsteps and door noises trigger suspicion sooner
- The final score is doubled compared to Standard

{{< callout "warning" >}}
Do not start Hardcore until you have completed at least one full Standard run to Rank 20+. Hardcore demands complete map knowledge, memorized tool upgrade costs, and reliable alarm-disabling routes. Most new players fail their first [Hardcore attempt](/crime-sim/hardcore/hardcore-survival-guide/) within the first 3 quotas.
{{< /callout >}}

**Hardcore survival checklist (before attempting):**
- [ ] Can you reach Rank 12 in Standard without dying?
- [ ] Do you know which houses have alarm panels and where?
- [ ] Have you memorized the tool upgrade path (costs and unlock ranks)?
- [ ] Can you identify high-value loot containers by sight (laptops in home offices, jewelry in bedroom drawers)?
- [ ] Do you have a reliable escape route from each district?

If the answer to any of these is "no", spend more time in Standard first.

## Completionist Mode

Completionist removes the quota timer entirely. There is no deadline -- you explore, loot, and progress at your own pace.

**How Completionist works:**
- Quotas still exist but they rise by $500 per run, with no time pressure
- Difficulty can be adjusted (the mode does not lock it)
- Objective: complete all available locations by looting everything
- No permadeath

This mode is designed for achievement hunting and map exploration. Without the quota pressure, you can methodically clear every container, test different tool combinations, and figure out the optimal routes for specific loot types.

{{< insight >}}
**Master thief** (steal 100 items in one game) is easiest in Completionist mode. Start a Completionist run, equip lockpicks and a flashlight, and clear every house district by district. A single large house has 15-25 lootable containers. By house 6 you will have 100+ items. Takes about 40 minutes.
{{< /insight >}}

## Quota System Mechanics

The quota is the core progression driver. Understanding how it scales lets you plan ahead.

**Quota rules:**
- A new quota appears every 3 in-game days (each day is roughly 10-15 minutes real time)
- The target is cumulative earnings from fence sales and job completion
- Items stored in hideout do not count -- only items sold
- Credits earned from completed jobs count toward quota
- Meeting the quota early does not skip the remaining days -- you still have time to loot and save for the next quota

**When you fail a quota:**
- First failure: warning (no penalty)
- Second failure: rank decrease (-2 ranks)
- Third failure: game over (save deleted on Hardcore)

{{< callout "tip" >}}
If you are close to failing a quota, sell your stored high-value items. One gold bar ($800) or an electronics item ($400-600) can close the gap. Keeping a "quota emergency stash" of 2-3 high-value items in your hideout is a good habit.
{{< /callout >}}

## Which Mode Should You Play?

- **First time?** Standard mode. Learn the maps, tool mechanics, and alarm patterns without pressure.
- **Experienced and want a challenge?** Hardcore. It forces perfect execution and punishes every mistake.
- **Going for achievements?** Completionist. Most Steam achievements are significantly easier without the quota timer.
- **Want the highest score?** Hardcore. The 2x score multiplier means your leaderboard position depends on surviving Hardcore as long as possible.

{{< resourcegrid >}}
  {{< resourcecard name="Steam Community Guide: Gameplay, Modes" url="https://steamcommunity.com/sharedfiles/filedetails/?id=3506289284" desc="In-depth community guide covering all three modes" >}}
  {{< resourcecard name="Crime Simulator Getting Started" url="/crime-sim/basics/getting-started/" desc="New player walkthrough -- first 30 minutes" >}}
  {{< resourcecard name="Steam Discussions" url="https://steamcommunity.com/app/2737070/discussions/" desc="Active community discussions on mode strategies" >}}
{{< /resourcegrid >}}
