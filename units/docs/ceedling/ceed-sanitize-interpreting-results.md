---
id: "ceed-sanitize-interpreting-results"
type: "concept"
domain: "test"
title: "Sanitize: Interpreting results"
summary: "Each sanitizer report begins with what it found and where, followed by the stack of calls that led there. Common findings include:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/sanitize.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/sanitize/#interpreting-results"
license: "MIT"
mode: "V"
---

Each sanitizer report begins with what it found and where, followed by the
stack of calls that led there. Common findings include:

| Sanitizer | Finding | Description |
|---|---|---|
| ASan | `heap-buffer-overflow` | Access past the end of a heap allocation |
| ASan | `stack-buffer-overflow` | Access past the end of a local array |
| ASan | `heap-use-after-free` | Access to memory already freed |
| ASan | `double-free` | Memory freed twice |
| UBSan | `runtime error: …` | Undefined behavior, such as signed overflow, an out-of-range shift, or a null pointer load |
| LSan | `detected memory leaks` | Memory allocated and never freed |

A finding’s location is the first stack frame in your code, past the
sanitizer’s own runtime.
