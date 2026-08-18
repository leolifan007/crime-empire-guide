---
title: "Police AI Behavior: Detection Distances, Chase Durations, and Best Hiding Spots"
date: 2026-06-18T18:25:00+08:00
draft: false
game: schedule-i
tag: POLICE
weight: 6
---

{{< callout "info" >}}
**Short answer:** Police in Schedule I use line-of-sight (LOS) detection with a 15m base range. Detection is blocked by walls, vehicles, and terrain. Chase duration scales with heat level: 30s at Level 1, 60s at Level 2, 90s at Level 3, 3min+ at Level 4. Entering a safe house clears all heat instantly. The parking garage roof near the motel is the only 100% safe spot at all heat levels as of v0.4.5.
{{< /callout >}}

This breakdown shows you exactly how cops think, so you can exploit their AI patterns instead of running blindly.

## Detection Distance By Situation

Police detection is not a fixed radius. It depends on what you're doing and how fast you're moving.

| Situation | Detection Range | Speed Factor | Special Conditions |
|-----------|----------------|-------------|-------------------|
| Walking with drugs in hand | 15m (front arc only) | 1x | Only if facing cop |
| Running with drugs | 20m (360 degrees) | 1.3x | Footsteps audible |
| Selling to customer | 12m | 1x | Transaction animation creates visual cue |
| Inside vehicle | 8m (only if speeding) | 0.5x | Moving slowly = invisible |
| In a hiding spot (bin/roof) | 0m (undetectable) | 0x | Must not have been seen entering |
| Pulling out weapon | 25m (instant) | 2x | All nearby cops alerted |
| At night (22:00-04:00) | 10m (reduced) | 0.7x | Cop vision cones narrow |

{{< insight >}}The most exploitable mechanic: police LOS is front-cone only, not 360 degrees. If you sprint perpendicular to a cop's facing direction and break LOS behind a wall within 3 seconds, the cop never registers a valid sighting. This is why perpendicular sprint is the most reliable escape opener.{{< /insight >}}

## Chase Duration By Heat Level

Once a cop has sighted you, the chase timer starts. The duration depends on your heat level and whether you maintain LOS.

| Heat Level | Base Chase Duration | If LOS Break (hide) | If Enter Safe House | If Leave District |
|------------|-------------------|---------------------|-------------------|-------------------|
| 1 - Investigating | 30s | 15s hidden | Instant | 10s |
| 2 - Wanted | 60s | 30s hidden | Instant | 20s |
| 3 - Wanted Dead or Alive | 90s | 45s hidden | Instant | 45s |
| 4 - Maximum | 3min+ | 90s hidden | Instant | 60s (if not roadblocked) |

**Source:** Cross-verified from TheGamer police evasion guide and community testing threads on r/Schedule_I.

### Practical Example

You trigger a Level 2 Wanted status by selling on Main Street during daytime — exactly the situation the [common mistakes guide](/schedule-i/money/common-mistakes/) warns about. A cop is 20m away and starts sprinting toward you.

**Step 1:** Sprint perpendicular (east, into the alley behind the pizza place). This breaks LOS in about 2 seconds.

**Step 2:** The cop reaches your last known position and switches to search mode (60s timer starts).

**Step 3:** Duck into the garbage bin behind the pizza place. The bin hides you instantly.

**Step 4:** Wait 30 seconds (half the chase timer). The Wanted indicator clears.

**Step 5:** Exit the bin, walk calmly to the Motel area. The cop is still searching the alley.

## Best Hiding Spots By District

Not all hiding spots are equal. Here are the community-ranked best spots per district, verified across v0.4+ patches.

| District | Rank 1 Spot | Rank 2 Spot | Emergency Option | Notes |
|----------|------------|------------|------------------|-------|
| Motel area | Parking garage roof | Garbage bin behind office | Any motel room door | Garage roof works at all levels |
| Downtown | Alley bin behind Pizza place | Rooftop of Gas-Mart | Enter any store (80% reliable) | Store entry patched in v0.4.5 |
| Northtown | Bin behind Dan's Hardware | Construction site pipes | Any safe house | Multiple bins in this area |
| Docks | Warehouse container (south) | Behind church | Jump into water | Water LOS break works |
| Suburbia | Garbage bin behind green house | Behind Mayor's house | Bush (decorative only - does NOT hide) | Bushes are fake -- don't use them |
| Westville | RV interior if unlocked | Behind Warehouse west wall | Alley behind laundromat | RV is safe if owned |

{{< callout "warning" >}}A common myth from early community posts: hiding in bushes works. It does not. Bushes are purely decorative in Schedule I. You need a bin, a roof, or a building interior to break LOS and hide. This was confirmed in multiple Reddit threads and the Fandom Wiki Newbie Guide.{{< /callout >}}

## Escape Route Time Comparison

Time from each major selling district to the nearest safe spot:

| Starting District | Fastest Escape | Time (sprint) | Time (skateboard) | Time (vehicle) | Risk Level |
|-----------------|---------------|--------------|-------------------|---------------|------------|
| Main Street Downtown | Pizza place alley bin | 8s | 5s | N/A (traffic) | Low |
| Near Ray's Realty | East side garbage bin | 12s | 8s | 20s (drive to Bungalow) | Low |
| Gas Station North | Behind station storage | 5s | 3s | N/A | Minimal |
| Motel area | Parking garage roof | 15s | 10s | 25s (drive to Bungalow) | Minimal |
| Warehouse District | South container | 10s | 7s | 15s (drive to Docks) | Low |
| Casino entrance | Side alley bin | 6s | 4s | N/A | Low |
| Docks | Church hiding spot | 18s | 12s | 30s (drive to Warehouse) | Medium |

{{< contentbox >}}
**Best Emergency Escape by Heat Level:**

Level 1-2: Garbage bin (any district). Takes 30-60s total. No gear needed.

Level 3: Parking garage roof (Motel area). Takes 20-30s total. 100% reliable as of v0.4.5.

Level 4: Safe house entry (instant clear). Keep a property in your active selling district.
{{< /contentbox >}}

## Police AI Patterns You Can Exploit

1. **Cops don't search vertically:** They won't climb stairs to reach the parking garage roof. This is the most reliable exploit in the game.

2. **Cops lose interest after 3 searches:** If you break LOS and hide successfully 3 times in the same chase, cops will de-escalate one level even without the timer. This is a hidden mechanic confirmed in community testing.

3. **Cops forget your last known location if you enter a vehicle:** Entering any vehicle (even a parked one) resets the cop's search pattern. They'll move to a new random patrol area instead of converging on your last position.

4. **Cops can't see through fences:** Chain-link fences, wooden fences, and construction barriers all block LOS. You can be 3m from a cop behind a fence and they won't detect you.

5. **NPC calls take time to register:** When an NPC spots you and starts calling the police, you have about 5 seconds to knock them out or break LOS before the call completes. Knocking out the NPC stops the call and prevents heat from registering.

For the full heat value reference, see the [Heat Risk Calculator](/schedule-i/police/heat-system/).

## Related Guides

- [Heat Risk Calculator](/schedule-i/police/heat-system/) -- exact heat values per action
- [10 Common Schedule I Mistakes](/schedule-i/money/common-mistakes/) -- avoid the police traps beginners fall into
- [Bungalow 8-Step Automation Blueprint](/schedule-i/automation/workshop/) -- set up production away from patrol routes
- [Map Zones Guide](/schedule-i/expansion/map-zones-guide/) -- police density per zone and safe selling districts
- [Casino Strategy](/schedule-i/money/casino-strategy/) -- safe zones for gambling runs with zero police risk
- [Common Mistakes](/schedule-i/money/common-mistakes/) -- specific heat-generating actions to avoid in each zone

{{< resourcegrid >}}
  {{< resourcecard name="Police Wiki (Fandom)" url="https://schedule-1.fandom.com/wiki/Police" desc="Official police mechanics page" >}}
  {{< resourcecard name="How to Lose Wanted (TheGamer)" url="https://www.thegamer.com/schedule-1-how-to-escape-police-search-wanted-guide/" desc="Police evasion methods" >}}
  {{< resourcecard name="Best Evasion Methods (Times of India)" url="https://timesofindia.indiatimes.com/sports/esports/news/best-ways-to-evade-police-in-schedule-1/articleshow/119952112.cms" desc="Line of sight and hiding techniques" >}}
{{< /resourcegrid >}}
