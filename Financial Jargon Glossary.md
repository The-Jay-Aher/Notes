# Financial Jargon Glossary

## Quick Summary

This note explains common finance, stock market, futures, options, commodities, macro, and trading terms in simple language. It is meant for someone who knows the basics but gets confused when traders say things like "short covering", "rollover", "IV crush", "basis", "OI buildup", "support broke", "margin call", or "risk-off".

Use this as a lookup reference while reading market news, broker reports, trading commentary, annual reports, charts, and derivatives data. The explanations are educational, not financial advice.

Related notes:

- [Fundamental Analysis](Fundamental%20Analysis.md)
- [Positional Trader](Positional%20Trader.md)
- [Probabilistic Trading Guide](Probabilistic%20Trading%20Guide.md)

## Institutional operating boundary

This glossary teaches language. Language is not edge. A trading term is useful only when it is connected to a mechanism, measurable data, and a decision.

Use this conversion rule:

```text
Jargon -> mechanism -> measurable variable -> trading consequence -> risk if wrong
```

Examples:

| Term | Mechanism | What to measure | Trading consequence |
| --- | --- | --- | --- |
| Breakout | Price accepts above prior supply | Close, volume, base length, retest | Possible continuation only if risk/reward is valid |
| Short covering | Short sellers buy back positions | Price up, OI down, volume high | Move may fade if fresh buying does not follow |
| IV crush | Implied volatility falls after uncertainty resolves | IV before/after event, option premium | Long options can lose despite correct direction |
| Liquidity | Ability to enter and exit cleanly | Spread, depth, traded value | Position size must fit exit capacity |

If a term cannot be connected to a trade rule or risk rule, treat it as background knowledge.

See also:

- [Misunderstanding Register](misunderstanding_register.md)
- [Trading Notes Audit Report](trading_notes_audit_report.md)

## How To Read Market Jargon

Market words usually answer one of these questions:

| Question | Example jargon |
| --- | --- |
| What is being traded? | Stock, future, option, commodity, ETF, index |
| What is the trader doing? | Long, short, hedge, average, square off, rollover |
| What is happening to price? | Breakout, breakdown, gap up, rally, correction |
| What is happening to positioning? | Long buildup, short buildup, short covering, unwinding |
| What is the risk? | Margin, drawdown, volatility, leverage, liquidity risk |
| What is the valuation? | PE, PB, EV/EBITDA, DCF, margin of safety |
| What is the macro backdrop? | Inflation, interest rates, yield, liquidity, risk-on |

If a word sounds complicated, translate it into this simpler format:

```text
Who is buying or selling?
What instrument are they using?
Is leverage involved?
What happens if price moves against them?
What is the time limit?
```

---

# 1. Basic Market Terms

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Financial market | A place where financial assets are bought and sold | Stock exchanges, commodity exchanges, bond markets, currency markets, and derivatives markets are all financial markets. They help buyers and sellers meet and discover prices. |
| Asset | Something with economic value | Stocks, bonds, commodities, cash, real estate, mutual funds, ETFs, futures, and options are assets or asset-linked instruments. |
| Security | A tradable financial instrument | Stocks, bonds, debentures, ETFs, and some derivatives are securities. In simple terms, it is an instrument that represents ownership, debt, or a financial claim. |
| Stock / share / equity | Ownership in a company | If you own shares, you own a small part of the company. Your return can come from price appreciation, dividends, buybacks, or corporate actions. |
| Equity market | Market where company shares are traded | In India, NSE and BSE are major equity exchanges. Equity prices move based on earnings, valuation, liquidity, sentiment, and macro conditions. |
| Exchange | Organized marketplace for trading | NSE, BSE, MCX, NYSE, and Nasdaq are examples. Exchanges provide standardized rules, trading systems, settlement, and market data. |
| Broker | Intermediary that lets you trade | A broker provides the trading account, order placement, margin facility, reports, and access to exchanges. |
| Demat account | Account that stores shares electronically | Shares are no longer held as paper certificates. A demat account stores ownership records electronically. |
| Trading account | Account used to place buy/sell orders | The trading account connects to the broker and exchange. The demat account holds securities; the trading account sends orders. |
| Index | A basket that tracks a market segment | NIFTY 50 tracks 50 large Indian companies. BANKNIFTY tracks major banking stocks. An index is not a stock; it is a calculated value based on its constituents. |
| Constituent | A member stock inside an index | If Reliance is part of NIFTY 50, it is a constituent of that index. Index movement depends on constituent weights. |
| Weight | Importance of one stock inside an index | A 10% weight means that stock has a bigger effect on the index than a 1% weight stock. |
| Market capitalization | Company value based on stock price | Formula: share price x total shares outstanding. A company with Rs 1,000 price and 10 crore shares has Rs 10,000 crore market cap. |
| Free float | Shares available for public trading | Promoter or government holdings may not trade regularly. Free-float market cap focuses on shares available to ordinary market participants. |
| Large cap | Large, established company by market value | Large caps are usually more liquid and institutionally owned, but they can still fall sharply. |
| Mid cap | Medium-sized listed company | Mid caps can grow faster than large caps but usually have more volatility and liquidity risk. |
| Small cap | Smaller listed company | Small caps can offer high growth but can also have weak liquidity, governance risk, and large drawdowns. |
| Blue chip | Large, reputed, established company | Usually refers to market leaders with long operating histories. Blue chip does not mean risk-free. |
| Penny stock | Very low-priced stock | Low price does not automatically mean cheap. Many penny stocks are illiquid, manipulated, or financially weak. |
| Liquidity | Ease of buying/selling without moving price much | High liquidity means tight spreads and good volume. Low liquidity means you may not get a fair exit when needed. |
| Volume | Number of shares/contracts traded | High volume shows activity. It does not automatically prove smart money buying or selling. |
| Turnover | Total traded value | Formula: price x traded quantity. A stock can have high volume but low turnover if price is very low. |
| Bid | Highest price buyers are offering | If bid is Rs 100, someone is currently willing to buy at Rs 100. |
| Ask / offer | Lowest price sellers are asking | If ask is Rs 101, someone is currently willing to sell at Rs 101. |
| Bid-ask spread | Difference between ask and bid | If bid is Rs 100 and ask is Rs 101, spread is Rs 1. Wide spreads increase trading cost. |
| LTP | Last traded price | The price at which the most recent trade happened. It may not equal the price available for your order. |
| OHLC | Open, high, low, close | A candle or bar usually contains these four prices for a time period. |
| Open price | First traded price of a session or candle | The market open can gap away from the previous close due to overnight news. |
| Close price | Final traded or settlement price of a session | Many indicators and reports use closing price because it summarizes the day. |
| High | Highest traded price in a period | Shows the top price reached during that candle/day/session. |
| Low | Lowest traded price in a period | Shows the bottom price reached during that candle/day/session. |
| CMP | Current market price | The price currently visible in the market. It changes continuously during trading hours. |
| Previous close | Last session's closing price | Used to calculate daily change and gap up/down. |
| Market depth | List of current bids and asks | Shows visible demand and supply near the current price. It can change quickly and can be misleading in illiquid stocks. |
| Circuit limit | Exchange-defined daily price movement limit | If a stock hits upper or lower circuit, trading may be restricted. This is common in less liquid stocks. |
| Upper circuit | Maximum allowed price rise for the day | Buyers may be present but sellers may disappear. You may not be able to buy. |
| Lower circuit | Maximum allowed price fall for the day | Sellers may be present but buyers may disappear. You may not be able to exit easily. |
| Trading halt | Temporary stop in trading | Can happen due to news, volatility, technical issues, or regulatory action. |
| Settlement | Final exchange of securities and funds | After a trade, shares and money are transferred through clearing and settlement systems. |
| T+1 / T+2 | Settlement after trade date plus days | T+1 means settlement happens one business day after trade date. Exact rules depend on market and instrument. |
| Delivery | Taking shares into demat account | In cash equity, delivery means you own the shares after settlement instead of closing intraday. |
| Intraday | Trade opened and closed on same day | Intraday traders do not carry the position overnight. |
| Positional trade | Trade held for days to months | Positional traders carry overnight risk and usually use wider stops than intraday traders. |
| Investment | Position held based on long-term value | Investing focuses more on business quality, valuation, and compounding than short-term chart movement. |
| Speculation | Taking risk based on expected price movement | Speculation is not automatically bad, but it must be sized and managed carefully. |
| Arbitrage | Trying to profit from price differences | Example: buying an asset cheaper in one market and selling higher in another, after costs. |

---

# 2. Price Movement And Market Direction

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Bullish | Expecting price to rise | A bullish trader wants upside. Bullish does not mean price will definitely rise. |
| Bearish | Expecting price to fall | A bearish trader expects downside or weakness. |
| Bull market | Long period of rising prices | Usually marked by higher highs, broad participation, optimism, and strong liquidity. |
| Bear market | Long period of falling prices | Usually marked by lower highs, weak breadth, fear, and large drawdowns. |
| Rally | Strong upward move | A rally can happen inside a bull market or as a temporary bounce inside a bear market. |
| Sell-off | Sharp downward move | Often caused by bad news, panic, weak global cues, margin pressure, or institutional selling. |
| Correction | Meaningful decline after a rise | Often used for a 10% or similar fall from recent highs, but exact usage varies. |
| Crash | Sudden severe fall | Usually driven by panic, liquidity shock, systemic risk, or major unexpected news. |
| Pullback | Temporary fall inside an uptrend | A pullback can be healthy if the larger trend remains intact. |
| Bounce | Short-term rise after a fall | A bounce may be a reversal or only a temporary relief move. |
| Dead cat bounce | Weak temporary bounce in a downtrend | It looks like recovery but the larger trend remains bearish. |
| Reversal | Trend changes direction | Example: price stops making lower lows and starts making higher highs. |
| Continuation | Trend resumes after pause | Example: a stock consolidates and then continues upward. |
| Consolidation | Sideways price movement | Buyers and sellers are balanced. Big moves often start after consolidation breaks. |
| Range-bound | Price stuck between support and resistance | Traders may buy near support and sell near resistance until the range breaks. |
| Breakout | Price moves above resistance | A breakout suggests buyers overcame sellers at a key level. It needs volume and follow-through for quality. |
| Breakdown | Price moves below support | A breakdown suggests sellers overcame buyers at a key level. |
| False breakout | Breakout that quickly fails | Traders who bought the breakout get trapped, and price returns below resistance. |
| False breakdown | Breakdown that quickly fails | Sellers get trapped, and price moves back above support. |
| Trap | Move that catches traders on wrong side | Bull trap catches buyers; bear trap catches sellers. |
| Bull trap | Price looks bullish but reverses down | Often happens after a failed breakout. |
| Bear trap | Price looks bearish but reverses up | Often happens after a failed breakdown. |
| Gap up | Opens above previous close | Can happen due to overnight news, strong global cues, results, or sentiment. |
| Gap down | Opens below previous close | Can happen due to bad news, weak global markets, or panic selling. |
| Gap fill | Price revisits the gap area | Traders say "gap filled" when price returns to the prior gap zone. |
| Momentum | Strength and speed of price movement | Strong momentum means price keeps moving in one direction with force. |
| Trend | Persistent price direction | Uptrend has higher highs/higher lows. Downtrend has lower highs/lower lows. |
| Uptrend | Price generally moving upward | Buyers are in control until structure breaks. |
| Downtrend | Price generally moving downward | Sellers are in control until structure improves. |
| Sideways trend | No clear direction | Price moves in a range. Strategies should change because trend-following can fail. |
| Higher high | New peak above previous peak | Supports an uptrend. |
| Higher low | Pullback low above previous low | Shows buyers are stepping in earlier. |
| Lower high | Bounce high below previous high | Shows sellers are appearing earlier. |
| Lower low | New low below previous low | Supports a downtrend. |
| Support | Price area where buying may appear | Support is not a guarantee. It is a zone where demand previously overcame supply. |
| Resistance | Price area where selling may appear | Resistance is a zone where supply previously overcame demand. |
| Demand zone | Area where buyers previously entered strongly | Often near previous consolidation or reversal areas. |
| Supply zone | Area where sellers previously entered strongly | Often near previous distribution or rejection areas. |
| All-time high | Highest price ever reached | Stocks at all-time highs may have strong momentum because there is little overhead supply. |
| 52-week high | Highest price in last 52 weeks | Often watched by momentum traders. |
| 52-week low | Lowest price in last 52 weeks | Can signal weakness, distress, or value opportunity depending on context. |
| Overbought | Price has risen sharply by an indicator measure | Overbought does not mean immediate fall. Strong stocks can stay overbought. |
| Oversold | Price has fallen sharply by an indicator measure | Oversold does not mean immediate rise. Weak stocks can stay oversold. |
| Mean reversion | Price returns toward average | Works better in range-bound markets than strong trends. |
| Trend following | Trading in direction of established trend | The idea is to ride winners and exit when trend weakens. |
| Relative strength | One asset outperforming another | If a stock rises while the index is flat, it shows relative strength. |
| Relative weakness | One asset underperforming another | If a stock falls while the index rises, it shows weakness. |
| Market breadth | How many stocks participate in a move | If index rises but most stocks fall, breadth is weak. |
| Advance-decline ratio | Advancing stocks vs declining stocks | A simple breadth measure. More advancers means broader strength. |
| Risk-on | Market prefers risky assets | Stocks, high beta names, commodities, and growth assets often do better. |
| Risk-off | Market avoids risky assets | Investors prefer cash, government bonds, defensive stocks, or safe havens. |

---

# 3. Orders, Execution, And Brokerage Terms

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Order | Instruction to buy or sell | An order tells the broker what instrument, quantity, side, and price condition you want. |
| Market order | Buy/sell immediately at best available price | Fast execution but price can slip, especially in illiquid instruments. |
| Limit order | Buy/sell only at specified price or better | Gives price control but may not execute if market does not reach the price. |
| Stop-loss order | Order used to exit if price moves against you | Helps control risk. It can still slip in fast markets. |
| Stop-loss market | Trigger creates a market order | More likely to exit, but final price may be worse than expected. |
| Stop-loss limit | Trigger creates a limit order | Controls worst execution price but may not fill if price moves too fast. |
| Trigger price | Price that activates a stop order | Example: if trigger is Rs 95, the stop order activates when market reaches Rs 95. |
| Target order | Order to book profit at planned level | A target is where you plan to exit with profit. |
| Bracket order | Entry with stop and target attached | Some brokers provide bracket-style orders, subject to product availability and regulation. |
| Cover order | Entry order with compulsory stop-loss | Designed to reduce risk but does not remove gap risk. |
| GTT / Good Till Triggered | Standing trigger order | Useful for longer-term stop/target planning, depending on broker support. |
| IOC | Immediate or cancel | Executes immediately for available quantity and cancels the rest. |
| Day order | Valid only for that trading day | If not executed by market close, it expires. |
| AMO | After-market order | Order placed after market hours for next session, depending on broker rules. |
| Slippage | Difference between expected and actual execution price | If stop was Rs 100 but exit happened at Rs 98, slippage is Rs 2. |
| Brokerage | Fee charged by broker | Total trading cost also includes taxes, exchange fees, STT/CTT, stamp duty, GST, and other charges depending on market. |
| STT | Securities Transaction Tax | Tax on securities transactions in India. Applies differently across delivery, intraday, futures, and options. |
| CTT | Commodities Transaction Tax | Similar transaction tax for certain commodity derivative trades in India. |
| Stamp duty | Duty charged on transactions | Usually charged on buy-side in Indian markets, subject to rules. |
| Exchange transaction charge | Fee charged by exchange | Part of trading cost. Higher turnover means higher cost. |
| Impact cost | Cost caused by your own order moving price | Large orders in illiquid markets can push price against you. |
| Fill | Executed portion of an order | If you place order for 1,000 shares and only 400 execute, you have a partial fill. |
| Partial fill | Only part of order executed | Common in illiquid instruments or large orders. |
| Square off | Close an open position | If you bought first, you square off by selling. If you shorted first, you square off by buying back. |
| Exit | Close a trade | Exit can happen through stop loss, target, manual decision, expiry, or assignment/exercise in derivatives. |
| Pledge | Use securities as collateral | Brokers may allow pledging shares to get margin. Pledged securities still carry market risk. |
| Margin | Money/collateral required to take a position | Margin is not the maximum loss. It is only the capital blocked to support the position. |
| Margin call | Demand to add funds/collateral | Happens when losses or margin changes make available funds insufficient. |
| Auto square-off | Broker closes position automatically | Can happen near market close, margin shortfall, or risk limits. It may not happen at a good price. |
| RMS | Risk management system | Broker/exchange risk checks that block or square off risky orders. |
| Freeze quantity | Maximum quantity allowed in one order | Exchanges may define order quantity limits for risk control. |
| Auction | Process to settle short delivery | If a seller fails to deliver shares, exchange auction mechanism may be used. |
| Short delivery | Seller fails to deliver shares | Can lead to auction penalty and settlement complications. |

---

# 4. Long, Short, And Positioning Terms

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Long position | You benefit if price rises | Buying stock is a long position. Buying a call is also bullish, but payoff is different. |
| Short position | You benefit if price falls | You sell first and plan to buy back lower. Shorting has different rules and risks by market/instrument. |
| Short selling | Selling something you do not own | In cash equity, rules are strict and delivery matters. In futures, shorting is easier because futures are contracts. |
| Cover | Close a short position by buying back | If you shorted at Rs 100 and buy back at Rs 90, you made Rs 10 before costs. |
| Short covering | Short sellers buying back to close shorts | This is often what people mean when they say "short coverup." If many short sellers rush to buy back, price can rise sharply even without fresh bullish buying. |
| Short squeeze | Forced rapid short covering | A sharp rise pressures short sellers. Their buying to cover pushes price even higher. |
| Long buildup | Price rises and open interest rises | Suggests new long positions are being created in futures/options. |
| Short buildup | Price falls and open interest rises | Suggests new short positions are being created. |
| Long unwinding | Price falls and open interest falls | Long traders are exiting. It is not necessarily fresh shorting. |
| Short covering in OI data | Price rises and open interest falls | Short positions are being closed. Price rises because shorts buy back. |
| Fresh buying | New buyers entering | Usually price and volume rise. In derivatives, OI may also rise. |
| Fresh selling | New sellers entering | Usually price falls with volume. In derivatives, OI may rise if new shorts are added. |
| Profit booking | Selling to lock in gains | Price may fall even if the long-term thesis remains intact. |
| Panic selling | Selling driven by fear | Often happens during crashes, bad news, margin pressure, or liquidity stress. |
| Accumulation | Gradual buying over time | Often used when strong hands build positions without pushing price too much. |
| Distribution | Gradual selling over time | Often used when large holders sell into strength. |
| Operator activity | Suspected manipulation by large players | This term is used loosely. Do not use it as a substitute for evidence. |
| Smart money | Supposedly informed institutions/pros | Often used in commentary, but not every large trade is intelligent or informed. |
| Weak hands | Traders likely to exit quickly | Usually refers to leveraged or emotional participants. |
| Strong hands | Holders with conviction or deeper capital | They can tolerate volatility better than weak hands. |
| Crowded trade | Too many participants on same side | Crowded trades can reverse violently when everyone tries to exit together. |
| Contrarian trade | Going against popular view | Can work if consensus is wrong, but being opposite is not edge by itself. |
| Consensus | Common market expectation | If everyone expects good results, the stock may need excellent results to rise. |
| Positioning | How traders are already placed | Price reaction depends not only on news, but also on whether participants were already long or short. |

---

# 5. Stocks, Ownership, And Corporate Actions

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Face value | Nominal value assigned to a share | Used for dividend percentage and accounting. Market price can be far above face value. |
| Book value | Net assets per share | Roughly assets minus liabilities divided by shares. More useful for banks and asset-heavy firms. |
| Promoter | Person/group controlling the company | In India, promoter holding is watched closely. High pledge or falling promoter stake can be a warning sign. |
| Promoter holding | Promoter ownership percentage | Stable high holding may show commitment, but very high holding can reduce free float. |
| Pledged shares | Promoter shares given as collateral | High pledge is risky because lenders may sell shares if price falls. |
| Institutional holding | Ownership by institutions | Includes mutual funds, FIIs, DIIs, insurance firms, pension funds, etc. |
| FII / FPI | Foreign institutional/portfolio investor | Foreign money can influence large-cap flows and market sentiment. |
| DII | Domestic institutional investor | Includes Indian mutual funds, insurers, banks, and financial institutions. |
| Mutual fund | Pooled investment vehicle | Investors pool money, and a fund manager invests according to fund objective. |
| ETF | Exchange-traded fund | A fund traded like a stock. Often tracks an index, sector, commodity, or theme. |
| Dividend | Cash paid by company to shareholders | Dividend reduces company cash and often adjusts price around ex-dividend date. |
| Dividend yield | Dividend divided by price | A Rs 5 dividend on Rs 100 stock is 5% yield. High yield can be attractive or a warning. |
| Ex-dividend date | Date from which buyer does not get declared dividend | If you buy on or after ex-dividend date, you usually do not receive that dividend. |
| Record date | Date company checks eligible shareholders | You need to be shareholder by the required settlement timeline to be on record. |
| Bonus issue | Free additional shares to shareholders | Example: 1:1 bonus doubles shares held, but price adjusts proportionally. Economic value does not automatically double. |
| Stock split | Reduces face value and increases share count | Example: 1 share of Rs 1,000 becomes 10 shares of Rs 100 each. Value is unchanged before market reaction. |
| Rights issue | Existing shareholders get right to buy new shares | Usually offered at a set price. If ignored, ownership may dilute. |
| Buyback | Company buys its own shares | Can return cash to shareholders and reduce share count, but price impact depends on terms and valuation. |
| Delisting | Company removed from exchange trading | Can be voluntary or forced. Liquidity and exit terms matter. |
| Merger | Two companies combine | Shareholders may receive shares/cash based on merger terms. |
| Demerger | Business split into separate company | Shareholders may receive shares of the new entity. Value depends on structure and listing. |
| Spin-off | A business unit becomes separate company | Similar to demerger; used to unlock value or simplify structure. |
| Open offer | Offer to buy shares from public shareholders | Often triggered by takeover rules or change in control. |
| Preferential allotment | Shares issued to selected investors | Can raise capital but may dilute existing shareholders. |
| QIP | Qualified institutional placement | Listed company raises money from qualified institutional buyers. |
| IPO | Initial public offering | Company sells shares to public for first time and lists on exchange. |
| FPO | Follow-on public offer | Already listed company raises more public equity. |
| OFS | Offer for sale | Existing shareholders, often promoters or government, sell shares through exchange mechanism. |
| Listing gains | Profit after IPO lists above issue price | IPO investing based only on listing gain can be risky. |
| Lock-in period | Period when shares cannot be sold | Common for promoters, pre-IPO investors, anchor investors, and some funds. |
| Anchor investor | Institutional investor in IPO before public issue | Their participation can affect sentiment, but it is not a guarantee of quality. |
| DRHP | Draft red herring prospectus | Preliminary IPO document filed with regulator. It contains business, risk, and financial details. |
| RHP | Red herring prospectus | Updated IPO offer document with key issue details. |
| Shareholding pattern | Ownership breakdown | Shows promoters, institutions, public, and other shareholder categories. |

---

# 6. Fundamental Analysis And Accounting Jargon

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Revenue | Money earned from selling goods/services | Also called sales, turnover, or revenue from operations. Growth quality matters more than headline growth. |
| Top line | Revenue | Called top line because revenue appears near top of income statement. |
| Bottom line | Net profit | Called bottom line because profit appears near bottom of income statement. |
| Gross profit | Revenue minus direct costs | Shows profit after cost of goods/services but before overheads. |
| Gross margin | Gross profit as % of revenue | Higher gross margin usually means pricing power or lower direct costs. |
| EBITDA | Earnings before interest, tax, depreciation, amortization | Used to estimate operating cash earnings, but it ignores capex, working capital, tax, and debt costs. |
| EBIT | Earnings before interest and tax | Operating profit before financing and tax. |
| Operating profit | Profit from core operations | Excludes some non-operating income/expenses depending on accounting presentation. |
| PAT | Profit after tax | Net profit available after tax. |
| EPS | Earnings per share | Net profit divided by shares. Diluted EPS accounts for potential dilution. |
| Dilution | Existing owners' percentage reduces | Happens when new shares are issued through QIP, ESOPs, conversion, rights issue, etc. |
| Cash flow | Actual cash moving in/out | Profit and cash flow can differ due to credit sales, inventory, receivables, capex, and accounting accruals. |
| CFO | Cash flow from operations | Cash generated by normal business operations. Important for earnings quality. |
| FCF | Free cash flow | Cash left after operating cash flow minus capex. Useful for dividends, debt repayment, and reinvestment. |
| Capex | Capital expenditure | Spending on long-term assets like plants, stores, machinery, technology, or infrastructure. |
| Opex | Operating expenditure | Day-to-day operating costs like salaries, rent, marketing, and utilities. |
| Working capital | Money tied in receivables, inventory, payables | Fast-growing businesses can report profit but consume cash due to working capital. |
| Receivables | Money customers owe company | Rising receivables faster than sales can signal collection risk. |
| Inventory | Goods held for sale/production | Too much inventory can mean weak demand or future write-downs. |
| Payables | Money company owes suppliers | Stretching payables can temporarily improve cash flow but may indicate stress. |
| Debt | Borrowed money | Debt can boost growth but increases interest and refinancing risk. |
| Net debt | Debt minus cash | Better than gross debt for companies with large cash balances. |
| Interest coverage | Ability to pay interest | Usually EBIT or EBITDA divided by interest expense. Higher is safer. |
| Leverage | Use of debt or borrowed exposure | Financial leverage magnifies gains and losses. |
| ROE | Return on equity | Net profit divided by shareholder equity. High ROE can be good, but check debt. |
| ROCE | Return on capital employed | Operating return on debt plus equity capital. Useful for capital-intensive businesses. |
| ROIC | Return on invested capital | Measures how efficiently company uses invested operating capital. |
| Asset turnover | Revenue generated per unit of assets | Higher turnover means assets are used efficiently. |
| Margin expansion | Profit margin improves | Can happen due to pricing power, cost control, operating leverage, or mix improvement. |
| Margin compression | Profit margin falls | Can happen due to competition, rising costs, discounting, or poor scale. |
| Operating leverage | Profit grows faster than revenue | When fixed costs are high, small revenue growth can strongly lift profit. It also works in reverse. |
| One-time item | Non-recurring gain/loss | Analysts adjust one-time items to estimate normalized profit. If it happens every year, it is not really one-time. |
| Exceptional item | Unusual item shown separately | Could be restructuring, impairment, legal settlement, sale gain, or other unusual event. |
| Impairment | Asset value written down | Company admits an asset is worth less than recorded value. |
| Goodwill | Premium paid above net assets in acquisition | Large goodwill can become impairment risk if acquisition underperforms. |
| Depreciation | Accounting charge for asset wear/use | Spreads cost of tangible assets over useful life. |
| Amortization | Similar charge for intangible assets | Applies to assets like software, patents, or acquired intangibles. |
| Contingent liability | Possible future liability | Example: legal case or tax dispute that may or may not become payable. |
| Related-party transaction | Deal with connected parties | Can be normal or risky. Need to check fairness and transparency. |
| Auditor qualification | Auditor raises concern | A qualified opinion or adverse comment can be a serious red flag. |
| Key audit matter | Important issue auditor focused on | Not automatically bad, but tells you where accounting judgment is significant. |
| Consolidated financials | Group-level financial statements | Includes subsidiaries. Often better for analyzing full business exposure. |
| Standalone financials | Parent company only | Useful in some cases but may miss subsidiaries and group-level debt. |
| Guidance | Management forecast/commentary | Can cover revenue, margin, growth, capex, demand, or industry outlook. |
| Order book | Value of confirmed future orders | Important for infrastructure, defense, EPC, industrials, and capital goods companies. |
| Backlog | Work/orders not yet recognized as revenue | Similar to order book in some sectors. |
| Run rate | Annualized current performance | If company makes Rs 100 crore revenue in a quarter, annualized run rate is Rs 400 crore, but seasonality matters. |
| Moat | Sustainable competitive advantage | Brand, cost advantage, network effect, distribution, patents, regulation, or switching costs can form moats. |
| TAM | Total addressable market | Maximum market opportunity if company captures the whole target market. Often exaggerated in presentations. |
| Unit economics | Profitability per customer/unit | Common in startups/platforms. Checks whether growth is economically sensible. |

---

# 7. Valuation Jargon

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Valuation | Estimating what something is worth | Price is what market quotes; value is your estimate based on cash flows, assets, growth, and risk. |
| Intrinsic value | Estimated true economic value | Usually based on future cash flows or asset value. It is an estimate, not a fact. |
| Market value | Current market price/value | What buyers and sellers currently agree on. |
| Fair value | Reasonable estimated value | Can be accounting fair value or analyst estimate depending on context. |
| Undervalued | Price below estimated value | Only useful if your estimate is sound and catalyst/risk are considered. |
| Overvalued | Price above estimated value | Overvalued stocks can remain expensive for long periods. |
| PE ratio | Price divided by earnings per share | Shows how much market pays for one rupee of earnings. Low PE is not automatically cheap. |
| Forward PE | Price divided by expected future EPS | Depends on analyst forecasts. Forecasts can be wrong. |
| Trailing PE | Price divided by past EPS | Uses historical earnings. May be misleading if earnings are cyclical. |
| PB ratio | Price divided by book value | Useful for banks, financials, and asset-heavy companies. Less useful for asset-light software firms. |
| PS ratio | Price divided by sales | Used when profits are low or negative, but sales alone do not prove value. |
| EV | Enterprise value | Market cap plus debt minus cash. Represents value of the whole business. |
| EV/EBITDA | Enterprise value divided by EBITDA | Common for comparing operating businesses, but weak for banks and capex-heavy firms. |
| EV/Sales | Enterprise value divided by revenue | Used for high-growth or low-profit companies. Must be linked to future margins. |
| PEG ratio | PE divided by earnings growth | Attempts to adjust PE for growth. Growth quality and durability still matter. |
| Dividend yield | Dividend per share divided by price | High yield can mean attractive income or market fear about sustainability. |
| Earnings yield | EPS divided by price | Inverse of PE. A PE of 20 equals 5% earnings yield. |
| FCF yield | Free cash flow divided by market value | Shows cash return relative to price. Useful if FCF is sustainable. |
| DCF | Discounted cash flow | Values business by estimating future cash flows and discounting them to present value. |
| Discount rate | Required return used in DCF | Higher risk means higher discount rate and lower value. |
| WACC | Weighted average cost of capital | Blended cost of debt and equity used as discount rate for firm cash flows. |
| Terminal value | Value after explicit forecast period | Often a large part of DCF. Small assumption changes can change valuation a lot. |
| Margin of safety | Gap between value and price | Larger margin protects against mistakes in assumptions. |
| Sum of the parts | Valuing business segments separately | Useful for conglomerates with different businesses. |
| Re-rating | Valuation multiple expands | A stock can rise because market pays higher PE/PB/EV multiple. |
| De-rating | Valuation multiple contracts | A stock can fall even if earnings grow, if market pays lower multiple. |
| Multiple expansion | Same as re-rating | Usually driven by better growth, lower risk, higher liquidity, or sentiment. |
| Multiple contraction | Same as de-rating | Usually driven by slower growth, higher rates, poor results, or risk. |
| Value trap | Looks cheap but keeps declining | Often because business quality is deteriorating or earnings are not sustainable. |
| Growth stock | Stock priced for high future growth | Can perform well if growth beats expectations; can fall sharply if growth slows. |
| Value stock | Stock priced cheaply vs fundamentals | Needs catalyst or patience. Cheap can become cheaper. |
| Cyclical stock | Earnings move with economic cycle | Metals, autos, cement, capital goods, and commodities often behave cyclically. |
| Defensive stock | Less sensitive to economic cycle | FMCG, utilities, healthcare, and staples are often considered defensive. |
| Secular growth | Long-term structural growth | Example: digital payments adoption, premiumization, formalization. |
| Mean reversion in valuation | Valuation returns toward historical average | A very expensive stock may de-rate; a very cheap sector may re-rate if fundamentals improve. |

---

# 8. Derivatives: General Terms

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Derivative | Contract whose value comes from underlying | Futures and options derive value from stocks, indexes, commodities, currencies, or rates. |
| Underlying | Asset on which derivative is based | NIFTY future has NIFTY index as underlying. Reliance option has Reliance stock as underlying. |
| Contract | Standardized derivative agreement | Specifies underlying, expiry, lot size, strike if applicable, and settlement rules. |
| Lot size | Minimum contract quantity | If lot size is 500, one contract represents 500 units. Lot size controls rupee risk. |
| Expiry | Date derivative contract ends | Futures/options must be closed, settled, exercised, or expire based on rules. |
| Near-month contract | Closest expiry contract | Usually most liquid in futures. |
| Next-month contract | Following expiry contract | Used for rollover or longer exposure. |
| Far-month contract | Later expiry contract | Often less liquid than near-month. |
| Open interest / OI | Number of open derivative contracts | OI rises when new positions are created and falls when positions close. |
| OI buildup | Increase in open interest | Must be read with price to infer long buildup, short buildup, short covering, or unwinding. |
| Change in OI | Difference in OI from previous period | Used to understand whether positions are being added or reduced. |
| Rollover | Moving position from current expiry to next | Close current contract and open next contract. Common near expiry. |
| Cost of carry | Cost/benefit of holding futures vs spot | Includes interest, dividends, storage, funding, and market expectations depending on asset. |
| Basis | Futures price minus spot price | Positive basis means futures above spot. Negative basis means futures below spot. |
| Contango | Futures price higher than spot or near expiry | Common in commodities when storage/funding costs matter. Can hurt long roll returns. |
| Backwardation | Futures price lower than spot or near expiry | Often signals tight near-term supply or strong immediate demand. |
| Mark-to-market / MTM | Daily profit/loss recognition | Futures gains/losses are settled regularly, affecting cash balance. |
| Initial margin | Margin required to open position | Not the maximum loss. It is the required collateral. |
| Maintenance margin | Minimum margin to keep position | If account falls below requirement, more funds may be needed. |
| Variation margin | Additional margin due to price moves | Common in futures because losses are settled as market moves. |
| SPAN margin | Risk-based margin system | Estimates potential loss under different scenarios. Used in derivatives risk management. |
| Exposure margin | Additional margin for risk | Extra margin beyond initial risk calculations. |
| Hedge | Position used to reduce risk | Example: buying puts to protect stock portfolio. |
| Speculative position | Position taken to profit from price movement | Not mainly for hedging. Needs strict risk control. |
| Spread | Combining two related positions | Examples: calendar spread, bull call spread, futures spread. |
| Calendar spread | Same underlying, different expiries | Used to trade time/roll/volatility differences. |
| Arbitrage spread | Price difference between related assets | Traders try to capture mispricing after costs and risk. |
| Physical settlement | Delivery of underlying asset | In some derivatives, final settlement can require delivery rather than cash. |
| Cash settlement | Settlement in money | Difference between contract price and settlement price is paid/received. |

---

# 9. Options Jargon

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Option | Contract giving a right, not obligation | Buyer pays premium for the right. Seller receives premium and takes obligation. |
| Call option | Right to buy underlying at strike | Generally bullish for buyer. Seller is obligated if exercised/assigned. |
| Put option | Right to sell underlying at strike | Generally bearish or protective for buyer. |
| Strike price | Price at which option can be exercised | Strike determines whether option is ITM, ATM, or OTM. |
| Premium | Price of option | Buyer pays premium. Seller receives premium. Long option max loss is premium paid. |
| Intrinsic value | Real in-the-money value | For call: spot minus strike if positive. For put: strike minus spot if positive. |
| Extrinsic value | Time and volatility value | Premium above intrinsic value. It decays as expiry approaches. |
| Time value | Part of premium from time left | More time generally means more premium. |
| ITM | In the money | Call ITM when spot above strike. Put ITM when spot below strike. |
| ATM | At the money | Strike near current underlying price. |
| OTM | Out of the money | No intrinsic value. Entire premium is extrinsic. |
| Deep ITM | Far in the money | Behaves more like underlying due to high delta. |
| Far OTM | Far out of the money | Cheap but low probability. Often expires worthless. |
| Break-even | Price needed to avoid loss at expiry | Long call break-even = strike + premium. Long put break-even = strike - premium. |
| Payoff | Profit/loss shape at expiry | Options have nonlinear payoff, unlike stock/futures. |
| Greeks | Risk measures for options | Delta, gamma, theta, vega, and rho describe option sensitivity. |
| Delta | Option sensitivity to underlying price | Delta 0.50 means option may move about Rs 0.50 for Rs 1 move in underlying, before other factors. |
| Gamma | Rate of change of delta | Gamma rises near expiry and near ATM strikes. It makes option movement faster. |
| Theta | Time decay | Long options lose time value as days pass, all else equal. |
| Vega | Sensitivity to implied volatility | Long options benefit from IV rise and suffer from IV fall. |
| Rho | Sensitivity to interest rates | Usually less important for short-term equity options but can matter in longer tenors. |
| Implied volatility / IV | Market's expected volatility priced into option | High IV means expensive options. Low IV means cheaper options, but not always better. |
| Historical volatility / HV | Past realized price movement | Compares actual past movement with IV expectations. |
| IV crush | Sharp fall in implied volatility | Common after events like earnings. Long option can lose even if direction is right. |
| IV rank | Current IV relative to past range | Helps judge whether options are expensive or cheap historically. |
| IV percentile | Percentage of past days IV was lower | Another way to compare current IV with history. |
| Option chain | Table of strikes, premiums, OI, IV | Used to analyze options market positioning and liquidity. |
| PCR | Put-call ratio | Put OI/volume divided by call OI/volume. Interpreted differently by context. |
| Max pain | Strike where option buyers lose most at expiry | Popular but not a reliable standalone trading signal. |
| Assignment | Option seller is assigned obligation | Happens when buyer exercises, depending on market rules. |
| Exercise | Option buyer uses the right | In many markets, exercise rules depend on European/American style and settlement. |
| European option | Exercisable only at expiry | Many index options follow European-style exercise. |
| American option | Exercisable before expiry | Some markets/instruments allow early exercise. Check contract rules. |
| Naked option selling | Selling option without hedge | Can have large or unlimited risk depending on structure. Dangerous without expertise. |
| Covered call | Own stock and sell call | Generates premium but caps upside above strike. |
| Protective put | Own stock and buy put | Acts like insurance against downside. |
| Collar | Own stock, buy put, sell call | Limits downside and upside, often reducing hedge cost. |
| Bull call spread | Buy lower strike call, sell higher strike call | Bullish defined-risk strategy with capped profit. |
| Bear put spread | Buy higher strike put, sell lower strike put | Bearish defined-risk strategy with capped profit. |
| Credit spread | Receive net premium | Profit if spread expires favorably. Risk must be defined and managed. |
| Debit spread | Pay net premium | Risk is usually limited to debit paid. Profit is capped. |
| Straddle | Buy call and put same strike/expiry | Profits from large move either direction, but expensive if IV high. |
| Strangle | Buy call and put different strikes | Cheaper than straddle but needs larger move. |
| Iron condor | Sell call spread and put spread | Range-bound strategy with defined risk. Can lose if price moves strongly. |
| Butterfly | Options spread centered on a target price | Profits if price finishes near middle strike, depending on structure. |
| Calendar spread | Same strike, different expiries | Trades time decay and volatility differences. |
| Diagonal spread | Different strikes and expiries | More flexible but more complex than calendar. |
| Synthetic future | Options combination behaving like future | Long call plus short put at same strike can mimic long futures. |
| Moneyness | Relationship between spot and strike | ITM, ATM, and OTM describe moneyness. |
| Pinning | Price stays near a strike near expiry | Can happen due to hedging flows and option positioning, but not guaranteed. |
| Expiry day | Day options/futures expire | Gamma, theta, and volatility behavior can become extreme near expiry. |
| Weekly option | Option expiring weekly | High theta decay and event sensitivity. |
| Monthly option | Option expiring monthly | Usually has more time value and often deeper liquidity in some contracts. |

---

# 10. Futures Jargon

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Future | Contract to buy/sell underlying at future date | Futures move nearly point-for-point with underlying but use margin and leverage. |
| Index future | Future on an index | NIFTY futures and BANKNIFTY futures are examples. Useful for index directional trades or hedges. |
| Stock future | Future on individual stock | Gives leveraged exposure to one stock. Single-stock risk can be high. |
| Commodity future | Future on commodity | Crude oil, gold, silver, natural gas, copper, and agricultural contracts are examples. |
| Notional value | Full value controlled by contract | Futures margin may be small relative to notional, but profit/loss is based on notional exposure. |
| Contract value | Same as notional value | Formula: futures price x lot size. |
| Tick size | Minimum price movement | If tick size is 0.05, price moves in increments of 0.05. |
| Tick value | Rupee value of one tick | Tick size x lot size. Important for scalping and risk calculation. |
| Settlement price | Price used for MTM/expiry settlement | May differ slightly from last traded price depending on exchange method. |
| Fair value | Theoretical futures value | Based on spot, interest, dividends, storage, and time to expiry. |
| Premium | Futures trading above spot | Can reflect cost of carry, bullishness, dividends, or market structure. |
| Discount | Futures trading below spot | Can reflect dividends, bearishness, supply-demand, or near-term pressure. |
| Rollover percentage | Portion of positions shifted to next expiry | High rollover can suggest participants are carrying positions forward. Direction still needs price/OI context. |
| Rollover cost | Cost of moving to next contract | Difference between current and next expiry plus execution cost. |
| Expiry settlement | Final settlement on expiry | Can be cash or physical depending on contract. |
| Physical delivery risk | Need to deliver/take underlying | Some stock and commodity derivatives may involve physical settlement. Understand rules before expiry. |
| Calendar spread in futures | Long one expiry, short another | Used to trade roll/basis differences. |
| Basis risk | Hedge does not perfectly match underlying | Example: hedging stock portfolio with index future can fail if portfolio behaves differently from index. |
| Carry trade | Profit from holding spread due to carry | Common in rates, currencies, and commodities. Needs funding and risk control. |
| Leverage ratio | Exposure divided by capital | If Rs 10 lakh exposure uses Rs 1 lakh capital, leverage is 10x. Losses are also magnified. |

---

# 11. Commodities Jargon

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Commodity | Raw material or primary product | Examples: crude oil, gold, silver, copper, natural gas, wheat, cotton. |
| Hard commodity | Mined/extracted commodity | Gold, crude oil, copper, iron ore, and natural gas are hard commodities. |
| Soft commodity | Agricultural commodity | Cotton, sugar, coffee, wheat, soybean, and similar goods. |
| Bullion | Precious metals | Usually gold and silver. |
| Base metals | Industrial metals | Copper, aluminum, zinc, nickel, and lead. Sensitive to industrial demand. |
| Energy commodities | Fuel/energy products | Crude oil, natural gas, gasoline, heating oil, coal, etc. |
| Spot price | Price for immediate delivery | The current cash market price. |
| Futures curve | Prices across expiries | Shows contango/backwardation and market expectations/carry. |
| Storage cost | Cost to store physical commodity | Important in commodities because storage affects futures pricing. |
| Convenience yield | Benefit of holding physical commodity | If supply is tight, holding physical inventory has value. |
| Inventory data | Reported stock levels | Low inventory can support prices; high inventory can pressure prices. |
| Seasonality | Repeating seasonal demand/supply pattern | Agriculture, natural gas, power, and some metals can have seasonal behavior. |
| OPEC | Oil-producing countries' group | OPEC decisions can affect crude supply and prices. |
| SPR | Strategic petroleum reserve | Government-held oil reserve. Releases/builds can affect crude sentiment. |
| Crack spread | Refining margin indicator | Difference between crude oil and refined products. Used in energy markets. |
| Crush spread | Processing margin in agriculture | Example: soybean value vs soybean oil/meal outputs. |
| Basis in commodities | Local cash price minus futures price | Used by hedgers to understand local supply/demand vs exchange price. |
| Hedger | Participant reducing price risk | Farmer, miner, refiner, airline, jeweler, or importer/exporter may hedge commodity exposure. |
| Speculator | Participant taking price risk for profit | Provides liquidity but can face large losses. |
| Delivery center | Location approved for physical delivery | Commodity contracts may specify delivery locations and quality standards. |
| Grade | Quality specification of commodity | Delivery must meet exchange-defined quality/grade. |
| Lot / contract unit | Quantity per commodity contract | Example: one contract may represent a fixed number of barrels, grams, kg, or units. |
| Cash and carry | Buy spot, sell futures | Arbitrage strategy if futures are rich enough after funding/storage costs. |
| Supply shock | Sudden supply disruption | War, weather, strike, export ban, pipeline issue, or mine disruption can cause price spikes. |
| Demand shock | Sudden demand change | Recession, reopening, heatwave, industrial boom, or policy change can affect demand. |
| Safe haven | Asset bought during stress | Gold is often called a safe haven, though it can still fall. |
| Inflation hedge | Asset expected to hold value in inflation | Commodities can hedge inflation sometimes, but relationship is not perfect. |

---

# 12. Technical Analysis And Indicator Jargon

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Candle / candlestick | Visual price bar | Shows open, high, low, close for a time period. |
| Timeframe | Duration of each candle | 5-min, 15-min, hourly, daily, weekly, monthly, etc. Higher timeframe usually carries more importance. |
| Moving average / MA | Average price over a period | Smooths price. 20 DMA means 20-day moving average. |
| DMA | Daily moving average | 50 DMA and 200 DMA are common trend references. |
| EMA | Exponential moving average | Gives more weight to recent prices than simple moving average. |
| SMA | Simple moving average | Equal-weighted average of past prices. |
| Golden cross | Shorter MA crosses above longer MA | Often 50 DMA above 200 DMA. Seen as bullish but can lag. |
| Death cross | Shorter MA crosses below longer MA | Often 50 DMA below 200 DMA. Seen as bearish but can lag. |
| RSI | Relative Strength Index | Momentum oscillator from 0 to 100. Above 70 often called overbought; below 30 oversold, but context matters. |
| MACD | Moving average convergence divergence | Trend/momentum indicator based on moving averages. |
| ATR | Average true range | Measures volatility. Useful for stop distance and position sizing. |
| Bollinger Bands | Volatility bands around moving average | Price near band does not automatically mean reversal. |
| VWAP | Volume-weighted average price | Average price weighted by volume. Institutions often track it intraday. |
| Anchored VWAP | VWAP from a chosen event/date | Used from earnings, breakout, major low/high, or gap day. |
| Volume profile | Volume traded at price levels | Shows where market traded most volume. |
| Point of control / POC | Highest volume price in profile | Price level with maximum traded volume in selected range. |
| RSI divergence | Price and RSI move differently | Bullish divergence: price makes lower low but RSI makes higher low. It is a warning, not a guarantee. |
| Trendline | Line connecting price highs/lows | Helps visualize trend but can be subjective. |
| Channel | Parallel trendlines containing price | Price moves between upper and lower boundaries. |
| Fibonacci retracement | Common pullback levels | 38.2%, 50%, 61.8% are watched. They are reference zones, not magic. |
| Head and shoulders | Reversal chart pattern | Shows possible trend exhaustion if neckline breaks. |
| Double top | Two failed attempts near same high | Can signal resistance and reversal if support breaks. |
| Double bottom | Two failed attempts near same low | Can signal support and reversal if resistance breaks. |
| Cup and handle | Rounded base then small pullback | Often used for breakout setups. |
| Flag | Small consolidation after sharp move | Can be continuation if breakout happens in trend direction. |
| Pennant | Triangle-like consolidation after move | Similar to flag. Needs breakout confirmation. |
| Doji | Candle with small body | Shows indecision. Meaning depends on location and context. |
| Hammer | Candle with long lower wick | Can show rejection of lower prices, especially near support. |
| Shooting star | Candle with long upper wick | Can show rejection of higher prices near resistance. |
| Engulfing candle | One candle body covers prior body | Bullish or bearish depending on direction and context. |
| Breakout retest | Price breaks level then tests it again | A successful retest can confirm old resistance becoming support. |
| Volume breakout | Breakout with high volume | More reliable than breakout on weak volume, but still not guaranteed. |
| Price action | Reading price behavior directly | Uses structure, candles, levels, trend, volume, and context. |

---

# 13. Risk, Money Management, And Portfolio Jargon

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Risk | Possibility of loss or bad outcome | Risk includes price loss, liquidity, leverage, fraud, timing, volatility, and opportunity cost. |
| Reward | Expected gain | Must be compared with risk and probability. |
| Risk-reward ratio | Potential loss vs potential gain | If risking Rs 1 to make Rs 2, risk-reward is 1:2. |
| R-multiple | Profit/loss measured in risk units | If initial risk is Rs 10,000 and profit is Rs 30,000, result is +3R. |
| Stop loss | Predefined exit if wrong | A stop controls loss but may slip in gaps. |
| Trailing stop | Stop moved as trade profits | Protects gains while allowing trend to continue. |
| Position sizing | Deciding how much to buy/sell | Based on capital, risk per trade, stop distance, and instrument risk. |
| Capital allocation | How capital is distributed | Decides how much goes to stocks, cash, sectors, strategies, or trades. |
| Exposure | Total market value at risk | Futures exposure can be much larger than margin. |
| Gross exposure | Total long plus short exposure | Measures total market activity regardless of direction. |
| Net exposure | Long exposure minus short exposure | Shows directional market bias. |
| Drawdown | Fall from peak capital | If capital falls from Rs 10 lakh to Rs 8 lakh, drawdown is 20%. |
| Max drawdown | Worst peak-to-trough decline | Key measure of strategy pain. |
| Volatility | Degree of price fluctuation | High volatility means larger swings. It can create opportunity and risk. |
| Beta | Sensitivity to market/index | Beta 1.5 means stock tends to move more than market; beta 0.7 means less. |
| Alpha | Return above benchmark/risk expectation | True alpha is hard to generate after costs and risk. |
| Sharpe ratio | Return per unit of volatility | Higher is better, but can be misleading if returns are not normally distributed. |
| Sortino ratio | Return per unit of downside volatility | Focuses on harmful volatility rather than all volatility. |
| VaR | Value at risk | Statistical estimate of potential loss over period at confidence level. It can miss extreme events. |
| Tail risk | Rare but severe loss risk | Market crashes, gap downs, currency shocks, and option selling blowups are tail risks. |
| Black swan | Rare unexpected extreme event | Used for events outside normal expectations. |
| Correlation | How two assets move together | High correlation means diversification may fail during stress. |
| Diversification | Spreading risk across assets | Helps reduce single-position risk but does not remove market risk. |
| Concentration risk | Too much exposure to one asset/theme | Big gains possible, but one mistake can damage portfolio. |
| Hedging | Reducing risk with another position | Example: long portfolio plus index put. Hedge cost and basis risk matter. |
| Leverage | Controlling more exposure than capital | Increases both gains and losses. Futures and margin trades are leveraged. |
| Kelly criterion | Formula for optimal bet size | Useful conceptually, but full Kelly can be too aggressive in real markets. |
| Risk of ruin | Chance of losing so much you cannot continue | Poor sizing and leverage increase risk of ruin. |
| Liquidity risk | Risk you cannot exit at fair price | Appears during panic, low-volume stocks, and far OTM options. |
| Gap risk | Price jumps beyond stop level | Overnight news can cause open price far from previous close. |
| Event risk | Risk from scheduled/unscheduled event | Earnings, policy, court orders, war, regulations, and management news. |
| Counterparty risk | Other party fails obligation | Reduced in exchange-traded contracts due to clearing, but relevant in OTC markets. |
| Opportunity cost | Return lost by choosing one option | Holding a weak stock may prevent investing in a better one. |
| Rebalancing | Resetting portfolio weights | Used to control risk and maintain target allocation. |
| Asset allocation | Split across asset classes | Example: equity, debt, gold, cash, real estate, commodities. |
| Benchmark | Reference used for comparison | NIFTY 50, S&P 500, sector index, or custom benchmark. |
| Tracking error | Difference from benchmark returns | Important for index funds and ETFs. |

---

# 14. Macro, Currency, Rates, And Economy Jargon

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| GDP | Value of goods/services produced | Broad measure of economic activity. Strong GDP can support earnings but market reaction depends on expectations. |
| Inflation | General rise in prices | High inflation can hurt margins, reduce purchasing power, and influence interest rates. |
| CPI | Consumer price index | Measures retail inflation paid by consumers. |
| WPI | Wholesale price index | Measures wholesale price inflation. Important for input cost trends. |
| Interest rate | Cost of borrowing money | Higher rates can reduce valuations and slow demand. |
| Repo rate | Central bank lending rate to banks | In India, RBI repo rate influences borrowing costs and liquidity. |
| Rate hike | Central bank increases rates | Usually tightens financial conditions. Can pressure equities. |
| Rate cut | Central bank lowers rates | Usually supports liquidity and growth assets, but context matters. |
| Yield | Return on bond/debt instrument | Bond yields affect equity valuation, currency, and borrowing costs. |
| Yield curve | Yields across maturities | Upward, flat, or inverted curve gives economic signals. |
| Yield curve inversion | Short-term yields above long-term yields | Often watched as recession warning in some markets. |
| Liquidity | Availability of money/credit | Easy liquidity supports risk assets; tight liquidity pressures them. |
| Quantitative easing / QE | Central bank buys assets/injects money | Usually increases liquidity and can support markets. |
| Quantitative tightening / QT | Central bank reduces liquidity | Can pressure risk assets and raise yields. |
| Fiscal deficit | Government spending exceeds revenue | Funded by borrowing. Can affect inflation, rates, and currency. |
| Current account deficit | Country imports more goods/services/income than exports | Can pressure currency if funding is weak. |
| Trade deficit | Imports exceed exports | Part of current account. Important for currency and macro stability. |
| Forex reserves | Central bank foreign currency reserves | Supports currency stability and external payments confidence. |
| USDINR | Dollar-rupee exchange rate | If USDINR rises, rupee weakens against dollar. |
| Currency depreciation | Currency loses value | Helps exporters but hurts importers and foreign debt borrowers. |
| Currency appreciation | Currency gains value | Helps importers but can hurt exporters. |
| DXY | US Dollar Index | Measures dollar strength against basket of major currencies. A strong dollar can pressure emerging markets. |
| Crude oil sensitivity | Impact of oil prices on economy/company | India imports crude, so high crude can affect inflation, currency, and margins. |
| Commodity cycle | Long rise/fall in commodity prices | Driven by supply, demand, inventories, capex, and macro cycle. |
| Recession | Broad economic contraction | Can reduce demand, earnings, credit growth, and risk appetite. |
| Soft landing | Inflation falls without severe recession | Positive macro outcome if achieved. |
| Hard landing | Tightening leads to recession/stress | Usually negative for risk assets. |
| Stagflation | High inflation plus weak growth | Difficult environment for central banks and equity valuations. |
| Risk premium | Extra return demanded for risk | Higher uncertainty increases risk premium and lowers valuations. |

---

# 15. Funds, Bonds, Banking, And Return Metrics

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Mutual fund scheme | Pooled investment product | Investors pool money, and the fund invests according to its stated objective. |
| NAV | Net asset value per unit | Mutual fund's per-unit value. Formula: fund assets minus liabilities divided by units. |
| AUM | Assets under management | Total money managed by a fund, AMC, advisor, or institution. |
| AMC | Asset management company | Company that manages mutual fund schemes and other investment products. |
| SIP | Systematic investment plan | Investing a fixed amount regularly, often monthly. Helps discipline and averaging. |
| SWP | Systematic withdrawal plan | Regular withdrawals from investment corpus. Used for income planning. |
| STP | Systematic transfer plan | Regular transfer from one mutual fund scheme to another, often liquid fund to equity fund. |
| Expense ratio | Annual fund management cost | Higher expense reduces investor return. Compare within same fund category. |
| Direct plan | Mutual fund plan without distributor commission | Usually lower expense ratio than regular plan. |
| Regular plan | Mutual fund plan through distributor | Expense ratio includes distributor commission. |
| Exit load | Fee for redeeming early | Funds may charge if you exit before specified period. |
| Lock-in | Period when redemption is restricted | ELSS and some other products have lock-in. |
| ELSS | Equity-linked savings scheme | Tax-saving mutual fund category in India with lock-in. |
| Index fund | Fund that tracks an index | Passive fund aiming to replicate benchmark performance. |
| Active fund | Fund manager selects securities | Tries to beat benchmark, but charges and consistency matter. |
| Passive fund | Tracks an index or rule | Does not try to pick winners actively. |
| Tracking error | Difference from index return | Lower tracking error is better for passive funds. |
| Tracking difference | Actual return gap vs index | Includes expenses, cash drag, and replication quality. |
| CAGR | Compounded annual growth rate | Smoothed annual return over multiple years. Does not show volatility. |
| Absolute return | Total percentage gain/loss | If Rs 100 becomes Rs 150, absolute return is 50%. Time period matters. |
| Annualized return | Return converted to yearly rate | Useful to compare investments with different holding periods. |
| XIRR | Return calculation for irregular cash flows | Useful for SIPs, staggered investments, and partial withdrawals. |
| IRR | Internal rate of return | Discount rate that makes cash flows equal to investment value. |
| Alpha in funds | Fund return above benchmark after adjustment | Persistent alpha is hard. One good year does not prove skill. |
| Beta in funds | Market sensitivity of fund | High beta fund rises/falls more with market. |
| Standard deviation | Return volatility measure | Higher standard deviation means returns fluctuate more. |
| Downside capture | How much fund falls when benchmark falls | Lower downside capture can show better downside protection. |
| Upside capture | How much fund rises when benchmark rises | Higher upside capture means fund participates strongly in up markets. |
| Bond | Debt instrument | Investor lends money to issuer and receives interest plus principal repayment if issuer does not default. |
| Coupon | Interest paid by bond | A 7% coupon on Rs 1,000 face value pays Rs 70 annually if annual coupon. |
| Face value / par value | Principal value of bond | Amount used to calculate coupon and often repaid at maturity. |
| Maturity | Date bond principal is repaid | Longer maturity usually has more interest-rate sensitivity. |
| YTM | Yield to maturity | Expected annualized return if bond is held to maturity and payments happen as expected. |
| Current yield | Coupon divided by current price | Simpler than YTM; ignores maturity gain/loss and reinvestment. |
| Bond price-yield relation | Bond prices fall when yields rise | This inverse relationship is critical for debt funds and bonds. |
| Duration | Bond sensitivity to interest rates | Higher duration means more price movement when rates change. |
| Modified duration | Approximate price change for yield change | If duration is 5, a 1% yield rise roughly means 5% price fall, before convexity. |
| Convexity | Curvature in bond price-yield relation | Helps refine duration estimate for larger yield moves. |
| Credit rating | Assessment of default risk | AAA is generally safer than lower ratings, but ratings can change. |
| Credit spread | Extra yield over safe benchmark | Higher spread compensates for credit risk, liquidity risk, or fear. |
| Default | Failure to pay interest/principal | Credit event that can cause large losses. |
| NPA | Non-performing asset | Loan where borrower has stopped paying as required. Important for banks/NBFCs. |
| Provisioning | Money set aside for expected losses | Banks provision for bad loans. Higher provisions reduce profit but improve prudence. |
| GNPA | Gross non-performing assets | Total bad loans before provisions. |
| NNPA | Net non-performing assets | Bad loans after provisions. Lower is better. |
| CASA | Current account savings account ratio | Low-cost deposit share for banks. Higher CASA can improve margins. |
| NIM | Net interest margin | Difference between interest earned and interest paid, relative to earning assets. |
| Credit growth | Growth in lending | Strong credit growth can support bank earnings if asset quality remains good. |
| Slippage | Fresh loans turning bad | In banking, slippage means standard loans becoming NPAs. In trading, slippage means execution price difference. Context matters. |
| Write-off | Removing bad loan/asset from books | Does not always mean recovery is impossible, but recognizes loss/accounting cleanup. |
| Restructuring | Changing loan terms for stressed borrower | Can avoid immediate default but may hide stress if abused. |
| Capital adequacy ratio | Bank capital vs risk-weighted assets | Shows buffer to absorb losses. |
| Tier 1 capital | Core bank capital | Higher Tier 1 capital means stronger loss-absorbing capacity. |
| NBFC | Non-bank finance company | Lends or finances without being a full bank. Funding risk is important. |
| ALM | Asset-liability management | Matching maturities and cash flows of assets and liabilities. Critical for lenders. |
| Spread income | Income from lending rate minus borrowing cost | Core income for banks/NBFCs. |
| Treasury income | Gains/income from investments | Can support bank profit but may be volatile. |
| Block deal | Large trade executed in special window | Usually between large investors. Can affect sentiment. |
| Bulk deal | Large trade crossing disclosure threshold | Exchange-reported large transaction. Shows who bought/sold if disclosed. |
| Insider trading | Trading using unpublished price-sensitive information | Illegal when based on confidential material information. |
| UPSI | Unpublished price-sensitive information | Information not public that can affect price if disclosed. |
| Pledged holding release | Promoter reduces pledged shares | Often seen positively because pledge risk falls. |
| Preferential issue | Shares/warrants issued to selected investors | Can bring capital but may dilute existing shareholders. |
| Warrant | Right to buy shares later at set price | Company/promoter/investor may use warrants. Conversion can dilute shareholding. |

---

# 16. News, Events, And Market Commentary Jargon

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| Catalyst | Event expected to move price | Earnings, order win, policy change, rate decision, merger, approval, or guidance update. |
| Earnings season | Period when companies report results | Volatility rises because expectations get tested. |
| Beat | Result better than expectations | Stock may still fall if beat was already priced in or guidance is weak. |
| Miss | Result worse than expectations | Stock may still rise if bad news was expected and future outlook improves. |
| Guidance raise | Management increases future forecast | Often bullish if credible. |
| Guidance cut | Management lowers future forecast | Often bearish because future estimates may be revised down. |
| Analyst upgrade | Analyst improves rating/target | Can influence sentiment, especially if from major broker. |
| Analyst downgrade | Analyst reduces rating/target | Can pressure stock if market respects the analyst or reasoning. |
| Price target | Analyst estimate of future price | It is an opinion based on assumptions, not a guarantee. |
| Street estimate | Market/analyst consensus forecast | Results are judged against expectations, not only absolute numbers. |
| Priced in | Already reflected in price | Good news may not lift stock if market already expected it. |
| Surprise | Outcome different from expectations | Markets move sharply on surprise, not just good/bad label. |
| Sentiment | Market mood | Can be bullish, bearish, fearful, euphoric, cautious, or neutral. |
| Narrative | Story market believes | Narratives can drive valuation until facts confirm or break them. |
| Theme | Broader investment idea | Examples: defense, railways, EV, AI, renewable energy, China+1. |
| Sector rotation | Money moves from one sector to another | Example: from IT to banks, or defensives to cyclicals. |
| Risk event | Event that can cause volatility | Budget, election, central bank meeting, war, court verdict, earnings. |
| Overhang | Issue limiting upside | Example: pending litigation, promoter pledge, regulatory uncertainty. |
| Tailwind | Helpful external factor | Example: falling raw material cost helps margins. |
| Headwind | Negative external factor | Example: rising interest rates hurt real estate demand. |
| Inflection point | Point where trend changes | Example: losses turn to profits, demand cycle improves, debt starts falling. |
| Green shoot | Early sign of improvement | Not proof yet; needs confirmation. |
| Structural growth | Long-term durable growth | Driven by deep changes, not short-term cycle. |
| Cyclical recovery | Recovery due to business cycle | Can be strong but may not last forever. |
| Decoupling | One market moves independently | Often claimed when local market ignores global cues. Usually temporary unless supported by fundamentals. |
| Contagion | Stress spreading between markets | Example: banking crisis affecting credit markets and equities. |
| Flight to safety | Investors move to safer assets | Usually into cash, government bonds, gold, or defensive assets. |

---

# 17. Trading Psychology And Slang

| Term | Simple meaning | Detailed explanation |
| --- | --- | --- |
| FOMO | Fear of missing out | Buying only because price is rising and you do not want to miss the move. Often leads to chasing. |
| Chasing | Entering after price has already run far | Chasing creates poor risk-reward because stop is far and entry is late. |
| Revenge trading | Trading to recover losses emotionally | Usually leads to oversized, low-quality trades. |
| Overtrading | Taking too many trades | Often caused by boredom, impatience, or need for action. |
| Confirmation bias | Seeing only evidence that supports your view | Dangerous because you ignore invalidation and risk. |
| Anchoring | Fixating on a price or past belief | Example: refusing to sell because stock once traded at Rs 500. |
| Averaging down | Buying more after price falls | Can work for investors with strong thesis, but can destroy traders if used without plan. |
| Averaging up | Buying more after price rises | Can be good in trend-following if risk is controlled. |
| Catching a falling knife | Buying during sharp fall | Risky because price can keep falling. Wait for stabilization if you need confirmation. |
| Bag holder | Person stuck holding losing position | Usually someone who did not exit when thesis failed. |
| Pump and dump | Price inflated then insiders sell | Common risk in illiquid stocks and social media tips. |
| Tip | Unverified trade recommendation | Tips without process are dangerous. You do not know entry, stop, size, or exit. |
| Noise | Random short-term movement/information | Not every tick or headline matters. |
| Edge | Repeatable advantage | Can come from information, analysis, execution, discipline, risk management, or structure. |
| Setup | Defined trade condition | Example: 52-week breakout with volume, sector strength, and clear stop. |
| Playbook | Documented set of setups and rules | Helps avoid random trades. |
| Conviction | Strength of belief | Conviction is useful only if supported by evidence and risk control. |
| Discipline | Following plan even under stress | More important than prediction in trading. |
| Patience | Waiting for quality setup | Good traders spend a lot of time doing nothing. |
| Hope trade | Holding because you hope it recovers | Hope is not a strategy. Define invalidation. |
| Paper trading | Practicing without real money | Useful for process testing, but emotions differ from live trading. |
| Backtesting | Testing rules on historical data | Must include costs, slippage, survivorship bias, and realistic execution. |
| Forward testing | Testing strategy live or paper going forward | Shows whether backtest logic survives real market behavior. |
| Journal | Record of trades and decisions | Helps identify repeat mistakes and improve process. |
| Process over outcome | Judge decision quality, not only profit | A good trade can lose; a bad trade can win. Focus on repeatable process. |

---

# 18. Common Confusing Pairs

| Pair | Difference |
| --- | --- |
| Price vs value | Price is market quote. Value is your estimate of worth. |
| Trading vs investing | Trading focuses on price movement and risk timing. Investing focuses on business value and long-term compounding. |
| Profit vs cash flow | Profit is accounting result. Cash flow is actual cash movement. |
| Revenue vs profit | Revenue is sales. Profit is what remains after costs. |
| Gross margin vs net margin | Gross margin is after direct costs. Net margin is after all expenses and tax. |
| Delivery volume vs total volume | Delivery volume suggests shares taken into demat; total volume includes intraday churn. |
| Volume vs open interest | Volume counts contracts traded today. OI counts contracts still open. |
| Long buildup vs short covering | Long buildup: price up, OI up. Short covering: price up, OI down. |
| Short buildup vs long unwinding | Short buildup: price down, OI up. Long unwinding: price down, OI down. |
| Futures margin vs maximum loss | Margin is required collateral. Maximum loss can be much larger. |
| Option premium vs option value | Premium is market price. Value depends on intrinsic/extrinsic components and probabilities. |
| IV vs historical volatility | IV is future volatility implied by option prices. Historical volatility is past movement. |
| Breakout vs false breakout | Breakout sustains above level. False breakout fails and returns below. |
| Correction vs crash | Correction is normal decline. Crash is sudden severe fall with panic/liquidity stress. |
| Hedge vs speculation | Hedge reduces existing risk. Speculation adds risk to seek profit. |
| Diversification vs diworsification | Diversification reduces useful risk. Diworsification adds too many low-quality positions without benefit. |

---

# 19. Quick Lookup: Positioning Terms From Price And OI

This is one of the most useful derivatives interpretation tables.

| Price | Open interest | Common interpretation | Simple meaning |
| --- | --- | --- | --- |
| Up | Up | Long buildup | New longs are entering. Bullish if supported by volume and context. |
| Down | Up | Short buildup | New shorts are entering. Bearish if supported by trend and context. |
| Up | Down | Short covering | Shorts are closing by buying back. Price rises, but it may not be fresh long-term buying. |
| Down | Down | Long unwinding | Longs are exiting. Price falls as existing buyers close positions. |

Important warning: this table is a useful clue, not proof. OI data does not reveal every participant's intention, hedge, or portfolio context.

---

# 20. Beginner Translation Examples

## "Short covering hua"

Meaning:

```text
Traders who had sold short are now buying back to close their shorts.
Their buying can push price upward.
This rise may be due to forced exit, not necessarily fresh bullish investment.
```

Example:

```text
Stock future falls from 500 to 450.
Many traders shorted.
Then price rises from 450 to 470 while OI falls.
This can indicate short covering.
```

## "Long unwinding ho raha hai"

Meaning:

```text
People who were already long are exiting.
Price falls and OI falls.
This is different from fresh shorting.
```

## "Fresh short buildup"

Meaning:

```text
New traders are creating short positions.
Price falls and OI rises.
This usually shows bearish pressure.
```

## "IV crush"

Meaning:

```text
Implied volatility falls sharply after an event.
Option premiums drop.
An option buyer can lose money even if direction was partly correct.
```

## "Margin call"

Meaning:

```text
Your losses or margin requirement increased.
Broker/exchange asks for more funds.
If you do not add funds, position may be squared off.
```

## "Gap risk"

Meaning:

```text
Price opens far above or below previous close.
Your stop loss may execute much worse than planned.
Overnight positions carry gap risk.
```

## "Priced in"

Meaning:

```text
The market already expected the news.
When the news actually comes, price may not move much.
Sometimes good news can still lead to a fall if expectations were even higher.
```

## "Rollover"

Meaning:

```text
A futures/options position near expiry is shifted to a later expiry.
The trader closes current expiry and opens next expiry.
This has cost, slippage, and basis impact.
```

---

# 21. Final Rule

Whenever you hear market jargon, do not stop at the word. Translate it into action, risk, and evidence.

```text
Jargon -> What happened? -> Who is trapped or gaining? -> What data proves it? -> What is the risk?
```

If you cannot translate a term into plain language, do not trade based on that term yet. Look it up, understand the mechanism, then decide whether it matters for your actual position.
