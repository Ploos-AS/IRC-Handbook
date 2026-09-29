# IRC Handbook

**Ploos IRC Handbook** is a practical, bilingual guide to Internet Relay Chat (IRC): from a first connection to running a persistent IRC setup with shell accounts, bouncers, bots and your own infrastructure.

Norwegian is the primary language. English is maintained as a first-class edition from the same source structure.

## M0 goals

- establish the book structure and publishing pipeline
- support HTML, EPUB, Kindle-friendly EPUB and PDF
- cover IRC fundamentals, shell accounts, bouncers and bots
- include modern IRCv3 concepts alongside classic IRC culture
- build toward reproducible hands-on labs
- keep examples and configurations testable where practical

## Planned editions

- `book/no/` — Norwegian edition
- `book/en/` — English edition

## Core topics

1. What IRC is and how it works
2. First connection and essential commands
3. Nick/account identity, TLS and SASL
4. IRC clients
5. Shell accounts, SSH, tmux and screen
6. Running IRC from a shell/VPS
7. Bouncers: ZNC, soju and classic approaches
8. Bots: Eggdrop, EnergyMech, Sopel and others
9. Writing a small IRC bot
10. IRC protocol and IRCv3
11. Operating IRC infrastructure
12. Security and privacy
13. Running an IRC server
14. Final lab: build a complete persistent IRC environment

## Build

The initial build system is intentionally lightweight and Pandoc-oriented. See `Makefile` and `docs/BUILDING.md`.

```sh
make html
make epub
make kindle
make pdf
```

## Repository layout

```text
book/
  no/          Norwegian manuscript
  en/          English manuscript
assets/        Images, diagrams and shared assets
examples/      Tested examples and configuration snippets
docs/          Project and publishing documentation
scripts/       Build/validation helpers
.github/       CI workflows
```

## Licensing

Documentation and book text are intended to use a Creative Commons license. Code examples and build tooling are intended to use the MIT license unless an included upstream component requires otherwise. See `LICENSES.md`.

## Status

**M0 — repository and book architecture.**
