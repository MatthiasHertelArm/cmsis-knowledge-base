---
id: "zep-kconfig-tips-and-best-practices-checking-changes-with-scripts-kconfig-li"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: Checking changes with `scripts/kconfig/lint.py`"
summary: "After you make Kconfig changes, you can use the scripts/kconfig/lint.py script to check for some potential issues, like unused symbols and symbols that are impossible to enable. Use --help to see available options."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

After you make Kconfig changes, you can use the
`scripts/kconfig/lint.py` script to check for some potential
issues, like unused symbols and symbols that are impossible to enable. Use
`--help` to see available options.

Some checks are necessarily a bit heuristic, so a symbol being flagged by a
check does not necessarily mean there's a problem. If a check returns a false
positive e.g. due to token pasting in C (`CONFIG_FOO_##index##_BAR`), just
ignore it.

When investigating an unknown symbol `FOO_BAR`, it is a good idea to run
`git grep FOO_BAR` to look for references. It is also a good idea to search
for some components of the symbol name with e.g. `git grep FOO` and
`git grep BAR`, as it can help uncover token pasting.
