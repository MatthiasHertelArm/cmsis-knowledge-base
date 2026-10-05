---
id: "ethu-driver-api-functions"
type: "concept"
domain: "edge-ai"
title: "Driver: API functions"
summary: "See Driver functions for the complete generated API and Driver structures for public data types."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/driver/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/driver/src/main.md#api-functions"
license: "Apache-2.0"
mode: "V"
---

| API Function | Build | Description |
| --- | --- | --- |
| ethosu_init() | Single-variant | Initialize and register an NPU instance using the compile-time device selection. |
| ethosu_init_ex() | Multi-variant | Initialize and register an NPU instance using a device descriptor, run-time configuration, and optional per-driver user operations. |
| ethosu_deinit() | Both | Unregister an idle NPU instance and release its synchronization resources. |
| ethosu_invoke_v3() | Both | Submit an inference to a specified driver and wait synchronously for completion. |
| ethosu_invoke_async(), ethosu_wait() | Both | Submit an inference asynchronously, then poll or block for completion. |
| ethosu_invoke_auto() | Multi-variant | Read the network's NPU requirements, reserve a matching driver, run the inference, and release the driver. |
| ethosu_get_product_config_from_cop_data() | Both | Read the Ethos-U product and MAC configuration from a Vela custom-operator payload. |
| ethosu_irq_handler() | Both | Handle an NPU completion or fault interrupt for a driver instance. |
| ethosu_get_driver_version(), ethosu_get_hw_info() | Both | Inspect the driver version and an NPU instance's hardware information. |
| ethosu_soft_reset() | Both | Reset an NPU instance and restore its configuration. |
| ethosu_request_power(), ethosu_release_power() | Both | Manage reference-counted NPU power requests. |
| ethosu_reserve_driver() | Single-variant | Block until an instance of the compile-time NPU variant is available and reserve it. |
| ethosu_reserve_driver_ex() | Both | Block until an instance matching the requested product and MAC configuration is available and reserve it. |
| ethosu_release_driver() | Both | Release a reserved driver instance. |

See Driver functions for the complete generated API
and Driver structures for public data types.
