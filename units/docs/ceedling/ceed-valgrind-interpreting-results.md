---
id: "ceed-valgrind-interpreting-results"
type: "concept"
domain: "test"
title: "Valgrind: Interpreting results"
summary: "See [Valgrind] documentation for more details."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/valgrind.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/valgrind/#interpreting-results"
license: "MIT"
mode: "V"
---

To review the log for a specific test:

```shell
cat build/artifacts/valgrind/test_my_module.log
```

Common Valgrind findings include:

| Finding | Description |
|---------|-------------|
| `definitely lost` | Memory was allocated but never freed — a confirmed leak |
| `indirectly lost` | Memory reachable only through another leaked block |
| `Invalid read/write` | Access outside allocated memory bounds |
| `Use of uninitialised value` | Reading memory before it was written |

See [Valgrind] documentation for more details.

[Valgrind]: https://valgrind.org
