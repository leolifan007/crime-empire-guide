---
title: "DDS2 Meth Recipe: Cook Your First Batch (Step-by-Step)"
date: 2026-06-09T14:10:00+08:00
draft: false
game: dds2
tag: RECIPES
weight: 1
---

The DDS2 Datamine v2 catalogs 73 substances. Meth starts at POT 0.88 (pure potency). The first cook is straightforward once you know the ingredient chain: ephedrine to compound to purify to cut. I wasted my first few batches guessing ratios. This guide walks through every step from ingredient sourcing to finished product.

{{< diagram "diagrams/dds2-meth-production.svg" "DDS2 meth production flow diagram showing ingredient chain from ephedrine to finished product" "720" >}}

**Step 1: Unlock the recipe**

Before you can cook meth, you need the recipe. The recipe card is a physical item found in the tutorial zone warehouse. Unlike some games where recipes auto-unlock, DDS2 requires you to find the card and interact with it. The recipe unlocks as part of the main story questline -- you will receive a prompt to find it after talking to your contact about making more money.

Do not rush to get the recipe before the story prompts you. The Reddit community advises waiting for the story trigger, as the recipe location may not spawn until the quest is active.

**Step 2: Source the ingredients:**

Based on the Datamine v2 (verified via community wiki and Steam FAQ guide):

| Ingredient | Source | Toxicity |
|-----------|--------|----------|
| Ephedrine (EPHE) | Pharmacy | 0.1 (low) |
| Iodoric Acid (HI) | Chemical supplier | 0.6 (medium) |
| Methylamine (METHYL) | Farm supply | 0.6 (medium) |
| Ammonia (AMMONIA) | Hardware store | 0.4 (medium) |
| Water | Any vendor | 0.0 (none) |

{{< callout "warning" >}}
Do NOT use gasoline or methanol as substitutes for any ingredient. The Datamine confirms TOX: 0.9 for both gasoline and methanol. Using them will produce highly toxic product that kills your customers rapidly. I learned this lesson when my customers started dropping after a batch cut with the wrong solvent. A dead customer is a permanent loss of revenue.
{{< /callout >}}

**Step 3: Create the compound:**

Once you have all ingredients, use the chemistry table to create Methamphetamine Compound. The Datamine lists these stats:

| Property | Value |
|----------|-------|
| Type | Fluid |
| Ingredients | Ephedrine + Iodoric Acid + Methylamine + Ammonia + Water |
| TOX (toxicity) | 0.3 (moderate) |
| POT (potency) | 1.03 (strong -- higher than finished product) |
| Status | Work-in-progress -- needs purification |

The compound is more potent than the finished meth (POT 1.03 vs 0.88), but this potency decreases during purification. Do not sell the compound directly -- it needs further processing.

**Step 4: Purify to powdered meth:**

Transfer the compound to the purification equipment. The output is METH-POWDER (Powdered Methamphetamine):

| Property | Value |
|----------|-------|
| POT (potency) | 0.88 (reduced from compound's 1.03 due to purification loss) |
| STR (strength) | 1.4 (strength multiplier affects perceived quality) |
| TOX (toxicity) | 0.3 (toxicity remains moderate) |

Purification is a batch process. Each batch of compound yields a specific amount of powdered meth. The exact yield depends on your equipment quality -- higher-tier purification tables produce less waste.

**Step 5: Cut for profit margin:**

The Datamine documents cutting agents and their effects. Use low-TOX agents to maximize profit without losing customers:

| Cutting Agent | Effect | Best For |
|--------------|--------|----------|
| Sugar | No effect, no toxicity | Pure volume increase |
| Flour | No effect, no toxicity | Best price-to-volume ratio |
| Salt | STR: 1.05, no toxicity | Quality preservation |
| Cough Syrup | POT: 1.01, ADD: 0.1 | Potency boost |
| Migraine Medicine | POT: 1.01, ADD: 0.1 | Potency boost |

{{< callout "tip" >}}
The Datamine's key finding: use low-TOX cutting agents like flour, sugar, or salt to maximize profit without losing customers. A customer who dies from toxic product is a permanent loss of revenue. The optimal cut ratio is approximately 30-50% cutting agent by weight, with the remainder being your purified meth. For premium batches, add 5-10% cough syrup for a minor potency boost without significant toxicity increase.
{{< /callout >}}

**Practical example: Profitability comparison**

Here is how different quality levels perform when selling through a dealer:

| Quality Level | Yield per Batch | Retail Value | Customer Retention |
|--------------|----------------|-------------|-------------------|
| Pure (POT 0.88) | Base | High | Good -- satisfied customers |
| Cut with flour (30%) | +30% volume | Medium | Excellent -- no toxicity increase |
| Cut with salt (30%) | +30% volume | Medium-High | Excellent -- slight STR boost |
| Cut with gas | +50% volume | Low | Poor -- customers die rapidly |
| Cut with washing powder | +40% volume | Low | Very poor -- high toxicity |

**Profit optimization formula:**

1. Cook base product (POT 0.88)
2. Cut with 30% flour or salt by weight
3. Add 5% cough syrup for potency boost
4. Result: adequate potency + low toxicity = repeat customer orders

**Step 6: Equipment upgrades for better yields:**

| Equipment Tier | Cost | Yield Bonus | Purification Efficiency |
|---------------|------|-------------|------------------------|
| Basic chemistry table | $800 | None | 70% |
| Standard lab station | $3,000 | +20% yield | 80% |
| Advanced processing unit | $8,000 | +40% yield | 90% |
| Industrial-grade setup | $15,000 | +60% yield | 95% |

Upgrading from basic to standard equipment is worth it once you have consistent ingredient supply. The 20% yield bonus means 1 extra batch for every 5 you cook.

**Related Guides:**

- [Cutting Agents Guide](/dds2/recipes/opium-guide/) -- Full cutting agent breakdown with toxicity and potency data
- [Early Money Guide](/dds2/money/early-money/) -- How to fund your first lab setup
- [Empire Guide](/dds2/money/empire-guide/) -- Scaling production with staff and multi-hideout strategy

{{< resourcegrid >}}
    {{< resourcecard name="DDS2 Datamine v2" url="https://drugdealersim.com/wiki/dds2/substances-cutting-agents" desc="73 substances catalog: all potency, toxicity, addiction values" target="_blank" rel="noopener noreferrer" >}}
    {{< resourcecard name="Steam FAQ Guide" url="https://steamcommunity.com/sharedfiles/filedetails/?id=3273716171" desc="Cooking, employees, and early-game strategy" target="_blank" rel="noopener noreferrer" >}}
{{< /resourcegrid >}}
