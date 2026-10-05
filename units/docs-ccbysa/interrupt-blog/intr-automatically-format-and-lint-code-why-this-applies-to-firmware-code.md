---
id: "intr-automatically-format-and-lint-code-why-this-applies-to-firmware-code"
type: "concept"
domain: "debug"
title: "Automatically format and lint code with pre-commit: Why this applies to firmware code"
summary: "Other popular languages/frameworks have de-facto styling tools, for example:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-27-pre-commit.md"
doc_source: "https://interrupt.memfault.com/blog/pre-commit#why-this-applies-to-firmware-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

Other popular languages/frameworks have de-facto styling tools, for example:

- Rust: <https://github.com/rust-lang/rustfmt>
- Python: <https://github.com/astral-sh/ruff> or <https://github.com/psf/black>
- Javascript: <https://prettier.io/>
- Go: <https://go.dev/blog/gofmt>

Firmware repositories tend to be a little different:

- ad-hoc or large variety of build systems/packaging approaches (no standard
  `package.json`)
- often multiple programming languages used (C/C++, Rust, Python, bash,
  Javascript, etc)
- tooling can be difficult to set up (especially across Linux/Windows/Mac hosts)
- sometimes enthusiasm for development tooling can be low (creates a need for
  extremely low friction tools)

Tools like `pre-commit` are especially relevant to firmware repositories:

- independent tooling setup (doesn't rely on an existing package manager)
- cross-language!
- quick and simple usage
