---
title: "Casino Strategy: Ride the Bus vs Blackjack, What I Actually Made"
date: 2026-06-15T12:15:00+08:00
draft: false
game: schedule-i
tag: MONEY
weight: 7
---

I spent a full evening testing the casino to see which game actually pays. Took notes, tried different strategies, reloaded saves when I busted. Here's what I found.

**Ride the Bus pays better than Blackjack.**

Reddit community analysis pegs Ride the Bus at roughly +25% expected value per hand, compared to Blackjack's -0.5% (even with perfect play). I can't verify the exact math, but my own testing matches the pattern -- Ride the Bus consistently grew my stack faster.

The reason is the multiplier structure. Three correct guesses in a row pays 8x your bet. With save-scumming (save before you start, reload if you lose big), there's no real downside.

**Ride the Bus strategy I use:**

| Card Range | My Guess | Why |
|-----------|----------|-----|
| 2 through 6 | Higher | Statistically safe, 70%+ chance |
| 7 through 9 | Higher (cautious) | Risky range, 50-60% |
| 10 through Ace | Lower | Safe bet, face cards skew lower |

Round 1 is a 50/50 color guess. Rounds 2 and 3 get better odds if you're paying attention. If the gap between two drawn cards is 3 or less (like a 7 then an 8), the odds drop. Skip that round and cash out if the 8x multiplier is already in play.

I start with $1,000 and bet 10% of my bankroll per round. Bet smaller on the color guess (first round), same bet on rounds 2 and 3. If I hit an 8x payout, I'm up to $8,000 and I go home to save.

**Blackjack basic strategy (if you prefer cards):**

I play Blackjack less often, but when I do, I use standard basic strategy:

- Hard 10 or 11: Double down (especially if dealer shows a low card)
- Hard 12-16: Stand if dealer shows 2-6, Hit if dealer shows 7+
- Hard 17+: Always stand
- Soft 18: Stand vs dealer 2-6, Hit vs 9-Ace
- Pairs: Always split Aces and 8s. Never split 10s.
- Never take insurance. It's a sucker bet. The math doesn't work out over time.

TheGamer and Fandom Wiki cover the same Blackjack rules I verified.

**Save-scumming is the real strategy:**

Here's the routine I settled on:

1. Save at my property before going to the casino
2. Go to the casino between 4PM and 5AM (closed outside those hours)
3. Start with $1,000-$2,000 on Ride the Bus
4. If I turn $1K into $5K+, go home and save
5. If I bust, reload the save and try again
6. Stop when I hit $20K-$30K and use that money for the Barn

The first time I tried this, I turned $1,000 into $22,000 in about 30 minutes of real time. Reloaded saves twice after bad streaks. Second time I had worse luck and walked away with $8K after 45 minutes. It's not consistent per-round, but with save-scumming you can't lose money long-term.

**When to stop:**

The casino is a tool, not your main income. Once you have $20K-$30K, you should be [buying the Barn](/schedule-i/automation/barn-and-warehouse/) ($25K) and [setting up automation](/schedule-i/automation/workshop/). Casino money is fast but unreliable. Automation money is slower but consistent. Use the casino to jumpstart your mid-game, then switch to production.

I see posts on Reddit asking "how to make millions at the casino" and honestly, save-scumming to $1M would take hours of reloading. At that point you'd make more money running a Barn for the same amount of time.

**One thing the casino nerfed:**

Earlier patches made the games slightly tighter. As of [v0.4.5](/schedule-i/patch/v045-update/), save-scumming still works but the minigame odds feel a bit more restricted than launch. Ride the Bus is still the best per-unit-time game according to community testing. The casino is north of main town, near the highway overpass -- no entry fee or rank requirement.

For the comparison with drug production income, see the [Profit Rankings](/schedule-i/recipes/profit/).

{{< resourcegrid >}}
  {{< resourcecard name="Casino Wiki (Fandom)" url="https://schedule-1.fandom.com/wiki/Casino" desc="Game rules and payout tables" >}}
  {{< resourcecard name="Reddit Infinite Money Guide" url="https://www.reddit.com/r/Schedule_I/comments/1jogce7/infinite_money_at_the_casino/" desc="Community Ride the Bus strategy" >}}
  {{< resourcecard name="ScalaCube Casino Guide" url="https://scalacube.com/blog/schedule-1/schedule-1-casino-guide" desc="Casino walkthrough with odds" >}}
{{< /resourcegrid >}}
