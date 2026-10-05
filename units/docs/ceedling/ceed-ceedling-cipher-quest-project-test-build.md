---
id: "ceed-ceedling-cipher-quest-project-test-build"
type: "concept"
domain: "test"
title: "Ceedling Cipher Quest Project: Test Build"
summary: "Run all unit tests (no feature symbols needed beyond TEST, which Ceedling applies automatically via the '' matcher in project.yml):"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/snapshot/examples/cipher_quest/README.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/snapshot/examples/cipher_quest/#test-build"
license: "MIT"
mode: "V"
---

Run all unit tests (no feature symbols needed beyond `TEST`, which Ceedling
applies automatically via the `'*'` matcher in `project.yml`):

```sh
ceedling test:all
```

Each test file that exercises a conditionally compiled feature gets its
own symbol via the `:defines` matcher in `project.yml`:

```yaml
:defines:
  :test:
    '*':
      - TEST
    :TestCipherRot13:
      - CIPHER_ROT13
    :TestCipherCaesar:
      - CIPHER_CAESAR
    :TestAnalyzer:
      - ANALYZER_ENABLED
```

This means each test executable sees only the symbols it needs. The ROT13
tests compile `cipher.c` with `CIPHER_ROT13` defined; the Caesar tests
compile it with `CIPHER_CAESAR`; neither affects the other.

You can also run a single test file:

```sh
ceedling test:TestCipherRot13
ceedling test:TestAnalyzer
```

Or all tests matching a pattern:

```sh
ceedling test:pattern[Cipher]
```

---
