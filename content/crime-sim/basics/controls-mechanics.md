---
title: "Crime Simulator Controls and Mechanics Deep Dive"
date: 2026-06-09T10:45:00+08:00
draft: false
game: crime-sim
tag: BASICS
weight: 2
---

{{< callout "info" >}}
Crime Simulator has a control system that rewards mastery. Unlike many stealth games, button mashing gets you killed. This guide covers every control binding, advanced mechanics (stealth bonuses, fall damage thresholds), and settings that impact gameplay.

{{< /callout >}}

{{< section "Keyboard Controls Reference" >}}

| Action | Default Key | Alternative | Notes |
|--------|------------|-------------|-------|
| Move | WASD | Arrow keys | - |
| Sprint | Shift | - | Drains stamina |
| Crouch | Ctrl | C | Toggle or hold (configurable) |
| Interact | E | F | Context-sensitive |
| Weapon slot 1 | 1 | Mouse wheel up | Melee |
| Weapon slot 2 | 2 | Mouse wheel down | Ranged |
| Tool slot | 3 | Q | Lockpick/crowbar |
| Flashlight | F | - | Toggle on/off |
| Map | M | Tab | Full map |
| Phone | P | - | Job board, contacts |
| Stealth mode | X | - | Slows movement, muffles sound |
| Quick save | F5 | - | Highly recommended before every job |

{{< section "Stealth Mechanics" >}}

### Sound and Detection

| Surface | Sound Radius | Detection Time | Notes |
|---------|-------------|----------------|-------|
| Carpet | 2m | 4s | Safest surface |
| Wood floor | 5m | 3s | Common in houses |
| Concrete | 8m | 2s | Warehouses, streets |
| Metal grating | 12m | 1s | Industrial zones |
| Glass shards | 15m | Instant | Alert all nearby NPCs |

**Detection cone:** NPCs have a 120 degree forward cone (day) and 90 degree cone (night). Night vision is reduced to 15m range vs 30m during day.

### Stealth Kill Multiplier

Attacking from stealth deals 3x damage. A basic melee weapon (crowbar) does 35 base damage. From stealth: 105 damage, enough to one-shot most civilian NPCs.

| Enemy Type | HP | Need Stealth Kill? |
|-----------|-----|--------------------|
| Civilian | 50 | Optional (50 base from crowbar) |
| Security Guard | 120 | Required (crowbar base 35, need 3 hits) |
| Gang Member | 150 | Required (survive 2 hits otherwise) |
| Elite Guard | 250 | Must stealth (4 hits alert everyone) |

{{< section "Fall Damage" >}}

| Height | Damage | Safe Landing Required |
|--------|--------|----------------------|
| 2m (ground floor window) | 0 | None |
| 4m (second floor) | 20 HP | Crouch landing (Ctrl before impact) |
| 6m (third floor) | 50 HP | Roll landing (Space before impact) |
| 8m+ (fourth floor+) | Instant death | Parachute or haystack |

Crouch landing reduces damage by 50%. Roll landing reduces by 75%. Practice these at your hideout before attempting vertical escapes.

{{< section "Advanced Mechanics" >}}

### Bribe System

| NPC Type | Bribe Cost | Success Chance | Notes |
|----------|-----------|---------------|-------|
| Police patrol | $500 | 70% | Refusal = arrest |
| Security guard | $300 | 85% | Usually accepts |
| Witness civilian | $100 | 95% | Cheap and reliable |
| Rival gang lookout | $1,000 | 50% | Risky, fight is better option |

### Lock Pick Minigame

The lockpicking system has 3 difficulty levels:

| Difficulty | Pins | Tolerance | Time Limit | Skill Required |
|-----------|------|-----------|------------|---------------|
| Easy | 3 | Wide | 30s | Lockpicking 1 |
| Medium | 5 | Medium | 20s | Lockpicking 2 |
| Hard | 7 | Tight | 15s | Lockpicking 3 |

**Technique:** Apply gentle pressure (mouse click), rotate pick slowly. When you feel resistance, hold position and increase pressure until the pin sets. If you hear a click, you broke the pin (permanent lock damage).

{{< section "Recommended Settings" >}}

| Setting | Recommendation | Why |
|---------|---------------|-----|
| Field of View | 90-100 | Better peripheral awareness during stealth |
| Sensitivity | 2-3 (low) | Precision aiming for lockpick |
| Crouch mode | Toggle | Saves pinky finger during long stealth sections |
| Auto-run | Off | Manual control is safer in tight spaces |
| Shadow quality | Medium | Shadows affect stealth detection range |
| Audio mix | Headphones | Footstep direction is critical for stealth |

{{< insight >}}The toggle crouch setting is the single most impactful change you can make. Hold-to-crouch fatigues your hand during the 15-20 minute stealth sections that make up most Crime Simulator gameplay. Switch it in Settings > Controls > Crouch Mode.{{< /insight >}}

<div class="resource-section">
  <h2>Community Verification</h2>
  {{< resourcegrid >}}
    {{< resourcecard name="Controls Discussion" url="https://steamcommunity.com/app/2463290/discussions" desc="Community control customization guides" >}}
    {{< resourcecard name="Lockpick Training Tool" url="https://steamcommunity.com/sharedfiles/filedetails/" desc="Third-party lockpick practice trainer" >}}
  {{< /resourcegrid >}}
</div>
