---
title: "Heat System: What Actually Triggers Police (and What Doesn't)"
date: 2026-06-15T12:15:00+08:00
draft: false
game: schedule-i
tag: POLICE
weight: 5
---

The Heat system in Schedule I isn't complicated once you understand what the game actually tracks. I spent my first few hours paranoid about police, hiding every time I saw a blue dot. Turns out I was overthinking it.

**How Heat actually works:**

There's no hidden "heat number." It's a Wanted status that escalates based on what the police *see* you do. The game uses line-of-sight detection -- if a cop can't see you commit the crime, it doesn't count. Simple as that.

Here's what I've confirmed through testing and cross-checking with Reddit and Fandom Wiki discussions:

| Action | Heat | Notes |
|--------|------|-------|
| Selling on the street | Low | Only if a cop is watching the transaction |
| Carrying drugs in public | Low | If a cop spots you during patrol |
| Fighting NPCs | Medium | Bystanders report you |
| Stealing a car | Medium | The owner calls it in |
| Pulling out a weapon | High | Immediate escalation |
| Resisting arrest | High | Skips straight to Wanted |
| Hitting a cop | Max | Wanted Dead or Alive instantly |

The most common way I got heat early game was selling on a street corner that happened to be on a police patrol route. After the third time, I started checking my minimap for blue icons before every sale. If there's a blue dot nearby, walk around the corner and sell there instead. Takes 5 seconds and saves you the chase.

**The 4 Heat levels:**

The game uses a tiered system. IGN and Fandom Wiki have slightly different names for the levels, but the behavior is consistent across sources:

- **Level 1 -- Investigating:** Cops walk toward where you were last seen. Move 2 blocks away or step inside a building. Clears in about 30 seconds.
- **Level 2 -- Wanted:** Active chase on foot. Cops use stun guns. Break line of sight and hide. Takes about 60 seconds to clear if you're hidden.
- **Level 3 -- Wanted Dead or Alive:** Cops use pistols. Roadblocks appear on main streets. Takes 90 seconds and you really want to stay out of sight.
- **Level 4 -- Maximum:** Full lockdown. Police at every intersection. I've only triggered this once (accidentally hit a cop during a chase). Took over 3 minutes to clear. I had to switch properties to lose it.

**What I do to clear Heat fast:**

The garbage bin method everyone talks about works. Found a bin behind a building, hopped in, waited 30-45 seconds, and the Wanted status cleared. But there are catches:

- If a cop sees you get into the bin, they'll pull you out. Break line of sight first.
- Don't use the same bin twice in a row. I've heard from other players that the cops learn -- whether that's actual game logic or just bad luck, I don't reuse bins anyway.
- The parking garage rooftop near the motel is the only 100% safe spot I've found. Police pathfinding can't reach the roof. Run up the ramp, jump to the top level, wait. Works at any Heat level. I've tested it through v0.4.5.

Other methods I've used:

- **Energy Drink + sprint:** Pop an Energy Drink ($5 at any gas station) for the speed boost. Combine with breaking line of sight. Good for Levels 1-2.
- **Enter a safe house:** Clears all Heat instantly. Keep a property near your selling district for quick escapes.
- **Don't sell within 3 blocks of the police station.** This is self-inflicted and I've done it too many times.

**Police patrol hotspots I've mapped:**

Based on where I keep getting caught:

| Location | Cop Density | Best Move |
|----------|-------------|-----------|
| Main Street downtown | 2 patrol cars + 1 walking cop | Sell here only at night |
| Near Ray's Realty | 1 walking cop during day | Sell on the east side |
| Gas station north | 1 patrol car every 2 min | Usually safe |
| Motel area | No patrols | Best early-game spot |
| Warehouse district | 1 patrol car at night | Enter through south entrance |
| Casino entrance | 1 walking cop | Use the side entrance |

**v0.4.5 change worth knowing:**

The Anniversary Update made cops respond faster to street dealing. They can also enter some buildings during Wanted Dead or Alive. Garbage bin hiding still works as of v0.4.5 based on my testing, but if a future patch breaks it, check the community links below for updates.

For detailed escape routes, see the [Evasion guide](/schedule-i/police/evasion/).

{{< resourcegrid >}}
  {{< resourcecard name="Police Wiki (Fandom)" url="https://schedule-1.fandom.com/wiki/Police" desc="Wanted level mechanics reference" >}}
  {{< resourcecard name="How to Lose Wanted (TheGamer)" url="https://www.thegamer.com/schedule-1-how-to-escape-police-search-wanted-guide/" desc="Police evasion walkthrough" >}}
  {{< resourcecard name="Hiding from Cops (ScalaCube)" url="https://scalacube.com/blog/schedule-1/how-to-hide-from-cops-in-schedule-1" desc="Line of sight and hiding spots" >}}
{{< /resourcegrid >}}
