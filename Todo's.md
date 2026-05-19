# Todo's

## Learning

- [ ] Learn AWS Solutions Architect Associate using the [[aws_saa_trading_bot_plan_checklist]] checklist.
- [ ] Learn networking fundamentals.
- [ ] Read Kubernetes documentation.
- [ ] Watch ADHD module.

## Trading Program Improvements

- [ ] Improve program.
  - [x] Test strategy on a bigger timeline.
    - [x] Confirm data was not fetched properly.
    - [x] Remove the max allocation ratio.
  - [ ] Research a swing-based strategy.
  - [ ] Use OI, volume, support, and resistance in the program where they fit the use case.
  - [ ] Research defined-risk options execution only after consolidated risk tracking exists.
    - [ ] Do not build naked option selling.
    - [ ] Do not allow manual hedges outside the program unless the program can see total exposure.
    - [ ] Define max loss, margin stress, IV rules, event filters, and kill switch before implementation.
  - [ ] Research new strategy idea.
    - [ ] ADX should be above 20 and increasing.
    - [ ] DMA should be above 20 and increasing.
    - [ ] Stop loss should be below VWAP; candle should close below VWAP.
  - [ ] Research ADX positive/mid/negative filtering and route RSI messages through those filters.
