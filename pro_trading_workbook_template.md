# Professional Trading Workbook Template

## Quick Summary

Use this workbook as the operating system for trading research and execution. It is intentionally stricter than normal retail notes. A strategy is not considered usable until it has explicit rules, realistic execution assumptions, risk limits, a test plan, a forward-test plan, and a review process.

This template does not prove profitability. It prevents vague ideas from pretending to be strategies.

---

# 1. Strategy Research Template

```text
Strategy name:
Research owner:
Created date:
Last reviewed:
Status: idea / researched / backtested / forward testing / live-small / retired

Market:
Instrument:
Universe:
Timeframe:
Holding period:
Strategy type: trend / mean reversion / breakout / event-driven / volatility / hedge / other

Hypothesis:
Why should this edge exist?
Who is on the other side of the trade?
What behavioral, structural, flow, or risk-premium reason supports the edge?

Market regime:
Works best when:
Fails when:
Regime filter:

Entry rules:
1.
2.
3.

Exit rules:
1.
2.
3.

Stop loss:
Initial stop:
Trailing stop:
Time stop:
Thesis stop:

Take profit:
Target method:
Partial exit method:
Runner method:

Position sizing:
Risk per trade:
Max notional exposure:
Max open positions:
Max correlated positions:

Risk limits:
Max daily loss:
Max weekly loss:
Max monthly drawdown:
Kill switch:

Execution assumptions:
Order type:
Fill assumption:
Slippage:
Spread:
Brokerage/taxes/charges:
Liquidity filter:

Data required:
Price:
Volume:
Corporate actions:
Futures OI:
Options chain:
Fundamentals:
News/events:

Backtest requirements:
Sample size:
Date range:
Regimes included:
Costs included:
Survivorship-bias handling:
Look-ahead-bias controls:
Signal execution timing:

Forward-test requirements:
Minimum paper trades:
Minimum weeks:
Required rule-following rate:
Required max drawdown:
Promotion criteria:

Common failure modes:
1.
2.
3.

Decision:
Reject / research more / backtest / forward test / live-small
```

---

# 2. Setup Definition Template

```text
Setup name:
Strategy family:
Allowed instruments:
Allowed timeframe:

Market regime required:
Sector condition required:
Volatility condition required:
Liquidity condition required:

Setup definition:
Exact pattern:
What must be true before entry:
What invalidates setup before entry:

Entry trigger:
Trigger candle/bar definition:
Volume requirement:
Close requirement:
Retest requirement:

Stop:
Initial stop location:
ATR/swing/structure basis:
Maximum stop distance:

Target:
First target:
Second target:
Trailing rule:

Risk:
Risk per trade:
Max concurrent setups:
Max sector exposure:

Do not trade if:
1.
2.
3.

Evidence required before live use:
Backtest trades:
Forward-test trades:
Screenshots:
Journal review:
```

---

# 3. Daily Trade Plan Template

```text
Date:
Market regime:
Index trend:
Breadth:
Volatility:
Key macro/news events:
Earnings/events to avoid:

Allowed setups today:
1.
2.

No-trade conditions:
1.
2.

Watchlist:
Symbol | Sector | Setup | Trigger | Stop | Risk | Notes

Risk limits:
Max risk per trade:
Max total open risk:
Daily stop:
Max new trades:

Scenario plan:
If market breaks above:
If market rejects resistance:
If market loses support:
If volatility spikes:

Main behavioral risk today:
Rule to enforce:
```

---

# 4. Trade Journal Template

| Field | Entry |
| --- | --- |
| Trade ID | |
| Date | |
| Symbol | |
| Instrument | |
| Direction | |
| Setup | |
| Market regime | |
| Sector regime | |
| Entry price | |
| Stop price | |
| Target | |
| Quantity | |
| Planned risk Rs | |
| Planned risk R | |
| Actual exit | |
| Actual result Rs | |
| Actual result R | |
| Fees/slippage | |
| MFE | |
| MAE | |
| Entry reason | |
| Invalidation | |
| Exit reason | |
| Rule followed? | |
| Mistake category | |
| Screenshot before | |
| Screenshot after | |
| Lesson | |

---

# 5. Post-Trade Review Template

```text
Trade ID:
Was this trade in the playbook?
Was market regime allowed?
Was entry valid?
Was stop valid?
Was sizing correct?
Were costs/slippage expected?
Was exit rule followed?

Grade:
Good win / good loss / bad win / bad loss

If bad trade:
Which rule was broken?
What caused it?
What rule prevents repeat?

If good loss:
Did the setup fail normally?
Any reason to change the setup?

If good win:
Was exit too early, too late, or correct?
Should trailing/target logic change?
```

---

# 6. Weekly Review Template

```text
Week:
Total trades:
Win rate:
Average win R:
Average loss R:
Expectancy R:
Profit factor:
Max drawdown:
Rule-following rate:
Best setup:
Worst setup:
Best regime:
Worst regime:
Largest mistake:
Most repeated mistake:

Keep:
Stop:
Change:
Test next week:
```

---

# 7. Monthly Review Template

```text
Month:
Starting capital:
Ending capital:
Return:
Max drawdown:
Number of trades:
Expectancy:
Profit factor:
Average holding period:
Fees/slippage total:
Best setup:
Worst setup:

Strategy decisions:
Promote:
Demote:
Retire:
Research:

Risk review:
Was max drawdown respected?
Were position limits respected?
Any concentration breaches?
Any gap losses?

Process review:
Rule-following rate:
Journal completion:
Backtest updates:
Forward-test progress:
```

---

# 8. Risk Checklist

Before trade:

```text
[ ] Setup is in playbook.
[ ] Market regime is allowed.
[ ] Instrument is liquid.
[ ] Spread is acceptable.
[ ] Entry trigger is specific.
[ ] Stop is defined before entry.
[ ] Reward-to-risk is acceptable.
[ ] Position size is calculated from stop distance.
[ ] Total open risk remains within limit.
[ ] Sector correlation is acceptable.
[ ] Event risk checked.
[ ] Gap risk acceptable.
[ ] No revenge trade.
```

During trade:

```text
[ ] Stop not moved farther away.
[ ] No unplanned averaging down.
[ ] Exit rule followed.
[ ] No new position added without risk recalculation.
```

After trade:

```text
[ ] Journal complete.
[ ] Result recorded in R.
[ ] Mistakes tagged.
[ ] Screenshot stored.
```

---

# 9. Backtest Review Checklist

```text
[ ] Rules are explicit enough to code.
[ ] Signal timestamp and execution timestamp are separated.
[ ] No look-ahead bias.
[ ] No survivorship bias.
[ ] Corporate actions handled.
[ ] Costs included.
[ ] Slippage/spread included.
[ ] Liquidity filter included.
[ ] Position sizing realistic.
[ ] Max positions enforced.
[ ] Overlapping trades handled.
[ ] News/event handling realistic.
[ ] Date range covers multiple regimes.
[ ] Out-of-sample or walk-forward test included.
[ ] Parameter sensitivity checked.
[ ] Results shown by regime and year.
[ ] Drawdown acceptable.
[ ] Trade count sufficient.
```

---

# 10. Live Trading Readiness Checklist

```text
[ ] Strategy has written rules.
[ ] Backtest passes realism checks.
[ ] Forward test completed.
[ ] Minimum 50-100 paper trades logged.
[ ] Rule-following rate above 90%.
[ ] Costs/slippage tracked.
[ ] Max drawdown acceptable.
[ ] Risk limits written.
[ ] Kill switch defined.
[ ] Broker execution tested.
[ ] Journal process stable.
[ ] No unresolved critical misconception.
[ ] Live size starts at tiny risk.
```

If any critical item is missing, the strategy is not ready for meaningful live capital.
