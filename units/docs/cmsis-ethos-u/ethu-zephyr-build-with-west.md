---
id: "ethu-zephyr-build-with-west"
type: "concept"
domain: "edge-ai"
title: "Zephyr: Build with west"
summary: "From the application directory, select an Ethos-U-capable board and perform a pristine build:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/zephyr/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/zephyr/src/main.md#build-with-west"
license: "Apache-2.0"
mode: "V"
---

From the application directory, select an Ethos-U-capable board and perform a
pristine build:

```bash
west build -b <board-name> . --pristine auto
```

Use the board's normal runner to flash hardware or start a simulator. For
example, a board with a configured simulation runner can use:

```bash
west build -t run
```

Consult the board documentation when a separate FVP launch command or debug
configuration is required.
