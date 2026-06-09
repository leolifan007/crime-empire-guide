---
title: "DDS2 Staff Management Guide: Hire, Assign, and Promote"
date: 2026-06-09T09:50:00+08:00
draft: false
game: dds2
tag: STAFF
weight: 1
---

{{< callout "info" >}}
Staff in DDS2 are not cosmetic hires. Each staff member has stats, loyalty, and a skill tree. Bad staff management loses you money. Optimal assignments double your production throughput. Here is everything about the staff system.

{{< /callout >}}

{{< section "Staff Stats Explained" >}}

Every hire has 5 visible stats and 2 hidden stats:

| Stat | Range | Effect |
|------|-------|--------|
| Skill | 1-10 | Task speed multiplier (10% per point) |
| Loyalty | 1-10 | Betrayal chance (10% per missing point) |
| Speed | 1-5 | Movement speed for runners/drivers |
| Reliability | 1-5 | Order completion rate |
| Negotiation | 1-5 | Supply cost reduction |

**Hidden stats (not shown in hiring screen):**
- **Stress level** -- increases over time, reduces loyalty by 1 per day above 50%
- **Rival affiliation** -- 5% chance of spies from rival cartels at high loyalty

{{< insight >}}A staff member with Skill 5 and Loyalty 3 is a better hire than Skill 8 and Loyalty 1. Low loyalty staff will steal from you, tip off police, or defect to rivals. The production loss from a defection costs more than the skill gain.{{< /insight >}}

{{< section "Staff Role Assignments" >}}

### Cooks

| Task | Skill Requirement | Output | Notes |
|------|------------------|--------|-------|
| Basic mixing | Skill 2+ | 2 batches/hr | Unlocked immediately |
| Quality processing | Skill 5+ | +15% sell price | Buy recipe upgrade $2k |
| Mass production | Skill 7+ | 4 batches/hr | Requires upgraded lab |

**Best cook assignment:** Skill 7+ cooks should always do mass production. The extra batch per hour at mass production beats the quality bonus from quality processing ($800/hr vs $450/hr).

### Runners

| Task | Skill Requirement | Output | Notes |
|------|------------------|--------|-------|
| Local delivery | Speed 3+ | 10 orders/hr | Low risk |
| Inter-zone transport | Speed 4+ | 8 orders/hr | Medium risk |
| Black market deals | Negotiation 4+ | 12 orders/hr | High risk, +25% payout |

**Best runner assignment:** Use Speed 4+ runners for inter-zone transport first, then fill remaining with local delivery. Black market deals are tempting but the arrest risk is high -- only use Negotiation 5+ runners.

### Guards

| Task | Skill Requirement | Effect | Notes |
|------|------------------|--------|-------|
| Patrol | Skill 2+ | -80% raid chance | Default assignment |
| Interrogation | Skill 5+ | Expose rival spies | Unlocks at rank 4 |
| Retaliation | Skill 8+ | Raid enemy hideouts | Unlocks at rank 6 |

{{< section "Hiring Strategy Timeline" >}}

| Net Worth | Hire | Priority |
|-----------|------|----------|
| $5,000 | 1 Runner | Speeds up delivery income |
| $8,000 | 1 Guard | Protects growing stash |
| $12,000 | 1 Cook | Doubles production |
| $20,000 | 2nd Runner | Expands delivery zone |
| $30,000 | 2nd Cook | Triples production |
| $50,000 | 1 Driver | Enables multi-hideout logistics |
| $100,000 | Manager | Automates task assignment |
| $200,000+ | Full squad (8+) | Complete empire automation |

{{< section "Loyalty Management" >}}

| Action | Loyalty Effect | Cost |
|--------|---------------|------|
| Pay bonus | +2 loyalty | 1 day's wage |
| Give time off | +1 loyalty per day | Lost production |
| Promote | +3 loyalty | +$50/day wage |
| Ignore complaints | -1 per day | Free but dangerous |
| Threaten | Temporary +1, permanent -1 | Risk betrayal |

**Optimal loyalty loop:** Every 7 days, give a bonus to your top 2 staff. Every 14 days, promote your best performer. Drop anyone below loyalty 4 immediately (fire them) -- they are more expensive to keep than replace.

{{< callout "warning" >}}Any staff member below loyalty 3 has a 30% daily chance of being a rival spy. You will notice missing product, failed orders, and police showing up at your lab. Fire them on sight. Do not give them a second chance.{{< /callout >}}

{{< section "Staff Economy Table" >}}

| Role | Wage/Day | Revenue/Day | Net/Day | Breakeven |
|------|----------|-------------|---------|-----------|
| Runner (lvl 1) | $50 | $400 | $350 | 1 day |
| Runner (lvl 5) | $120 | $1,200 | $1,080 | 1 day |
| Cook (lvl 1) | $80 | $600 | $520 | 2 days |
| Cook (lvl 5) | $180 | $2,200 | $2,020 | 2 days |
| Guard (lvl 1) | $100 | $0 (prevention) | -$100 | N/A (insurance) |
| Driver (lvl 1) | $150 | $800 | $650 | 2 days |
| Manager | $200 | $500 (efficiency) | $300 | 5 days |

<div class="resource-section">
  <h2>Resources</h2>
  {{< resourcegrid >}}
    {{< resourcecard name="Staff Calculator" url="https://steamcommunity.com/sharedfiles/filedetails/?id=3400112789" desc="Spreadsheet for staff ROI calculations" >}}
    {{< resourcecard name="Steam Community Forum" url="https://steamcommunity.com/app/1708850/discussions" desc="Staff management Q&A" >}}
  {{< /resourcegrid >}}
</div>
