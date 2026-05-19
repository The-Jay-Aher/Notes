# Positional Trader

## Quick Summary

This note is a detailed operating manual for learning positional trading across **cash stocks, ETFs, stock futures, index futures, stock options, and index options**. It is written mainly for Indian markets, but the process applies broadly: understand the market regime, choose the right sector and instrument, build a thesis, size the position, manage risk, execute calmly, and review the trade.

A **positional trader** holds trades for **several days to several weeks or months**, depending on the setup. The goal is not to catch every small intraday move. The goal is to identify a meaningful move, enter with defined risk, survive normal noise, and exit with discipline.

This guide is written mainly for **stocks, stock futures, index futures, and index/stock options in India**, but the framework applies broadly.

This is educational material, not financial advice. Derivatives can multiply both gains and losses. SEBI's investor education material describes futures and options as derivatives whose value comes from an underlying security, and it highlights that leverage can multiply losses when the view is wrong. ([SEBI Investor][6])

The starting assumption must be defensive. SEBI's 2024 study reported that **93% of individual traders in Indian equity F&O incurred losses between FY22 and FY24**, with aggregate losses exceeding Rs 1.8 lakh crore. ([SEBI][11]) That does not mean nobody can trade derivatives; it means leverage, expiry, costs, and behavior make F&O a poor training ground for undisciplined traders.

Related notes:

- [Financial Jargon Glossary](Financial%20Jargon%20Glossary.md)
- [Fundamental Analysis](Fundamental%20Analysis.md)
- [Probabilistic Trading Guide](Probabilistic%20Trading%20Guide.md)

How the three notes fit together:

| Note | Use it for |
| --- | --- |
| [Financial Jargon Glossary](Financial%20Jargon%20Glossary.md) | Meaning of market words such as short covering, OI, IV crush, rollover, margin, and basis |
| [Fundamental Analysis](Fundamental%20Analysis.md) | Business quality, valuation, accounting, catalysts, and whether a stock/index deserves attention |
| [Probabilistic Trading Guide](Probabilistic%20Trading%20Guide.md) | Expectancy, R-multiples, trade scoring, sample size, and rule-based discretionary decisions |
| This note | Converting market context and thesis into a controlled positional trading process |

## Institutional operating boundary

This guide is detailed enough for learning and structured paper trading. It is not evidence that any strategy is profitable. A positional setup becomes tradeable only when it is written, tested, journaled, and reviewed as a repeatable process.

Current permission level:

| Activity | Status | Reason |
| --- | --- | --- |
| Learning | Allowed | The notes cover the required concepts |
| Chart replay | Allowed | Use it to define setups and collect examples |
| Structured paper trading | Allowed with restrictions | Only written setups, full journal, realistic costs |
| Small live testing | Not ready | No paper sample or execution record exists in this vault |
| Futures trading | Not ready | Contract-level margin, lot, rollover, and gap risk are not documented |
| Options buying | Not ready for live | Strike, expiry, IV, spread, and exit rules need paper testing |
| Option selling | Blocked | Use defined-risk structures only after a tested risk engine exists |
| Live trading bot | Blocked | Strategy evidence, simulator, risk engine, and logs are missing |

For the first serious training cycle, reduce the active playbook to two setups:

```text
1. Trend Pullback Continuation
2. Base Breakout
```

Everything else stays as study material until those two have a clean replay and paper-trading sample.

Use these audit and workbook files for stricter execution rules:

- [Professional Trading Workbook Template](pro_trading_workbook_template.md)
- [Trading Notes Audit Report](trading_notes_audit_report.md)
- [Action Plan](action_plan.md)

---

# 1. What Positional Trading Actually Means

## Positional trading sits between swing trading and investing

| Style              |         Holding Period | Main Focus                                              |
| ------------------ | ---------------------: | ------------------------------------------------------- |
| Intraday           |    Minutes to same day | Fast execution, liquidity, volatility                   |
| Swing trading      |      2 days to 2 weeks | Short-term momentum or mean reversion                   |
| Positional trading | Several days to months | Trend, structure, events, fundamentals, sector rotation |
| Investing          |        Months to years | Business quality, valuation, compounding                |

A positional trader is not necessarily an investor. You may buy a stock because the business is improving, but your job is still to manage the trade rather than convert it into a long-term investment only because the price moved against you.

---

# 2. The Real Goal of a Pro Positional Trader

Your goal is **not** to predict every market move. Your goal is to build a repeatable decision process where risk is known before entry and performance can be reviewed after exit.

A professional positional trader answers seven questions before taking a trade:

1. **What should I trade?**
   Stock, index, sector, future, option, ETF.

2. **Why should I trade it?**
   Trend, earnings, sector rotation, macro trigger, breakout, valuation re-rating, institutional flow.

3. **Where do I enter?**
   Breakout, pullback, retest, close-based trigger, event confirmation, or staged entry.

4. **Where am I wrong?**
   Stop loss, invalidation level, thesis failure.

5. **How much can I lose?**
   Position sizing, portfolio exposure, gap risk.

6. **How do I exit?**
   Target, trailing stop, time stop, event exit, thesis exit.

7. **How do I review performance?**
   R-multiple, rule adherence, setup quality, mistake rate, and market-condition context.

A weak question is:

```text
Will this stock go up?
```

A better question is:

```text
Is this setup worth risking Rs X for a possible Rs Y, and does it fit my written system?
```

If you cannot answer that before entering, the trade is not ready.

---

# 3. Difference Between Amateur and Professional Positional Traders

| Amateur                        | Professional                                               |
| ------------------------------ | ---------------------------------------------------------- |
| Looks for tips                 | Builds a repeatable process                                |
| Enters because price is moving | Enters because setup, risk, and context align              |
| Thinks only about profit       | Thinks first about loss                                    |
| Averages losers randomly       | Adds only when thesis improves                             |
| Uses one indicator             | Combines trend, structure, volume, fundamentals, sentiment |
| Blames operator manipulation   | Reviews execution and thesis                               |
| Exits from fear                | Exits from rules                                           |
| Overtrades                     | Waits for quality                                          |

Professional trading is boring most of the time. That is the point. If it feels constantly exciting, something is probably wrong, usually your risk.

---

## Core Skills You Need

To become a serious positional trader, develop five skill groups. Do not skip risk and review because charts feel more interesting. The profession is not chart drawing; the profession is controlled decision-making under uncertainty.

### 1. Market understanding

You need to understand:

* How stocks, indices, ETFs, futures, options, sectors, and commodities move.
* How market regime changes from bullish to sideways to bearish.
* How sector rotation creates leadership.
* How breakouts fail and trap late buyers.
* How institutional buying and selling can appear through volume, delivery, OI, and relative strength.
* How liquidity affects entry and exit quality.
* How news, earnings, macro events, policy, and market sentiment affect positions.

### 2. Technical analysis

Useful technical analysis means reading market behavior, not decorating charts. Focus on:

* Trend.
* Support and resistance.
* Market structure.
* Breakouts and failed breakouts.
* Pullbacks and retests.
* Volume.
* Relative strength.
* Volatility.
* Failed patterns and trapped positioning.

### 3. Risk management

Risk management is the core skill. You need rules for:

* Risk per trade.
* Stop loss.
* Position sizing.
* Maximum open risk.
* Maximum drawdown.
* Sector exposure.
* Leverage.
* Gap risk.
* Kill switch.

### 4. Trade execution

Execution decides whether your theoretical plan survives the actual market. Learn:

* Market order vs limit order.
* Stop-loss market vs stop-loss limit.
* Slippage.
* Liquidity.
* Bid-ask spread.
* Partial entries.
* Partial exits.
* Gap openings.
* Broker/platform reliability.

### 5. Review and improvement

Every trade becomes data. Track:

* Win rate.
* Average win.
* Average loss.
* Expectancy.
* Profit factor.
* Maximum drawdown.
* Mistake rate.
* Setup-wise performance.
* Market-condition-wise performance.

Without review, the trader repeats behavior without knowing what is actually working.

---

# 4. The Full Positional Trading Framework

A complete positional trade has these layers:

```text
1. Market regime
2. Sector selection
3. Stock selection
4. Trade thesis
5. Technical setup
6. Risk sizing
7. Entry execution
8. Trade management
9. Exit plan
10. Review and improvement
```

Do not skip layers. Many losing trades begin as trades, then become forced "investments" only after the original plan fails.

## Instrument selection is part of the setup

The instrument must match the thesis. A bullish view can be expressed through cash equity, futures, call options, call spreads, or no trade at all. Those are not interchangeable.

| Instrument | Best use | Main advantage | Main risk |
| --- | --- | --- | --- |
| Cash stock | Multi-day to multi-month bullish view | No expiry, no mark-to-market margin call, direct ownership | Full downside exposure, capital tied up |
| ETF | Broad index, sector, commodity, or theme exposure | Lower single-stock disaster risk | Liquidity varies; moves may be slower |
| Stock future | Strong directional view on one liquid stock | Efficient leverage and easy shorting | Large notional exposure, gap risk, margin calls |
| Index future | Directional view on index or portfolio hedge | High liquidity and clean beta exposure | Leverage, basis movement, overnight gap risk |
| Long call | Limited-risk bullish trade before a catalyst | Defined loss to premium | Theta decay and IV crush |
| Long put | Limited-risk bearish trade or hedge | Defined loss to premium | Premium decay and liquidity risk |
| Debit spread | Directional options trade with lower premium | Defined risk and lower cost than naked long option | Capped upside and spread execution risk |
| Covered call | Own stock and sell limited upside | Premium income | Upside capped and assignment risk |
| Protective put | Own stock but want downside protection | Insurance-like payoff | Hedge cost reduces return |
| Collar | Own stock, cap upside to reduce hedge cost | Downside control with lower net cost | Limited upside |

Simple rule:

```text
Long-term thesis -> prefer cash equity.
Broad theme thesis -> prefer ETF or index instrument.
High-conviction directional trade -> consider futures only if rupee risk is controlled.
Catalyst-based limited-risk view -> consider options or spreads.
Unclear timing -> avoid short-dated options.
Unclear thesis -> no trade.
```

Derivatives should come after thesis, not before it.

For most beginners and intermediate traders, cash stocks are the cleanest training ground. They still carry risk, but they remove expiry, option Greeks, margin calls, and rollover decisions. Use futures or options only when the instrument solves a real problem that cash equity cannot solve.

---

# 5. Market Regime Analysis

Before choosing stocks, understand the market environment.

## Market regime asks:

> Is the broader market supportive, hostile, or mixed?

For Indian markets, track:

| Factor                            | What To Check                                        |
| --------------------------------- | ---------------------------------------------------- |
| NIFTY trend                       | Above/below 20, 50, 100, 200 DMA                     |
| BANKNIFTY trend                   | Especially important for index direction             |
| Market breadth                    | Advancers vs decliners, % stocks above 50 DMA        |
| Sector rotation                   | Which sectors are leading or weakening               |
| Volatility                        | India VIX, gap risk, event risk                      |
| FII/DII flows                     | Directional institutional pressure                   |
| Macro                             | RBI policy, inflation, crude, USDINR, global indices |
| Earnings season                   | Stock-specific volatility increases                  |
| Election/budget/geopolitical risk | Can override technical setups                        |

SEBI’s investor risk material stresses that market participants should understand their goals, risk appetite, and risk-return profile before investing or trading securities. That is not paperwork language; it is the foundation of position sizing and instrument choice. ([investor.sebi.gov.in][1])

## Simple regime classification

| Regime          | Meaning                                         | Trading Action                              |
| --------------- | ----------------------------------------------- | ------------------------------------------- |
| Bull trend      | Index above key moving averages, breadth strong | Prefer long positions                       |
| Bear trend      | Index below key averages, breadth weak          | Avoid longs, prefer shorts/hedges           |
| Sideways        | Index range-bound, mixed breadth                | Trade selectively, reduce size              |
| High volatility | Big gaps, unstable news, VIX rising             | Reduce size, wider stops, avoid weak setups |
| Event-driven    | Budget, results, policy, global shock           | Respect gap risk                            |

## For positional trading, regime matters a lot

A mediocre stock in a strong bull market can rise.
A strong stock in a weak market can fail.

This is why regime comes before stock selection. A good stock in a hostile market can still fail as a trade.

---

# 6. Sector Selection

Professional positional traders often start with sectors, not individual stocks.

## Why sector matters

Stocks usually move in groups:

* Banks move together.
* IT moves together.
* Metals move with global commodity cycles.
* Autos move with demand, margins, rural income, EV theme.
* Pharma moves with USFDA, export pricing, product approvals.
* Oil & gas moves with crude, refining margins, gas prices.
* Realty moves with rates, housing demand, liquidity.
* PSU stocks often move with policy, capex, divestment, narratives.

## Sector analysis checklist

| Question                               | Why It Matters                          |
| -------------------------------------- | --------------------------------------- |
| Is the sector outperforming NIFTY?     | Shows relative strength                 |
| Is money rotating into the sector?     | Increases probability of follow-through |
| Are multiple stocks breaking out?      | Confirms broad participation            |
| Is there a fundamental trigger?        | Supports sustained move                 |
| Is the move news-driven or structural? | Helps decide holding period             |
| Is valuation stretched?                | Helps avoid late entries                |
| Are results improving?                 | Earnings drive positional moves         |

## Relative strength

Compare:

```text
Stock / NIFTY
Sector Index / NIFTY
Stock / Sector Index
```

You want stocks that are stronger than both:

1. The broader market.
2. Their own sector.

A stock outperforming in a weak market is often worth tracking. It may become a leader when the market turns.

---

# 7. Stock Selection Framework

A positional trader should maintain a **watchlist**, not randomly scan thousands of stocks without a process.

## Watchlist categories

| Category                 | Examples                                       |
| ------------------------ | ---------------------------------------------- |
| Large caps               | Liquid, lower gap risk, institutional interest |
| Sector leaders           | Best companies in strong sectors               |
| High beta names          | Bigger moves, bigger risk                      |
| Turnaround names         | Improving fundamentals                         |
| Earnings momentum stocks | Strong quarterly growth                        |
| Breakout candidates      | Near all-time high or multi-month resistance   |
| Event stocks             | Results, demerger, policy, capex, order wins   |
| Weak stocks for shorts   | Breakdown candidates                           |

## Minimum filters

For positional trading, avoid illiquid, low-quality names.

Basic filters:

* Average daily traded value should be high.
* Bid-ask spread should be tight.
* Stock should have enough history.
* Avoid stocks with repeated lower circuits.
* Avoid unknown smallcaps unless you deeply understand the risk.
* Avoid stocks with pending fraud, pledge, governance issues.
* Avoid stocks where one news event can destroy liquidity.

## Quality filters

For cash equity positional trades:

| Filter                | What To Prefer                         |
| --------------------- | -------------------------------------- |
| Sales growth          | Consistent or improving                |
| Profit growth         | Stable or accelerating                 |
| Margins               | Expanding or stable                    |
| Debt                  | Manageable                             |
| Cash flow             | Positive operating cash flow preferred |
| ROE/ROCE              | Higher is usually better               |
| Promoter pledge       | Lower is safer                         |
| Institutional holding | Rising can be supportive               |
| Valuation             | Not absurd relative to growth          |

You do not need deep fundamental analysis for every positional trade, but you should know whether you are buying strength, value, turnaround, or narrative.

---

# 8. The Four Main Positional Trading Styles

## 1. Trend-following positional trading

You buy stocks already trending up and hold while the trend continues.

### Good for:

* Strong bull markets.
* Sector rotation.
* Momentum stocks.
* Breakout continuation.

### Tools:

* Moving averages.
* Higher highs and higher lows.
* Relative strength.
* Volume confirmation.
* Trailing stop.

### Example rules:

```text
Buy when:
- Stock is above 50 DMA and 200 DMA.
- 50 DMA is above 200 DMA.
- Stock breaks above 20-day high.
- Volume is above 20-day average.
- Sector is outperforming NIFTY.
- Stop is below recent swing low or ATR-based level.
```

### Risk:

You may buy late and suffer pullbacks.

---

## 2. Breakout positional trading

You buy when price breaks above a major resistance zone.

### Good breakout characteristics:

* Long consolidation before breakout.
* Tight range before move.
* Volume expansion.
* Strong close above resistance.
* Sector support.
* Relative strength improving.
* No major overhead supply nearby.

### Weak breakout signs:

* Breakout on low volume.
* Huge gap above resistance with no entry control.
* Breakout after already extended move.
* Market breadth weak.
* Stock reverses below breakout level quickly.
* News hype already everywhere.

### Breakout entry types:

| Entry Type        | Meaning                                  | Pros                       | Cons                |
| ----------------- | ---------------------------------------- | -------------------------- | ------------------- |
| Close breakout    | Enter after daily close above level      | Avoids fake intraday break | May enter late      |
| Retest entry      | Enter when price retests breakout zone   | Better risk-reward         | May never retest    |
| Intraday breakout | Enter during breakout                    | Early                      | More false signals  |
| Staggered entry   | Partial entry on breakout, add on retest | Balanced                   | Requires discipline |

---

## 3. Pullback positional trading

You buy an uptrending stock when it corrects to support.

### Common pullback zones:

* 20 DMA.
* 50 DMA.
* Prior breakout level.
* Fibonacci zone.
* Trendline.
* VWAP anchor from major event.
* Demand zone.
* Previous swing high turned support.

### Good pullback signs:

* Low volume decline.
* Price holds support.
* Bullish reversal candle.
* RSI cools but does not collapse.
* Sector remains strong.
* Broader market stabilizes.

### Risk:

The “healthy pullback” can become a trend reversal. Because apparently markets enjoy humiliating labels.

---

## 4. Mean reversion positional trading

You buy oversold quality stocks expecting recovery, or short overextended weak stocks expecting correction.

### Useful when:

* Stock is fundamentally strong but temporarily sold off.
* Panic selling is overdone.
* Price reaches major support.
* Bad news is already priced in.
* Risk-reward is clearly favorable.

### Dangerous when:

* Business quality is poor.
* Stock is falling due to real earnings damage.
* Debt or governance issue exists.
* You average down blindly.
* You call every falling stock “value.”

Mean reversion is where many traders accidentally become long-term bagholders.

---

# 9. Trade Thesis: The Most Important Part

Every positional trade needs a **thesis**.

A thesis is the reason the trade should work.

## Thesis examples

### Technical thesis

```text
The stock has formed a 3-month base, broken above resistance with strong volume, and is outperforming both NIFTY and its sector.
```

### Fundamental thesis

```text
The company has reported strong earnings growth, margin expansion, and management guidance suggests continued demand.
```

### Sector thesis

```text
The entire sector is seeing institutional buying due to policy support and improving earnings.
```

### Event thesis

```text
The company received a major order that may improve future revenue visibility.
```

### Derivatives thesis

```text
Futures open interest and price are rising together, indicating long buildup, while options data shows resistance shifting higher.
```

## A good thesis must include invalidation

Bad thesis:

```text
Stock is strong. Might go up.
```

Good thesis:

```text
Stock is breaking out above ₹1,200 from a 10-week base with volume expansion. Thesis remains valid while price holds above ₹1,150 on closing basis. If it closes below ₹1,150 with high volume, breakout has failed.
```

---

# 10. Technical Analysis Framework

Technical analysis for positional trading should answer:

1. What is the trend?
2. Where is support?
3. Where is resistance?
4. Is momentum strong?
5. Is volume confirming?
6. Where is invalidation?
7. Is reward worth the risk?

## Core tools

### 1. Trend structure

Uptrend:

```text
Higher high + higher low
```

Downtrend:

```text
Lower high + lower low
```

Sideways:

```text
Price trapped in range
```

Do not overcomplicate this. A chart does not become more professional because you add twelve indicators until it looks like a hospital monitor.

---

### 2. Moving averages

Useful moving averages:

|      MA | Use                               |
| ------: | --------------------------------- |
|  10 EMA | Short-term momentum               |
|  20 EMA | Pullback support in strong trends |
|  50 DMA | Medium-term trend                 |
| 100 DMA | Deeper trend support              |
| 200 DMA | Long-term trend filter            |

Basic interpretation:

| Price Location                 | Meaning                        |
| ------------------------------ | ------------------------------ |
| Above 20/50/200 DMA            | Strong trend                   |
| Above 200 DMA but below 50 DMA | Pullback or weakening          |
| Below 200 DMA                  | Avoid long unless special case |
| MA compression                 | Possible breakout setup        |
| Price far above MA             | Extended, avoid chasing        |

---

### 3. Support and resistance

Support is where demand may appear.
Resistance is where supply may appear.

Important levels:

* Previous swing highs.
* Previous swing lows.
* All-time high.
* 52-week high.
* Prior breakout zone.
* Gap zones.
* Volume profile high-volume nodes.
* Round numbers.
* Moving averages.
* Previous earnings day high/low.

## Strong support/resistance has:

* Multiple touches.
* High volume.
* Clear rejection.
* Long time duration.
* Alignment with moving average or prior breakout zone.

---

### 4. Volume

Volume confirms participation.

| Price + Volume             | Interpretation          |
| -------------------------- | ----------------------- |
| Price up, volume up        | Strong buying           |
| Price up, volume down      | Weak move               |
| Price down, volume up      | Strong selling          |
| Price down, volume down    | Normal pullback         |
| Breakout with high volume  | Higher quality breakout |
| Breakdown with high volume | Serious weakness        |

Volume is not magic. It says activity increased. It does not reveal everyone’s pure intentions, because apparently markets are not obligated to provide emotional transparency.

---

### 5. RSI

RSI can help measure momentum.

For positional trading:

| RSI Zone | Meaning                         |
| -------- | ------------------------------- |
| 40-50    | Pullback zone in uptrend        |
| 50-60    | Improving momentum              |
| 60-70    | Strong momentum                 |
| Above 70 | Strong but possibly extended    |
| Below 40 | Weakness                        |
| Below 30 | Oversold, not automatically buy |

In strong trends, RSI can stay high. Do not short just because RSI is above 70. That is how people donate money to momentum traders.

---

### 6. ATR

ATR measures volatility.

Use ATR for:

* Stop placement.
* Position sizing.
* Avoiding too-tight stops.
* Measuring expected move.
* Filtering high-volatility stocks.

Example:

```text
Entry = ₹1,000
ATR = ₹30
Stop = Entry - 2 × ATR = ₹940
```

ATR stops adjust to volatility better than random percentage stops.

---

### 7. Relative strength

Relative strength is one of the most important positional tools.

A strong stock:

* Falls less when market falls.
* Rises more when market rises.
* Breaks out before index.
* Holds key levels better than peers.

Track:

```text
Stock vs NIFTY
Stock vs sector index
Sector index vs NIFTY
```

Best long candidates usually come from:

```text
Strong stock + strong sector + improving market
```

---

# 11. Fundamental Analysis for Positional Trading

You do not need to value every company like Warren Buffett trapped in Excel for 9 hours, but you need enough fundamentals to avoid obvious traps.

## Key fundamental factors

| Factor                | What It Tells You                     |
| --------------------- | ------------------------------------- |
| Revenue growth        | Demand strength                       |
| Profit growth         | Earnings power                        |
| Margins               | Pricing power and cost control        |
| Debt                  | Financial risk                        |
| Cash flow             | Quality of profits                    |
| ROE/ROCE              | Capital efficiency                    |
| Promoter holding      | Ownership confidence                  |
| Pledged shares        | Risk warning                          |
| Institutional holding | Smart money interest                  |
| Guidance              | Future expectations                   |
| Order book            | Revenue visibility                    |
| Valuation             | Whether expectations are already high |

## Positional trader’s earnings checklist

Before trading around earnings, check:

* Revenue growth YoY and QoQ.
* EBITDA margin.
* PAT growth.
* Management commentary.
* Segment performance.
* Debt changes.
* Cash flow.
* One-time gains/losses.
* Guidance.
* Market reaction.
* Analyst upgrades/downgrades.
* Gap risk.

## Earnings reaction matters more than earnings alone

A stock can report good results and fall.

Why?

* Results were already priced in.
* Margins disappointed.
* Guidance was weak.
* Valuation was stretched.
* Management commentary was cautious.
* Big players used liquidity to exit.

So track:

```text
Result quality + price reaction + volume + next-day follow-through
```

---

# 12. News and Event Analysis

Positional traders must understand news properly.

## News categories

| News Type              | Positional Importance |
| ---------------------- | --------------------- |
| Earnings               | Very high             |
| Management guidance    | Very high             |
| Order wins             | Medium to high        |
| M&A                    | High                  |
| Regulatory approval    | High                  |
| Policy changes         | High                  |
| Sector reforms         | High                  |
| Credit rating change   | Medium                |
| Promoter pledge        | High                  |
| Insider buying/selling | Medium                |
| Litigation             | High                  |
| Product launch         | Medium                |
| Analyst upgrade        | Medium                |
| Rumor                  | Low unless confirmed  |

## How professionals read news

They ask:

1. Is this expected or unexpected?
2. Is it already priced in?
3. Does it affect earnings?
4. Does it affect valuation?
5. Does it affect liquidity?
6. Does it affect sector sentiment?
7. Is the impact one-time or structural?
8. Is the market reaction confirming the news?
9. Are institutions likely to care?
10. Is there follow-through after the first reaction?

## Example

Bad reading:

```text
Company won ₹500 crore order. Buy.
```

Professional reading:

```text
Order size is ₹500 crore. Annual revenue is ₹10,000 crore, so order is 5% of revenue. Margins unknown. Execution timeline is 3 years. Impact is positive but not transformational. Need to check whether price already rallied before announcement.
```

That is the difference between trading and clapping at headlines.

---

# 13. Derivatives Data for Positional Trading

For Indian markets, derivatives can help confirm positioning.

## Futures data

Track:

| Data                 | Meaning        |
| -------------------- | -------------- |
| Price up + OI up     | Long buildup   |
| Price down + OI up   | Short buildup  |
| Price up + OI down   | Short covering |
| Price down + OI down | Long unwinding |

## Use futures OI carefully

OI tells you positioning changed. It does **not** tell you guaranteed direction.

Use it with:

* Price structure.
* Volume.
* Sector trend.
* News.
* Delivery data.
* Options positioning.

## Options data

Useful for:

* Support/resistance zones.
* Sentiment.
* Short-term positioning.
* Expiry pressure.
* Max pain context.
* IV expansion/contraction.
* Risk around events.

For positional stock trades, options data is secondary. For index positional trades, it matters more.

## Important options metrics

| Metric        | Use                           |
| ------------- | ----------------------------- |
| Call OI       | Potential resistance          |
| Put OI        | Potential support             |
| PCR           | Sentiment                     |
| IV            | Expected volatility           |
| IV percentile | Whether options are expensive |
| OI change     | Fresh positioning             |
| Volume        | Activity                      |
| Skew          | Demand for calls/puts         |

## Caution

High call OI does not mean price cannot cross that level. If price breaks above heavy call OI and call writers cover, the move can accelerate.

Treat support and resistance as zones of behavior, not fixed walls. A heavy call OI level can fail if price momentum forces writers to cover.

---

# 14. Risk Management

This is the most important section.

A trader without risk management is operating without a survival system.

## Core rule

Before entering, define:

```text
Entry
Stop loss
Position size
Target area
Exit rule
Maximum loss
```

## Risk per trade

Common professional range:

```text
0.25% to 1% of capital per trade
```

For learning:

```text
0.25% to 0.5% is better
```

Use this as a practical starting point:

| Trader level | Risk per trade |
| --- | ---: |
| Beginner | 0.25% to 0.5% |
| Intermediate | 0.5% to 1% |
| Experienced | 1% to 1.5% |
| Aggressive professional | Around 2%, rarely |

Most traders should not risk more than 1% per trade. If a setup cannot produce a sensible quantity at 1% risk, the position is too large, the stop is too wide, or the instrument is wrong.

Example:

```text
Capital = ₹5,00,000
Risk per trade = 0.5%
Max loss = ₹2,500
Entry = ₹1,000
Stop = ₹950
Risk per share = ₹50
Quantity = ₹2,500 / ₹50 = 50 shares
```

If stop hits, the expected loss is about Rs 2,500 plus charges and slippage. In a gap, actual loss can be worse, so overnight positions must be smaller than intraday confidence would suggest.

## Position sizing formula

```text
Quantity = Max Risk Per Trade / Risk Per Share
```

Where:

```text
Risk Per Share = Entry Price - Stop Loss
```

For shorts:

```text
Risk Per Share = Stop Loss - Entry Price
```

## Never size based on confidence alone

Confidence is not a position-sizing model. Evidence, stop distance, volatility, liquidity, and portfolio risk are the sizing inputs.

Use:

* Stop distance.
* Volatility.
* Liquidity.
* Portfolio exposure.
* Event risk.
* Correlation.
* Market regime.

## Portfolio heat

Portfolio heat means total open risk across all open trades.

Example:

```text
Trade 1 risk: 1.00%
Trade 2 risk: 1.00%
Trade 3 risk: 0.75%
Trade 4 risk: 0.75%
Total portfolio heat: 3.50%
```

Suggested maximum open risk:

| Trader level | Maximum open portfolio risk |
| --- | ---: |
| Beginner | 2% to 3% |
| Intermediate | 4% to 6% |
| Experienced | 6% to 8%, only with tested systems |

If market regime becomes hostile, reduce portfolio heat before the market forces you to reduce it.

## Kill switch

Stop trading temporarily when:

* You hit the monthly loss limit.
* You break rules repeatedly.
* You are emotionally unstable.
* Your system enters a deep drawdown.
* Market volatility changes sharply.
* You do not understand the current market behavior.

Useful default guardrails:

```text
Risk per trade: 0.25% to 1%
Maximum open portfolio risk: 4% to 6%
Maximum single-stock allocation: 20%
Maximum sector allocation: 35%
Maximum weekly loss: 3%
Maximum monthly loss: 6%
Reduce size by 50% after 5% drawdown
Stop trading and review after 10% drawdown
```

---

# 15. Portfolio-Level Risk

Positional trading has overnight risk, gap risk, and correlation risk.

## Portfolio controls

| Rule                        | Example            |
| --------------------------- | ------------------ |
| Max risk per trade          | 0.5%               |
| Max open trade risk         | 3% total           |
| Max sector exposure         | 25%                |
| Max single stock exposure   | 10%                |
| Max leveraged exposure      | Strictly capped    |
| Max weekly loss             | 2-3%               |
| Max monthly loss            | 5-6%               |
| Stop trading after drawdown | Mandatory cool-off |

## Correlation risk

Do not hold:

* HDFC Bank long.
* ICICI Bank long.
* Axis Bank long.
* SBI long.
* BANKNIFTY long.

…and pretend you have five independent trades. You have one banking bet wearing five costumes.

## Gap risk

A positional stop loss is not guaranteed.

A stock can close at ₹1,000 and open at ₹900.

So account for:

* Earnings.
* Policy announcements.
* Global market shocks.
* Crude shocks.
* Currency shocks.
* Court rulings.
* War/geopolitical events.
* Fraud/news accidents.

---

# 16. Stop Loss Methods

## 1. Structure-based stop

Place stop below a swing low for long trades.

Good because it respects price structure.

Example:

```text
Entry = ₹1,000
Recent swing low = ₹940
Stop = ₹935
```

## 2. ATR-based stop

Good for volatile stocks.

Example:

```text
Stop = Entry - 2 × ATR
```

## 3. Moving average stop

Useful in trends.

Examples:

* Exit if daily close below 20 EMA.
* Exit if weekly close below 10-week MA.
* Exit if price closes below 50 DMA.

## 4. Time stop

Exit if trade does not move after a defined time.

Example:

```text
If stock does not move at least 3% in 10 trading days, exit.
```

This prevents dead capital.

## 5. Thesis stop

Exit when reason for trade is invalid.

Example:

* Breakout fails.
* Earnings thesis breaks.
* Sector reverses.
* Management guidance disappoints.
* Regulatory issue appears.

## 6. Volatility stop

Exit if volatility expands abnormally against position.

Useful for leveraged positions.

---

# 17. Target and Exit Methods

## Target types

| Target Type        | Method                      |
| ------------------ | --------------------------- |
| Fixed R multiple   | 2R, 3R, 4R                  |
| Resistance-based   | Exit near major supply zone |
| Trailing stop      | Ride trend                  |
| Partial profit     | Book some, trail rest       |
| Fundamental target | Re-rating complete          |
| Event target       | Exit before/after event     |
| Time target        | Exit after holding period   |

## R-multiple

If your risk is ₹10 per share:

| Move | Meaning |
| ---- | ------- |
| +₹10 | +1R     |
| +₹20 | +2R     |
| -₹10 | -1R     |

A good positional system should aim for positive expectancy:

```text
Expectancy = (Win Rate × Avg Win) - (Loss Rate × Avg Loss)
```

You can be profitable with 40% win rate if winners are much bigger than losers.

---

# 18. Entry Techniques

## 1. Full entry

Enter full position at once.

Good for:

* Clean breakout.
* Strong confirmation.
* Liquid stocks.

Bad because:

* No flexibility.
* Worse if entry is mistimed.

## 2. Staggered entry

Enter in parts.

Example:

```text
50% on breakout
25% on retest
25% after follow-through
```

Good for positional trading because it reduces timing pressure.

## 3. Pullback entry

Wait for price to return to support.

Good risk-reward, but you may miss strong movers.

## 4. Confirmation entry

Enter only after daily close or weekly close confirms.

Good for avoiding false breakouts.

Bad because entry may be late.

## 5. Event entry

Enter after news reaction confirms direction.

Usually safer than guessing before results.

---

# 19. Adding to Winning Trades

Adding is allowed only when the trade is working.

Professional adding rules:

* Add only after price moves in your favor.
* Add near fresh breakout or pullback support.
* Never increase total risk beyond portfolio limit.
* Move stop logically, not emotionally.
* Do not add after a vertical move.
* Do not add just to “recover missed profit.”

Good pyramiding example:

```text
Initial entry: ₹1,000
Stop: ₹940
Price moves to ₹1,080
Stock consolidates
Breaks above ₹1,100
Add position
Trail stop to ₹1,030
```

Bad pyramiding:

```text
Stock up 18% in 4 days. Buy more because FOMO has entered the bloodstream.
```

---

# 20. Averaging Down

Averaging down is dangerous.

It is acceptable only when:

* It was planned before entry.
* The thesis is still valid.
* Price is near major support.
* Fundamental reason remains intact.
* Position size remains within risk limits.
* You are not using leverage.
* You know exactly where you exit.

It is unacceptable when:

* You are emotionally refusing loss.
* Bad news changed the thesis.
* Stock broke support.
* Volume confirms selling.
* Sector is collapsing.
* You are using margin.
* You say “it has fallen so much, how much more can it fall?”

The answer is: a lot. Markets are creative like that.

---

# 21. Positional Trading Using Futures

Futures are powerful because they give large notional exposure with less upfront capital than cash equity. That is also why they are dangerous.

A futures contract is not an investment in the company. It is an exchange-traded contract linked to the price of an underlying index or stock. NSE contract specifications define practical details such as trading cycle, expiry day, settlement, and contract availability; always check the current contract page before trading. ([NSE India][7])

The same risk principle applies globally: futures and futures options are complex leveraged products, and regulator education material consistently warns that speculative futures trading can lead to losses beyond the amount initially committed. ([CFTC][10])

## Futures mechanics you must understand

| Concept | Meaning | Why it matters |
| --- | --- | --- |
| Underlying | The index or stock the future tracks | Determines price behavior and news sensitivity |
| Lot size | Quantity represented by one contract | Converts points into rupee profit/loss |
| Notional value | Futures price x lot size x lots | Shows true market exposure |
| Margin | Capital blocked by broker/exchange | Can change with volatility and risk conditions |
| Mark-to-market | Daily profit/loss settlement | Losses can require additional funds before final exit |
| Basis | Futures price minus spot price | Shows premium/discount vs cash market |
| Expiry | Date contract settles/expires | Forces exit or rollover decision |
| Rollover | Closing current expiry and opening next expiry | Adds cost, slippage, and basis risk |
| Liquidity | Volume, OI, bid-ask spread | Determines whether entry/exit is realistic |

NSE's margin framework includes SPAN-style initial margin and extreme loss margin. It also describes end-of-day obligations including futures mark-to-market profit/loss and options premium/exercise/assignment obligations. ([NSE India][2])

## Advantages

* High liquidity in index futures.
* Easier shorting.
* No theta decay.
* Direct directional exposure.
* Better for index positional trades.
* Cleaner payoff than options when the view is directional and timing is uncertain.
* Useful for hedging broad portfolio beta if sized correctly.

## Risks

* Leverage.
* Mark-to-market loss.
* Overnight gaps.
* Margin changes.
* Rollover cost.
* Larger capital requirement.
* Forced exit if margin is insufficient.
* Basis movement between spot and futures.
* Corporate action and expiry adjustments in stock futures.
* Behavioral risk because profit/loss moves fast.

NSE’s equity derivatives margin framework uses initial margin based on value-at-risk models; for futures, margin can account for a longer risk horizon where next-day settlement collection is not possible. The practical lesson is simple: leverage is not free, and margin should be treated as a risk control rather than a target for maximum position size. ([NSE India][2])

## Futures sizing math

Before taking any futures trade, calculate exposure and rupee risk.

```text
Notional exposure = futures price x lot size x number of lots
Point value = lot size x number of lots
Rupee risk = abs(entry price - stop price) x point value
Risk % of capital = rupee risk / total trading capital
```

Example:

```text
Futures price: 1,000
Lot size: 500
Lots: 1
Notional exposure: 1,000 x 500 = 500,000
Entry: 1,000
Stop: 960
Point risk: 40
Rupee risk: 40 x 500 = 20,000
```

If your planned risk per trade is 10,000, this trade is too large even if the margin required is less than the notional value.

## When futures make sense

Use futures only when:

* The underlying is liquid.
* The setup has a clear invalidation level.
* The stop distance produces acceptable rupee risk.
* You have extra cash buffer beyond required margin.
* You are prepared for overnight gaps.
* You know the expiry date and rollover plan.
* You understand that notional exposure is the real exposure.

## When futures are the wrong instrument

Avoid futures when:

* The stop is very far away.
* You are using futures only because cash equity feels too slow.
* You cannot tolerate daily mark-to-market swings.
* The stock is event-heavy and gaps frequently.
* Liquidity is thin outside the near-month contract.
* The trade would dominate your total portfolio risk.
* You are trying to recover losses quickly.

## Basis and rollover

Basis is:

```text
Basis = futures price - spot price
```

Futures may trade above or below spot due to interest rates, dividends, borrow demand, positioning, and market stress. For positional trades, basis matters because:

* You may enter at a futures premium and exit after the premium shrinks.
* Rollover can add slippage.
* Near-expiry contracts can behave differently from next-month contracts.
* Futures and spot converge near expiry.

Track:

```text
Spot price
Futures price
Basis
Open interest
Volume
Days to expiry
Rollover cost
```

## Futures positional checklist

Before entering:

```text
[ ] Is the contract liquid?
[ ] What is the lot size?
[ ] What is the notional exposure?
[ ] What is the initial margin requirement?
[ ] What extra cash buffer is available?
[ ] What is the stop loss in points?
[ ] What is the rupee risk?
[ ] What is the basis vs spot?
[ ] What is the expiry date?
[ ] What is the rollover plan?
[ ] Is there earnings, policy, budget, court, or global event risk?
[ ] What slippage should be assumed?
[ ] Can I survive a gap beyond the stop?
```

---

# 22. Positional Trading Using Options

Options can be useful, but they are often misused because they look cheap in premium terms while hiding time decay, volatility risk, and poor probability.

An option gives the buyer a right, not an obligation. A call gives upside exposure; a put gives downside exposure. The buyer pays premium. The seller receives premium and takes on obligations. Investor.gov's options education notes that option holders can lose the entire premium if the option expires out of the money. ([Investor.gov][8])

## Options mechanics you must understand

| Concept | Meaning | Why it matters |
| --- | --- | --- |
| Call | Right to buy the underlying at strike price | Bullish or hedge-related use |
| Put | Right to sell the underlying at strike price | Bearish or protective use |
| Strike | Price at which option can be exercised | Determines moneyness and payoff |
| Expiry | Date option expires | Controls time decay and event window |
| Premium | Price paid/received for option | Maximum loss for long option buyer |
| Intrinsic value | In-the-money value if exercised now | Real value component |
| Extrinsic value | Time/volatility value above intrinsic | Decays over time |
| Implied volatility | Market-implied expected movement | High IV can make options expensive |
| Delta | Approximate price sensitivity to underlying | Helps choose directional exposure |
| Gamma | Rate of delta change | Matters near expiry and near strike |
| Theta | Time decay | Hurts long options, helps option sellers |
| Vega | Sensitivity to implied volatility | Explains IV expansion/crush impact |
| Open interest | Outstanding contracts | Helps judge liquidity and positioning |
| Bid-ask spread | Execution cost | Wide spreads can destroy edge |

## Buying options positionally

Useful when:

* You expect a fast directional move.
* Volatility is not too expensive.
* Event risk is favorable.
* Risk must be limited to premium paid.
* The strike and expiry match the expected move.
* The option is liquid enough to enter and exit.

Problems:

* Theta decay.
* IV crush.
* Wrong strike selection.
* Low liquidity.
* Wide spreads.
* Direction right but option still loses.
* Stop loss is psychologically ignored because the premium already feels "small."
* Far OTM options require a large move before expiry.

## Long options decision checklist

Before buying a call or put:

```text
[ ] What exact move do I expect?
[ ] By what date should the move happen?
[ ] Is the expected move larger than the premium break-even?
[ ] Is implied volatility already elevated?
[ ] What happens after the event if IV falls?
[ ] Is the strike liquid?
[ ] Is bid-ask spread acceptable?
[ ] Am I buying because the setup is good or because the premium looks cheap?
[ ] What is my exit if the thesis is slow but not fully invalid?
```

## Strike selection

| Strike type | Use | Risk |
| --- | --- | --- |
| ITM option | Higher delta, behaves more like underlying | Higher premium outlay |
| ATM option | Balanced sensitivity and liquidity | Still decays meaningfully |
| Slight OTM option | Lower cost with directional leverage | Needs a stronger move |
| Far OTM option | Cheap premium, lottery-like payoff | Often expires worthless |

For positional trades, avoid choosing strike only by premium affordability. Choose strike based on expected move, probability, liquidity, and time available.

## Expiry selection

Shorter expiry:

* Lower premium.
* Faster theta decay.
* Higher timing pressure.
* More sensitive near event dates.

Longer expiry:

* Higher premium.
* Slower theta decay.
* More time for thesis to work.
* Still vulnerable to IV changes.

If the thesis does not have a clear timing edge, do not force it into a short-dated option.

## Better option structures

For positional trades, consider:

| Structure | Use | Main trade-off |
| --- | --- | --- |
| Debit spread | Directional view with lower cost | Upside capped |
| Bull call spread | Bullish limited-risk trade | Needs move before expiry |
| Bear put spread | Bearish limited-risk trade | Profit capped |
| Covered call | Holding stock, generating premium | Upside capped and assignment possible |
| Protective put | Hedge stock position | Premium drag |
| Collar | Limit downside and upside | Gains capped |
| Calendar spread | Volatility/time structure view | More complex Greeks and expiry risk |
| Long straddle | Expect large move, direction uncertain | Expensive if IV is high |
| Long strangle | Expect large move with lower cost than straddle | Needs even larger move |

## Covered calls and collars for investors

Covered calls and collars are useful only when they match the investment plan.

Covered call:

```text
Own stock
+ sell call option
= collect premium, but cap upside above strike
```

Good when:

* You already own the stock.
* You are willing to sell or reduce above the strike.
* You expect sideways to moderate upside movement.
* Liquidity is good.

Bad when:

* You are strongly bullish.
* Earnings/event can create a sharp upside gap.
* You would regret assignment.

Collar:

```text
Own stock
+ buy put
+ sell call
= reduce downside, reduce or offset hedge cost, cap upside
```

Good when:

* You want to protect gains.
* You have event risk but do not want to sell.
* You accept limited upside during the hedge period.

## Short options warning

Short options can look attractive because premium is received upfront. The risk is that losses can be large, nonlinear, and fast. Margin can increase when volatility rises. Investor.gov's margin material warns that margin accounts can expose investors to losses beyond the amount initially invested and forced sales when requirements are not met. ([Investor.gov][9])

For learning:

* Prefer defined-risk spreads over naked short options.
* Never sell options only because premium looks high.
* Know max loss, margin, assignment/exercise behavior, and exit rules before entry.
* Do not sell options on illiquid contracts.
* Do not treat historical win rate as proof of safety.

## Event trading with options

Options around results, policy decisions, budgets, court rulings, approvals, or global events require a volatility view.

Ask:

```text
What is the market-implied move?
What move do I expect?
Is implied volatility cheap or expensive?
Will IV collapse after the event?
What is my break-even at expiry?
Can I exit before the event if price moves early?
```

If the event is already fully priced in, buying options after IV has expanded can lose money even when the direction is correct.

## Avoid

* Far OTM lottery options.
* Holding weekly options without strong reason.
* Buying options after IV has already exploded.
* Illiquid stock options.
* Entering near expiry with vague thesis.
* Selling naked options without understanding margin and tail risk.
* Treating option premium as a small harmless bet.
* Holding an option only because there is still some premium left.

For positional trading, **stock or futures are often cleaner than naked long options**, unless you specifically understand volatility and time decay.

---

# 23. Timeframe Framework

Use multiple timeframes.

## Recommended structure

| Timeframe       | Purpose                              |
| --------------- | ------------------------------------ |
| Monthly         | Major trend and long-term resistance |
| Weekly          | Positional structure                 |
| Daily           | Entry and trade management           |
| 75-min / 1-hour | Fine-tune entry                      |
| 15-min          | Execution only, not thesis           |

For positional trading, the **weekly chart gives context**, the **daily chart gives setup**, and the **intraday chart gives entry**.

Do not build a positional thesis from a 5-minute chart. Use intraday charts for execution timing, not for the main thesis.

---

# 24. Market Breadth

Breadth tells whether participation is broad or narrow.

Track:

* Advance-decline ratio.
* % stocks above 20 DMA.
* % stocks above 50 DMA.
* New 52-week highs vs lows.
* Sector participation.
* Smallcap/midcap strength.
* Equal-weight index vs market-cap-weighted index.

## Interpretation

| Breadth                        | Meaning               |
| ------------------------------ | --------------------- |
| Strong index + strong breadth  | Healthy rally         |
| Strong index + weak breadth    | Narrow rally, caution |
| Weak index + weak breadth      | Risk-off              |
| Weak index + improving breadth | Possible bottoming    |

---

# 25. Institutional Flow

For Indian positional trading, track:

* FII cash flow.
* DII cash flow.
* FII index futures positioning.
* FII stock futures positioning.
* Mutual fund buying themes.
* Block deals.
* Bulk deals.
* Promoter transactions.
* Insider trades.
* Delivery volume.

Do not blindly follow institutional flow. Institutions can hedge, rebalance, or trade for reasons you do not see.

But consistent buying in a sector can support positional moves.

---

# 26. Delivery Volume

Delivery volume can help identify real accumulation.

High delivery with price rise may suggest stronger buying.

Track:

```text
Delivery percentage
Delivery quantity
Price movement
Volume
Breakout level
```

Good sign:

```text
Price up + volume up + delivery up + breakout
```

Weak sign:

```text
Price up + intraday volume high + delivery low
```

Delivery data is useful, but not perfect. Use it as supporting evidence, not holy scripture.

---

# 27. Liquidity and Execution

A good setup is useless if execution is bad.

## Liquidity checklist

* Tight bid-ask spread.
* High average volume.
* Enough market depth.
* Low impact cost.
* No frequent circuits.
* Options/futures liquid if using derivatives.
* Avoid entering large size in illiquid names.

## Order types

| Order Type          | Use                                  |
| ------------------- | ------------------------------------ |
| Market order        | Fast entry, but slippage risk        |
| Limit order         | Controls price, but may not fill     |
| SL order            | Stop loss trigger                    |
| SL-M order          | Execution certainty, slippage risk   |
| GTT/GTC-like orders | Useful if broker supports            |
| Basket order        | Multi-leg execution                  |
| Iceberg             | Large order slicing, where available |

## For positional trades

Prefer:

* Limit orders near planned levels.
* Avoid chasing opening gaps.
* Avoid illiquid pre-close entries.
* Place stop loss logically.
* Avoid entering before major events unless planned.

---

# 28. Slippage and Transaction Costs

Your backtest and journal must include costs.

Costs include:

* Brokerage.
* STT.
* Exchange transaction charges.
* SEBI charges.
* Stamp duty.
* GST.
* Slippage.
* Spread.
* Impact cost.
* Funding/margin cost.
* Futures rollover cost.
* Options theta decay and IV change.

Professional traders do not ignore costs. A setup that works on a chart can fail in the account after brokerage, taxes, slippage, spreads, theta decay, and rollover costs.

---

# 29. Building a Positional Trading System

You need written rules.

## Strategy template

```text
Strategy Name:
Market:
Universe:
Timeframe:
Trade Direction:
Setup Type:
Entry Rule:
Stop Loss:
Target:
Trailing Rule:
Position Size:
Max Holding Period:
Exit Rule:
Market Regime Filter:
Sector Filter:
Event Filter:
Risk Per Trade:
Max Portfolio Exposure:
Review Metrics:
```

## Full trading plan template

A strategy template describes one setup. A trading plan describes the entire business of trading.

```text
Market:
Instruments:
Timeframe:
Holding period:
Capital:
Maximum risk per trade:
Maximum portfolio risk:
Maximum sector exposure:
Maximum single-position allocation:
Allowed setups:
Disallowed setups:
When to trade aggressively:
When to reduce size:
When to stop trading:
Review frequency:
```

Setup rules:

```text
Setup name:
Market condition required:
Sector condition required:
Stock selection rules:
Entry trigger:
Stop loss rule:
Target rule:
Trailing stop rule:
Exit rule:
Invalidation rule:
```

Risk rules:

```text
Risk per trade:
Maximum open trades:
Maximum daily loss:
Maximum weekly loss:
Maximum monthly drawdown:
When to stop trading:
When to reduce size:
When to increase size:
```

Execution rules:

```text
Order type:
Entry timing:
Stop placement:
Partial profit rule:
Gap handling rule:
News/event handling rule:
```

## Example: Positional breakout strategy

```text
Market:
NSE cash stocks, F&O universe only.

Universe:
Top 300 liquid stocks.

Direction:
Long only.

Market filter:
NIFTY above 50 DMA and 200 DMA.

Sector filter:
Sector index outperforming NIFTY over last 20 trading days.

Stock filter:
Stock above 50 DMA and 200 DMA.
Stock within 10% of 52-week high.
Average daily traded value above threshold.

Setup:
Stock consolidates for at least 20 trading days.
Resistance tested at least twice.
Breakout close above resistance.

Entry:
Buy next day if price sustains above breakout level.

Stop:
Below breakout base or 2 ATR below entry, whichever gives logical invalidation.

Target:
Partial exit at 2R.
Trail remaining below 20 EMA or latest swing low.

Position sizing:
Risk 0.5% of capital.

Exit:
Stop hit, trend breaks, 30-day failure, or thesis invalidation.
```

This is specific. Specific is testable. Vague is where backtests go to become fiction.

---

# 30. Backtesting Positional Strategies

You should backtest before trading real money.

## Backtest must include

* Entry rules.
* Exit rules.
* Stop logic.
* Gap handling.
* Slippage.
* Transaction costs.
* Liquidity filter.
* Corporate actions.
* Survivorship bias control.
* Realistic execution price.
* Position sizing.
* Portfolio-level constraints.
* Holding period.
* Re-entry rules.

## Common backtest mistakes

| Mistake                                     | Why It Is Bad      |
| ------------------------------------------- | ------------------ |
| Using today’s stock universe for past test  | Survivorship bias  |
| Buying at breakout price after close signal | Look-ahead bias    |
| Ignoring gaps                               | Unrealistic        |
| Ignoring costs                              | Overstates returns |
| Ignoring liquidity                          | Fake fills         |
| Optimizing too many parameters              |verfitting        |
| Testing only bull market                    | Fragile            |
| Ignoring delisted stocks                    | Survivorship bias  |
| No walk-forward testing                     | Weak validation    |

## Metrics to track

| Metric                    | Meaning                         |
| ------------------------- | ------------------------------- |
| CAGR                      | Annualized return               |
| Max drawdown              | Worst peak-to-trough fall       |
| Sharpe ratio              | Return per unit volatility      |
| Sortino ratio             | Downside-risk adjusted return   |
| Win rate                  | % winning trades                |
| Avg win / avg loss        | Payoff quality                  |
| Expectancy                | Average expected gain per trade |
| Profit factor             | Gross profit / gross loss       |
| Exposure                  | Time in market                  |
| Turnover                  | Trading frequency               |
| Slippage sensitivity      | Robustness                      |
| Monthly returns           | Consistency                     |
| Longest drawdown duration | Psychological stress            |
| Best/worst trade          | Tail behavior                   |

## Minimum acceptable backtest attitude

Do not ask:

```text
How much profit?
```

Ask:

```text
Where does this fail?
```

That one shift saves careers.

---

# 31. Forward Testing and Paper Trading

After backtest, do forward test.

## Forward test goals

* Check if rules are executable live.
* Check if signals come on time.
* Check slippage.
* Check emotional response.
* Check broker execution.
* Check journal discipline.
* Check alert quality.
* Check real-world missed trades.

## Paper trading period

For positional systems:

```text
Minimum 30-50 trades
or
3-6 months
```

Do not judge from 5 trades. Five trades are noise with a spreadsheet costume.

---

# 32. Journaling System

A trading journal is mandatory.

## Record before trade

```text
Date:
Stock:
Direction:
Entry:
Stop:
Target:
Position size:
Risk amount:
Setup type:
Market regime:
Sector condition:
Trade thesis:
Invalidation:
Expected holding period:
Event risk:
Screenshot:
```

## Record during trade

```text
Price action:
Volume behavior:
News updates:
Stop adjustment:
Partial exits:
Emotional state:
Mistakes:
```

## Record after exit

```text
Exit price:
Profit/loss:
R-multiple:
Holding period:
Did I follow rules?
Was thesis correct?
Was entry good?
Was exit good?
What should improve?
Screenshot after exit:
```

## Grade trades by process, not profit

| Grade | Meaning                    |
| ----- | -------------------------- |
| A     | Followed rules, good setup |
| B     | Minor mistake              |
| C     | Poor execution             |
| D     | Emotional trade            |
| F     | Rule violation             |

A winning F-grade trade is dangerous because it rewards poor process.

---

# 33. Psychology of Positional Trading

Positional trading tests patience.

## Common psychological problems

| Problem         | Result                    |
| --------------- | ------------------------- |
| FOMO            | Late entries              |
| Fear of loss    | Exiting too early         |
| Hope            | Holding losers            |
| Ego             | Refusing invalidation     |
| Recency bias    | Overconfidence after wins |
| Revenge trading | Oversizing after loss     |
| News addiction  | Constant thesis flipping  |
| P&L watching    | Emotional decisions       |

## Positional trader mindset

* You do not need every move.
* You will miss trades.
* You will exit early sometimes.
* You will be wrong often.
* Losses are business expenses.
* Your job is to protect capital.
* One trade means nothing.
* Series of trades matters.
* Process beats prediction.

---

# 34. Building Your Daily Routine

## Pre-market routine

Check:

* Global markets.
* GIFT NIFTY.
* US market close.
* Asian markets.
* Crude oil.
* USDINR.
* Major news.
* Sector news.
* Results calendar.
* Open positions.
* Watchlist alerts.
* Risk exposure.

## During market

For positional traders:

* Do not stare at every tick.
* Check key levels.
* Avoid impulsive entries.
* Update alerts.
* Track volume on breakout candidates.
* Watch index structure.
* Watch sector strength.
* Execute only planned trades.

## Post-market routine

* Review open positions.
* Update stops.
* Scan for setups.
* Study breakout/breakdown stocks.
* Check delivery and volume.
* Read company announcements.
* Update journal.
* Prepare next day plan.

## Weekly routine

* Review weekly charts.
* Review sector rotation.
* Review trade journal.
* Update watchlist.
* Study winners and losers.
* Check market breadth.
* Check earnings calendar.
* Review portfolio exposure.

---

# 35. Information Sources

Use clean sources. Avoid noisy communities that mix rumors, hindsight charts, and undeclared promotion.

## Useful sources

| Source Type                    | Use                         |
| ------------------------------ | --------------------------- |
| Exchange filings               | Official announcements      |
| Company investor presentations | Business updates            |
| Earnings call transcripts      | Management commentary       |
| Annual reports                 | Deep business understanding |
| Screener tools                 | Financial filters           |
| Broker platforms               | Price/volume/OI             |
| NSE/BSE websites               | Corporate announcements     |
| SEBI website                   | Regulatory updates          |
| News portals                   | Event tracking              |
| Sector reports                 | Industry context            |

SEBI’s investor charter covers investor rights, responsibilities, grievance mechanisms, and do’s/don’ts, which is basic but important infrastructure knowledge for anyone operating in Indian markets. ([investor.sebi.gov.in][3])

## Avoid

* Random WhatsApp groups.
* Unverified Telegram tips.
* Influencers showing only wins.
* Paid groups promising guaranteed returns.
* Operators claiming “inside news.”
* Anyone selling certainty.

SEBI’s material on research analysts emphasizes risk disclosure, suitability, conflict disclosure, and avoidance of misleading claims. This is basic hygiene: if a source hides risk and only markets upside, treat it as unsafe. ([investor.sebi.gov.in][4])

## Learning resources

Study categories, not only titles:

| Category | What to learn |
| --- | --- |
| Technical analysis | Trend, structure, breakouts, volume, market cycles |
| Trading psychology | Discipline, patience, loss acceptance, emotional control |
| Market history | Bull markets, bear markets, bubbles, crashes, sector rotations |
| Risk and probability | Expectancy, drawdowns, position sizing, portfolio heat |
| Fundamental analysis | Earnings, valuation, balance sheets, business quality |

Useful books:

* *Market Wizards* by Jack Schwager.
* *How to Make Money in Stocks* by William O'Neil.
* *Technical Analysis of the Financial Markets* by John Murphy.
* *Trading in the Zone* by Mark Douglas.
* *The New Trading for a Living* by Alexander Elder.
* *Reminiscences of a Stock Operator* by Edwin Lefevre.

Do not worship any book. Extract principles, test them, and keep only what survives your own review data.

---

# 36. Legal and Regulatory Awareness

You do not need to become a lawyer, but you should know the boundaries.

## Important points

* Do not trade on insider information.
* Do not spread rumors.
* Do not manipulate prices.
* Do not blindly follow unregistered advisors.
* Understand margin rules.
* Understand tax treatment.
* Keep records.
* Use registered intermediaries.
* Know complaint mechanisms.
* Understand product risk before trading derivatives.

In India, investment advisers and research analysts are regulated categories, and SEBI material describes registration, qualification, disclosure, and conduct expectations for such professionals. ([investor.sebi.gov.in][5])

This matters because tips, rumors, and claims of insider access are not a trading process. They create legal, execution, and behavioral risk without giving you a verified edge.

---

# 37. Tax and Accounting Basics

Do not ignore taxes and charges. A strategy that looks profitable before costs can become weak or negative after brokerage, taxes, slippage, and poor execution.

You should track:

* Trade date.
* Instrument.
* Quantity.
* Buy price.
* Sell price.
* Brokerage.
* Charges.
* STT or applicable market transaction tax.
* Exchange transaction charges.
* GST/taxes.
* Stamp duty.
* Realized P&L.
* Unrealized P&L.
* Short-term capital gains.
* Business income classification, where applicable.
* F&O profit/loss.
* Turnover.
* Audit applicability.
* Advance tax obligations.
* Dividend and corporate action adjustments.

Rules vary by country and change over time. For Indian markets, check current official exchange, SEBI, and tax resources, then use a CA who understands trading taxation if your activity becomes serious. Internet commentary is not a tax system.

---

# 38. Data You Should Track

## Market data

* OHLCV.
* Adjusted price.
* Corporate actions.
* Volume.
* Delivery.
* Futures OI.
* Options chain.
* IV.
* Sector index data.
* Breadth data.
* FII/DII flow.
* News events.
* Earnings dates.

## Trade data

* Entry.
* Exit.
* Stop.
* Quantity.
* Setup type.
* Risk.
* Reward.
* R-multiple.
* Slippage.
* Mistakes.
* Screenshots.
* Thesis.
* Result.

## Portfolio data

* Total capital.
* Exposure.
* Open risk.
* Sector allocation.
* Correlation.
* Drawdown.
* Cash available.
* Margin used.
* Leverage.

---

# 39. Tools to Build

Since you are already building trading systems, you should eventually build these modules.

## Positional trading dashboard

Must show:

* Watchlist.
* Market regime.
* Sector strength.
* Breakout candidates.
* Pullback candidates.
* Open positions.
* Risk per trade.
* Portfolio exposure.
* Upcoming earnings.
* News alerts.
* Stop-loss levels.
* R-multiple status.

## Scanners

Build scanners for:

### Trend scanner

```text
Price > 50 DMA
Price > 200 DMA
50 DMA > 200 DMA
Relative strength improving
Volume above average
```

### Breakout scanner

```text
Close > 20-day high
Volume > 1.5 × 20-day average
Close near high of day
Sector outperforming
```

### Pullback scanner

```text
Stock above 50 DMA
Pullback to 20 EMA or 50 DMA
RSI between 40 and 60
Volume declining on pullback
```

### Weakness scanner

```text
Price below 50 DMA
Price below 200 DMA
Lower high struture
Breakdown on volume
Sector underperforming
```

### Earnings momentum scanner

```text
Sales growth improving
Profit growth improving
Margins expanding
Price near 52-week high
Volume expansion after result
```

---

# 40. Position Management Rules

Once in a trade, your job changes.

Before entry:

```text
Find opportunity.
```

After entry:

```text
Manage risk.
```

## Open trade checklist

Every day ask:

1. Is the thesis still valid?
2. Is price structure intact?
3. Is sector still supportive?
4. Has market regime changed?
5. Is there upcoming event risk?
6. Should stop be moved?
7. Is position too large?
8. Is there better opportunity elsewhere?
9. Am I reacting emotionally?
10. Would I enter this trade today?

The last question is powerful. If the answer is no, you should examine why you are still holding.

---

# 41. Exit Mistakes

## Bad exits

* Exiting because of minor noise.
* Exiting because someone tweeted.
* Holding after stop breaks.
* Moving stop lower.
* Refusing partial profit near major resistance.
* Exiting winners too early and holding losers too long.
* Ignoring sector reversal.
* Ignoring thesis failure.
* Panic exiting during normal pullback.

## Good exits

* Stop hit.
* Target reached.
* Trend breaks.
* Thesis invalidated.
* Better opportunity appears.
* Event risk too high.
* Position becomes too large.
* Market regime turns hostile.
* Trade stagnates beyond time limit.

---

# 42. Drawdown Management

Drawdown is unavoidable.

## Drawdown rules

|         Drawdown | Action                   |
| ---------------: | ------------------------ |
| -2% from capital | Reduce size slightly     |
|              -4% | Stop adding new risk     |
|              -6% | Trade only A+ setups     |
|              -8% | Pause and review         |
|             -10% | Stop trading, full audit |

Adjust numbers based on your risk tolerance, but have rules before damage happens.

## During drawdown

Do not:

* Increase size.
* Change strategy randomly.
* Trade lower-quality setups.
* Blame market.
* Revenge trade.
* Add new indicators desperately.

Do:

* Reduce risk.
* Review journal.
* Check if market regime changed.
* Check execution quality.
* Check if edge is failing.
* Wait for clean setups.

---

# 43. Skill Development Roadmap

## Stage 1: Market literacy

Learn:

* Market structure.
* Order types.
* Cash vs futures vs options.
* Index behavior.
* Sector indices.
* Corporate actions.
* Earnings.
* Basic accounting.
* Risk management.

Goal:

```text
Understand what you are trading.
```

---

## Stage 2: Chart reading

Learn:

* Trend.
* Support/resistance.
* Breakouts.
* Pullbacks.
* Volume.
* Moving averages.
* Relative strength.
* ATR.
* Multi-timeframe analysis.

Goal:

```text
Read price without indicator addiction.
```

---

## Stage 3: Fundamental context

Learn:

* Financial statements.
* Revenue/profit growth.
* Margins.
* Debt.
* Cash flow.
* Valuation.
* Sector drivers.
* Earnings quality.
* Management commentary.

Goal:

```text
Know whether price move has business support.
```

---

## Stage 4: Strategy building

Learn:

* Define setups.
* Write rules.
* Backtest.
* Forward test.
* Measure expectancy.
* Track failure modes.
* Avoid overfitting.

Goal:

```text
Trade repeatable setups, not impulse.
```

---

## Stage 5: Risk and portfolio control

Learn:

* Position sizing.
* Portfolio exposure.
* Correlation.
* Drawdown control.
* Gap risk.
* Leverage control.
* Hedging basics.

Goal:

```text
Stay alive long enough for edge to matter.
```

---

## Stage 6: Professional execution

Learn:

* Entry planning.
* Stop placement.
* Order execution.
* Slippage control.
* Partial exits.
* Scaling.
* Journaling.
* Review loop.

Goal:

```text
Reduce avoidable mistakes.
```

---

## Stage 7: Advanced trading

Learn:

* Factor investing.
* Momentum models.
* Earnings drift.
* Sector rotation systems.
* Event-driven trading.
* Options structures.
* Volatility analysis.
* Regime models.
* Portfolio optimization.

Goal:

```text
Develop durable edge.
```

---

# 44. Advanced Concepts Worth Knowing

These may not matter immediately, but you should understand them.

## 1. Post-earnings announcement drift

Sometimes stocks continue moving in the direction of earnings surprise for days or weeks.

Use:

* Result surprise.
* Gap direction.
* Volume.
* Analyst revisions.
* Follow-through.

## 2. Relative momentum

Stocks that outperform often continue outperforming for some time.

Use:

* 3-month returns.
* 6-month returns.
* Relative strength line.
* Sector strength.

## 3. Volatility contraction

Big moves often come after quiet periods.

Look for:

* Narrow range.
* Bollinger Band contraction.
* ATR compression.
* Low volume consolidation.
* Breakout trigger.

## 4. Anchored VWAP

Useful from:

* Earnings day.
* Major breakout.
* Budget day.
* Election result.
* Major gap.
* All-time high breakout.

If price respects anchored VWAP, institutions may be active around that level.

## 5. Volume profile

Helps identify:

* High-volume zones.
* Low-volume gaps.
* Supply/demand areas.
* Acceptance/rejection levels.

## 6. Market profile

Useful but not mandatory.

Focuses on:

* Value area.
* Auction behavior.
* Balance vs imbalance.
* Acceptance vs rejection.

Do not start here. Market profile is useful later, after core trend, risk, execution, and review skills are stable.

---

# 45. Common Positional Setups

Every setup below must still pass the same execution test:

```text
Market regime -> sector strength -> stock quality -> setup -> entry -> stop -> size -> exit
```

The pattern alone is not enough. The reason these setups work is usually one of four mechanisms:

* **Supply absorption**: sellers at a level get exhausted.
* **Institutional accumulation**: larger buyers keep supporting pullbacks.
* **Positioning pressure**: trapped longs/shorts are forced to exit.
* **Earnings or narrative re-rating**: market changes what it is willing to pay.

## Setup 1: 52-week high breakout

Rules:

```text
Stock near 52-week high.
Sector strong.
Market supportive.
Consolidation before breakout.
Breakout with volume.
Stop below breakout base.
Trail with 20 EMA or swing low.
```

Why it works:

Strong stocks making new highs often attract institutional momentum.

---

## Setup 2: Earnings breakout

Rules:

```text
Strong results.
Gap up or strong close.
Volume expansion.
Stock holds earnings-day low.
Enter on consolidation breakout or retest.
Stop below earnings-day low.
```

Why it works:

Earnings can trigger re-rating. A strong result matters most when the market was not already fully pricing it in and the stock holds the event-day low. Good results with weak price action are a warning because markets trade expectations, not press-release adjectives.

---

## Setup 3: Sector leader pullback

Rules:

```text
Sector in uptrend.
Stock is leader.
Pullback to 20/50 DMA.
Volume dries up.
Bullish reversal.
Enter above reversal high.
Stop below pullback low.
```

Why it works:

Institutions often buy leaders on dips.

Avoid when:

```text
Market regime is bearish.
Pullback has heavy selling volume.
Stock breaks the prior swing low.
Sector loses relative strength.
```

---

## Setup 4: Base breakout

Rules:

```text
Stock moves sideways for 6-12 weeks.
Volatility contracts.
Resistance clear.
Volume low inside base.
Breakout with volume.
Stop below base midpoint or breakout level.
```

Why it works:

Long consolidation can create energy for expansion.

Cleaner version:

```text
Base lasts at least 3-8 weeks.
Resistance is obvious.
Volume dries inside the base.
Price stays near highs instead of collapsing.
Breakout closes above resistance.
Breakout volume is at least 1.5x-2x average volume.
```

---

## Setup 5: Breakout retest

Rules:

```text
Stock breaks above resistance.
Price pulls back to old resistance.
Old resistance acts as support.
Pullback volume is controlled.
Market is not breaking down.
Enter on bounce from retest or break above previous day's high.
Stop below retest low.
```

Why it works:

The retest checks whether the breakout level has changed from supply to demand. It often gives better risk-reward than chasing the first breakout candle.

---

## Setup 6: Failed breakdown reversal

Rules:

```text
Stock breaks support.
Quickly recovers.
Closes back inside range.
Volume high.
Shorts trapped.
Enter above reclaim level.
Stop below failed breakdown low.
```

Why it works:

Trapped sellers can fuel reversal.

---

## Setup 7: Weak stock breakdown

Rules:

```text
Stock below 50/200 DMA.
Sector weak.
Lower highs.
Support breaks with volume.
Enter short via futures/options if liquid.
Stop above breakdown level.
```

Why it works:

Weak stocks can continue lower in hostile regimes.

---

## Setup 8: Reversal from accumulation

Rules:

```text
Stock had a major decline.
Selling pressure reduces.
Price stops making lower lows.
Higher lows begin to form.
Volume improves on up days.
Price reclaims 50 DMA first, then 200 DMA later.
Fundamentals, sector conditions, or news flow begin improving.
Enter on base breakout, higher low, or trendline break.
Stop below base low or recent swing low.
```

Why it works:

Reversals work when the old sellers are mostly exhausted and new buyers begin accepting higher prices. They fail often, so confirmation matters more than catching the exact bottom.

---

## Setup 9: Event-driven positional trade

Rules:

```text
Clear catalyst exists.
Price confirms with volume.
Market reaction is strong.
Risk is definable.
Enter after confirmation, not before guessing.
Use event candle low or post-event consolidation as invalidation.
Exit if price fills the event gap or momentum fades.
```

Why it works:

Events can change earnings expectations, valuation multiples, or positioning quickly. The trade should be based on market reaction plus risk control, not only on whether the headline sounds good.

---

# 46. Trading Plans by Market Condition

## Bull market

Prefer:

* Breakouts.
* Pullbacks in leaders.
* Earnings momentum.
* Sector rotation.
* Pyramiding winners.

Avoid:

* Shorting strong stocks.
* Overpaying for extended names.
* Ignoring risk because everything rises.

## Bear market

Prefer:

* Cash.
* Smaller size.
* Shorts in weak stocks.
* Hedged trades.
* Quick profit booking.
* Defensive sectors.

Avoid:

* Buying every dip.
* Averaging down.
* Assuming “quality stock” cannot fall.

## Sideways market

Prefer:

* Range trades.
* Mean reversionSmaller targets.
* Partial booking.
* Selective breakouts only.

Avoid:

* Chasing every breakout.
* Oversizing.
* Expecting smooth trends.

## High-volatility market

Prefer:

* Reduced size.
* Wider stops.
* More cash.
* Event awareness.
* Hedging.

Avoid:

* Tight stops.
* Leveraged overnight trades.
* Illiquid options.

---

# 47. How To Combine Technicals, Fundamentals, and News

Best positional trades usually have alignment.

## Strongest setup

```text
Market supportive
+ sector strong
+ stock strong
+ fundamental trigger
+ technical breakout
+ volume confirmation
+ clear risk level
```

## Medium setup

```text
Technical setup
+ sector support
+ no fundamental red flags
```

## Weak setup

```text
Only indicator signal
+ no sector support
+ no thesis
+ bad risk-reward
```

The more independent evidence you have, the better. But do not wait for perfection. Perfect setups are usually visible only in screenshots after the move.

---

# 48. Risk-Reward Framework

Minimum risk-reward:

```text
1:2 or better
```

Meaning:

```text
Risk ₹1 to make at least ₹2
```

But do not blindly use fixed targets.

A 1:2 trade into major resistance is bad.
A 1:1.5 trade with very high probability may be acceptable.
A trend trade with trailing stop may produce 3R, 5R, or more.

## Think in expectancy

A system can work with:

```text
40% win rate
Average win = 3R
Average loss = 1R
```

Expectancy:

```text
(0.40 × 3R) - (0.60 × 1R) = 0.60R
```

That means average profit is 0.60R per trade before costs.

---

# 49. What To Avoid

Avoid:

* Trading without stop loss.
* Trading illiquid stocks.
* Buying after huge vertical moves.
* Averaging down blindly.
* Holding through earnings without plan.
* Taking oversized futures positions.
* Buying far OTM options.
* Following tips.
* Changing rules after every loss.
* Over-optimizing backtests.
* Ignoring market regime.
* Confusing news with edge.
* Holding losers as “investments.”
* Trading because bored.
* Watching P&L every 10 minutes.
* Believing one indicator can solve life.


# 50. Your Professional Positional Trader Checklist

Before entering:

```text
[ ] Is market regime supportive?
[ ] Is sector strong?
[ ] Is stock liquid?
[ ] Is stock showing relative strength?
[ ] Is there a clear setup?
[ ] Is there a clear thesis?
[ ] Is there a defined invalidation level?
[ ] Is risk-reward acceptable?
[ ] Is position size calculated?
[ ] Is event risk checked?
[ ] Is stop loss planned?
[ ] Is exit plan defined?
[ ] Is portfolio exposure acceptable?
[ ] Is this trade in my playbook?
```

During trade:

```text
[ ] Is thesis still valid?
[ ] Is price structure intact?
[ ] Is volume confirming?
[ ] Has sector changed?
[ ] Has market regime changed?
[ ] Should stop be trailed?
[ ] Is risk still acceptable?
[ ] Am I following rules?
```

After trade:

```text
[ ] Did I follow my plan?
[ ] Was entry valid?
[ ] Was stop logical?
[ ] Was exit disciplined?
[ ] What was R-multiple?
[ ] What mistake occurred?
[ ] What should be improved?
```

---

# 51. The Training Plan

## Simple 90-day action plan

This is the practical beginner-to-serious-trader path. Judge progress by discipline and evidence, not by one lucky trade.

| Days | Focus | Concrete task |
| --- | --- | --- |
| 1-15 | Foundation | Learn trend, support/resistance, volume, moving averages, ATR, and risk per trade. Study 100 charts manually. |
| 16-30 | Watchlist | Build a 100-200 stock liquid watchlist, divide by sector, mark leaders and 52-week high candidates. |
| 31-45 | Playbook | Write exact rules for two setups: base breakout and trend pullback. Include entry, stop, target, trailing, invalidation. |
| 46-60 | Manual backtesting | Test at least 50 breakout trades and 50 pullback trades. Record R-multiple, drawdown, and mistakes. |
| 61-75 | Paper trading | Take only valid setups, record real-time entries, include slippage, and review every weekend. |
| 76-90 | Small live trading | Risk only 0.25% to 0.5% per trade. Take limited trades and grade execution quality, not profit. |

At the end of 90 days, answer:

```text
Did I follow written setups?
Did I size every trade correctly?
Did I keep a journal?
Did I avoid random tips?
Did I respect stops?
Do I have evidence of positive expectancy?
What market regime did I test in?
What mistakes repeated?
```

If the answer is weak, repeat the cycle with smaller size. Scaling comes from data, not impatience.

---

## Month 1: Foundation

Study:

* Trend.
* Support/resistance.
* Volume.
* Moving averages.
* ATR.
* Position sizing.
* Basic fundamentals.

Task:

```text
Create a watchlist of 100 liquid stocks.
Review weekly and daily charts.
Mark major levels manually.
```

---

## Month 2: Setup building

Pick two setups only:

```text
1. Breakout
2. Pullback
```

For each setup, define:

* Entry.
* Stop.
* Target.
* Filter.
* Risk.
* Exit.

Task:

```text
Collect 50 historical examples of each setup.
Study winners and failures.
```

---

## Month 3: Backtesting

Build simple backtests.

Track:

* Win rate.
* Average win.
* Average loss.
* Drawdown.
* Profit factor.
* Expectancy.
* Slippage impact.

Task:

```text
Reject weak setups.
Keep only setups with logical edge and manageable drawdown.
```

---

## Month 4: Paper trading

Trade your rules without money.

Task:

```text
Take 30-50 paper trades.
Journal everything.
Compare live behavior vs backtest.
```

---

## Month 5: Small capital live trading

Use tiny risk.

```text
Risk 0.25% per trade.
No leverage abuse.
No averaging down.
No options lottery trades.
```

Task:

```text
Prove discipline, not profit.
```

---

## Month 6+: Scale slowly

Increase size only if:

* Rules are stable.
* Journal is clean.
* Drawdown controlled.
* Execution reliable.
* You are not emotionally unstable after losses.
* System performs across different market conditions.

---

# 52. The Professional Mindset

A pro positional trader does not need to predict everything.

They need to:

* Find asymmetric opportunities.
* Control downside.
* Let winners work.
* Cut invalid trades.
* Avoid low-quality setups.
* Keep records.
* Improve continuously.
* Survive bad periods.
* Scale only proven behavior.

Your goal is not to be right.

Your goal is to make money when right, lose small when wrong, and avoid any single decision that can damage your capital beyond recovery.

---

# 53. Simple Final Model

Use this as your master framework:

```text
Market Regime:
Should I be aggressive, defensive, or inactive?

Sector:
Where is money flowing?

Stock:
Which names show strength, liquidity, and clean structure?

Thesis:
Why should this move continue?

Setup:
What exact pattern allows entry?

Risk:
Where am I wrong and how much can I lose?

Execution:
How do I enter without chasing?

Management:
How do I trail, add, reduce, or exit?

Review:
What did this trade teach me?
```

That is the skeleton of professional positional trading.

Not prediction.
Not tips.
Not indicator worship.
A repeatable decision system with risk control.

[1]: https://investor.sebi.gov.in/securities-risks_trade_derivatives.html "Key Risks in Investing in Securities Market"
[2]: https://www.nseclearing.in/risk-management/equity-derivatives/margins "Margins | NSE Clearing Limited"
[3]: https://investor.sebi.gov.in/Investor-charter.html "Investor Charter of SEBI"
[4]: https://investor.sebi.gov.in/research_analyst.html "Understanding Research Analysts"
[5]: https://investor.sebi.gov.in/investment_advisor.html "Understanding Investment Advisors"
[6]: https://investor.sebi.gov.in/understanding_derivatives.html "Understanding derivatives"
[7]: https://www.nseindia.com/static/products-services/equity-derivatives-contract-specifications "Equity derivatives contract specifications"
[8]: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-63 "Investor Bulletin: An Introduction to Options"
[9]: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-29 "Investor Bulletin: Understanding Margin Accounts"
[10]: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/FuturesMarketBasics/index.htm "Basics of Futures Trading"
[11]: https://www.sebi.gov.in/media-and-notifications/press-releases/sep-2024/updated-sebi-study-reveals-93-of-individual-traders-incurred-losses-in-equity-fando-between-fy22-and-fy24-aggregate-losses-exceed-1-8-lakh-crores-over-three-years_86906.html "SEBI study on individual equity F&O trader losses"
