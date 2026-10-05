---
id: "zep-iterable-sections-step-3-provide-a-linker-script"
type: "concept"
domain: "rtos"
title: "Iterable Sections: Step 3: Provide a linker-script"
summary: "The linker script uses ITERABLE_SECTION_RAM or ITERABLE_SECTION_ROM to emit the actual section."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/iterable_sections/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/iterable_sections/index.rst"
license: "Apache-2.0"
mode: "V"
---

The linker script uses `ITERABLE_SECTION_RAM` or
`ITERABLE_SECTION_ROM` to emit the actual section.

RAM-resident:

```c

/* sections-ram.ld */
#include <zephyr/linker/iterable_sections.h>

ITERABLE_SECTION_RAM(my_data, Z_LINK_ITERABLE_SUBALIGN)
```
ROM-resident:

```c

/* sections-rom.ld */
#include <zephyr/linker/iterable_sections.h>

ITERABLE_SECTION_ROM(my_data, Z_LINK_ITERABLE_SUBALIGN)
```
Register the linker-script from `CMakeLists.txt`:

```cmake

zephyr_linker_sources(<location> <path-to-ld-file>)
```
See `zephyr_linker_sources()` in `cmake/modules/extensions.cmake` for the full argument list and
a more detailed explanation of the available `<location>` options.
