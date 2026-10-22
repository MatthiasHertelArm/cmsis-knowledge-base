---
id: "ceed-ceedling-cipher-quest-project-feature-symbols"
type: "concept"
domain: "test"
title: "Ceedling Cipher Quest Project: Feature Symbols"
summary: "Both CIPHER_ROT13 and CIPHER_CAESAR can be defined simultaneously. If none of the three symbols is defined at compile time, main.c raises a #error to prevent building a binary that can't do anything useful."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/snapshot/examples/cipher_quest/README.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/snapshot/examples/cipher_quest/#feature-symbols"
license: "MIT"
mode: "V"
---

| Symbol             | Enables                              |
|--------------------|--------------------------------------|
| `CIPHER_ROT13`     | ROT13 encode/decode                  |
| `CIPHER_CAESAR`    | Caesar cipher encrypt/decrypt        |
| `ANALYZER_ENABLED` | Character count, frequency, palindrome detection |

Both `CIPHER_ROT13` and `CIPHER_CAESAR` can be defined simultaneously.
If none of the three symbols is defined at compile time, `main.c` raises
a `#error` to prevent building a binary that can't do anything useful.

---
