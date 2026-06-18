---
title: "DDS2 Cutting Agents Guide: Maximize Profit Without Killing Customers"
date: 2026-06-09T14:20:00+08:00
draft: false
game: dds2
tag: RECIPES
weight: 2
---

The DDS2 Datamine v2 reveals that cutting agents have three key properties: TOX (toxicity), POT (potency multiplier), and ADD (addiction). Use low-TOX agents like flour and sugar to double volume without losing customers. I tested a few cutting ratios and the difference in customer retention is dramatic.

**How cutting agents work:**

Each cutting agent modifies the final product's stats. The goal is to maximize volume while keeping TOX low enough that customers survive to re-order.

| Property | Meaning | Optimal Value |
|----------|---------|--------------|
| TOX (Toxicity) | Customer health risk | As low as possible (under 0.5) |
| POT (Potency) | Multiplies drug strength | Over 1.0 = stronger |
| ADD (Addiction) | Customer dependency | Low keeps customers alive longer |
| STR (Strength) | Perceived quality | Over 1.0 = customers happy |

**Top cutting agents ranked:**

| Rank | Agent | TOX | Best Use |
|------|-------|-----|----------|
| 1 | Flour | 0.0 | Safe volume increase |
| 2 | Salt | 0.0 | Completely safe, no side effects |
| 3 | Sugar | 0.0 | Safe, widely available |
| 4 | Water | 0.0 | Base diluent, no effect |
| 5 | Vinegar | 0.0 | Safe but limited use |
| 6 | Soda (baking) | 0.1 | Minimal risk |
| 7 | Ephedrine | 0.1 | Low toxicity source |
| 8 | Cough Syrup | 0.0 | Boosts potency slightly |
| 9 | Migraine Meds | 0.0 | Boosts potency slightly |
| 10 | Ethanol | 0.2 | Risk-reward tradeoff |

NEVER USE: Gasoline (TOX: 0.9), Methanol (TOX: 0.9), Washing Powder (TOX: 0.7), Explosive Compound (TOX: 0.9). These will rapidly kill your customer base. I made this mistake once and lost half my regulars.

**Profit optimization formula I use:**

1. Cook base product (POT 0.88 for meth)
2. Cut with 30-50% flour or sugar by weight
3. Add 5-10% cough syrup for potency boost
4. Result: adequate potency + low toxicity = repeat orders

The DDS2 community consensus from the Datamine: use low-TOX cutting agents like flour, sugar, or salt to maximize profit without losing customers.

{{< resourcegrid >}}
    {{< resourcecard name="DDS2 Datamine v2" url="https://drugdealersim.com/wiki/dds2/substances-cutting-agents" desc="Full 73-substance catalog with all properties" target="_blank" rel="noopener noreferrer" >}}
    {{< resourcecard name="Steam FAQ Guide" url="https://steamcommunity.com/sharedfiles/filedetails/?id=3273716171" desc="Cooking recipes and employee management" target="_blank" rel="noopener noreferrer" >}}
{{< /resourcegrid >}}
