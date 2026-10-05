---
id: "rtx-mempool-run-using-fvp"
type: "concept"
domain: "rtos"
title: "MemPool: Run using FVP"
summary: "The project is configured for execution on Arm Virtual Hardware which removes the requirement for a physical hardware board."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Examples/MemPool/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Examples/MemPool/README.md#run-using-fvp"
license: "Apache-2.0"
mode: "V"
---

The project is configured for execution on Arm Virtual Hardware which removes the requirement for a physical hardware board.

To execute application image on Arm Virtual Hardware use below command syntax:

`<model-executable> -f ./fvp_config.txt <image>`

Examples:

- Run on model for Cortex-M3 (AC6 image)

  ```sh
  FVP_MPS2_Cortex-M3 -f ./fvp_config.txt ./out/MemPool/FVP/Debug/MemPool.axf
  ```

- Run on model for Cortex-M3 (GCC/CLANG image)

  ```sh
  FVP_MPS2_Cortex-M3 -f ./fvp_config.txt ./out/MemPool/FVP/Debug/MemPool.elf
  ```

- Run on model for Cortex-M3 (IAR image)

  ```sh
  FVP_MPS2_Cortex-M3 -f ./fvp_config.txt ./out/MemPool/FVP/Debug/MemPool.out
  ```
