---
id: "drv-storage-interface-arm-storage-info"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_STORAGE_INFO"
summary: "It describes the characteristics of a Storage device. This includes total storage, programming size, a default value for erased memory etc."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_STORAGE_INFO
```


It describes the characteristics of a Storage device. This includes total
storage, programming size, a default value for erased memory etc. This
information can be obtained from the Storage device datasheet and is used by the
middleware in order to properly interact with the Storage device.

Total available storage (in bytes) is contained in **total_storage.** Minimum
programming size (in bytes) is described by **program_unit** (applicable only if
the **programmable** attribute is set for a block). It defines the granularity
for programming data. The offset of the start of a program-range and the size
should also be aligned with **program_unit.**
**Note:**: setting **program_unit** to 0 has the effect of disabling the size and
alignment restrictions (setting it to 1 also has the same effect).

Optimal programming page-size (in bytes) is specified by \em
optimal_program_unit. Some storage controllers have internal buffers into which
to receive data. Writing in chunks of **optimal_program_unit** would achieve
maximum programming speed. Like with **program_unit,** this is applicable only
if the **programmable** attribute is set for the underlying storage block(s).

**program_cycles** is a measure of endurance for reprogramming.
A value of **ARM_STORAGE_PROGRAM_CYCLES_INFINITE** may be used to signify
infinite or unknown endurance.

Contents of erased memory is specified by the **erased_value.** It is usually
`1` to indicate erased bytes with state 0xFF.

**memory_mapped** can be set to `1` to indicate that the storage device
has a mapping onto the processor's memory address space.
**Note:**: For a memory-mapped block which isn't erasable but is programmable,
writes should be possible directly to the memory-mapped storage without going
through the ARM_Storage_ProgramData operation.

The field **programmability** holds a value to indicate storage programmability.
Similarly, **retention_level** holds a for encoding data-retention levels for
all storage blocks.

**Note:**
These fields serve a different purpose than the ones contained in
ARM_STORAGE_CAPABILITIES, which is another structure containing device-level
metadata. ARM_STORAGE_CAPABILITIES describes the API capabilities, whereas
ARM_STORAGE_INFO describes the device. Furthermore ARM_STORAGE_CAPABILITIES fits
within a single word, and is designed to be passed around by value;
ARM_STORAGE_INFO, on the other hand, contains metadata which doesn't fit into a
single word and requires the use of pointers to be moved around.

**Returned by:**
  - ARM_Storage_GetInfo
******************************************************************************************************************
