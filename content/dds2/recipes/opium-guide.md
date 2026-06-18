---
title: "DDS2 Cutting Agents Guide: Maximize Profit Without Killing Customers"
date: 2026-06-09T14:20:00+08:00
draft: false
game: dds2
tag: RECIPES
weight: 2
---

The DDS2 Datamine v2 reveals that cutting agents have three key properties: TOX (toxicity), POT (potency multiplier), and ADD (addiction). Use low-TOX agents like flour and sugar to double volume without losing customers. I tested several cutting ratios and the difference in customer retention is dramatic -- switching from high-TOX to low-TOX agents turned my business around from losing customers to steady repeat orders.

**How cutting agents work:**

Each cutting agent modifies the final product's stats when mixed in. The goal is to maximize volume (by adding cheap filler) while keeping toxicity low enough that customers survive to re-order.

| Property | Meaning | Optimal Value |
|----------|---------|--------------|
| TOX (Toxicity) | Customer health risk per dose | As low as possible (under 0.5) |
| POT (Potency) | Multiplies drug strength/effect | Over 1.0 = stronger product |
| ADD (Addiction) | Customer dependency rate | Low keeps customers alive longer |
| STR (Strength) | Perceived quality by customers | Over 1.0 = customers are satisfied |

The formula for final product stats is a weighted average based on the percentage of each cutting agent used. A product cut 50/50 with a TOX 0.0 agent and a TOX 0.6 agent will end up with approximately TOX 0.3.

**Top cutting agents ranked by safety and effectiveness:**

| Rank | Agent | TOX | POT | Best Use |
|------|-------|-----|-----|----------|
| 1 | Flour | 0.0 | 1.0 | Safe volume increase, widely available |
| 2 | Salt | 0.0 | 1.0 | Completely safe, no side effects |
| 3 | Sugar | 0.0 | 1.0 | Safe, available at general stores |
| 4 | Water | 0.0 | 1.0 | Base diluent, no effect on stats |
| 5 | Vinegar | 0.0 | 1.0 | Safe but limited availability |
| 6 | Soda (baking) | 0.1 | 1.0 | Minimal risk, slightly lower safety |
| 7 | Cough Syrup | 0.0 | 1.01 | Boosts potency slightly, safe |
| 8 | Migraine Meds | 0.0 | 1.01 | Boosts potency slightly, safe |
| 9 | Ephedrine | 0.1 | 1.0 | Low toxicity, adds precursor value |
| 10 | Ethanol | 0.2 | 1.0 | Risk-reward tradeoff |

{{< callout "warning" >}}
NEVER USE these agents: Gasoline (TOX: 0.9), Methanol (TOX: 0.9), Washing Powder (TOX: 0.7), Explosive Compound (TOX: 0.9). These will rapidly kill your customer base. I made this mistake once with gasoline and lost half my regulars within three in-game days. A dead customer is a permanent loss of revenue. The short-term volume gain is never worth the long-term customer loss.
{{< /callout >}}

**Practical example: Profit optimization formula**

Here is the exact cutting formula I use for meth that maximizes profit while keeping customers alive:

1. Cook 100g of base meth (POT 0.88, TOX 0.3)
2. Add 40g of flour (TOX 0.0, POT 1.0) -- safe volume boost
3. Add 10g of salt (TOX 0.0, STR 1.05) -- slight quality improvement
4. Add 5g of cough syrup (TOX 0.0, POT 1.01) -- minor potency boost
5. Result: 155g total product with approximately TOX 0.19 and POT ~0.71

The resulting product has lower toxicity than pure meth (0.19 vs 0.3) because the cutting agents have zero toxicity. Customers survive longer and re-order more frequently. The total volume increased by 55% with minimal potency loss.

| Metric | Pure Meth | Cut Meth (this formula) |
|--------|-----------|------------------------|
| Weight per batch | 100g | 155g |
| Potency (POT) | 0.88 | ~0.71 |
| Toxicity (TOX) | 0.3 | ~0.19 |
| Total sale value | Base | +55% volume |
| Customer retention | Good | Excellent |

**Cutting agents by drug type:**

Different base drugs respond differently to cutting agents. Here are the recommended cuts for each:

| Drug | Recommended Cut | Ratio | Expected Result |
|------|----------------|-------|-----------------|
| Meth | Flour + Salt | 60:30:10 (product:flour:salt) | Safe volume boost |
| Cannabis | Sugar | 80:20 (product:sugar) | Minimal quality loss |
| Amphetamine | Baking soda | 70:30 (product:soda) | Stable product |
| Opium | Flour | 75:25 (product:flour) | Good retention |
| Cocaine | Salt + Caffeine | 70:20:10 | Premium quality |

**Common cutting mistakes:**

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Using gasoline for volume | TOX 0.9 kills customers fast | Use flour instead |
| Over-cutting (more than 50% filler) | Potency too low, customers unsatisfied | Keep cut under 40% |
| Using toxic medicines | Unexpected customer deaths | Check TOX before using any agent |
| Mixing incompatible agents | Unpredictable stat results | Test new combinations on small batches first |

{{< callout "info" >}}
The DDS2 community consensus from the Datamine is clear: use low-TOX cutting agents like flour, sugar, or salt to maximize profit without losing customers. The ideal cut ratio is 30-50% cutting agent by weight. Higher than 50% and product quality drops too much. Lower than 30% and you are leaving profit on the table. Test your cut on a small batch first and monitor customer feedback before scaling up.
{{< /callout >}}

**Related Guides:**

- [Meth Cooking Guide](/dds2/recipes/cook-meth/) -- Step-by-step meth production from ingredients to finished product
- [Early Money Guide](/dds2/money/early-money/) -- How to fund your production operation
- [Empire Guide](/dds2/money/empire-guide/) -- Scaling production with multi-hideout strategy

{{< resourcegrid >}}
    {{< resourcecard name="DDS2 Datamine v2" url="https://drugdealersim.com/wiki/dds2/substances-cutting-agents" desc="Full 73-substance catalog with all properties" target="_blank" rel="noopener noreferrer" >}}
    {{< resourcecard name="Steam FAQ Guide" url="https://steamcommunity.com/sharedfiles/filedetails/?id=3273716171" desc="Cooking recipes and employee management" target="_blank" rel="noopener noreferrer" >}}
{{< /resourcegrid >}}
