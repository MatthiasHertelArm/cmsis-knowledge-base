---
id: "rtx-system-requirements-control-block-sizes"
type: "concept"
domain: "rtos"
title: "System Requirements: Control Block Sizes"
summary: "Keil RTX v5 specific control block definitions (including sizes) as well as memory pool and message queue memory requirements are defined in the header file rtxos.h:"
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/system_reqs.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/system_reqs.md#control-block-sizes"
license: "Apache-2.0"
mode: "V"
---

Keil RTX v5 specific control block definitions (including sizes) as well as memory pool and message queue memory requirements are defined in the header file **rtx_os.h**:

If you provide memory for the RTOS objects, you need to know the size that is required for each object control block.

The memory of the control block is provided by the parameter `attr` of the related`osXxxxNew` function. The element `cb_mem` is the memory address, `cb_size` is the size of the control block memory.

Refer to StaticObjectMemory for more information.

The following table lists the control block sizes:

Category                      | Control Block Size Attribute      | Size       | \#define symbol
:-----------------------------|:----------------------------------|:-----------|:--------------------
CMSIS_RTOS_ThreadMgmt    | osThreadAttr_t::cb_mem       | 80 bytes   | osRtxThreadCbSize
CMSIS_RTOS_TimerMgmt     | osTimerAttr_t::cb_mem        | 32 bytes   | osRtxTimerCbSize
CMSIS_RTOS_EventFlags    | osEventFlagsAttr_t::cb_mem   | 16 bytes   | osRtxEventFlagsCbSize
CMSIS_RTOS_MutexMgmt     | osMutexAttr_t::cb_mem        | 28 bytes   | osRtxMutexCbSize
CMSIS_RTOS_SemaphoreMgmt | osSemaphoreAttr_t::cb_mem    | 16 bytes   | osRtxSemaphoreCbSize
CMSIS_RTOS_PoolMgmt      | osMemoryPoolAttr_t::cb_mem   | 36 bytes   | osRtxMemoryPoolCbSize
CMSIS_RTOS_Message       | osMessageQueueAttr_t::cb_mem | 52 bytes   | osRtxMessageQueueCbSize
