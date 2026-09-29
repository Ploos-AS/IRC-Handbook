# Building IRC Handbook

The M0 build uses Pandoc as the common conversion layer.

## Requirements

- GNU Make
- Pandoc
- XeLaTeX (for PDF)

On Debian/Ubuntu, a practical starting point is:

```sh
sudo apt install make pandoc texlive-xetex
```

## Build Norwegian edition

```sh
make LANG=no all
```

## Build English edition

```sh
make LANG=en all
```

Artifacts are written below `build/<language>/`.

## Formats

- HTML
- EPUB
- Kindle-friendly EPUB
- PDF

The Kindle target intentionally remains EPUB-based in M0. Later milestones can add Kindle Previewer/Kindle-specific validation without coupling the main EPUB artifact to that workflow.

## M0 validation philosophy

M0 establishes repeatable source-to-artifact builds. Later milestones should add:

- EPUB validation
- link checking
- spelling/style checks for NO and EN
- code/configuration tests
- screenshot/diagram checks
- publishing metadata
- cover integration
- deterministic containerized publishing environment
