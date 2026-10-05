---
id: "x-debugger-troubleshooting-5"
type: "concept"
domain: "debug"
title: "Flashing an ELF that drops its RW init data (LMA and VMA)"
status: "draft"
extracted_from: "proc-debugger-troubleshooting"
source: "debugger-troubleshooting/SKILL.md"
---

**Garbage pointers (`0xFFFFFFFF`, or values that look like erased flash) during static initialisation mean that RW data was never initialised.** The usual cause is a flashing mistake, not a linker bug: see section 6.

An initialised-data section has its execution address in RAM and its load address in flash. A tool that places sections by their virtual address writes those bytes to RAM, where the next reset discards them, and never programs the flash copy. The startup code then copies erased flash into RAM, and the image dies in static initialisation.
`flash` and `cmsis_action load` program from the cbuild-run file with pyOCD, which uses the load addresses. Prefer them over any hand-made `objcopy` binary or a probe tool's "load file" on an ELF.
Verify instead of assuming: `get_section_layout` gives the load address of the RW section; `read_memory` there must show the initial values, not `0xFF`.
When the image has to be programmed with a vendor tool, program the LOAD segment by its physical address. `arm-none-eabi-readelf -l <image>` lists offset, file size and physical address of each segment; reading the ELF on the host is allowed.
