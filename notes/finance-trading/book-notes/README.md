# Finance and Trading Book Notes

This directory is a reading system, not a flat collection of book-title files. Each book has its own stable folder so chapter notes, exercises, revision sheets, and source checks can grow without turning one Markdown file into an unmaintainable notebook.

## Library

1. [[01-trading-and-exchanges-larry-harris/00-roadmap|Trading and Exchanges — Larry Harris]]
2. [[02-option-volatility-and-pricing-sheldon-natenberg/00-roadmap|Option Volatility & Pricing — Sheldon Natenberg]]
3. [[03-volatility-trading-euan-sinclair/00-roadmap|Volatility Trading — Euan Sinclair]]
4. [[04-expected-returns-antti-ilmanen/00-roadmap|Expected Returns — Antti Ilmanen]]

## Folder Convention

```text
book-notes/
├── README.md
├── CHANGELOG.md
├── 01-book-title-author/
│   ├── 00-roadmap.md
│   ├── 01-reading-notes.md
│   └── CHANGELOG.md
└── 02-next-book-author/
    └── ...
```

The numeric folder prefix records the intended reading order. The lowercase slug keeps links and command-line paths predictable. The author is included because different books can share similar titles.

## File Convention Inside a Book

| File range | Purpose | Create when |
|---|---|---|
| `00-roadmap.md` | Edition, coverage, learning route, and navigation | Always |
| `01-reading-notes.md` | First-pass notes and the current master explanation | Always |
| `02-49-*.md` | Chapter groups or concept deep dives | The master note becomes crowded or a concept deserves independent treatment |
| `50-69-*.md` | Worked examples, data studies, and applications | There is something concrete to analyze |
| `70-79-*.md` | Failure cases, objections, and misconceptions | Important traps accumulate |
| `80-89-*.md` | Questions, exercises, and answer keys | Material is ready for retrieval practice |
| `90-revision-sheet.md` | Compact second-pass revision | The first reading is substantially complete |
| `99-glossary.md` | Book-specific vocabulary | Terminology can no longer be handled clearly in context |
| `CHANGELOG.md` | Material changes and corrections | Always |

Do not create every optional file in advance. Empty structure creates the appearance of progress without knowledge. Split a note when there is real content to move.

## Reading Workflow

```mermaid
flowchart LR
    A[Record edition and scope] --> B[Capture rough chapter notes]
    B --> C[Rewrite in your own words]
    C --> D[Explain cause and mechanism]
    D --> E[Add examples and counterexamples]
    E --> F[Connect books and existing vault notes]
    F --> G[Test with questions]
    G --> H[Revise weak explanations]
    H --> I[Record the change]
```

For every major claim, distinguish among:

- **Author's claim:** what the book argues.
- **My interpretation:** what you think it means.
- **External verification:** what an authoritative source or dataset supports.
- **Trading inference:** what might be testable but is not yet evidence of an edge.

This distinction prevents a persuasive passage from silently turning into an untested trading rule.

## Note-Writing Standard

Each durable explanation should answer:

1. What is the concept?
2. Why does it exist?
3. What mechanism produces it?
4. What assumptions does it depend on?
5. What would falsify or weaken it?
6. How does it connect to the other three books?
7. What could go wrong if it is applied mechanically?
