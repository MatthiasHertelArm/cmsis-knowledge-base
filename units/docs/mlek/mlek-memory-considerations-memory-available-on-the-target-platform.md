---
id: "mlek-memory-considerations-memory-available-on-the-target-platform"
type: "concept"
domain: "edge-ai"
title: "Memory considerations: Memory available on the target platform"
summary: "All embedded target platforms supported have platform specific header files that contain memory and other definitions. For example, MPS3 and MPS4 target header files can be found under the HAL sources' platform subdirectory and contains the following definitions:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/memory_considerations.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/memory_considerations.md#memory-available-on-the-target-platform"
license: "Apache-2.0"
mode: "V"
---

All embedded target platforms supported have platform specific header files that contain memory and other definitions.
For example, MPS3 and MPS4 target header files can be found under the HAL sources' platform subdirectory and contains the
following definitions:

```c
#define ISRAM0_SIZE           (0x00100000)     /* ISRAM0 size */
#define ISRAM1_SIZE           (0x00100000)     /* ISRAM1 size */
```

As these SRAM banks are being used for holding the tensor arena, the total size should be limited to **2 MiB** for
Arm® *Corstone™-300* target platform. This size is directly linked to the size mentioned in the linker scripts. See
snippet from the scatter file for Arm® *Corstone™-300* below:

```log
;-----------------------------------------------------
; FPGA internal SRAM of 2MiB - reserved for activation
; buffers.
; This region should have 3 cycle read latency from
; both Cortex-M55 and Ethos-U NPU
;-----------------------------------------------------
isram.bin       0x31000000  UNINIT ALIGN 16 0x00200000
{
    ...
}
```

When not using the Arm Ethos-U NPU at all or using only Arm Ethos-U55 in `Shared_Sram` or `Sram_Only` modes, the limit
in the linker script (and the platform memory definition header file) is applicable.

However, for `Dedicated_Sram` memory mode (applies only for Arm Ethos-U65 and Arm Ethos-U85),
the tensor arena will not sit in this SRAM space and therefore,
the use case can be allowed to have larger `${use_case}_ACTIVATION_BUF_SZ`.
See next section for more details on this.

For custom requirements (like always placing the tensor arena in DDR), the user can change the `BufAttributes.hpp` file
along with the linker scripts.

### Parameters linked to SRAM size definitions

Other than the obvious link between the linker script and the target profile description in
CMake files, there are other parameters linked to what the reserved space for activation
buffers is. These are:

- The file [npu_config.py](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/py/mlek_tools/setup/npu_config.py) contains a
  parameter called `_DEFAULT_SHARED_SRAM_ARENA_SIZE`:

  ```python
  # 2 MiB default shared SRAM arena size (2 banks of 1 MiB each)
  _DEFAULT_SHARED_SRAM_ARENA_SIZE = 2 * 1024 * 1024  # 2 MiB
  ```

  This size of **2 MiB** here is provided here to allow the default vela optimisation process to
  use this size as a hint for the available SRAM size for use by the CPU and the NPU.

- In every `usecase.cmake` file (present within each use case's source directory), there is
  a parameter called `${use_case}_ACTIVATION_BUF_SZ` set to a fixed value by default. This
  default value should be less than, or equal to, the available SRAM on the target platform if
  the activation buffer needs to be reserved in the target platform's SRAM region.
