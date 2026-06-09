---
title: "DDS2 Meth Recipe: Cook Your First Batch (Step-by-Step)"
date: 2026-06-09T14:10:00+08:00
draft: false
game: dds2
tag: RECIPES
weight: 1
---

{{< callout "info" >}}
The DDS2 Datamine v2 (drugdealersim.com) catalogs 73 substances. Meth starts at POT 0.88 (pure). The first cook is straightforward once you know the ingredient chain: ephedrine -> compound -> purify -> cut.

{{< /callout >}}

{{< diagram "diagrams/dds2-meth-production.svg" "DDS2 Meth Production: From Ingredients to Finished Product" "720" >}}

{{< section "Step 1: Source the Ingredients" >}}

Based on the DDS2 Datamine v2 (verified via drugdealersim.com wiki and Steam FAQ guide):

| Icon | Ingredient | Source | Toxicity |
|------|-----------|--------|----------|
| {{< material dds2-ephedrine >}} | Ephedrine (EPHE) | Pharmacy | 0.1 (low) |
| | Iodoric Acid (HI) | Chemical supplier | 0.6 (medium) |
| | Methylamine (METHYL) | Farm supply | 0.6 (medium) |
| | Ammonia (AMMONIA) | Hardware store | 0.4 (medium) |
| | Water | Any vendor | 0.0 (none) |

{{< callout "warning" >}}Do NOT use gasoline or methanol as substitutes. The Datamine confirms TOX: 0.9 for both -- you will poison your customer base rapidly.{{< /callout >}}

{{< section "Step 2: Create the Compound" >}}

The Datamine lists METH-COMP (Methamphetamine Compound) as:

- Type: Fluid
- Ingredients: Ephedrine + Iodoric Acid + Methylamine + Ammonia + Water
- TOX: 0.3 | POT: 1.03
- Status: Work-in-progress, needs purification

{{< section "Step 3: Purify to Powdered Meth" >}}

Purifying the compound produces METH-POWDER (Powdered Methamphetamine):
- Type: SolidPowder
- POT: 0.88 (reduced from compound's 1.03 due to purification loss)
- STR: 1.4 (strength multiplier affects perceived quality)
- TOX: 0.3 (toxicity remains moderate)
- This is the base product before cutting

{{< section "Step 4: Cut for Profit Margin" >}}

The Datamine documents cutting agents and their effects. Use low-TOX agents to maximize profit without losing customers:

| Cutting Agent | Effect | Best For |
|--------------|--------|----------|
| Sugar | No effect, no toxicity | Pure volume increase |
| Flour | No effect, no toxicity | Best price-to-volume |
| Salt | STR: 1.05, no toxicity | Quality preservation |
| Cough Syrup | POT: 1.01, ADD: 0.1 | Potency boost |
| Migraine Medicine | POT: 1.01, ADD: 0.1 | Potency boost |

{{< insight >}}The Datamine's key finding: "Use low-TOX cutting agents like flour, sugar, or salt to maximize profit without losing customers." A customer who dies from toxic product is a permanent loss of revenue.{{< /insight >}}

{{< section "Profitability Comparison" >}}

| Quality Level | Yield per Batch | Retail Value | Customer Retention |
|--------------|----------------|-------------|-------------------|
| Pure (POT 0.88) | Base | High | Good |
| Cut with flour | +30% volume | Medium | Excellent (low tox) |
| Cut with gas | +50% volume | Low | Poor (customers die) |
| "Smurf Dope" (POT 0.95) | Special recipe | Highest | Best (requires Casino DLC) |

<div class="resource-section">
  <h2>Community Resources</h2>
  {{< resourcegrid >}}
    {{< resourcecard name="DDS2 Datamine v2" url="https://drugdealersim.com/wiki/dds2/substances-cutting-agents" desc="73 substances catalog: all potency, toxicity, addiction values" target="_blank" rel="noopener noreferrer" >}}
    {{< resourcecard name="Steam FAQ Guide" url="https://steamcommunity.com/sharedfiles/filedetails/?id=3273716171" desc="Cooking, employees, and early-game strategy" target="_blank" rel="noopener noreferrer" >}}
    {{< resourcecard name="DDS2 Wiki Substances" url="https://drugdealersim.com/wiki/dds2/substances-cutting-agents" desc="Full cutting agents reference with properties" target="_blank" rel="noopener noreferrer" >}}
  {{< /resourcegrid >}}
</div>
