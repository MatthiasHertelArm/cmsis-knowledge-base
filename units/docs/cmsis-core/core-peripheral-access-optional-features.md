---
id: "core-peripheral-access-optional-features"
type: "concept"
domain: "core"
title: "Peripheral Access: Optional Features"
summary: "Optionally, the file device.h may define:"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_peripheral.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_peripheral.txt"
license: "Apache-2.0"
mode: "V"
---

Optionally, the file **_device_.h** may define:

-  core_cmsis_pal_bitfields and \#define constants that simplify access to peripheral registers.
	These constants may define bit-positions or other specific patterns that are required for
    programming peripheral registers. The identifiers should start with
    **<_device abbreviation_>_** and **<_peripheral name_>_**.
    It is recommended to use CAPITAL letters for \#define constants.

-   More complex functions (i.e. status query before
    a sending register is accessed). Again, these functions start with
    **<_device abbreviation_>_** and **<_peripheral name_>_**.
