---
id: "zep-installing-west-structure"
type: "concept"
domain: "project"
title: "Installing west: Structure"
summary: "West's code is distributed via PyPI in a Python package named west. This distribution includes a launcher executable, which is also named west (or west.exe on Windows)."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/install.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/install.rst"
license: "Apache-2.0"
mode: "V"
---

West's code is distributed via PyPI in a Python package named `west`.
This distribution includes a launcher executable, which is also named
`west` (or `west.exe` on Windows).

When west is installed, the launcher is placed by `pip3` somewhere in
the user's filesystem (exactly where depends on the operating system, but
should be on the `PATH` environment variable). This
launcher is the command-line entry point to running both built-in commands
like `west init`, `west update`, along with any extensions discovered
in the workspace.

In addition to its command-line interface, you can also use west's Python
APIs directly. See west-apis for details.
