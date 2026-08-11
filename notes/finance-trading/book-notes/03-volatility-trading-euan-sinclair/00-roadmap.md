# Volatility Trading — Euan Sinclair: Roadmap

## Book Record

| Field | Value |
|---|---|
| Author | Euan Sinclair |
| Edition | Second Edition, 2013 |
| Reading status | Foundations in progress |
| Main notes | [[01-reading-notes|01-reading-notes.md]] |

## Current Coverage

The master note currently develops:

- BSM as a pricing and risk language;
- implied versus realized volatility;
- signed Greek P&L attribution;
- Gamma, Theta, and Delta-hedged intuition;
- event variance and IV crush;
- skew, term structure, and surface dynamics;
- analysis, debugging, and risk controls.

It is not yet a complete chapter-by-chapter treatment of the second edition.

## Planned Deep Dives

1. `02-volatility-measurement.md`
2. `03-stylized-facts-and-volatility-forecasting.md`
3. `04-implied-volatility-surface-dynamics.md`
4. `05-hedging-and-hedged-position-distributions.md`
5. `06-money-management-and-trade-evaluation.md`
6. `07-variance-premium-vix-and-leveraged-etfs.md`
7. `08-trade-life-cycle-and-psychology.md`
8. `80-practice-questions.md`
9. `90-revision-sheet.md`
10. `99-glossary.md`

## Causal Learning Route

```text
Option pricing language
    → measure realized volatility
    → understand empirical return behavior
    → forecast future volatility
    → compare forecast with implied volatility
    → choose and hedge exposure
    → size for uncertainty and tails
    → evaluate process and P&L
```

## Completion Standard

The notes are complete only when the volatility forecast, surface entry price, hedge rule, costs, sizing, failure scenarios, and post-trade attribution can be stated before a hypothetical trade is accepted.
