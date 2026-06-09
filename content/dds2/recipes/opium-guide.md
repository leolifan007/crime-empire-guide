---
title: "DDS2 Cutting Agents Guide: Maximize Profit Without Killing Customers"
date: 2026-06-09T14:20:00+08:00
draft: false
game: dds2
tag: RECIPES
weight: 2
---

{{< callout "info" >}}
The DDS2 Datamine v2 reveals that cutting agents have three key properties: TOX (toxicity), POT (potency multiplier), and ADD (addiction). Use low-TOX agents like flour and sugar to double your volume without losing customers.

{{< /callout >}}

{{< section "How Cutting Agents Work" >}}

From the Datamine: each cutting agent modifies the final product's stats. The goal is to maximize volume while keeping TOX low enough that customers survive to re-order.

| Property | Meaning | Optimal Value |
|----------|---------|--------------|
| TOX (Toxicity) | Customer health risk | As low as possible (under 0.5) |
| POT (Potency) | Multiplies drug strength | Over 1.0 = stronger |
| ADD (Addiction) | Customer dependency | Low keeps customers alive longer |
| STR (Strength) | Perceived quality | Over 1.0 = customers happy |

{{< section "Top Cutting Agents Ranked" >}}

| Rank | Agent | TOX | POT | ADD | STR | Best Use |
|------|-------|-----|-----|-----|-----|----------|
| 1 | Flour | 0.0 | - | - | - | Safe volume increase (baking base) |
| 2 | Salt | 0.0 | - | - | - | Completely safe, no side effects |
| 3 | Sugar | 0.0 | - | - | - | Safe, widely available |
| 4 | Water | 0.0 | - | - | - | Base diluent, no effect |
| 5 | Vinegar | 0.0 | - | - | - | Safe but limited use |
| 6 | Soda (baking) | 0.1 | - | - | - | Minimal risk |
| 7 | Ephedrine | 0.1 | - | - | - | Low toxicity source |
| 8 | Cough Syrup | 0.0 | 1.01 | 0.1 | - | Boosts potency slightly |
| 9 | Migraine Meds | 0.0 | 1.01 | 0.1 | - | Boosts potency slightly |
| 10 | Ethanol | 0.2 | - | 0.1 | 1.05 | Risk-reward tradeoff |

{{< callout "warning" >}}NEVER USE: Gasoline (TOX: 0.9), Methanol (TOX: 0.9), Washing Powder (TOX: 0.7), Explosive Compound (TOX: 0.9). These will rapidly kill your customer base.{{< /callout >}}

{{< section "Advanced Cutting: Intermediate Compounds" >}}

The Datamine lists several intermediate compounds that can be used as cutting bases:

| Compound | TOX | POT | Effect |
|----------|-----|-----|--------|
| Amphetamine Salts | 0.85 | 1.03 | Risky but potent (STR: 1.1) |
| Cannabis Powder (POT 0.95) | - | - | Expensive to use as cut |
| Crack Lump | 0.5 | 1.04 | Moderate risk, STR: 1.6 |
| Ephedrine Compound | 0.5 | 1.03 | Moderate risk, STR: 1.1 |

{{< section "Profit Optimization Formula" >}}

1. Cook base product (POT 0.88 for meth)
2. Cut with 30-50% flour or sugar by weight
3. Add 5-10% cough syrup for potency boost
4. Customer gets: adequate potency + low toxicity = repeat orders

The DDS2 community consensus: "Use low-TOX cutting agents like flour, sugar, or salt to maximize profit without losing customers."

<div class="resource-section">
  <h2>Community Resources</h2>
  {{< resourcegrid >}}
    {{< resourcecard name="DDS2 Datamine v2" url="https://drugdealersim.com/wiki/dds2/substances-cutting-agents" desc="Full 73-substance catalog with all properties" target="_blank" rel="noopener noreferrer" >}}
    {{< resourcecard name="DDS2 Wiki Cutting Agents" url="https://drugdealersim.com/wiki/dds2/substances-cutting-agents" desc="Cutting agents section with detailed effects" target="_blank" rel="noopener noreferrer" >}}
    {{< resourcecard name="Steam FAQ Guide" url="https://steamcommunity.com/sharedfiles/filedetails/?id=3273716171" desc="Cooking recipes and employee management" target="_blank" rel="noopener noreferrer" >}}
  {{< /resourcegrid >}}
</div>
