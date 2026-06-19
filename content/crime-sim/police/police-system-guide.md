---
title: "Crime Simulator Police System Guide: AI Behavior and Evasion"
date: 2026-06-18
draft: false

game: crime-sim
tags: [police, evasion, stealth, detection, guide]
weight: 3
description: "Complete guide to the Crime Simulator police AI system -- how detection works, response times, evasion strategies, and how to avoid police entirely."
---

The police system in Crime Simulator is the primary fail state. Understanding exactly how it works -- what triggers it, how fast police respond, and how to evade them -- is the difference between a clean score and a deleted save in Hardcore mode.

The [common mistakes guide](/crime-sim/beginner/common-mistakes/) shows the specific police traps new players fall into.

## How Police Detection Works

Police are triggered by a heat system. Every action you take generates heat. When your heat reaches a threshold, police are called.

**Heat-generating actions:**
- Breaking windows without a glass knife (high heat)
- Using crowbar on doors (high heat)
- Being spotted by NPCs (instant high heat)
- Triggering house alarms (very high heat)
- Sprinting in view of neighbors (moderate heat)
- Making noise near patrol routes (moderate heat)
- Leaving doors open (low heat over time)

Your tool choice directly affects heat generation -- the [tools guide](/crime-sim/tools/complete-tools-guide/) ranks each tool by noise level.

**Heat-reducing actions:**
- Staying still in darkness (slow reduction)
- Hiding in closets or bathrooms (fast reduction)
- Leaving the area (full reset after 60 seconds)
- Completing a heist cleanly (resets for next heist)

| Action | Heat Generated | Detection Radius | Notes |
|--------|:--------------:|:----------------:|-------|
| Broken window (crowbar) | High | 30 meters | Immediate neighbor alert |
| Broken window (glass knife) | Very low | 5 meters | Safe if no one is nearby |
| Lockpicked door | None | 0 meters | Completely silent |
| Crowbar on door | High | 20 meters | Avoid at all costs |
| Trigger alarm | Critical | Full map | Police dispatched instantly |
| NPC spot you | Critical | Full map | Immediate police call |
| Sprinting outside | Moderate | 15 meters | Worse during day |

## Police Response Times

Police response varies by district and difficulty. In Standard mode on Normal difficulty, expect:

| District | Response Time (first call) | Escalation Time | Best Evasion Strategy |
|----------|:--------------------------:|:---------------:|----------------------|
| Starter Town | 45-60 seconds | +15 sec per alert | Hide in nearby house |
| Suburban | 30-45 seconds | +10 sec per alert | Closets, bathroom |
| Industrial | 60-90 seconds | +20 sec per alert | Dumpsters, warehouses |
| Downtown | 20-30 seconds | +5 sec per alert | Alley hiding spots |
| Heist Locations | 15-25 seconds | Instant on second call | Pre-planned escape |

{{< callout "warning" >}}
In Hardcore mode, police response is approximately 50% faster across all districts. Downtown response drops to 10-15 seconds. If you trigger an alarm in Downtown on Hardcore, you have less than 15 seconds to hide before police arrive. I learned this the hard way.
{{< /callout >}}

## Police AI Behavior

The police AI follows a predictable pattern once dispatched:

### Phase 1: Dispatch
Police spawn at district entry points. They head toward the triggered location. During this phase, you have roughly 30-60 seconds to hide or leave the area.

### Phase 2: Search
Police arrive at the location and begin searching. They check rooms systematically. If they find an open door or broken window, they enter the building.

**Search behavior:**
- Police check rooms in a set order (ground floor first, then upstairs)
- They listen for movement noise (sprinting and running are detected)
- They check closets and bathrooms if the room is dark
- They leave after approximately 60 seconds if nothing is found
- They search with flashlights at night, making dark corners less safe

### Phase 3: Chase
If police spot you, a chase begins. Chases escalate in intensity:
- **1 star:** One police car, simple evasion possible
- **2 stars:** Two cars, tighter search grid
- **3 stars:** Helicopter joins, very hard to escape

{{< insight >}}
The key insight about police AI is that they respond to noise, not to you directly (unless an NPC spots you). If you are hiding silently in a closet and police enter the room, they will check the closet only if they have reason to believe someone is there. Stay still. Do not even shift your crouch position. I have been in a closet while a cop walked past it three times because I stayed completely still.
{{< /insight >}}

## Evasion Map: Best Hiding Spots by District

Knowing where to hide is essential. Here are reliable hiding spots for each district:

**Starter Town:**
- Closets in any house (best option)
- Bathroom stalls (if you entered a house with a bathroom)
- Behind garden sheds (exterior, risky)
- Under beds in master bedrooms

**Suburban:**
- Walk-in closets (large, easy to enter)
- Basement corners (dark, hard to spot)
- Garage storage areas
- Behind large furniture (couches, cabinets)

**Industrial:**
- Warehouse containers (excellent, dark)
- Dumpsters (reliable but smelly)
- Behind machinery (good cover)
- Rooftop corners (if accessible)

**Downtown:**
- Alley dumpsters (most reliable)
- Apartment building hallways (enter any open door)
- Rooftops (if you can access via fire escape)
- Underground parking (dark, multiple exits)

## Step-by-Step Evasion Protocol

1. **Stop moving** the moment you hear a siren or see a police car
2. **Identify your nearest hiding spot** (closet, bathroom, dumpster, alley)
3. **Crouch-walk** to the hiding spot (do not sprint -- footsteps are audible)
4. **Enter the hiding spot** and hold still
5. **Watch the search indicator** -- it pulses while police are searching
6. **Wait for the indicator to fully disappear** plus 15 extra seconds
7. **Crouch-walk** to the nearest exit
8. **Exit the district** if possible (cross-district travel resets police)

## How to Avoid Police Entirely

The best strategy is never triggering police in the first place.

**Golden rules:**
- Always use lockpicks, never crowbars, for door entry
- Use glass knives for window entry on alarmed houses
- Move at night when possible (darker = harder for neighbors to spot you)
- Close doors behind you (reduces visual evidence)
- Check the street before exiting (wait for patrols to pass)
- Never sprint in front of windows
- Disable alarm panels before looting (faster than suppressing alarms)

{{< callout "tip" >}}
The single most effective police avoidance tactic is closing doors behind you. An open door is visible from the street and tells patrols someone is inside. It takes 2 seconds to close a door and can prevent an entire police response. I close every door I open, even interior doors.
{{< /callout >}}

## Practical Example: Avoiding a Close Call

I hit a suburban house at night. Inside, I found a laptop ($280) and cash ($120). On my way out, a patrol car turned onto the street. Instead of running out the front door, I:
1. Moved to a back window (verified no patrols visible)
2. Used the glass knife to cut the window silently
3. Dropped into the backyard
4. Crouch-walked along the fence line
5. Exited through the neighbor's yard to the next street over

Total delay: 45 seconds. Police never entered the house because I closed the front door behind me and exited through the back. They circled the block twice and left.

## Related Guides

- [Hardcore Survival Guide](/crime-sim/hardcore/hardcore-survival-guide/) -- police evasion in permadeath mode
- [Getting Started](/crime-sim/basics/getting-started/) -- basic police avoidance for beginners
- [Co-op Heist Planning](/crime-sim/coop/coop-heist-planning/) -- coordinated evasion for teams

{{< resourcegrid >}}
  {{< resourcecard name="Crime Simulator Steam Discussions" url="https://steamcommunity.com/app/2737070/discussions/" desc="Player discussions on police AI and evasion" >}}
  {{< resourcecard name="Steam Guides" url="https://steamcommunity.com/app/2737070/guides/" desc="Community-created guides on stealth and evasion" >}}
  {{< resourcecard name="Understanding Game Modes" url="https://steamcommunity.com/sharedfiles/filedetails/?id=3506289284" desc="Community guide on police behavior by difficulty" >}}
{{< /resourcegrid >}}
