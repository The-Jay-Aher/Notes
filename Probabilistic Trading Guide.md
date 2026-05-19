# Probabilistic Trading Guide

## Quick Summary

Probabilistic trading means you stop asking, "Will this trade win?" and start asking, "Is this setup, at this location, in this market condition, worth risking money on over a large sample of similar trades?"

That is the entire shift. A single trade is uncertain. A good process can still lose today. A bad process can still win today. What matters is whether the same decision repeated across 50, 100, or 300 trades has positive expectancy while keeping downside controlled.

This guide is educational, not financial advice. Short-term trading is risky, especially with leverage. Investor.gov warns that day trading is fast-moving, speculative, often uses leverage, and can lead to quick and substantial losses. ([Investor.gov][1]) The CFTC also warns that many retail OTC forex customers lose money after spreads, financing, fees, and other costs are included. ([CFTC][2])

Related notes:

- [Positional Trader](Positional%20Trader.md)
- [Financial Jargon Glossary](Financial%20Jargon%20Glossary.md)
- [Fundamental Analysis](Fundamental%20Analysis.md)

How these notes fit together:

| Note | Use it for |
| --- | --- |
| [Financial Jargon Glossary](Financial%20Jargon%20Glossary.md) | Definitions: OI, short covering, IV crush, margin, R-multiple, slippage, spread |
| [Fundamental Analysis](Fundamental%20Analysis.md) | Business quality, valuation, accounting, and catalysts |
| [Positional Trader](Positional%20Trader.md) | Full positional trading operating manual |
| This note | Probability, expectancy, decision scoring, sample size, and manual trade review |

## Institutional operating boundary

This guide describes how to think in distributions. It does not prove that any current setup has positive expectancy. A claim about edge is valid only after it is measured from a clean sample.

Minimum evidence before calling a setup tradeable:

```text
1. Setup rules are written before testing.
2. Entry, stop, target, and invalidation are objective.
3. At least 50 replay or paper trades are recorded.
4. Costs, spread, slippage, and gap-through-stop behavior are included.
5. Every trade is recorded in R.
6. Rule-following rate is measured.
7. Expectancy is calculated by setup, not by random mixed trades.
8. Bad wins are treated as process failures.
```

The 8-point scorecard in this note is a permission filter, not a probability model. Do not increase size because a trade "feels A-grade" unless your own data shows that score bucket has better expectancy.

Use these workbook and audit files when building evidence:

- [Professional Trading Workbook Template](pro_trading_workbook_template.md)
- [Action Plan](action_plan.md)

---

# 1. The Core Idea: Probability, Not Prophecy

A probabilistic trader does not need to be right on every trade. The job is to repeatedly execute trades where the expected value is positive and the damage from wrong trades is controlled.

Weak question:

```text
Will this trade win?
```

Better question:

```text
If I take this same setup 100 times under similar conditions, does the total result justify the risk?
```

Best question:

```text
What is the base rate of this setup, what improves or worsens it today, what is my reward-to-risk, and what happens if I am wrong?
```

## The probabilistic mindset

| Question | Probabilistic answer |
| --- | --- |
| Can this trade lose? | Yes. Every trade can lose. |
| Does a loss mean the setup is bad? | Not by itself. One result is weak evidence. |
| Does a win mean the setup is good? | Not by itself. Bad trades can win. |
| What matters? | A large sample of similar trades. |
| What is the goal? | Positive expectancy with controlled downside. |
| What is the enemy? | Oversizing, random entries, moving stops, and judging by one trade. |

The expert version of trading is not "always right." It is **wrong often, small, and according to plan**. A trader who accepts small planned losses can survive long enough for a real edge to show up.

## Probability language you should use

Replace emotional statements with probability statements.

| Emotional statement | Probabilistic version |
| --- | --- |
| This stock must go up | This setup has historically worked when trend, level, and trigger align |
| I cannot take another loss | A loss is acceptable if it is inside planned R |
| I am sure | The setup is A-grade, but still uncertain |
| I will hold until it recovers | The thesis is invalid if price breaks the defined level |
| I made money, so I was right | The trade outcome was profitable; now check whether the process was valid |
| I lost money, so I was wrong | The trade outcome was negative; now check whether the process was followed |

---

# 2. Expected Value: The Formula Behind Trading

Every trade has an expected value, even if you do not calculate it formally.

```text
EV = (Win probability x Average win) - (Loss probability x Average loss) - Costs
```

Example:

```text
Win rate: 45%
Average win: 2R
Average loss: 1R
Costs: ignored for now

EV = (0.45 x 2R) - (0.55 x 1R)
EV = 0.90R - 0.55R
EV = +0.35R per trade
```

This setup can lose more often than it wins and still be profitable because winners are larger than losers.

## Costs matter

The real formula is:

```text
EV after costs =
  (Win probability x Average win)
- (Loss probability x Average loss)
- brokerage
- taxes/charges
- slippage
- spread cost
- financing/margin cost
- option theta/IV impact, if applicable
```

A strategy that is profitable on screenshots can fail in the account if costs are ignored.

## Why accuracy is not enough

High win rate can still lose money.

Example:

```text
Win rate: 80%
Average win: 0.25R
Average loss: 2R

EV = (0.80 x 0.25R) - (0.20 x 2R)
EV = 0.20R - 0.40R
EV = -0.20R
```

This system wins often but loses money over time.

Low win rate can still make money.

```text
Win rate: 35%
Average win: 3R
Average loss: 1R

EV = (0.35 x 3R) - (0.65 x 1R)
EV = 1.05R - 0.65R
EV = +0.40R
```

This system loses more often than it wins but can still work.

---

# 3. Think In R, Not Rupees

R means the amount you planned to risk on the trade.

```text
1R = planned risk on the trade
```

If you risk Rs 1,000:

| Result | Meaning |
| --- | --- |
| -1R | Lost Rs 1,000 |
| -0.5R | Lost Rs 500 |
| +1R | Made Rs 1,000 |
| +2R | Made Rs 2,000 |
| +3R | Made Rs 3,000 |

R makes different trades comparable. Without R, your journal becomes random money amounts with no risk context.

## Why R is better than rupees

| Rupee thinking | R thinking |
| --- | --- |
| I made Rs 5,000 | I made +2R |
| I lost Rs 3,000 | I lost -1R |
| This trade felt big | The risk was 0.5% of capital |
| I want to recover yesterday's loss | I will only take valid setups inside risk limits |
| This stock is expensive | Position size depends on risk per share, not price alone |

## R-based journal fields

Every trade should record:

```text
Initial risk amount:
Initial R:
Final result in R:
Maximum favorable excursion in R:
Maximum adverse excursion in R:
Did I follow the plan?
Was the trade A, B, C, or invalid?
```

Maximum favorable excursion tells how far the trade went in your favor. Maximum adverse excursion tells how far it moved against you before exit. These two fields reveal whether stops, targets, and trailing rules are sensible.

---

# 4. Break-Even Win Rate

If your average winner is bigger than your average loser, you do not need a high win rate.

```text
Break-even win rate = 1 / (1 + reward-to-risk)
```

| Reward-to-risk | Break-even win rate before costs |
| --- | ---: |
| 1:1 | 50.0% |
| 1.5:1 | 40.0% |
| 2:1 | 33.3% |
| 3:1 | 25.0% |
| 4:1 | 20.0% |

Example:

```text
Target = 2R
Break-even = 1 / (1 + 2)
Break-even = 33.3%
```

Costs raise the real break-even rate. Slippage, brokerage, spreads, bad fills, and taxes mean a theoretical 33.3% break-even may need 35%, 38%, or more in practice.

## The break-even trap

A trade with 2R potential is not automatically good. Ask:

* Is 2R target before a major resistance/support?
* Does the setup historically reach 2R often enough?
* Is volatility normal enough for the stop to survive?
* Is the spread small enough?
* Is there event risk before target?
* Am I entering near the level or late?

Reward-to-risk is a required filter. It is not a complete edge.

---

# 5. Distributions, Variance, And Sample Size

Trading outcomes come in distributions. A good setup will still have losing streaks. A bad setup will still have winning streaks.

## One trade proves almost nothing

| Result | What it proves |
| --- | --- |
| One good win | Almost nothing |
| One good loss | Almost nothing |
| One bad win | Dangerous because it rewards rule-breaking |
| One bad loss | Useful if it exposes a fixable behavior |
| 50 planned trades | Early evidence |
| 100 planned trades | Better evidence |
| 300 planned trades | Stronger evidence if market regimes vary |

## Variance

Variance means results can swing around the average. Even a positive-expectancy system can have:

* 5 losses in a row.
* 10 flat trades.
* Winners that almost hit target and reverse.
* Strong periods followed by weak periods.
* Different performance in bull, bear, and sideways regimes.

The trader's job is to size positions so normal variance does not destroy capital or psychology.

## Losing streak expectation

If your win rate is 45%, your loss rate is 55%. Losing streaks are normal.

Do not respond to a normal losing streak by:

* Doubling size.
* Changing the strategy after three trades.
* Moving stops wider.
* Adding random filters.
* Abandoning journaling.

First ask whether the losses followed the plan. If yes, keep collecting sample. If no, fix execution.

---

# 6. The Chart-Only Decision Process

When you only have a chart in front of you, use the same sequence every time.

```text
Regime -> levels -> location -> hypothesis -> trigger -> stop -> target -> size -> execute or skip
```

## Step 1: Identify market regime

| Regime | What it looks like | Best approach |
| --- | --- | --- |
| Uptrend | Higher highs, higher lows | Buy pullbacks or breakouts |
| Downtrend | Lower highs, lower lows | Sell rallies or breakdowns |
| Range | Price trapped between support and resistance | Buy low, sell high, avoid middle |
| Compression | Tight candles, volatility shrinking | Wait for breakout or expansion |
| Expansion | Large candles, fast movement | Trade continuation carefully or wait |
| Transition | Trend weakening, failed pushes | Be cautious; reversals possible |
| Unclear | Structure is mixed | No trade |

First question:

```text
Is this market trending, ranging, compressing, expanding, transitioning, or unclear?
```

If unclear, skip.

## Step 2: Mark key levels

Mark only levels that matter.

| Level type | Why it matters |
| --- | --- |
| Prior swing high | Resistance or breakout level |
| Prior swing low | Support or breakdown level |
| Previous day high/low | Reaction zones for shorter-term traders |
| Session high/low | Liquidity and stop areas |
| Range high/low | Mean reversion or breakout zones |
| Breakout retest level | Continuation area |
| Strong rejection zone | Possible supply/demand area |

Your chart should answer:

```text
Where is price likely to react?
```

Do not mark every minor turn. Too many levels make every price look important, which makes the chart useless.

## Step 3: Decide location

Location controls reward-to-risk.

| Question | Good answer |
| --- | --- |
| Am I buying near support or after a pullback? | Yes |
| Am I shorting near resistance or after a failed rally? | Yes |
| Am I entering in the middle of a range? | Avoid |
| Is there enough room before the next obstacle? | Yes |
| Is my stop where the idea is invalidated? | Yes |

A good setup in a poor location is still a poor trade.

## Step 4: Define the trade hypothesis

Before entry, write:

```text
My trade idea is valid because:
My trade is wrong if:
My entry trigger is:
My stop goes at:
My target is:
My reward-to-risk is:
My position size is:
```

Example:

```text
The market is in an uptrend.
Price pulled back to the prior breakout level.
Sellers failed to push below support.
If price breaks above the rejection candle, I enter long.
The trade is wrong if price breaks below the pullback low.
Target is the prior high.
Reward-to-risk is 2:1.
```

If you cannot explain the trade in a few clear sentences, skip it.

---

# 7. The 8-Point Trade Score

Use this as a permission checklist. The score does not tell you to bet bigger. It tells you whether the trade is allowed.

Give each item 1 point.

| Item | Question |
| --- | --- |
| 1. Regime | Is the market regime clear? |
| 2. Direction | Is the trade aligned with dominant structure? |
| 3. Location | Is price at a meaningful level? |
| 4. Trigger | Is there a clear entry trigger? |
| 5. Invalidation | Is there an obvious stop level? |
| 6. Reward | Is there at least 1.5R to 2R before the next major obstacle? |
| 7. Volatility | Is volatility tradable, not dead and not extreme? |
| 8. Risk | Is the trade inside daily, weekly, and per-trade risk limits? |

## Trade grading

| Score | Action |
| ---: | --- |
| 7-8 | A-grade trade; allowed at normal planned risk |
| 5-6 | B/C-grade; reduce size, paper trade, or skip |
| 0-4 | No trade |

Important rule:

```text
Score changes permission, not maximum risk.
```

Even an 8/8 setup can lose. Do not use a high score as an excuse to violate risk limits.

---

# 8. Four Manual Setups To Master First

Do not trade everything. Master one or two setups first, then expand.

## Setup 1: Trend Pullback Continuation

Best for trending markets.

### Long version

| Rule | Description |
| --- | --- |
| Regime | Uptrend: higher highs and higher lows |
| Location | Pullback to prior support, moving average, VWAP, or breakout retest |
| Trigger | Rejection candle, bullish engulfing, reclaim, or break of minor lower high |
| Entry | Above trigger candle or on retest |
| Stop | Below pullback low |
| Target | Prior high, extension, or 2R |
| Avoid | Buying after extended vertical candles |

### Short version

| Rule | Description |
| --- | --- |
| Regime | Downtrend |
| Location | Pullback to resistance |
| Trigger | Rejection, bearish engulfing, lower high break |
| Stop | Above pullback high |
| Target | Prior low or 2R |

Why it works:

Trend pullbacks work because you are joining the dominant side after price offers a better location. You are not trying to catch the exact top or bottom.

## Setup 2: Range Mean Reversion

Best for sideways markets.

| Rule | Long setup | Short setup |
| --- | --- | --- |
| Regime | Range | Range |
| Location | Range low/support | Range high/resistance |
| Trigger | Failed breakdown, rejection wick, reclaim | Failed breakout, rejection wick, breakdown |
| Stop | Below range low | Above range high |
| Target | Mid-range first, opposite side second | Mid-range first, opposite side second |
| Avoid | Strong breakout volume or trend day | Strong breakdown volume or trend day |

Main rule:

```text
Never enter in the middle of the range.
```

The middle has weak probability because both support and resistance are far enough to create unclear reward-to-risk.

## Setup 3: Breakout Continuation

Best for compression followed by expansion.

| Rule | Description |
| --- | --- |
| Regime | Tight range, compression, or clear resistance/support |
| Entry type | Breakout close or breakout retest |
| Stop | Inside range or below/above retest level |
| Target | Measured move, next level, or 2R |
| Confirmation | Strong close, volume expansion, acceptance beyond level |
| Avoid | Chasing huge candles far from the level |

Cleaner sequence:

```text
Breakout -> retest -> hold -> enter
```

Weaker sequence:

```text
Huge candle far from base -> late entry -> poor stop distance -> poor expectancy
```

## Setup 4: Failed Breakout Reversal

Best for trapping late breakout traders.

| Rule | Description |
| --- | --- |
| Context | Price breaks a major high/low but fails to hold |
| Long version | Price breaks below support, rejects, reclaims support |
| Short version | Price breaks above resistance, rejects, loses resistance |
| Entry | On reclaim/loss of level |
| Stop | Beyond failed breakout extreme |
| Target | Mid-range, opposite side, or 2R |
| Avoid | Strong trend continuation after breakout |

Why it works:

Failed breakouts create trapped participants. If they entered late and the level fails, their exits can fuel movement in the opposite direction.

---

# 9. Manual Trading Flow: From Chart To Trade

## Stage 1: Bias

Ask:

```text
What is the dominant structure?
```

Possible answers:

```text
Bullish
Bearish
Range
Unclear
```

If unclear, skip or wait.

## Stage 2: Scenario

Do not predict. Build conditional plans.

Example:

```text
If price holds above 100 and forms a higher low, I look for longs.
If price loses 100 and retests from below, I look for shorts.
If price stays between 100 and 104, I do nothing in the middle.
```

Weak process:

```text
I think it will go up.
```

Better process:

```text
If X happens at Y level with Z confirmation, I will take A trade with B risk.
```

## Stage 3: Trigger

A trigger is the exact thing that gets you in.

| Trigger | Meaning |
| --- | --- |
| Break of previous candle high | Momentum confirmation |
| Reclaim of support | Failed breakdown |
| Loss of support | Breakdown continuation |
| Retest hold | Breakout accepted |
| Lower high forms | Sellers defending |
| Higher low forms | Buyers defending |

No trigger, no trade.

## Stage 4: Stop

Your stop should be placed where the trade idea is invalidated.

Bad stop:

```text
I will stop when I feel uncomfortable.
```

Good stop:

```text
I am long because price held support.
If price breaks below the support swing low, the idea is wrong.
Stop goes below that level.
```

The stop is the definition of being wrong.

## Stage 5: Target

Targets should come from structure.

| Target type | Example |
| --- | --- |
| Prior high/low | Exit near previous swing high |
| Range midpoint | First target in range |
| Opposite range side | Full target in range |
| Measured move | Breakout range projected |
| Fixed R | 1.5R, 2R, 3R |

Skip the trade if the first logical obstacle is too close.

Example:

```text
Risk = 10 points
Nearest resistance = 8 points away
Reward-to-risk = 0.8R
Decision = skip
```

---

# 10. Use Objective Raw Values As A Referee

Your system should not become something you blindly obey. It should provide objective context.

Use raw values as a **referee**, not a guru.

| Raw value | Manual use |
| --- | --- |
| ATR / volatility | Set realistic stops and targets |
| Trend strength | Decide whether to favor continuation or mean reversion |
| Volume | Confirm participation or detect weak moves |
| Spread | Avoid bad execution conditions |
| Relative strength | Choose stronger longs and weaker shorts |
| Market breadth | Confirm risk-on or risk-off environment |
| Correlation | Avoid taking the same trade in multiple forms |
| Time-of-day stats | Avoid dead zones or chaotic periods |
| Prior setup stats | Estimate base rate |

Example trade allowed:

```text
Chart says long pullback setup.
ATR says normal volatility.
Trend score says bullish.
Spread is acceptable.
Reward-to-risk is 2R.
No major resistance before target.
Decision = trade allowed.
```

Example trade skipped:

```text
Chart looks like breakout.
ATR is extremely high.
Spread is wide.
Price is far from base.
Nearest resistance is close.
Decision = skip.
```

The system's most important job is often preventing bad trades, not finding more trades.

---

# 11. Bayesian-Style Thinking Without Fake Precision

You can think probabilistically without pretending to know exact probabilities.

## Start with base rate

From your journal:

```text
Trend pullback continuation:
Win rate = 48%
Average win = 1.8R
Average loss = 1R
Expectancy = positive
```

That is your prior.

Then adjust based on current evidence:

| Evidence | Effect |
| --- | --- |
| Strong trend alignment | Improves setup quality |
| Clean pullback to level | Improves setup quality |
| Entry far from level | Reduces setup quality |
| Choppy range | Reduces trend setup quality |
| Wide spread | Reduces expectancy |
| Nearby resistance | Reduces reward |
| News event soon | Increases uncertainty |
| Good trigger candle | Improves timing |
| Weak market breadth | Reduces long-trade quality |
| Strong sector alignment | Improves long-trade quality |

Do not write:

```text
This trade has 63.74% probability.
```

That is fake precision unless you have a serious tested model. Use categories:

| Grade | Meaning |
| --- | --- |
| A | Clean context, clean trigger, clean risk |
| B | Decent but imperfect |
| C | Too many problems; reduce size or skip |
| No trade | Unclear or poor reward/risk |

---

# 12. Position Sizing For Manual Trading

Use fixed fractional risk.

| Experience level | Risk per trade |
| --- | ---: |
| New / training | 0.10% to 0.25% |
| Developing | 0.25% to 0.50% |
| Consistent and audited | 0.50% to 1.00% |
| Above 1% | Usually unnecessary aggression |

Formula:

```text
Position size = Account risk per trade / Stop distance
```

For stocks:

```text
Shares = Rupee risk / Rupee stop distance
```

Example:

```text
Account = Rs 500,000
Risk per trade = 0.5%
Risk amount = Rs 2,500

Entry = Rs 100
Stop = Rs 95
Stop distance = Rs 5

Shares = Rs 2,500 / Rs 5
Shares = 500 shares
```

If 500 shares is too large because of exposure, liquidity, or margin, reduce it.

## Never change risk after entry

Do not increase stop distance after entry because price is approaching it.

Wrong:

```text
My stop is about to hit, so I will give it more room.
```

Correct:

```text
My stop is where the idea is invalid. If it hits, I exit and record the result.
```

---

# 13. Daily Risk Rules

Use hard limits before the market opens.

| Rule | Example |
| --- | --- |
| Max risk per trade | 0.25% to 1% |
| Max daily loss | 2R or 3R |
| Max trades per day | 2 to 5 |
| Max consecutive losses | Stop after 2 or 3 |
| Max open positions | Depends on correlation |
| No revenge trades | Immediate shutdown |
| No moving stop away | Ever |
| No averaging losers | Unless pre-planned and tested |
| No trade before news | Unless strategy is built for news |
| No trade without stop | Ever |

Investor.gov highlights that leveraged trading can produce quick and substantial losses in fast-moving short-term trading environments. ([Investor.gov][1]) This is why risk rules must exist before the trade, not after the loss is already emotional.

## Daily shutdown rule

Example:

```text
Daily stop = -2R
If down -2R, stop trading for the day.
No exceptions.
Review after market.
```

Why this works:

* Prevents revenge trading.
* Protects mental capital.
* Keeps one bad day from becoming a catastrophic day.
* Forces review instead of emotional execution.

---

# 14. Trade Management

You need predefined management rules.

## Option A: Fixed target

```text
Enter
Stop at invalidation
Target at 2R
Exit fully
```

Good for training because it keeps decisions simple.

## Option B: Partial exit

```text
Take 50% off at 1R
Move stop only if structure supports it
Let rest run to 2R or next level
```

Useful, but can reduce expectancy if partials are taken too early.

## Option C: Structure trailing

```text
In a long trade:
Trail stop below higher lows

In a short trade:
Trail stop above lower highs
```

Useful in trends because it allows large winners.

## Bad management

```text
Take profit early because scared
Hold loser because hopeful
Move target farther because greedy
Move stop wider because emotional
```

That is not trade management. It is rule abandonment.

---

# 15. Daily Manual Trading Routine

## Before market opens

| Task | Output |
| --- | --- |
| Check higher timeframe | Bullish, bearish, range, unclear |
| Mark key levels | Support, resistance, prior high/low |
| Check volatility | Normal, low, extreme |
| Check major news/events | Trade, reduce size, or avoid |
| Define scenarios | Long above X, short below Y, no trade between |
| Decide max risk | Daily stop and trade count |
| Review mistakes | One behavior to avoid today |

Pre-market plan example:

```text
Market regime: Uptrend but extended
Key resistance: 104
Key support: 100
Long plan: Only if price pulls back to 100-101 and holds
Short plan: Only if price fails above 104 and re-enters range
No-trade zone: 101.5 to 103.5
Max trades: 3
Daily stop: -2R
Main mistake to avoid: Chasing breakouts
```

## During market

Before entry:

```text
1. What setup is this?
2. What regime am I trading?
3. What level am I trading from?
4. What is my trigger?
5. Where is my stop?
6. Where is my target?
7. What is the reward-to-risk?
8. What is my position size?
9. What will prove me wrong?
10. Am I taking this because of my plan or because I want action?
```

If it is not from the plan, skip it.

## After market

Journal every trade.

| Field | Example |
| --- | --- |
| Date | 2026-05-19 |
| Market | NIFTY / BTC / EURUSD / AAPL |
| Setup | Trend pullback |
| Direction | Long |
| Regime | Uptrend |
| Entry reason | Pullback to prior breakout level |
| Entry price | 100 |
| Stop | 95 |
| Target | 110 |
| Result | +2R |
| Mistake? | No |
| Screenshot before | Required |
| Screenshot after | Required |
| Emotion | Calm / rushed / revenge / FOMO |
| Rule followed? | Yes/No |

Separate outcomes:

| Trade type | Meaning |
| --- | --- |
| Good win | Followed plan, made money |
| Good loss | Followed plan, lost money |
| Bad win | Broke rules, made money |
| Bad loss | Broke rules, lost money |

The most dangerous category is bad win because it teaches the brain that rule-breaking can be rewarded.

---

# 16. Weekly Review System

Every week, calculate:

| Metric | Why it matters |
| --- | --- |
| Win rate | How often setup wins |
| Average win | Size of winners |
| Average loss | Size of losers |
| Expectancy | Edge per trade |
| Profit factor | Gross wins / gross losses |
| Max drawdown | Worst equity decline |
| Rule-following rate | Discipline quality |
| Best setup | Where edge exists |
| Worst setup | What to remove |
| Time-of-day performance | When you trade well or badly |

Expectancy:

```text
Expectancy = (Win rate x Avg win) - (Loss rate x Avg loss)
```

Example:

```text
Win rate = 40%
Avg win = 2.2R
Loss rate = 60%
Avg loss = 1R

Expectancy = (0.40 x 2.2) - (0.60 x 1)
Expectancy = 0.88 - 0.60
Expectancy = +0.28R
```

This can be tradable if costs and execution do not destroy it.

## Weekly questions

Ask:

* Which setup made money?
* Which setup lost money?
* Which setup had the most rule violations?
* Which market regime worked best?
* Did I overtrade?
* Did I trade outside my playbook?
* Did I exit early too often?
* Did I move stops?
* Did I respect daily loss limits?
* What one behavior should I remove next week?

---

# 17. Manual Trading Playbook Template

Build one playbook per setup.

## Setup name

```text
Trend Pullback Continuation
```

## Market condition

```text
Only trade in clear trend.
Avoid range and choppy market.
```

## Long rules

```text
1. Higher timeframe must be bullish.
2. Price must pull back to support or breakout retest.
3. Pullback must show slowing selling pressure.
4. Entry only after bullish trigger.
5. Stop below pullback low.
6. Minimum reward-to-risk: 1.5R, preferably 2R.
```

## Short rules

```text
1. Higher timeframe must be bearish.
2. Price must rally into resistance.
3. Rally must show slowing buying pressure.
4. Entry only after bearish trigger.
5. Stop above pullback high.
6. Minimum reward-to-risk: 1.5R, preferably 2R.
```

## Invalid conditions

```text
Do not trade if:
- Price is in the middle of a range.
- Stop is too wide.
- Target is too close.
- Spread is abnormal.
- Volatility is extreme.
- Major news is imminent.
- You are emotionally tilted.
```

## Management

```text
Take full profit at 2R
or
Take partial at 1R and trail remainder by structure
```

## Screenshot library

Keep at least:

```text
10 clean winners
10 clean losers
10 skipped trades
```

Skipped trades matter because they train restraint.

---

# 18. Training Drills For Discretionary Chart Reading

## Drill 1: Regime classification

Open charts and label each as:

```text
Trend
Range
Compression
Expansion
Transition
Unclear
```

Do not trade. Just classify.

Goal:

```text
100 charts
```

## Drill 2: Level marking

Mark:

```text
Major high
Major low
Range high
Range low
Breakout retest level
Failed breakout area
```

Then scroll forward and see where price reacted.

Goal:

```text
50 charts
```

## Drill 3: Screenshot replay

Use replay if available. Pause the chart before the right side is visible.

Write:

```text
Bias:
Key level:
Setup:
Entry:
Stop:
Target:
Trade or no trade:
```

Then reveal what happened.

Goal:

```text
100 simulated decisions
```

## Drill 4: One setup only

For two to four weeks, trade or simulate only one setup.

Example:

```text
Only trend pullbacks.
No breakouts.
No reversals.
No random "this looks good."
```

This builds pattern recognition without mixing five different systems.

---

# 19. Real-Time Decision Tree

Use this in live or paper trading.

```text
1. Is the market structure clear?
   No -> no trade.
   Yes -> continue.

2. Is price at a meaningful level?
   No -> no trade.
   Yes -> continue.

3. Is there a known setup from my playbook?
   No -> no trade.
   Yes -> continue.

4. Is there a trigger?
   No -> wait.
   Yes -> continue.

5. Is invalidation clear?
   No -> no trade.
   Yes -> continue.

6. Is reward-to-risk acceptable?
   No -> no trade.
   Yes -> continue.

7. Is risk within limits?
   No -> reduce size or no trade.
   Yes -> enter.

8. After entry, did invalidation happen?
   Yes -> exit.
   No -> manage according to plan.
```

The process should feel repetitive. Repetition is useful because it makes mistakes visible.

---

# 20. Semi-Systematic Manual Trading Model

This is the best blend when you have both raw values and discretionary chart reading.

## Your system provides

```text
Trend state
Volatility state
ATR
Spread
Volume
Relative strength
Major levels
Time-of-day stats
Setup history
```

## Your manual process decides

```text
Is the chart clean?
Is price at a good location?
Is the trigger valid?
Is the stop logical?
Is the reward worth the risk?
Should I trade, skip, or wait?
```

## Final decision model

| Condition | Decision |
| --- | --- |
| System positive + chart clean | Trade allowed |
| System positive + chart messy | Wait or skip |
| System neutral + chart clean | Smaller size or paper only |
| System negative + chart tempting | Skip |
| System extreme volatility/spread warning | Skip |

The system provides evidence. The playbook provides rules. The risk model controls damage. The journal proves whether the edge exists.

---

# 21. Full Trade Walkthrough

## Situation

Price has been making:

```text
Higher high
Higher low
Higher high
Higher low
```

Regime:

```text
Uptrend
```

Price pulls back to a previous breakout level.

Levels:

```text
Support = 100
Resistance / prior high = 110
```

Price rejects 100 and forms a bullish trigger candle.

## Plan

```text
Setup: Trend pullback continuation
Direction: Long
Entry: Above bullish trigger candle at 102
Stop: Below swing low at 98
Risk: 4 points
Target: Prior high at 110
Reward: 8 points
Reward-to-risk: 2R
```

## Decision

| Item | Status |
| --- | --- |
| Clear trend | Yes |
| Key level | Yes |
| Pullback | Yes |
| Trigger | Yes |
| Stop clear | Yes |
| Reward-to-risk 2R | Yes |
| Volatility okay | Yes |
| Risk within limit | Yes |

Score:

```text
8/8
```

Decision:

```text
Trade allowed at planned size.
```

## Management

```text
If price reaches 106, trade is +1R.
If plan says partials, take partial.
If plan says hold to 110, hold.
If price breaks below 98, exit.
No debating after invalidation.
```

---

# 22. No-Trade Walkthrough

## Situation

Price is between support and resistance.

```text
Support = 100
Resistance = 110
Current price = 105
```

You see a bullish candle.

Weak decision:

```text
Looks strong. Buy.
```

Probabilistic decision:

```text
Price is in the middle of the range.
Reward to resistance is 5 points.
Stop below support is 5+ points.
Reward-to-risk is poor.
No trade.
```

Correct plan:

```text
Wait for price near 100 for long
or
Wait for price near 110 for short
or
Wait for breakout and retest
```

No trade is a valid decision.

---

# 23. Personal Trading Constitution

Write these rules and keep them visible.

```text
1. I trade only defined setups.
2. Every trade must have entry, stop, target, and invalidation.
3. I risk a fixed amount per trade.
4. I stop trading after my daily loss limit.
5. I do not move stops away.
6. I do not average losers unless the setup is explicitly designed and tested for scaling.
7. I do not trade unclear structure.
8. I do not chase extended moves.
9. I review every trade in R-multiples.
10. My goal is process quality, not emotional satisfaction.
```

Add this rule:

```text
I do not judge myself by one trade.
I judge myself by the quality of repeated execution.
```

---

# 24. Minimum Viable Manual Trading System

## Market

Choose one market first.

```text
Example:
NIFTY
one stock index
one futures contract
one liquid stock universe
one currency pair
```

Do not jump across too many charts while learning.

## Timeframes

Use three:

| Timeframe | Purpose |
| --- | --- |
| Higher timeframe | Bias |
| Trading timeframe | Setup |
| Lower timeframe | Entry timing |

Example for intraday:

| Role | Timeframe |
| --- | --- |
| Bias | 1H |
| Setup | 15m |
| Entry | 5m |

Example for swing or positional:

| Role | Timeframe |
| --- | --- |
| Bias | Weekly / Daily |
| Setup | Daily / 4H |
| Entry | Daily / 1H |

## Setups

Start with two:

```text
Trend pullback continuation
Range mean reversion
```

## Risk

```text
Risk per trade: 0.25% to 0.50% while learning
Daily max loss: 2R
Max trades per day: 3
Minimum reward-to-risk: 1.5R
Preferred reward-to-risk: 2R
```

## Review

```text
Daily journal
Weekly stats
Monthly playbook refinement
```

---

# 25. What Not To Do

Avoid these:

| Bad habit | Why it kills performance |
| --- | --- |
| Trading without a setup | No measurable edge |
| Entering mid-range | Poor location |
| Moving stops | Destroys risk model |
| Taking profits too early always | Reduces expectancy |
| Averaging losers | Can create account-damaging losses |
| Overtrading | Costs and mistakes compound |
| Switching strategies constantly | No sample size |
| Judging by one trade | Randomness fools you |
| Increasing size after losses | Revenge trading |
| Trading because bored | Creates low-quality decisions |
| Ignoring costs | Turns theoretical edge into real loss |
| Ignoring spread | Bad fills reduce expectancy |
| Trading before major news without a plan | Gap and volatility risk |

---

# 26. The 30-Day Training Plan

## Week 1: Observation only

Do not trade live.

Tasks:

```text
Classify 100 charts by regime.
Mark key levels.
Write possible scenarios.
No entries.
```

Goal:

```text
Improve chart reading.
```

## Week 2: One setup in replay

Choose one setup.

Example:

```text
Trend pullback continuation only.
```

Tasks:

```text
Take 50 replay trades.
Record R result.
Screenshot every trade.
```

Goal:

```text
Learn execution rules.
```

## Week 3: Paper trading

Trade live market conditions, but paper only.

Rules:

```text
Max 3 trades per day.
Same risk model.
Same journal.
No random trades.
```

Goal:

```text
Test discipline in real-time movement.
```

## Week 4: Tiny-size live trading

Only if paper trading was disciplined.

Rules:

```text
Risk 0.10% to 0.25% per trade.
Daily stop: -2R.
No size increase for at least 20 valid trades.
```

Goal:

```text
Feel real execution without damaging capital.
```

If discipline is poor, repeat paper trading. Do not rush size.

---

# 27. One-Page Checklist

Before any manual trade:

```text
Market regime:
Trend / range / compression / expansion / unclear

Bias:
Bullish / bearish / neutral

Key level:
____________________

Setup:
Trend pullback / range reversal / breakout / failed breakout

Entry trigger:
____________________

Entry price:
____________________

Stop:
____________________

Target:
____________________

Reward-to-risk:
____________________

Risk amount:
____________________

Position size:
____________________

Invalidation:
____________________

Reason to skip:
____________________
```

Final question:

```text
Would I take this trade again 100 times under the same conditions?
```

If the answer is no, skip.

---

# 28. Review Notes From A Strict Probabilistic Trader

These are the rules that matter after reviewing the whole framework.

## 1. The trade must start with location

A trade without location is usually late. Price must be near a meaningful level or have just accepted beyond one.

Good locations:

* Pullback to support in uptrend.
* Rally into resistance in downtrend.
* Range edge.
* Breakout retest.
* Failed breakout reclaim.

Poor locations:

* Middle of range.
* Far above breakout level.
* Just below resistance for longs.
* Just above support for shorts.

## 2. Reward-to-risk must be structural

Do not place target only because you want 2R. Ask where price can realistically go before it hits supply, demand, prior high/low, or volatility limits.

## 3. Base rate beats opinion

If your journal says a setup loses money, your current opinion does not matter. Fix the setup or stop trading it.

## 4. Small losses are information

A planned -1R loss means the invalidation worked. It is not a personal failure.

## 5. Bad wins must be punished in review

If you broke rules and made money, grade the trade as bad. The market paid you for behavior that may later damage the account.

## 6. Size comes last

The order is:

```text
Setup quality
-> stop distance
-> account risk
-> position size
```

Never:

```text
Desired profit
-> large quantity
-> hope stop survives
```

## 7. No-trade is a professional action

Skipping unclear trades is not inactivity. It is capital preservation.

---

# 29. Final Model

A strong manual-plus-system workflow looks like this:

```text
System gives objective raw values.
Chart gives structure and location.
Playbook defines valid setups.
Risk model controls damage.
Journal proves whether edge exists.
Review removes weak behavior.
```

The final probabilistic belief:

```text
I can follow my rules and lose.
I can break my rules and win.
One trade proves almost nothing.
A sample of trades proves something.
My job is to execute good risk repeatedly.
```

Manual trading can work only if it becomes **rule-based discretion**.

Not random discretion.
Not emotional discretion.
Not prediction dressed up as analysis.

Rule-based discretion means:

```text
I know the setup.
I know the location.
I know the trigger.
I know the stop.
I know the target.
I know the size.
I know the invalidation.
I know how this trade will be reviewed.
```

That is the complete loop.

[1]: https://www.investor.gov/additional-resources/spotlight/formerdirectorlorischock-directors-take/thinking-day-trading-know-risks "Thinking of Day Trading? Know the Risks"
[2]: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html "Customer Advisory: Eight Things You Should Know Before Trading Forex"
