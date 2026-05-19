# Trading Misunderstanding Register

## Quick Summary

This register lists the weak, incomplete, or dangerous ideas found while reviewing the finance-related notes in this vault. It does not mean every idea is wrong. It means the current documents often teach the concept but do not yet convert it into measured, testable, execution-ready trading rules.

Severity scale:

| Severity | Meaning |
| --- | --- |
| Low | Mostly educational gap |
| Medium | Can create poor analysis or inconsistent execution |
| High | Can cause serious trading losses if used live |
| Critical | Can create uncontrolled risk or false confidence |

---

# 1. Setup Versus Strategy

| Field | Detail |
| --- | --- |
| Topic | Setup definition |
| Source | `Positional Trader.md`, `Probabilistic Trading Guide.md` |
| My current understanding | A breakout, pullback, retest, or relative-strength pattern can be traded if it looks clean and passes a checklist. |
| Problem | A setup is not a strategy unless market, timeframe, entry, stop, exit, sizing, risk limits, costs, and invalidation are all explicit. |
| Correct understanding | A setup is a pattern. A strategy is a complete operating rule set with evidence. |
| Severity | High |
| How to fix it | Rewrite each setup into a strategy specification and test it separately. |
| Study or test next | Build 50 historical examples each for base breakout and trend pullback, then paper trade only those two. |

---

# 2. Undefined Confirmation

| Field | Detail |
| --- | --- |
| Topic | Confirmation |
| Source | `Positional Trader.md`, `Financial Jargon Glossary.md` |
| My current understanding | Wait for confirmation before entering. |
| Problem | "Confirmation" is vague. It can be reinterpreted after the trade and cannot be tested reliably. |
| Correct understanding | Confirmation must be an observable rule, such as daily close above resistance, volume greater than 1.5x 20-day average, or retest hold with close above prior level. |
| Severity | High |
| How to fix it | Replace every use of "confirmation" with the exact trigger. |
| Study or test next | Compare breakout-on-close vs breakout-retest entries using the same universe and cost assumptions. |

---

# 3. Vague Breakout Definition

| Field | Detail |
| --- | --- |
| Topic | Breakouts |
| Source | `Positional Trader.md`, `Probabilistic Trading Guide.md`, `Financial Jargon Glossary.md` |
| My current understanding | A breakout occurs when price moves above resistance. |
| Problem | This misses base length, close requirement, volume, overhead resistance, retest rule, and failure rule. |
| Correct understanding | A breakout must define the level, minimum consolidation, close condition, volume condition, stop, failure rule, and minimum reward-to-risk. |
| Severity | High |
| How to fix it | Use the stricter Base Breakout rules now integrated into `Positional Trader.md`, then record trades using `pro_trading_workbook_template.md`. |
| Study or test next | Track 100 breakout candidates, including skipped trades and failures. |

---

# 4. Support And Resistance Treated Too Casually

| Field | Detail |
| --- | --- |
| Topic | Support and resistance |
| Source | `Positional Trader.md`, `Probabilistic Trading Guide.md` |
| My current understanding | Support and resistance are zones where price may react. |
| Problem | That is directionally correct but incomplete. The notes do not consistently define zone width, number of touches, reaction quality, timeframe, or invalidation. |
| Correct understanding | A level is useful only if it defines trade location, stop placement, and reward-to-risk. |
| Severity | Medium |
| How to fix it | Record zone range, timeframe, touches, volume, and invalidation in the trade plan. |
| Study or test next | Mark 50 charts and record whether price reacted at premarked levels without changing them afterward. |

---

# 5. Relative Strength Without Formula

| Field | Detail |
| --- | --- |
| Topic | Relative strength |
| Source | `Positional Trader.md` |
| My current understanding | Prefer stocks stronger than the index or sector. |
| Problem | Correct idea, but not yet measurable. It needs a time window, benchmark, ranking method, and threshold. |
| Correct understanding | Relative strength should be calculated, for example 1-month, 3-month, and 6-month return vs index and sector, plus proximity to 52-week high. |
| Severity | Medium |
| How to fix it | Add relative-strength fields to watchlist and journal. |
| Study or test next | Compare top-quintile relative-strength stocks against lower quintiles in the same market regime. |

---

# 6. Volume Confirmation Without Consistent Threshold

| Field | Detail |
| --- | --- |
| Topic | Volume |
| Source | `Positional Trader.md`, `Financial Jargon Glossary.md` |
| My current understanding | High volume confirms breakouts and low volume supports pullbacks. |
| Problem | Mostly correct but incomplete. The threshold and comparison window must be explicit. |
| Correct understanding | Define volume rules before testing, such as breakout volume greater than 1.5x 20-day average and pullback volume below advance volume. |
| Severity | Medium |
| How to fix it | Add exact volume conditions per setup. |
| Study or test next | Test breakout performance with and without volume filter. |

---

# 7. Trade Score Treated As Objective Edge

| Field | Detail |
| --- | --- |
| Topic | 8-point trade score |
| Source | `Probabilistic Trading Guide.md` |
| My current understanding | A 7-8 score means an A-grade trade. |
| Problem | The score is useful as a checklist, but it is subjective until calibrated with data. |
| Correct understanding | The score is a permission filter, not proof of probability. Higher score should not mean higher size until journal evidence shows better expectancy. |
| Severity | Medium |
| How to fix it | Record score on every paper trade and review expectancy by score bucket after 50-100 trades. |
| Study or test next | Measure whether 7-8 score trades outperform 5-6 score trades after costs. |

---

# 8. Expected Value Without Real Sample

| Field | Detail |
| --- | --- |
| Topic | Expectancy |
| Source | `Probabilistic Trading Guide.md` |
| My current understanding | Positive expectancy can exist with low win rate if average win is larger than average loss. |
| Problem | Correct math, but the current vault has no trade sample proving those inputs. |
| Correct understanding | Expectancy is only meaningful when calculated from actual backtest, replay, paper, or live trades with costs included. |
| Severity | High |
| How to fix it | Start a structured journal and calculate expectancy monthly by setup. |
| Study or test next | Collect at least 50 valid paper trades before any live claim. |

---

# 9. Fundamentals Mistaken For Timing

| Field | Detail |
| --- | --- |
| Topic | Fundamental analysis |
| Source | `Fundamental Analysis.md` |
| My current understanding | Strong fundamentals support investment and trading decisions. |
| Problem | Correct but incomplete. Fundamentals can identify quality and value, but not exact timing. |
| Correct understanding | Fundamentals need catalyst, technical confirmation, invalidation, and risk sizing before becoming a trade. |
| Severity | Medium |
| How to fix it | End every fundamental note with thesis, catalyst, timing, invalidation, instrument, and maximum loss. |
| Study or test next | Convert three companies into complete investment or positional trade memos. |

---

# 10. Valuation Precision Risk

| Field | Detail |
| --- | --- |
| Topic | Valuation |
| Source | `Fundamental Analysis.md` |
| My current understanding | DCF and multiples can estimate fair value. |
| Problem | Mostly correct, but valuation is sensitive to assumptions and may create false precision. |
| Correct understanding | Valuation should be shown as a range with sensitivity tables and scenario assumptions. |
| Severity | Medium |
| How to fix it | Use bear/base/bull cases and require sensitivity to margin, growth, and discount rate. |
| Study or test next | Build a simple valuation range for one stock and document what would invalidate it. |

---

# 11. Fundamental Data Look-Ahead Risk

| Field | Detail |
| --- | --- |
| Topic | Point-in-time data |
| Source | `Fundamental Analysis.md` |
| My current understanding | Fundamental data must be point-in-time in backtests. |
| Problem | The note correctly identifies the issue, but there is no implemented process or data source in the vault. |
| Correct understanding | Backtests must use report date, filing availability date, restatements, and historical constituents. |
| Severity | High |
| How to fix it | Do not backtest fundamental features until point-in-time data handling is documented. |
| Study or test next | Create a data dictionary for one fundamental field with actual availability date. |

---

# 12. Futures Treated As Directional Shortcut

| Field | Detail |
| --- | --- |
| Topic | Futures |
| Source | `Fundamental Analysis.md`, `Positional Trader.md` |
| My current understanding | Futures can be used for directional trades after understanding risk. |
| Problem | Correct but still too permissive. Futures require lot size, margin, mark-to-market, gap risk, rollover, and liquidity rules. |
| Correct understanding | Futures are allowed only after the underlying cash strategy is tested and contract-level sizing works. |
| Severity | High |
| How to fix it | Create a futures trade memo before any futures trade. |
| Study or test next | Calculate risk for one index future and one stock future using entry, stop, lot size, and margin stress. |

---

# 13. Options Treated As Cheaper Stock

| Field | Detail |
| --- | --- |
| Topic | Options buying |
| Source | `Fundamental Analysis.md`, `Positional Trader.md` |
| My current understanding | Options can be useful for limited-risk directional trades. |
| Problem | Correct but incomplete. Direction can be right and the option can still lose due to time decay, IV crush, strike choice, and spread. |
| Correct understanding | Options require expected move, expected time, implied volatility, expiry, strike, liquidity, and exit rule. |
| Severity | High |
| How to fix it | Use options only after completing an options trade memo with max loss and Greeks. |
| Study or test next | Paper trade 20 long-option structures and compare underlying move vs option P&L. |

---

# 14. Option Selling Mode

| Field | Detail |
| --- | --- |
| Topic | Selling-only options mode |
| Source | `Todo's.md` |
| My current understanding | Add a mode that sells options while manual buying remains outside the program. |
| Problem | This is dangerous. Selling options without consolidated portfolio risk tracking can create undefined tail risk, especially if manual hedges are outside the bot. |
| Correct understanding | No option selling system should exist without defined risk, hedge tracking, margin stress, stop rules, event filters, and portfolio-level exposure. |
| Severity | Critical |
| How to fix it | Block naked selling in the learning system. Only define spread-based structures with max loss. |
| Study or test next | Study defined-risk spreads, margin, IV, tail risk, and broker execution before designing this mode. |

---

# 15. Trading Bot Before Trading Evidence

| Field | Detail |
| --- | --- |
| Topic | Trading bot project |
| Source | `aws_saa_trading_bot_plan_checklist.md`, `aws_saa_trading_bot_plan_checklist_v2.md` |
| My current understanding | Build bot features like signals, paper order placement, notifications, backtest, and cloud deployment during DevOps learning. |
| Problem | Good DevOps practice, but trading automation before strategy validation can create false confidence. |
| Correct understanding | Bot development must start with strategy spec, simulator, risk engine, and logging before cloud deployment. |
| Severity | High |
| How to fix it | Treat bot as DevOps sandbox unless strategy evidence exists. |
| Study or test next | Build a no-live paper-only simulator with full logs and replay. |

---

# 16. Paper Trading Without Realistic Fill Model

| Field | Detail |
| --- | --- |
| Topic | Paper trading |
| Source | `aws_saa_trading_bot_plan_checklist.md`, `aws_saa_trading_bot_plan_checklist_v2.md`, `Positional Trader.md` |
| My current understanding | Paper trading can validate execution discipline. |
| Problem | Correct, but paper trading is weak if it assumes perfect fills or ignores spread, slippage, rejected orders, and gap-through-stop behavior. |
| Correct understanding | Paper mode must model next tradable price, spread, slippage, costs, stop execution, and rejected trades. |
| Severity | High |
| How to fix it | Add paper fill assumptions to every test. |
| Study or test next | Compare close-price fills vs next-open/limit fills for the same signals. |

---

# 17. No Evidence Layer In Vault

| Field | Detail |
| --- | --- |
| Topic | Evidence |
| Source | Entire finance-related workspace |
| My current understanding | The notes contain detailed knowledge and plans. |
| Problem | There are no journals, backtest outputs, trade lists, screenshots, or forward-test metrics in the vault. |
| Correct understanding | Current readiness is educational. No strategy can be treated as validated from these notes alone. |
| Severity | Critical |
| How to fix it | Create a journal, backtest tracker, forward-test tracker, and monthly review process. |
| Study or test next | Run a 30-day structured paper test using one setup only. |

---

# 18. Too Many Setups Too Early

| Field | Detail |
| --- | --- |
| Topic | Strategy focus |
| Source | `Positional Trader.md` |
| My current understanding | A positional trader should understand many strategies. |
| Problem | Learning many setups at once causes inconsistent execution and no clean sample size. |
| Correct understanding | Start with one or two setups, collect enough trades, then expand. |
| Severity | Medium |
| How to fix it | Use only Trend Pullback and Base Breakout for the first 90 days. |
| Study or test next | Build a setup library with valid, invalid, winning, losing, and skipped examples. |

---

# 19. Risk Percent Without Gap-Risk Adjustment

| Field | Detail |
| --- | --- |
| Topic | Position sizing |
| Source | `Positional Trader.md`, `Probabilistic Trading Guide.md` |
| My current understanding | Risk 0.25% to 1% per trade based on stop distance. |
| Problem | Good starting point, but overnight gaps can exceed stop loss, especially in positional trading. |
| Correct understanding | Size should account for planned stop loss and plausible gap-through-stop loss. |
| Severity | High |
| How to fix it | Reduce size before earnings/events, avoid illiquid stocks, cap correlated open risk. |
| Study or test next | Track historical gap size for traded universe and include gap stress in sizing. |

---

# 20. Screenshots And Anecdotes As Evidence

| Field | Detail |
| --- | --- |
| Topic | Review evidence |
| Source | `Positional Trader.md`, `Probabilistic Trading Guide.md` |
| My current understanding | Screenshots before and after trades help review setups. |
| Problem | Screenshots are useful but can be cherry-picked and are not enough to prove edge. |
| Correct understanding | Screenshots support the journal. Trade list, rules, costs, and metrics prove or disprove the strategy. |
| Severity | Medium |
| How to fix it | Store screenshots only with complete trade records and include skipped trades. |
| Study or test next | Create a 30-example library: 10 winners, 10 losers, 10 skipped trades. |
