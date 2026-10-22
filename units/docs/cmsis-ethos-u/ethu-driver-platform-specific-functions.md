---
id: "ethu-driver-platform-specific-functions"
type: "concept"
domain: "edge-ai"
title: "Driver: Platform-specific functions"
summary: "The driver provides default implementations for platform-specific functions listed below. The default weak function implementation of the driver should be carefully review and overwritten when needed."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/driver/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/driver/src/main.md#platform-specific-functions"
license: "Apache-2.0"
mode: "V"
---

The driver provides default implementations for
platform-specific functions listed below. The
default weak function implementation of the driver should be carefully review
and overwritten when needed.

| API Function | When an overwrite is needed |
| --- | --- |
| ethosu_flush_dcache(), ethosu_invalidate_dcache() | CPU-cached memory is shared with the NPU and requires platform-specific cache maintenance. |
| ethosu_address_remap() | The CPU and NPU use different addresses for the same storage. |
| ethosu_config_select() | Memory-region attributes depend on the address or run-time placement. |
| Mutex and semaphore functions in Platform-specific functions | Multiple threads or NPUs can use the driver and require platform-specific RTOS locking. |
| ethosu_inference_begin(), ethosu_inference_end() | Inference tracing, power control, or application callbacks are required. |

Cache policy, linker placement, and region configuration are system-level 
decisions. Detailed guidance is in the chapter Integration.
