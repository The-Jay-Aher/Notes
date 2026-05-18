# Fundamental analysis framework for a stock or an index

## Quick Summary

This note is a detailed framework for analyzing a stock or index from primary sources. It focuses on business exposure, economics, accounting quality, normalized financial statements, valuation, risks, index construction, and cross-standard comparability across IFRS, US GAAP, Ind AS, local GAAP, banks, insurers, and sector-specific reporting.

Fundamental analysis is not “check PE ratio and feel wise.” That is how people turn Excel into a slot machine. Proper fundamental analysis is a disciplined process for answering four questions:

1. **What is the business or index actually exposed to?**
2. **How good are the economics?**
3. **How reliable are the reported numbers?**
4. **What is it worth versus the market price?**

For a stock, the unit of analysis is a company/security. For an index, the unit of analysis is a basket of companies, weights, sectors, currencies, accounting regimes, and index rules. The index part is where people often get sloppy, because apparently “Nifty is expensive” or “S&P is cheap” feels scientific enough if said confidently.

The framework below is designed to work across **IFRS, US GAAP, Ind AS, local GAAP, bank reporting, insurance reporting, and company-specific reporting labels**. The trick is not memorizing every possible line-item name. The trick is building a **normalization layer** that maps raw reported labels into analytical concepts while preserving the original accounting treatment.

---

# 1. Start with the correct objective

Before touching a ratio, define the purpose.

## For a stock

You are trying to estimate:

| Question                              | What you need to know                                               |
| ------------------------------------- | ------------------------------------------------------------------- |
| Is this business financially healthy? | Liquidity, solvency, cash flow, debt maturity, profitability        |
| Is it growing?                        | Revenue, earnings, cash flow, market share, reinvestment efficiency |
| Is growth valuable?                   | ROIC versus cost of capital                                         |
| Are earnings real?                    | Cash conversion, accruals, working capital, accounting quality      |
| Is management trustworthy?            | Capital allocation, governance, related-party transactions          |
| Is the price attractive?              | DCF, multiples, asset value, margin of safety                       |
| What can break the thesis?            | Leverage, competition, regulation, fraud risk, cyclicality          |

## For an index

You are trying to estimate:

| Question                              | What you need to know                                            |
| ------------------------------------- | ---------------------------------------------------------------- |
| What does the index really own?       | Constituents, weights, sectors, countries, currencies            |
| Is valuation attractive?              | Aggregate PE, PB, EV/EBITDA, dividend yield, earnings yield      |
| Is the index concentrated?            | Top 5/10 weights, sector dominance, single-stock dependence      |
| Are earnings broad-based?             | Breadth of earnings growth, sector contribution                  |
| What macro factors dominate?          | Rates, FX, commodities, credit cycle, policy                     |
| How does methodology affect exposure? | Float adjustment, rebalancing, eligibility rules                 |
| Is the ETF/fund tracking it clean?    | Tracking error, fees, replication, securities lending, liquidity |

CFA Institute describes financial analysis as interpreting a company’s performance and position in the context of its economic environment, which is the right framing: numbers without context are just accounting confetti. ([CFA Institute][1])

---

# 2. Use the right source hierarchy

Do not rely on screenshots, social media summaries, broker app ratios, or finance websites as the primary source. Those are useful for quick checks, not serious analysis.

## Primary sources for a listed stock

Use these in order:

| Source                                    | Use                                                         |
| ----------------------------------------- | ----------------------------------------------------------- |
| Annual report / 10-K / 20-F               | Full audited business, risk, financial, and note disclosure |
| Quarterly report / 10-Q / interim results | Recent performance                                          |
| Earnings release                          | Management’s presentation of recent results                 |
| Investor presentation                     | Strategy, KPIs, segment data, guidance                      |
| Earnings call transcript                  | Management tone, explanations, analyst pushback             |
| Proxy / governance filing                 | Compensation, ownership, board, related-party matters       |
| Credit rating report                      | Debt, liquidity, covenant, credit risk                      |
| Exchange filings                          | Material announcements                                      |
| Corporate action filings                  | Splits, buybacks, rights issues, dividends                  |
| Regulator filings                         | Industry-specific risk, capital, solvency                   |

For US-listed companies, Form 10-K is the comprehensive annual filing and includes audited financial statements; the SEC’s EDGAR system is the official place to retrieve filings. ([Investor][2]) Foreign private issuers in the US commonly use Form 20-F, and the SEC accepts IFRS financial statements from foreign private issuers when prepared under IFRS as issued by the IASB without US GAAP reconciliation. ([SEC][3])

## Primary sources for an index

For an index, gather:

| Source                                 | Use                                                     |
| -------------------------------------- | ------------------------------------------------------- |
| Index methodology document             | Eligibility, weighting, rebalancing, float adjustment   |
| Current constituents                   | What the index owns today                               |
| Historical constituents                | Avoid survivorship bias                                 |
| Constituent weights                    | Actual exposure                                         |
| Sector/country/currency classification | Risk decomposition                                      |
| Index factsheet                        | Summary metrics                                         |
| ETF/fund holdings                      | Actual investable product exposure                      |
| ETF prospectus                         | Replication, fees, derivatives, lending, tracking error |

Many equity indexes are free-float adjusted rather than simply weighted by total shares outstanding. MSCI defines free float as the proportion of shares outstanding deemed available for purchase in public markets. ([MSCI][4]) That matters because promoter/government/strategic holdings may be excluded or partially excluded.

---

# 3. The accounting-standard-proof framework

You said you do not want to miss something because it is written differently. Good. That is exactly where most amateur analysis breaks.

You need three layers:

## Layer 1: Raw reported facts

Store what the company reported exactly.

Example:

| Field                      | Example                 |
| -------------------------- | ----------------------- |
| Company                    | Tata Motors             |
| Filing                     | Annual report FY2025    |
| Reporting standard         | Ind AS                  |
| Statement                  | Profit and loss         |
| Raw label                  | Revenue from operations |
| Amount                     | ₹X million              |
| Period                     | FY2025                  |
| Currency                   | INR                     |
| Source page / note         | Note 28                 |
| Taxonomy tag, if available | XBRL tag                |
| Sign                       | Positive or negative    |
| Consolidated or standalone | Consolidated            |

Never destroy the raw label. Never silently “correct” the company’s terminology. Preserve the source like evidence at a crime scene, because sometimes accounting is basically a legally formatted hiding place.

## Layer 2: Normalized analytical concepts

Map different labels into one analytical concept.

Example:

| Raw labels                                                                               | Normalized concept    |
| ---------------------------------------------------------------------------------------- | --------------------- |
| Revenue, sales, net sales, turnover, revenue from operations                             | Revenue               |
| Cost of revenue, cost of goods sold, raw materials consumed, purchases of stock-in-trade | Cost of revenue       |
| Borrowings, loans, notes payable, debentures, bonds, lease liabilities                   | Debt-like liabilities |
| Trade receivables, accounts receivable, sundry debtors                                   | Receivables           |
| Property, plant and equipment, fixed assets, tangible assets                             | PPE                   |
| Cash flow from operating activities, net cash provided by operations                     | CFO                   |

## Layer 3: Analytical adjustments

This is where you adjust for accounting differences.

Examples:

| Issue                                                                | Adjustment                                                                    |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| IFRS company capitalizes development cost, US GAAP peer expenses R&D | Either expense all development costs or capitalize R&D analytically for both  |
| One company reports operating lease expense differently              | Normalize lease debt and lease interest                                       |
| Company uses LIFO inventory under US GAAP                            | Adjust using LIFO reserve if disclosed                                        |
| Company reports large “adjusted EBITDA”                              | Rebuild EBITDA yourself                                                       |
| One-time restructuring appears every year                            | Treat it as recurring, because apparently “one-time” has a subscription model |
| Acquisition-related amortization distorts operating profit           | Analyze both GAAP EBIT and cash operating earnings                            |
| Foreign currency translation affects equity                          | Separate operating performance from FX translation                            |

---

# 4. Accounting standards you must support

A robust framework should be standard-aware, not standard-dependent.

## Major standards and regimes

| Standard / regime                                     | Where commonly relevant                          |
| ----------------------------------------------------- | ------------------------------------------------ |
| IFRS Accounting Standards                             | Many global listed companies                     |
| US GAAP                                               | US companies                                     |
| Ind AS                                                | Many Indian companies                            |
| Local GAAP                                            | Smaller domestic companies in many jurisdictions |
| Japanese GAAP                                         | Japan                                            |
| China Accounting Standards                            | China                                            |
| UK GAAP / FRS                                         | Some UK entities                                 |
| Bank regulatory reporting                             | Banks                                            |
| Insurance statutory / IFRS 17 / local insurance rules | Insurers                                         |
| REIT / property-specific reporting                    | Real estate vehicles                             |
| Non-GAAP / alternative performance measures           | Management-adjusted metrics                      |

IFRS is widely used globally; the IFRS Foundation says IFRS Accounting Standards are required in more than 140 jurisdictions. ([IFRS][5]) US GAAP is organized through the FASB Accounting Standards Codification, which FASB describes as the single official source of authoritative nongovernmental US GAAP. ([FASB][6]) In India, Ind AS materials and notifications are maintained through ICAI/MCA-related resources, including updates to the Companies Indian Accounting Standards Rules. ([ICAI][7])

## Use taxonomies when available

For machine-readable analysis, use official XBRL taxonomies where possible:

| Taxonomy                 | Use                              |
| ------------------------ | -------------------------------- |
| IFRS Accounting Taxonomy | IFRS-tagged financial statements |
| US GAAP Taxonomy         | US GAAP XBRL filings             |
| Local taxonomies         | Jurisdiction-specific filings    |

The IFRS Accounting Taxonomy exists to tag IFRS financial statements digitally so investors can extract, compare, and analyze them more efficiently. ([IFRS][8]) FASB also maintains GAAP reporting taxonomies, including the 2025 GAAP Financial Reporting Taxonomy. ([FASB][9])

But do not trust tags blindly. Companies use custom extensions, classify things oddly, and occasionally treat XBRL like a creative writing exercise. Always reconcile tagged data to the statement and notes.

---

# 5. Minimum financial statement package

Under IFRS, IAS 1 sets out overall requirements for financial statement presentation and requires a complete set of financial statements at least annually with comparative information. ([IFRS][10]) IFRS 18 will replace IAS 1 for annual reporting periods beginning on or after January 1, 2027, with earlier application permitted, so your system should be ready for presentation changes. ([IFRS][11])

For any serious analysis, collect:

| Statement                                       | What it tells you                        |
| ----------------------------------------------- | ---------------------------------------- |
| Income statement / profit and loss              | Revenue, margins, profit, taxes          |
| Balance sheet / statement of financial position | Assets, liabilities, equity, leverage    |
| Cash flow statement                             | Cash generation, capex, financing        |
| Statement of changes in equity                  | Dilution, buybacks, dividends, OCI       |
| Notes to accounts                               | The hidden machinery                     |
| Segment reporting                               | Business-level economics                 |
| Accounting policy note                          | How numbers were measured                |
| Auditor report                                  | Audit opinion, key audit matters         |
| Management discussion                           | Strategy, risks, performance explanation |

The notes are not optional. They are where leases, debt maturities, revenue recognition, related-party transactions, contingencies, pensions, provisions, stock compensation, and segment details live. Ignoring notes is like inspecting a car by admiring the paint.

---

# 6. Universal line-item mapping dictionary

This is the part that protects you from missing something just because it is written differently.

## Income statement mapping

| Normalized concept       | Possible labels                                                                                      | Watch-outs                                                         |
| ------------------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Revenue                  | Revenue, net sales, sales, turnover, revenue from operations, gross written premium, interest income | Banks and insurers do not behave like industrial companies         |
| Other operating income   | Other operating revenue, ancillary income, service income                                            | May include recurring or non-recurring items                       |
| Cost of revenue          | COGS, cost of sales, cost of revenue, raw materials consumed, purchases of stock-in-trade            | Presentation by nature vs function changes labels                  |
| Gross profit             | Gross margin, gross operating profit                                                                 | Not always reported                                                |
| Employee cost            | Salaries, wages, staff cost, personnel expense                                                       | Important for service/software companies                           |
| R&D expense              | Research and development, product development, engineering expense                                   | May be expensed or capitalized depending on standard               |
| SG&A                     | Selling, general and administrative, distribution, admin expense                                     | Some companies split these                                         |
| Depreciation             | Depreciation, depletion, amortization of PPE                                                         | Separate from intangible amortization if possible                  |
| Amortization             | Amortization of intangibles, acquired intangible amortization                                        | Acquisition-heavy firms can look optically worse                   |
| Operating profit         | EBIT, operating income, profit from operations                                                       | Company-defined “adjusted operating profit” may exclude real costs |
| EBITDA                   | Earnings before interest, tax, depreciation, amortization                                            | Not a GAAP metric; rebuild it yourself                             |
| Finance income           | Interest income, investment income                                                                   | Banks treat this differently                                       |
| Finance cost             | Interest expense, borrowing cost, lease interest                                                     | Include debt-like costs                                            |
| Share of associates/JVs  | Equity-accounted investee income                                                                     | May be operational or investment-like                              |
| Profit before tax        | PBT, income before taxes                                                                             | Useful for tax normalization                                       |
| Tax expense              | Current tax, deferred tax                                                                            | Separate cash tax from accounting tax                              |
| Net income               | Profit after tax, PAT, net profit, earnings attributable                                             | Use income attributable to common shareholders for EPS             |
| Non-controlling interest | Minority interest, NCI                                                                               | Needed for valuation and ownership claims                          |
| EPS                      | Basic EPS, diluted EPS                                                                               | Always use diluted when assessing public equity                    |

## Balance sheet mapping

| Normalized concept     | Possible labels                                                | Watch-outs                                     |
| ---------------------- | -------------------------------------------------------------- | ---------------------------------------------- |
| Cash                   | Cash, bank balances, cash and cash equivalents                 | Restricted cash should be separated            |
| Short-term investments | Marketable securities, treasury bills, liquid investments      | Check fair value and liquidity                 |
| Receivables            | Trade receivables, accounts receivable, sundry debtors         | Rising faster than revenue is a warning        |
| Contract assets        | Unbilled revenue, accrued revenue                              | Can signal aggressive revenue recognition      |
| Inventory              | Inventories, stock, raw materials, WIP, finished goods         | Obsolescence risk                              |
| PPE                    | Property plant equipment, fixed assets, tangible assets        | Revaluation differences matter                 |
| Right-of-use assets    | ROU assets, lease assets                                       | Lease accounting normalization required        |
| Goodwill               | Goodwill on consolidation                                      | Watch acquisition excess and impairment        |
| Intangibles            | Brands, patents, software, licenses, development assets        | Internally generated vs acquired matters       |
| Investments            | Associates, JVs, financial assets                              | Fair value versus equity method                |
| Deferred tax asset     | DTA                                                            | May depend on future profitability             |
| Debt                   | Borrowings, loans, debentures, bonds, notes payable            | Split current and non-current                  |
| Lease liabilities      | Lease obligations                                              | Debt-like for most analytical purposes         |
| Payables               | Trade payables, accounts payable, creditors                    | DPO and supplier financing matter              |
| Provisions             | Legal, warranty, restructuring, decommissioning                | May hide future cash outflows                  |
| Contract liabilities   | Deferred revenue, customer advances                            | Good for SaaS, risky if obligations rise oddly |
| Pension liabilities    | Retirement benefit obligations                                 | Often buried in notes                          |
| Equity                 | Share capital, securities premium, retained earnings, reserves | OCI and revaluation reserves matter            |
| Treasury stock         | Treasury shares, own shares                                    | Reduces equity                                 |
| NCI                    | Non-controlling interest                                       | Deduct when valuing common equity              |

## Cash flow mapping

| Normalized concept             | Possible labels                                                      | Watch-outs                                          |
| ------------------------------ | -------------------------------------------------------------------- | --------------------------------------------------- |
| CFO                            | Cash flow from operations, net cash provided by operating activities | Compare to net income                               |
| Cash generated from operations | Operating cash before tax/interest                                   | Classification differs by standard                  |
| Working capital movement       | Change in receivables, inventory, payables                           | Large swings can distort CFO                        |
| Capex                          | Purchase of PPE, capital expenditure, acquisition of fixed assets    | Maintenance vs growth capex matters                 |
| Intangible capex               | Purchase/development of intangibles, software capitalization         | Crucial for tech/pharma                             |
| Acquisitions                   | Purchase of subsidiaries/businesses                                  | Do not mix with organic capex blindly               |
| Asset sales                    | Proceeds from sale of PPE/investments                                | Non-recurring cash inflow                           |
| Debt issued/repaid             | Proceeds/repayment of borrowings                                     | Financing health                                    |
| Dividends paid                 | Dividend distribution                                                | Sometimes operating/financing classification varies |
| Buybacks                       | Purchase of own shares                                               | Capital allocation and EPS effect                   |
| Free cash flow                 | CFO minus capex                                                      | Define your formula explicitly                      |

IAS 7 requires cash flows to be classified into operating, investing, and financing activities, but IFRS allows some flexibility for interest and dividends classification outside financial institutions. ([IFRS][12]) So when comparing companies, reclassify cash flows consistently.

---

# 7. Important accounting differences that can distort analysis

This section is essential. Same business, different accounting standard, different reported result. Welcome to civilization.

## 7.1 R&D and development costs

Under IFRS IAS 38, research expenditure is expensed, while development expenditure meeting specified criteria is capitalized as an intangible asset. ([IFRS][13]) Under US GAAP, R&D costs in the scope of ASC 730 are generally expensed as incurred, with specific exceptions such as certain software-related accounting. ([Viewpoint][14])

### Analytical problem

A US software company may expense most R&D immediately. An IFRS company may capitalize part of development cost. The IFRS company may show higher current profit, higher assets, and lower current expense.

### Adjustment options

Use one of two approaches:

| Approach                   | Method                                                                      |
| -------------------------- | --------------------------------------------------------------------------- |
| Conservative comparability | Expense all capitalized development costs                                   |
| Economic comparability     | Capitalize R&D for all companies and amortize over an estimated useful life |

For high-growth tech, pharma, and engineering companies, ignoring this can wreck comparability.

---

## 7.2 Leases

IFRS 16 uses a single lessee accounting model and generally requires recognition of right-of-use assets and lease liabilities for leases longer than 12 months, unless low-value exemptions apply. ([IFRS][15]) US GAAP ASC 842 also brings leases onto the balance sheet, but retains finance versus operating lease classification effects in income statement and cash flow presentation. ([storage.fasb.org][16])

### Analytical problem

Lease-heavy companies such as retailers, airlines, logistics firms, and restaurants may look less leveraged if lease liabilities are ignored.

### Adjustment

Treat most lease liabilities as debt-like. For valuation:

```text
Enterprise Value = Market Cap + Debt + Lease Liabilities + Preferred Equity + NCI - Cash & Equivalents
```

For EBITDA comparisons, be careful: IFRS 16 can inflate EBITDA because lease expense is split into depreciation and interest.

---

## 7.3 Inventory

Under IFRS, LIFO is prohibited; US GAAP allows LIFO. ([KPMG][17])

### Analytical problem

In inflationary periods, LIFO can reduce reported profit and lower inventory carrying value. FIFO and weighted-average companies may look more profitable.

### Adjustment

If a US GAAP company uses LIFO and discloses a LIFO reserve:

```text
FIFO Inventory = LIFO Inventory + LIFO Reserve
FIFO Equity ≈ Reported Equity + LIFO Reserve × (1 - Tax Rate)
FIFO COGS Adjustment = Change in LIFO Reserve
```

---

## 7.4 PPE and revaluation

IAS 16 permits PPE to be carried using either the cost model or, where fair value can be measured reliably, a revaluation model. ([IFRS][18])

### Analytical problem

Two identical property-heavy businesses may report very different asset bases and equity depending on historical cost versus revaluation.

### Adjustment

For ROIC, ROA, and leverage:

* Identify revaluation reserves.
* Separate operating asset value from accounting uplift.
* Use replacement cost or appraised NAV where relevant.
* For real estate and infrastructure, asset value may be more meaningful than book cost.

---

## 7.5 Revenue terminology and recognition

Different companies may use:

* Revenue
* Net sales
* Turnover
* Revenue from operations
* Gross sales less discounts
* Net interest income
* Premium income
* Contract revenue

Do not blindly map all top-line labels to “sales.” Banks, insurers, brokers, and asset managers have sector-specific revenue structures.

### Questions to answer

| Question                                | Why it matters                                            |
| --------------------------------------- | --------------------------------------------------------- |
| Is revenue gross or net?                | Marketplace/platform companies may report only commission |
| Is the company principal or agent?      | Affects reported revenue scale                            |
| Are returns, rebates, discounts netted? | Affects true price realization                            |
| Are contract assets growing?            | Could signal aggressive revenue recognition               |
| Is revenue cash-backed?                 | Revenue without cash is a polite hallucination            |
| Is deferred revenue rising?             | Can be healthy for subscriptions                          |
| Are customers concentrated?             | Revenue fragility                                         |

---

## 7.6 Goodwill and acquisition accounting

Goodwill appears when a company buys another company for more than identifiable net assets.

### Watch-outs

* Serial acquisitions can inflate assets and hide weak organic growth.
* Impairments may arrive late.
* “Adjusted earnings” often exclude amortization and acquisition costs.
* Earn-outs and contingent consideration can affect future earnings.
* Purchase price allocation can distort margins.

### Adjustment

Analyze:

```text
Organic Revenue Growth = Reported Revenue Growth - Acquisition Contribution - FX Impact
```

Also compare:

```text
Cash ROIC = Cash Operating Profit / Tangible Invested Capital
```

---

## 7.7 Deferred taxes

Deferred tax assets and liabilities can distort book value and earnings.

### Watch-outs

| Item                                                | Meaning                                       |
| --------------------------------------------------- | --------------------------------------------- |
| Deferred tax asset from losses                      | Only valuable if future taxable profit exists |
| Valuation allowance                                 | Management doubts recoverability              |
| Deferred tax liability from revaluation/intangibles | May not be immediate cash debt                |
| Low cash taxes versus reported tax                  | Could reverse later                           |

Use normalized cash tax rates for valuation, not just reported effective tax rate.

---

## 7.8 Share-based compensation

Stock compensation is real dilution, not fairy dust.

### Common mistake

Companies add back stock-based compensation to “adjusted EBITDA” and pretend shareholders are not diluted. Cute. Wrong.

### Treatment

Analyze both:

```text
Cash FCF before SBC
Economic FCF after SBC
Diluted share count impact
Buybacks required to offset SBC dilution
```

---

## 7.9 Minority interest / non-controlling interest

If a parent consolidates a subsidiary it does not fully own, revenue and EBITDA may include 100% of the subsidiary, but shareholders only own part of it.

### Correct treatment

For enterprise value multiples:

```text
EV includes NCI
EBITDA includes consolidated EBITDA
```

For equity valuation:

```text
Net Income to Common = Net Income - NCI Share
```

---

# 8. Full stock fundamental analysis process

## Step 1: Identify exactly what security you are analyzing

Do not skip this. A company and a stock are not always the same economic claim.

Check:

| Item                                 | Why it matters                                            |
| ------------------------------------ | --------------------------------------------------------- |
| Ticker                               | Basic identifier                                          |
| ISIN / CUSIP / SEDOL                 | Avoid ticker confusion                                    |
| Share class                          | Voting rights, economics                                  |
| ADR/GDR ratio                        | Foreign listings may represent multiple underlying shares |
| Holding company vs operating company | Claim on cash flows may be indirect                       |
| VIE structure                        | Important for some China-related listings                 |
| Common vs preferred shares           | Different claims                                          |
| Fully diluted shares                 | Options, RSUs, convertibles                               |
| Treasury shares                      | Buybacks and share count                                  |
| Promoter/insider ownership           | Control risk                                              |
| Free float                           | Liquidity and index inclusion                             |
| Pledged shares                       | Forced selling risk                                       |
| Currency                             | Reporting and trading currency may differ                 |

Compute:

```text
Market Cap = Share Price × Diluted Shares Outstanding
Enterprise Value = Market Cap + Debt + Lease Liabilities + Preferred Equity + NCI -Cash & Investments
```

Use diluted shares unless there is a good reason not to.

---

## Step 2: Understand the business model

Answer this in plain English:

> How does the company make money, from whom, why do customers pay, and what could stop them?

Break down:

| Area                  | Questions                                                                   |
| --------------------- | --------------------------------------------------------------------------- |
| Products/services     | What is sold? Is it essential or discretionary?                             |
| Customers             | Consumers, enterprises, government, financial institutions?                 |
| Revenue model         | One-time sales, subscriptions, transaction fees, interest spread, premiums? |
| Pricing power         | Can the company raise prices?                                               |
| Cost structure        | Fixed vs variable costs                                                     |
| Capital intensity     | Does growth require heavy capex?                                            |
| Working capital       | Does growth consume or generate cash?                                       |
| Unit economics        | Contribution margin, CAC, payback, churn                                    |
| Distribution          | Direct, dealer, platform, marketplace                                       |
| Competitive advantage | Brand, cost, network effects, regulation, switching costs                   |
| Regulation            | Licenses, tariffs, capital requirements                                     |
| Cyclicality           | Sensitive to GDP, rates, commodities, FX?                                   |

A good business usually has some combination of:

* High gross margin
* Pricing power
* Recurring revenue
* Low customer churn
* Low maintenance capex
* Strong cash conversion
* High ROIC
* Low leverage
* Durable competitive advantage

A bad business can still be a good stock if priced cheaply. A great business can be a terrible stock if priced like it has discovered immortality.

---

## Step 3: Analyze industry and macro context

Fundamentals do not exist in a vacuum.

Check:

| Factor            | Examples                                       |
| ----------------- | ---------------------------------------------- |
| Industry growth   | Is the market expanding or shrinking?          |
| Market structure  | Monopoly, oligopoly, fragmented competition    |
| Entry barriers    | Capital, regulation, brand, tech, distribution |
| Supplier power    | Commodity inputs, labor, key vendors           |
| Customer power    | Concentrated customers, price sensitivity      |
| Substitution risk | New technologies, changing consumer behavior   |
| Regulation        | Tariffs, taxes, price controls, licensing      |
| Interest rates    | Banks, real estate, leveraged firms            |
| Inflation         | Pricing power vs cost pressure                 |
| Currency          | Exporters/importers, foreign debt              |
| Commodity prices  | Energy, metals, chemicals, agriculture         |
| Credit cycle      | NBFCs, banks, real estate                      |
| Political risk    | Defense, infrastructure, utilities             |

For cyclical companies, never value peak earnings as normal earnings. That is how people buy commodity stocks right before earnings fall off a cliff, then call it “long-term investing” to preserve dignity.

---

## Step 4: Analyze management and governance

Numbers tell you what happened. Governance tellu whether you can trust what happened.

Check:

| Area                          | What to inspect                                   |
| ----------------------------- | ------------------------------------------------- |
| Promoter/founder ownership    | Alignment or control abuse                        |
| Insider buying/selling        | Signal, not proof                                 |
| Related-party transactions    | Revenue, loans, guarantees, purchases             |
| Auditor                       | Reputation, tenure, resignation                   |
| Audit opinion                 | Qualified, adverse, going concern                 |
| Key audit matters             | Where judgment risk sits                          |
| Board independence            | Real independence or decorative independence      |
| Compensation                  | Linked to ROIC/FCF or just revenue/EBITDA?        |
| Capital allocation            | Buybacks, dividends, acquisitions, debt reduction |
| Dilution history              | Frequent equity issuance                          |
| Pledging                      | Promoter shares pledged against loans             |
| Political/regulatory exposure | Especially infrastructure, finance, utilities     |

Red flags:

* Auditor resignation
* Frequent CFO changes
* Late filings
* Qualified audit opinion
* Related-party sales
* Loans to promoter-linked entities
* Constant “adjusted” metrics
* Large unexplained receivables
* Weak internal controls
* Promoter share pledging
* Aggressicquisitions
* Repeated equity dilution

---

# 9. Financial statement analysis

## 9.1 Income statement analysis

Analyze at least 5 years if available. For cyclical businesses, use 10 years if possible.

### Revenue analysis

Calculate:

```text
Revenue Growth = Revenue_t / Revenue_t-1 - 1
CAGR = (Revenue_final / Revenue_initial)^(1 / years) - 1
```

Break revenue by:

| Dimension              | Why                                         |
| ---------------------- | ------------------------------------------- |
| Segment                | Different businesses have different margins |
| Geography              | FX, regulation, country risk                |
| Product                | Growth drivers                              |
| Customer type          | Concentration                               |
| Organic vs acquisition | Quality of growth                           |
| Price vs volume        | Pricing power                               |
| Recurring vs one-time  | Durability                                  |

Revenue red flags:

* Revenue grows but cash collection weakens
* Receivables grow faster than revenue
* Contract assets rise sharply
* Large quarter-end sales
* Heavy discounts hidden in gross/net presentation
* Related-party customers
* Revenue concentration in one customer
* Management changes revenue definitions

---

### Margin analysis

Calculate:

```text
Gross Margin = Gross Profit / Revenue
EBIT Margin = EBIT / Revenue
EBITDA Margin = EBITDA / Revenue
Net Margin = Net Income / Revenue
```

Trend each margin over time.

Ask:

| Margin movement                    | Possible meaning                            |
| ---------------------------------- | ------------------------------------------- |
| Gross margin rising                | Pricing power, mix shift, lower input costs |
| Gross margin falling               | Competition, inflation, discounting         |
| SG&A rising faster than revenue    | Weak operating leverage                     |
| R&D falling                        | Could be efficiency or underinvestment      |
| EBITDA rising but CFO weak         | Accounting quality issue                    |
| Net margin rising from tax benefit | Not operating improvement                   |

---

### Operating leverage

Operating leverage matters when fixed costs are high.

```text
Operating Leverage ≈ % Change in EBIT / % Change in Revenue
```

High operating leverage is beautiful in growth and brutal in decline. Like most human inventions.

---

### Non-recurring items

Separate:

| Item                      | Treatment                              |
| --------------------------- | -------------------------------------- |
| Litigation settlement       | Usually non-recurring, unless frequent |
| Restructuring               | Non-recurring only if truly occasional |
| Asset impairment            | Non-cash but economically meaningful   |
| FX gain/loss                | Depends on recurring exposure          |
| Gain on asset sale          | Exclude from operating earnings        |
| Acquisition costs           | Adjust but monitor frequency           |
| Disaster/insurance proceeds | Usually non-recurring                  |
| Government grants           | Maybe recurring depending on policy    |

Rule: if a company has “one-time” charges every year, they are recurring.

---

## 9.2 Balance sheet analysis

The balance sheet answers:

* What does the company own?
* What does it owe?
* How much risk sits between assets and liabilities?
* How much accounting judgment is embedded?

### Liquidity
culate:

```text
Current Ratio = Current Assets / Current Liabilities
Quick Ratio = (Cash + Marketable Securities + Receivables) / Current Liabilities
Cash Ratio = Cash / Current Liabilities
```

But context matters. Retailers may have low current ratios because inventory turns quickly. Banks require a completely different framework.

---

### Working capital

Calculate:

```text
Net Working Capital = Receivables + Inventory - Payables
```

For operating analysis, exclude cash, debt, tax balances, and non-operating items.

Efficiency ratios:

```text
DSO = Receivables / Revenue × 365
DIO = Inventory / COGS × 365
DPO = Payables / COGS × 365
Cash Conversion Cycle = DSO + DIO - DPO
```

Watch:

| Signal                         | Meaning                              |
| ------------------------------ | ------------------------------------ |
| DSO rising                     | Slower collections, aggressive sales |
| Inventory rising               | Demand weakness or buildup           |
| DPO rising                  | Supplier financing or stress         |
| Negative working capital       | Can be powerful if sustainable       |
| Sudden working capital release | May be temporary cash boost          |

---

### Debt and leverage

Calculate:

```text
Gross Debt = Short-term Debt + Long-term Debt + Lease Liabilities
Net Debt = Gross Debt - Cash & Equivalents
Net Debt / EBITDA = Net Debt / EBITDA
Interest Coverage = EBIT / Interest Expense
Fixed Charge Coverage = EBITDAR / (Interest + Rent/Lease Payments)
Debt / Equity = Debt / Book Equity
```

Also inspect:

* Debt maturity schedule
* Floating vs fixed rate
* Currency of debt
* Covenants
* Secured vs unsecured debt
* Refinancing risk
* Off-balance sheet commitments
* Guarantees
* Supplier financing
* Factoring/receivables financing

A company does not go bankrupt because net income is ugly. It goes bankrupt because cash and creditors stop cooperating.

---

### Asset quality

Inspect:

| Asset               | Risk                      |
| ------------------- | ------------------------- |
| Receivables         | Collectability            |
| Inventory           | Obsolescence              |
| Goodwill            | Overpaid acquisitions     |
| Intangibles         | Amortization/impairment   |
| Deferred tax assets | Future profit assumption  |
| Investments         | Fair value risk           |
| PPE                 | Obsolescence, revaluation |
| Capitalized costs   | Expense deferral risk     |

---

## 9.3 Cash flow analysis

Cash flow is harder to fake than earnings, though not impossible. Humans are inventive when bonuses are involved.

### Core metrics

```text
Operating Cash Flow = CFO
Capital Expenditure = Purchase of PPE + Purchase/Development of Intangibles
Free Cash Flow = CFO - Capex
FCF Margin = FCF / Revenue
Cash Conversion = CFO / Net Income
FCF Conversion = FCF / Net Income
```

### Analyze CFO

Ask:

| Question                                | Why                    |
| --------------------------------------- | ---------------------- |
| Is CFO consistently above net income?   | Good earnings quality  |
| Is CFO below net income for many years? | Possible accrual issue |
| Is CFO boosted by payables?             | May reverse            |
| Is cash tax unusually low?              | May normalize higher   |
| Is working capital volatile?            | Forecast risk          |

### Capex

Separate:

| Type              | Meaning                            |
| ----------------- | ---------------------------------- |
| Maintenance capex | Required to sustain operations     |
| Growth capex      | Optional expansion                 |
| Regulatory capex  | Required compliance                |
| Intangible capex  | Software, development, licenses    |
| Acquisition spend | External growth, not organic capex |

For valuation, maintenance capex is critical.

Approximation:

```text
Owner Earnings ≈ Net Income
               + Depreciation & Amortization
               - Maintenance Capex
               - Required Working Capital Investment
```

---

## 9.4 Statement  changes in equity

This statement often gets ignored. Do not.

Check:

| Item                | Why                                         |
| ------------------- | ------------------------------------------- |
| Share issuance      | Dilution                                    |
| Buybacks            | Capital return or SBC offset                |
| Dividends           | Payout sustainability                       |
| OCI                 | FX translation, pension, fair value changes |
| Revaluation reserve | Asset uplift under some standards           |
| Retained earnings   | Cumulative profitability                    |
| NCI movement        | Ownership changes                           |
| Stock options/RSUs  | Future dilution                             |

Calculate:

```text
Dilution Rate = Diluted Shares_t / Diluted Shares_t-1 - 1
Buyback Yield = Buyback Amount / Market Cap
Dividend Yield = Dividend per Share / Share Price
Total Shareholder Yield = Dividend Yield + Buyback Yield - Dilution
```

---

# 10. Ratio framework

Ratios are useful only after normalization. Otherwise you are dividing one accounting mess by another and calling it insight.

## 10.1 Growth ratios

| Ratio             | Formula                           |
| ----------------- | --------------------------------- |
| Revenue growth    | Revenue_t / Revenue_t-1 - 1       |
| EBITDA growth     | EBITDA_t / EBITDA_t-1 - 1         |
| EBIT growth       | EBIT_t / EBIT_t-1 - 1             |
| EPS growth        | EPS_t / EPS_t-1 - 1               |
| FCF growth        | FCF_t / FCF_t-1 - 1               |
| Book value growth | Book Value_t / Book Value_t-1 - 1 |

Check organic growth separately.

---

## 10.2 Profitability ratios

| Ratio         | Formula                              |
| ------------- | ------------------------------------ |
| Gross margin  | Gross Profit / Revenue               |
| EBITDA margin | EBITDA / Revenue                     |
| EBIT margin   | EBIT / Revenue                       |
| Net margin    | Net Income / Revenue                 |
| ROA           | Net Income / Total Assets            |
| ROE           | Net Income to Common / Common Equity |
| ROIC          | NOPAT / Invested Capital             |

ROIC is one of the most important.

```text
NOPAT = EBIT × (1 - Tax Rate)

Invested Capital =
  Net Working Capital
+ Net PPE
+ Operating Intangibles
+ Right-of-use Assets
+ Other Operating Assets
- Operating Liabilities
```

Alternative:

```text
Invested Capital = Debt + Lease Liabilities + Equity + NCI - ExcessCash - Non-operating Investments
```

Interpretation:

| ROIC result            | Meaning                                        |
| ---------------------- | ---------------------------------------------- |
| ROIC > WACC            | Value creation                                 |
| ROIC ≈ WACC            | Value neutral                                  |
| ROIC < WACC            | Value destruction                              |
| High growth + low ROIC | Faster destruction, just with better marketing |---

## 10.3 Efficiency ratios

| Ratio                 | Formula                     |
| --------------------- | --------------------------- |
| Asset turnover        | Revenue / Total Assets      |
| Receivables turnover  | Revenue / Receivables       |
| Inventory turnover    | COGS / Inventory            |
| Payables turnover     | COGS / Payables             |
| DSO                   | Receivables / Revenue × 365 |
| DIO                   | Inventory / COGS × 365      |
| DPO                   | Payaes / COGS × 365       |
| Cash conversion cycle | DSO + DIO - DPO             |

---

## 10.4 Liquidity ratios

| Ratio                      | Formula                                               |
| -------------------------- | ----------------------------------------------------- |
| Current ratio              | Current Assets / Current Liabilities                  |
| Quick ratio                | Cash + Securities + Receivables / Current Liabilities |
| Cash ratio                 | Cash / Current Liabiities                            |
| CFO to current liabilities | CFO / Current Liabilities                             |

---

## 10.5 Solvency ratios

| Ratio                    | Formula                   |
| ------------------------ | ------------------------- |
| Net debt / EBITDA        | Net Debt / EBITDA         |
| Gross debt / EBITDA      | Gross Debt / EBITDA       |
| Debt / equity            | Debt / Equity             |
| Interest coverage        | EBIT / Interest Expense   |
| EBITDA interest coverage | EBITDA / Interest Expense |
| FCF / debt               | FCF / Gross Debt          |

For highly leveraged companies, maturity schedule matters more than one clean ratio.

---

## 10.6 Cash flow ratios

| Ratio             | Formula              |
| ----------------- | -------------------- |
| CFO margin        | CFO / Revenue        |
| FCF margin        | FCF / Revenue        |
| CFO / net income  | CFO / Net Income     |
| FCF / net income  | FCF / Net Income     |
| Capex intensity   | Capex / Revenue      |
| Reinvestment rate | Reinvestment / NOPAT |

---

## 10.7 Valuation ratios

| Ratio          | Formula                           | Use                                |
| -------------- | --------------------------------- | ---------------------------------- |
| PE             | Market Cap / Net Income to Common | Mature profitable companies        |
| Forward PE     | Market Cap / Forecast Earnings    | Growth/forecast comparison         |
| PB             | Market Cap / Book Equity          | Banks, insurers, asset-heavy firms |
| EV/Sales       | EV / Revenue                      | Low-profit growth companies        |
| EV/EBITDA      | EV / EBITDA                       | Capital-intensive but imperfect    |
| EV/EBIT        | EV / EBIT                         | Better when depreciation matters   |
| P/FCF          | Market Cap / FCF                  | Cash-generating firms              |
| Dividend yield | DPS / Price                       | Income stocks                      |
| Earnings yield | EPS / Price                       | Inverse of PE                      |
| FCF yield      | FCF / Market Cap                  | Cash return                        |

Do not use EV/EBITDA for banks. Do not use PE for companies with distorted one-time earnings. Do not compare software EV/Sales to cement EV/Sales unless your hobby is nonsense.

---

# 11. Earnings quality framework

Earnings quality asks: are profits real, repeatable, and convertible into cash?

## Key checks

| Check               | Formula / Method                      | Red flag                         |
| ------------------- | ------------------------------------- | -------------------------------- |
| CFO vs net income   | CFO / Net Income                      | Persistently below 1             |
| Accruals            | Net Income - CFO                      | Rising accruals                  |
| Receivables growth  | AR growth vs revenue growth           | AR grows faster                  |
| Inventory growth    | Inventory growth vs COGS/revenue      | Inventory pile-up                |
| Deferred revenue    | Deferred revenue trend                | Falling in subscription business |
| Capitalized costs   | Capitalized cost / expenses           | Rising sharply                   |
| One-time items      | Adjustments over years                | Recurring “one-time” charges     |
| Related-party sales | Note disclosure                       | Material or rising               |
| Tax quality         | Cash tax vs accounting tax        | Persistent gap                   |
| SBC dilution        | SBC and share count                   | Buybacks only offset dilution    |
| Segment mismatch    | Segment profit vs consolidated profit | Corporate cost hiding            |

## Sloan accrual ratio

One common earnings quality measure:

```text
Accrual Ratio = (Net Income - CFO) / Average Total Assets
```

Higher accruals can indicate lower earnings quality.

---

# 12. Normalization adjustments

Before valuation, normalize earnings.

## Common adjustments

| Adjustment              | What to do                                                                      |
| ----------------------- | ------------------------------------------------------------------------------- |
| Restructuring charges   | Exclude only if genuinely non-recurring                                         |
| Litigation              | Exclude one-time settlements, but consider recurring legal risk                 |
| Impairments             | Exclude from normalized EBIT, but include in capital allocation assessment      |
| Acquisition costs       | Exclude from operating earnings, but track if acquisition strategy is recurring |
| FX gains/losses         | Separate operating FX from financing FX                                         |
| SBC                     | Treat as economic cost or model dilution                                        |
| R&D                     | Standardize capitalization/expense policy                                       |
| Leases                  | Add lease liabilities to debt-like obligations                                  |
| Pension cost            | Separate service cost from financing/actuarial effects                          |
| Tax                     | Use normalized tax rate                                                         |
| NCI                     | Use income attributable to common shareholders                                  |
| Discontinued operations | Remove from continuing earnings                                                 |
| Asset sale gains        | Remove from operating profit                                                    |
| Inventory LIFO/FIFO     | Adjust if comparing US GAAP and IFRS peers                                      |

## Rebuild adjusted EBIT

Do not blindly use company-provided adjusted EBIT.

```text
Reported EBIT
+ Truly non-recurring restructuring
+ One-off legal settlement
+ Acquisition transaction costs
- Gain on asset sale
± FX operating adjustment
± R&D normalization
± Leasormalization
= Analyst-normalized EBIT
```

Then:

```text
Normalized NOPAT = Normalized EBIT × (1 - Normalized Tax Rate)
```

---

# 13. Forecasting framework

Forecasts should be driver-based, not “revenue grows 12% because I typed 12%.”

## Revenue forecast

Break revenue into drivers.

Examples:

### Consumer company

```text
Revenue = Volume Sold × Average Selling Price
```

### Bank

```text
Net Interest Income = Earning Assets × Net Interest Margin
Fee Income = AUM / Transactions / Accounts ×e
```

### SaaS

```text
Revenue = Customers × ARPU
Net Revenue Retention = Expansion - Churn
```

### Commodity company

```text
Revenue = Production Volume × Realized Price
```

### Retail

```text
Revenue = Stores × Sales per Store
Same-store Sales Growth
```

## Margin forecast

Forecast:

* Gross margin
* Employee cost
* R&D
* SG&A
* Depreciation
* EBIT margin
* Tax rate

Tie margin changes to real drivers:

| Margin driver | Example                            |
| ------------- | ------------------------------- |
| Pricing power | Price hikes above inflation        |
| Scale         | SG&A grows slower than revenue     |
| Mix           | Higher-margin segment grows faster |
| Input cost    | Raw material inflation             |
| Competition   | Discounting                        |
| Regulation    | Price caps                         |

## Working capital forecast

Forecast:

```text
Receivables = Revenue × DSO / 365
Inventory = COGS × DIO / 365
Payables = COGS × DPO / 365
```

## Capex forecast

:

```text
Capex / Revenue
Capex / Depreciation
Maintenance capex estimate
Growth capex estimate
```

## Debt and interest

Forecast:

```text
Interest Expense = Average Debt × Interest Rate
```

Include refinancing risk.

## Share count

Forecast dilution:

```text
Diluted Shares_t = Diluted Shares_t-1 + SBC Dilution + Convertible Dilution - Buybacks
```

---

# 14. Valuation methods

Use multiple methods. No single valuation model deserves religious devotion.

## 14.1 Discounted cash flow: FCFF

Free cas flow to firm:

```text
FCFF =
  EBIT × (1 - Tax Rate)
+ Depreciation & Amortization
- Capex
- Change in Net Working Capital
```

Value:

```text
Enterprise Value = Σ FCFF_t / (1 + WACC)^t + Terminal Value / (1 + WACC)^n
```

Terminal value:

```text
Gordon Growth TV = FCFF_n × (1 + g) / (WACC - g)
```

Then:

```text
Equity Value =
  Enterprise Value
- Debt
- Lease Liabilities
- Preferred Equity
- NCI
+ Cash & Investments
```

```text
Intrinsic Value per Share = Equity Value / Diluted Shares
```

### DChecks

| Check           | Rule                                                            |
| --------------- | --------------------------------------------------------------- |
| Terminal growth | Should not exceed long-run economy growth unless very justified |
| WACC            | Must reflect business/country/currency risk                     |
| Tax             | Use normalized tax                                              |
| Capex           | Maintenance and growth must make sense                          |
| ROIC            | Terminal ROIC should be realistic                               |
| Working capital | Do not forget growth consumes cash                              |
| Currency        | Cash flows and discount rate must use same currency             |

---

## 14.2 FCFE valuation

Free cash flow to equity:

```text
FCFE =
  Net Income
+ D&A
- Capex
- Change in Working Capital
+ Net Borrowing
```

Use FCFE when capital structure is stable and debt assumptions are explicit.

---

## 14.3 Dividend discount model

Useful for banks, utilities, mature dividend companies.

```text
Value = Dividend_1 / (Cost of Equity - Growth)
```

But if dividend policy is unstable, DDM becomes a decorative formula.

---

## 14.4 Relative valuation

Compare to peers.

Peer selection must match:

| Dimension           | Why                                        |
| ------------------- | ------------------------------------------ |
| Business model      | Software vs hardware is not the same       |
| Geography           | Country risk and growth differ             |
| Size                | Scale affects margins                      |
| Growth              | Higher growth deserves different multiples |
| Margin              | Quality difference                         |
| ROIC                | Value creation                             |
| Leverage            | Risk                                       |
| Accounting standard | Comparability                              |
| Capital intensity   | EV/EBITDA distortions                      |

Use:

```text
EV/EBITDA
EV/EBIT
EV/Sales
PE
PB
P/FCF
Dividend Yield
```

### Multiples sanity

| Multiple       | Common mistake                                 |
| -------------- | ---------------------------------------------- |
| PE             | Using it when earnings are cyclical or one-off |
| EV/EBITDA      | Ignoring capex, leases, working capital        |
| EV/Sales       | Ignoring margins                               |
| PB             | Using it for asset-light companies             |
| P/FCF          | Using one-year working capital boost           |
| Dividend yield | Ignoring payout sustainability                 |

---

## 14.5 Sum-of-the-parts valuation

Use when a company has very different businesses.

Example:

```text
Segment A Value = EBITDA_A × Peer Multiple_A
Segment B Value = Revenue_B × Peer Multiple_B
Segment C Value = Book Value_C × PB Multiple_C
Total EV = Sum Segment Values
Less Net Debt and NCI
= Equity Value
```

SOTP is useful for conglomerates, hong companies, financial groups, and companies with listed subsidiaries.

---

## 14.6 Asset-based valuation

Use for:

* Real estate
* Investment holding companies
* Mining
* Distressed firms
* Liquidation situations
* Banks/insurers in some cases

Methods:

```text
NAV = Fair Value of Assets - Liabilities
Liquidation Value = Recoverable Asset Value - Debt - Wind-down Costs
Replacement Cost = Cost to recreate assets
```

---

# 15. Sector-specific fundamental analysis

Do not force one generic ratio framework onto every sector. Banks are not factories. Insurers are not SaaS firms. REITs are not steel companies. This apparently needed saying.

## 15.1 Banks and lenders

Key metrics:

| Metric                | Formula / Meaning                               |
| --------------------- | ----------------------------------------------- |
| Net interest margin   | Net interest income / earning assets            |
| Loan growth           | Growth in advances                              |
| Deposit growth        | Funding strength                                |
| CASA ratio            | Low-cost deposits, India-specific common metric |
| Cost of funds         | Interest expense / funding base                 |
| Credit cost           | Provisions / loans                              |
| NPA/NPL ratio         | Bad loans / total loans                         |
| Provision coverage    | Provisions / bad loans                          |
| CET1 ratio            | Core regulatory capital                         |
| ROA                   | Net income / assets                             |
| ROE                   | Net income / equity                             |
| Efficiency ratio      | Operating expense / revenue                     |
| Loan-to-deposit ratio | Lending aggressiveness                          |
| Liquidity coverage    | Short-term liquidity strength                   |

Valuation:

```text
PB
PE
ROE versus Cost of Equity
Excess capital
Dividend capacity
```

Do not use EV/EBITDA for banks. Debt is raw material for banks, not just financing.

---

## 15.2 Insurance

Key metrics:

| Metric                | Meaning                         |
| --------------------- | ------------------------------- |
| Gross written premium | Volume                          |
| Net written premium   | Retained premium                |
| Loss ratio            | Claims / premiums               |
| Expense ratio         | Expenses / premiums             |
| Combined ratio        | Loss ratio + expense ratio      |
| Investment yield      | Return on float/investments     |
| Solvency ratio        | Capital strength                |
| Embedded value        | Life insurance valuation metric |
| Persistency           | Policy retention                |
| Reserve adequacy      | Claims risk                     |

Valuation:

```text
P/Embedded Value
PB
ROE
Dividend yield
```

---

## 15.3 REITs and real estate

Key metrics:

| Metric                   | Meaning                        |
| ------------------------ | ------------------------------ |
| NOI                      | Net operating income           |
| Occupancy                | Utilization                    |
| Same-property NOI growth | Organic growth                 |
| Cap rate                 | NOI / Property Value           |
| FFO                      | Funds from operations          |
| AFFO                     | Adjusted funds from operations |
| Debt / EBITDA            | Leverage                       |
| Loan-to-value            | Debt / property value          |
| Lease maturity           | Rollover risk                  |
| WALE                     | Weighted average lease expiry  |

Valuation:

```text
Price / FFO
Price / AFFO
Dividend yield
NAV discount/premium
```

---

## 15.4 Software / SaaS

Key metrics:

| Metric        | Meaning                              |
| ------------- | ------------------------------------ |
| ARR           | Annual recurring revenue             |
| NRR           | Net revenue retention                |
| GRR           | Gross retention                      |
| Churn         | Lost customers/revenue               |
| CAC           | Customer acquisition cost            |
| LTV/CAC       | Unit economics                       |
| Rule of 40    | Growth + FCF margin or EBITDA margin |
| Gross margin  | Product economics                    |
| R&D intensity | Innovation                           |
| SBC dilution  | Shareholder cost                     |

Watch out for aggressive adjusted EBITDA and stock compensation add-backs.

---

## 15.5 Commodity producers

Key metrics:

| Metric             | Meaning                |
| ------------------ | ---------------------- |
| Production volume  | Output                 |
| Realized price     | Actual selling price   |
| Cash cost          | Operating cost         |
| AISC               | All-in sustaining cost |
| Reserves/resources | Mine/oilfield life     |
| Replacement ratio  | Reserve sustainability |
| Capex intensity    | Required reinvestment  |
| Hedging            | Price exposure         |
| Depletion          | Asset consumption      |

Valuation:

```text
NAV
EV/Reserves
EV/Production
EV/EBITDA at cycle-normal prices
```

Use cycle-normal commodity prices. Valuing miners at peak prices is a classic way to donate money to strangers.

---

## 15.6 Industrials and manufacturing

Key metrics:

| Metric                | Meaning            |
| --------------------- | ------------------ |
| Order book            | Future revenue     |
| Book-to-bill          | Demand trend       |
| Capacity utilization  | Operating leverage |
| Gross margin          | Pricing/cost       |
| Working capital cycle | Cash intensity     |
| Capex / sales         | Capital intensity  |
| ROIC                  | Value creation     |
| Export mix            | FX exposure        |

---

## 15.7 Retail and restaurants

Key metrics:

| Metric                         | Meaning                |
| ------------------------------ | ---------------------- |
| Same-store sales               | Organic growth         |
| Store count                    | Expansion              |
| Sales per square foot          | Productivity           |
| Gross margin                   | Pricing and shrinkage  |
| Inventory turns                | Stock efficiency       |
| Lease liabilities              | Hidden leverage        |
| Franchise vs company-owned mix | Margin/capital profile |
| Customer traffic               | Demand health          |

---

# 16. Index fundamental analysis

Now the index version, because people love saying “the marketâif it were one organism with a Bloomberg terminal.

## Step 1: Get the index methodology

You need:

| Item                       | Why                                                     |
| -------------------------- | ------------------------------------------------------- |
| Eligibility rules          | What can enter                                          |
| Weighting method           | Market cap, float-adjusted, equal weight, factor weight |
| Rebalancing schedule       | Turnover and flow impact                                |
| Corporate action treatment | Splits, mergers, spin-offs                              |
| Free float treatment       | Investability                                           |
| Sector classification      | Exposure                                                |
| Country classification     | Macro/geopolitical risk                                 |
| Currency treatment         | FX risk                                                 |
| Buffer rules               | Turnover control                                        |

## Step 2: Get current and historical constituents

For each constituent:

| Field                 |
| --------------------- |
| Ticker                |
| Company               |
| ISIN                  |
| Weight                |
| Sector                |
| Country               |
| Currency              |
| Market cap            |
| Free-float market cap |
| Revenue               |
| EBIT                  |
| EBITDA                |
| Net income            |
| Book equity           |
| Debt                  |
| Cash                  |
| FCF                   |
| Dividend              |
| Reporting standard    |
| Fiscal year-end       |
| Filing date           |

Use historical constituents for backtesting. If you only analyze today’s members, you commit survivorship bias. Tiny little error, merely enough to destroy your entire conclusion.

## Step 3: Normalize all constituents

For index analysis, normalize:

| Issue                      | Requireaction                    |
| -------------------------- | ---------------------------------- |
| Different currencies       | Convert using consistent FX date   |
| Different fiscal year-ends | Align trailing twelve months       |
| Different standards        | Apply accounting adjustments       |
| Different sectors          | Use sector-specific metrics        |
| Negative earnings          | Handle separately                  |
| Dual listings              | Avoid duplicate exposure           |
| Holding companies          | Avoid double-counting subsidiaries |
| NCI                        | Adjust ownership economics         |
| Banks/insurers             | Use separate sector metrics        |

## Step 4: Calculate aggregate valuation correctly

Do **not** average PE ratios arithmetically.

Bad:

```text
Index PE = Average(Company PE)
```

Better:

```text
Index PE = Aggregate Market Cap / Aggregate Net Income
```

Or:

```text
Index Earnings Yield = Σ Weight_i × Earnings Yield_i
Index PE = 1 / Index Enings Yield
```

For EV multiples:

```text
Index EV/EBITDA = Aggregate EV / Aggregate EBITDA
```

For PB:

```text
Index PB = Aggregate Market Cap / Aggregate Book Equity
```

For ROE:

```text
Index ROE = Aggregate Net Income / Aggregate Book Equity
```

For dividend yield:

```text
Index Dividend Yield = Σ Weight_i × Dividend Yield_i
```

## Step 5: Decompose by sector

Index-level valuation can hide everything.

Calculate by sector:

| Metric                |
| --------------------- |
| Weight              |
| Revenue contribution  |
| Earnings contribution |
| FCF contribution      |
| PE                    |
| PB                    |
| ROE                   |
| Debt / EBITDA         |
| Dividend yield        |
| Earnings growth       |
| Margin trend          |

Example problem:

An index may look expensive because technology is expensive, while banks and energy are cheap. Or it may look cheap because commodity earnings are temporarily inflated. Aggregates lie politely.

## Step 6: Measure concentration

Calculate:

```text
Top 5 Weight
Top 10 Weight
Herfindahl-Hirschman Index = Σ Weight_i²
Sector Concentration = Max Sector Weight
Country Concentration = Max Country Weight
```

High concentration means the index is not as diversified as the brochure wants you to believe.

## Step 7: Index quality metrics

Calculate weighted or aggregate:

| Metric            | Method                                       |
| ----------------- | -------------------------------------------- |
| ROE               | Aggrete net income / aggregate equity      |
| ROIC              | Aggregate NOPAT / aggregate invested capital |
| Net debt / EBITDA | Aggregate net debt / aggregate EBITDA        |
| FCF yield         | Aggregate FCF / aggregate market cap         |
| Earnings quality  | Aggregate CFO / aggregate net income         |
| Buyback yield     | Aggregate buybacks / aggregate market cap    |
| Dividend payout   | Aggregate dividends / aggregate net income   |
| Revenue growth    | Aggregate or weighted TTM growth             |
| Earnings growth   | Aggregate or weighted TTM growth             |

## Step 8: Index macro sensitivity

Map index exposure to:

| Factor          | Examples                                     |
| --------------- | -------------------------------------------- |
| Interest rates  | Banks, real estate, utilities, growth stocks |
| FX              | Exporters/importers, foreign revenue         |
| Oil             | Energy producers vs consumers                |
| Metals          | Miners, industrials                          |
| Credit spreads  | Banks, NBFCs, real estate                    |
| Inflation       | Staples vs discretionary                     |
| Regulation      | Utilities, telecom, banks                    |
| Global growth   | IT services, exporters, commodities          |
| Domestic demand | Consumer, autos, real estate                 |

## Step 9: Compare index valuation to history

Compare:

| Metric         |
| -------------- |
| PE             |
| Forward PE     |
| PB             |
| EV/EBITDA      |
| Dividend yield |
| Earnings yield |
| FCF yield      |
| ROE            |
| ROIC           |
| Profit margins |
| Sector weights |

But be careful: historical PE is less useful if the sector composition changed dramatically.

A 2010 index with heavy energy and banks is not the same animal as a 2026 index dominated by technology and platforms. Same index name, different beast. Humans do love branding continuity over analytical truth.

---

# 17. Red flags checklist

## Accounting red flags

| Red flag                                     |
| -------------------------------------------- |
| CFO consistently below net income            |
| Receivables growing faster than revenue      |
| Inventory growing faster than sales          |
| Frequent one-time adjustments                |
| Aggressive capitalization of costs           |
| Large related-party transactions             |
| Auditor resignation                          |
| Qualified audit opinion                      |
| Restatements                                 |
| Late filings                                 |
| Weak internal controls                       |
| Large unexplained deferred tax asset         |
| Goodwill keeps rising from acquisitions      |
| Segment reporting changes frequently         |
| Non-GAAP profit diverges from GAAP profit    |
| High profits but no cash                     |
| Sudden margin expansion with no clear driver |

## Business red flags

| Red flag                                 |
| ---------------------------------------- |
| Customer concentration                   |
| Supplier dependence                      |
| Commodity price exposure without hedging |
| Regulatory investigation                 |
| Declining market share                   |
| High churn                               |
| Low reinvestment despite claimed growth  |
| Price cuts hidden as promotions          |
| Excessive leverage                       |
| Refinancing wall                         |
| Promoter pledging                        |
| Frequent equity dilution                 |
| Management overpromising                 |
| Acquisition addiction                    |

## Valuation red flags

| Red flag                                                   |
| ---------------------------------------------------------- |
| Valuation assumes permanent high growth                    |
| Terminal value dominates DCF                               |
| Margin assumptions exceed industry leaders                 |
| ROIC forecast rises without explanation                    |
| Working capital ignored                                    |
| Capex understated                                          |
| SBC ignored                                                |
| Tax rate unrealistically low                               |
| Debt maturity ignored                                      |
| Peer group cherry-picked                                   |
| Using EV/EBITDA for a business where capex matters heavily |

---

# 18. Fundamental analysis in a trading or quant system

Since you are building a trading system, this part matters. Fundamental data is dangerous in backtests if mishandled.

## Point-in-time rule

Use the **filing date**, not the fiscal period end date.

Bad:

```text
Use FY2025 results on March 31, 2025
```

Better:

```text
Use FY2025 results only after the company actually filed/released them
```

Otherwise you are using future data. The backtest will look brilliant, which is the first sign it is lying.

## Store fundamentals as point-in-time data

Your data model should include:

```text
company_id
ticker
reporting_period_end
filing_date
accepted_date
source_type
statement_type
accounting_standard
currency
consolidation_basis
raw_label
normalized_concept
amount
unit
period_type
taxonomy_tag
source_url_or_file
adjustment_flag
restatement_flag
```

## Use features, not vague opinions

Examples:

| Feature             | Formula                                               |
| ------------------- | ----------------------------------------------------- |
| earnings_yield      | EPS / Price                                           |
| fcf_yield           | FCF / Market Cap                                      |
| book_to_market      | Book Equity / Market Cap                              |
| gross_profitability | Gross Profit / Assets                                 |
| asset_growth        | Assets_t / Assets_t-1 - 1                             |
| accruals            | Net Income - CFO                                      |
| leverage            | Net Debt / EBITDA                                     |
| ROIC                | NOPAT / Invested Capital                              |
| revenue_growth      | Revenue_t / Revenue_t-1 - 1                           |
| margin_expansion    | EBIT Margin_t - EBIT Margin_t-1                       |
| quality_score       | Composite of ROIC, FCF conversion, leverage, accruals |

## Backtesting requirements

For fundamental strategies:

| Requirement              | Why                                    |
| ------------------------ | -------------------------------------- |
| Point-in-time filings    | Avoid look-ahead bias                  |
| Historical constituents  | Avoid survivorship bias                |
| Restatement handling     | Avoid using restated numbers too early |
| Filing lag               | Use realistic availability             |
| Currency conversion date | Avoid FX distortion                    |
| Corporate actions        | Correct share counts/prices            |
| Sector-neutral testing   | Avoid hidden sector bets               |
| Liquidity filters        | Avoid impossible trades                |
| Transaction costs        | Avoid fantasy alpha                    |
| Rebalance rules          | Make strategy executable               |

---

# 19. Practical scoring framework

You can score a stock across five pillars.

## Pillar 1: Growth

| Metric         | Good sign              |
| -------------- | ---------------------- |
| Revenue growth | Consistent and organic |
| EPS growth     | Not only from buybacks |
| FCF growth     | Tracks earnings        |
| Market share   | Stable/rising          |
| Segment growth | Strong core business   |

## Pillar 2: Profitability

| Metric       | Good sign                       |
| ------------ | ------------------------------- |
| Gross margin | Stable/rising                   |
| EBIT margin  | Stable/rising                   |
| ROIC         | Above cost of capital           |
| ROE          | High without excessive leverage |
| FCF margin   | Strong                          |

## Pillar 3: Financial strength

| Metric            | Good sign         |
| ----------------- | ----------------- |
| Net debt/EBITDA   | Low or manageable |
| Interest coverage | High              |
| Debt maturity     | Spread out        |
| Liquidity         | Adequate          |
| Cash conversion   | Strong            |

## Pillar 4: Accounting quality

| Metric         | Good sign              |
| -------------- | ---------------------- |
| CFO/net income | Around or above 1      |
| Accruals       | Low                    |
| Receivables    | Not outgrowing revenue |
| Adjustments    | Limited                |
| Audit          | Clean                  |

## Pillar 5: Valuation

| Metric    | Good sign                            |
| --------- | ------------------------------------ |
| PE        | Reasonable vs growth/quality         |
| EV/EBIT   | Reasonable vs peers                  |
| FCF yield | Attractive                           |
| PB        | Reasonable for asset/financial firms |
| DCF       | Margin of safety                     |

Example scoring:

```text
Total Score =
  25% Quality
+ 20% Growth
+ 20% Valuation
+ 20% Financial Strength
+ 15% Accounting Quality
```

Do not pretend this score is truth. It is a decision-support tool.

---

# 20. Final analyst checklist

Before making a conclusion, answer every item below.

## Business

* What does the company sell?
* Who buys it?
* Why do customers choose it?
* Is demand recurring?
* Is the company cyclical?
* What are the key cost drivers?
* What are the key growth drivers?
* What can disrupt the business?

## Accounting

* What accounting standard is used?
* Is it consolidated or standalone?
* Has the standard changed?
* Were there restatements?
* Is the audit opinion clean?
* Are there key audit matters?
* Are there related-party transactions?
* Are there aggressive accounting policies?
* Are costs capitalized?
* Are leases properly included?
* Are non-GAAP metrics reasonable?

## Income statement

* Is revenue growing?
* Is growth organic?
* Are margins improving?
* Are expenses controlled?
* Are one-time items truly one-time?
* Is tax rate sustainable?
* Is EPS growth driven by operations or buybacks?

## Balance sheet

* Is leverage reasonable?
* Are debt maturities manageable?
* Are assets high quality?
* Is goodwill large?
* Are receivables collectible?
* Is inventory healthy?
* Are provisions adequate?
* Are pension/lease obligations material?

## Cash flow

* Does CFO track net income?
* Is FCF positive?
* Is capex sustainable?
* Is working capital consuming cash?
* Are dividends covered by FCF?
* Are buybacks funded by real cash or debt?

## Valuation

* What is normalized earnings power?
* What is intrinsic value?
* What is the margin of safety?
* What assumptions drive valuation?
* What does reverse DCF imply?
* Are peers truly comparable?
* Is valuation cheap for a reason?

## Risk

* What can permanently impair capital?
* What would break the thesis?
* What is the debt/refinancing risk?
* What is the regulatory risk?
* What is the fraud/accounting risk?
* What is the liquidity risk?
* What is the macro sensitivity?

## Index-specific

* What are the constituents?
* What are the top weights?
* Is the index concentrated?
* What sectors dominate?
* What countries/currencies dominate?
* Are index PE/PB/ROE calculated correctly?
* Are negative earners handled correctly?
* Has sector composition changed?
* Is valuation driven by one sector?
* Is the investable ETF tracking the index cleanly?

---

# 21. The most important rule

A proper fundamental framework must separate:

```text
Reported accounting number
≠
Normalized analytical number
≠
Economic reality
≠
Market price
```

Your job is to move carefully from the first to the fourth without lying to yourself in the middle.

A serious framework should preserve raw filings, map labels into standardized concepts, adjust for accounting policy differences, evaluate business quality, test cash conversion, forecast conservatively, value with multipleds, and track risks over time.

That is how you avoid missing something just because one report says “turnover,” another says “net sales,” another says “revenue from operations,” and some management team decides “adjusted profit before vibes” is a useful metric.

[1]: https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/introduction-financial-statement-analysis?utm_source=chatgpt.com "Introduction to Financial Statement Analysis"
[2]: https://www.investor.gov/introduction-investing/investing-basics/glossary/form-10-k?utm_source=chatgpt.com "Form 10-K"
[3]: https://www.sec.gov/files/form20-f.pdf?utm_source=chatgpt.com "Form 20-F"
[4]: https://www.msci.com/index/methodology/latest/FreeFloatData?utm_source=chatgpt.com "MSCI Free Float Data Methodology"
[5]: https://www.ifrs.org/use-around-the-world/use-of-ifrs-standards-by-jurisdiction/?utm_source=chatgpt.com "Who uses IFRS Accounting Standards?"
[6]: https://www.fasb.org/standards?utm_source=chatgpt.com "Standards"
[7]: https://www.icai.org/post/indian-accounting-standards-indas?utm_source=chatgpt.com "Indian Accounting Standards (Ind AS)"
[8]: https://www.ifrs.org/issued-standards/ifrs-taxonomy/?utm_source=chatgpt.com "IFRS Accounting Taxonomy"
[9]: https://www.fasb.org/page/detail?pageId=%2Fprojects%2FFASB-Taxonomies%2F2025-gaap-financial-reporting-taxonomy.html&utm_source=chatgpt.com "2025 GAAP Financial Reporting Taxonomy"
[10]: https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/?utm_source=chatgpt.com "IAS 1 Presentation of Financial Statements"
[11]: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/?utm_source=chatgpt.com "IFRS 18 Presentation and Disclosure in Financial Statements"
[12]: https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/?utm_source=chatgpt.com "IAS 7 Statement of Cash Flows"
[13]: https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/?utm_source=chatgpt.com "IAS 38 Intangible Assets"
[14]: https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/property_plant_equip/property_plant_equip_US/chapter_7_other_asse_US/73_research_and_deve_US.html?utm_source=chatgpt.com "8.3 Research and development costs - Viewpoint"
[15]: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/?utm_source=chatgpt.com "IFRS 16 Leases"
[16]: https://storage.fasb.org/ASU%202016-02_Section%20A.pdf?utm_source=chatgpt.com "Leases (Topic 842)"
[17]: https://kpmg.com/us/en/articles/2023/inventory-accounting.html?utm_source=chatgpt.com "Inventory accounting: IFRS® Standards vs US GAAP"
[18]: https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2022/issued/part-a/ias-16-property-plant-and-equipment.pdf?bypass=on&utm_source=chatgpt.com "IAS 16 Property, Plant and Equipment"
