---
id: "core-introduction-migration-from-cmsis-v5"
type: "concept"
domain: "core"
title: "Introduction: Migration from CMSIS v5"
summary: "The functionality of individual CMSIS v6 software components is kept primarily same as in CMSIS v5.9.0. However, some CMSIS components are now delivered in their standalone CMSIS packs and may also have different naming, structure and dependencies."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/General/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/General/src/mainpage.md#migration-from-cmsis-v5"
license: "Apache-2.0"
mode: "V"
---

The functionality of individual CMSIS v6 software components is kept primarily same as in CMSIS v5.9.0. However, some CMSIS components are now delivered in their standalone CMSIS packs and may also have different naming, structure and dependencies.

While use of CMSIS-Pack concept greatly helps to abstract many of this changes from users, there are still some simple adaptation required to fully enable CMSIS v6 support in software developed based on CMSIS v5 structure. Following migration guides explain necessary steps for such porting:

 - [Migrating CMSIS-based projects from CMSIS v5 to CMSIS v6](https://learn.arm.com/learning-paths/microcontrollers/project-migration-cmsis-v6)
 - [CMSIS-Pack Migration Guide](https://learn.arm.com/learning-paths/microcontrollers/pack-migration-cmsis-v6)

> **Note**
> - In the version 6.0.0, the CMSIS-Core header files for Cortex-M devices have received some modifications that are incompatible with previous CMSIS-Core versions. Refer to the [CMSIS-Core Revision History](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/General/src/../Core/core_revisionHistory.html) for more information.
