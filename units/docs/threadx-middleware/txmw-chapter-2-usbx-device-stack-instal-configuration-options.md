---
id: "txmw-chapter-2-usbx-device-stack-instal-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Device Stack Installation: Configuration Options"
summary: "There are several configuration options for building the USBX library. All options are located in the ux_user.h."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-device-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-device-stack-2.md#configuration-options"
license: "MIT"
mode: "V"
---

There are several configuration options for building the USBX library. All options are located in the ***ux_user.h***.

The list below details each configuration option.

|          Configuration Option                   | Description |
| ----------------------------------------------- | ----------- |
| **UX_PERIODIC_RATE**                            | This value represents how many ticks per seconds for a specific hardware platform. The default is 1000 indicating 1 tick per millisecond. |
| **UX_THREAD_STACK_SIZE**                        | This value is the size of the stack in bytes for the USBX threads. It can be typically 1024 bytes or 2048 bytes depending on the processor used and the host controller. |
| **UX_THREAD_PRIORITY_CLASS**                    | This is the ThreadX priority value for the standard USBX threads. |
| **UX_THREAD_PRIORITY_DCD**                      | This is the ThreadX priority value for the device controller thread. |
| **UX_ALIGN_MIN**                                | This value represents minimal allocated memory alignment in number of bytes. The default is UX_ALIGN_8 (0x07) to align allocated memory to 8 bytes. |
| **UX_ENFORCE_SAFE_ALIGNMENT**                   | This value forces the memory allocation scheme to enforce alignment of memory with the UX_SAFE_ALIGN field. |
| **UX_NO_TIME_SLICE**                            | This value actually defines the time slice that will be used for threads. For example, if defined to 0, the ThreadX target port does not use time slices. |
| **UX_MAX_SLAVE_CLASS_DRIVER**                   | This value is the maximum number of classes in the device stack that can be loaded by USBX. |
| **UX_MAX_SLAVE_INTERFACES**                     | This value is the maximum number of interfaces in the device framework. |
| **UX_DEVICE_ENDPOINT_BUFFER_OWNER**             | This value represents the endpoint buffer owner. 0 The default, endpoint buffer is managed by core stack. Each endpoint takes UX_SLAVE_REQUEST_DATA_MAX_LENGTH bytes, 1 Endpoint buffer managed by classes. In this case not all endpoints consume UX_SLAVE_REQUEST_DATA_MAX_LENGTH bytes |
| **UX_SLAVE_REQUEST_CONTROL_MAX_LENGTH**         | This value represents the maximum number of bytes received on a control endpoint in the device stack. The default is 256 bytes but can be reduced in memory constrained environments. |
| **UX_SLAVE_REQUEST_DATA_MAX_LENGTH**            | This value represents the maximum number of bytes that can be received or transmitted on any endpoint. This value cannot be less than the maximum packet size of any endpoint. The default is 4096 bytes but can be reduced in memory constrained environments. For cd-rom support in the storage  class, this value cannot be less than 2048. |
| **UX_DEVICE_BIDIRECTIONAL_ENDPOINT_SUPPORT**    | If defined, the device side enables bi-directional-endpoints support, e.g., endpoints addressed 0x01 and 0x81. Otherwise (the default case), endpoint number must be unique in same configuration. Note the feature must be used with compatible DCD and peripheral. |
| **UX_DEVICE_ALTERNATE_SETTING_SUPPORT_DISABLE** | This macro disables interface alternate setting support. |
| **UX_DEVICE_INITIALIZE_FRAMEWORK_SCAN_DISABLE** | This macro disables device framework scan, where max number of endpoints (except EP0) and max number of interfaces are calculated at runtime, as a base to allocate memory for interfaces and endpoints structures and their buffers. Undefined, the following two macros must be defined to initialize memory structures. |
| **UX_MAX_DEVICE_ENDPOINTS**                     | This value represents max number of endpoints (except EP0) activated at the same time. Works if UX_DEVICE_INITIALIZE_FRAMEWORK_SCAN_DISABLE is defined. |
| **UX_MAX_DEVICE_INTERFACES**                    | This value represents max number of interfaces activated at the same time. Works if UX_DEVICE_INITIALIZE_FRAMEWORK_SCAN_DISABLE is defined. |
| **UX_NAME_REFERENCED_BY_POINTER**               | Defined, the _name in structs are referenced by pointer instead of by contents. By default the _name is an array of string that saves characters, the contents are compared to confirm match. If referenced by pointer the address pointer to const string is saved, the pointers are compared to confirm match. |
| **UX_DEVICE_SIDE_ONLY**                         | This value will only enable the device side of USBX. |
| **UX_STANDALONE**                               | This macro will enable the standalone mode of USBX. |
| **UX_DEBUG_LOG_SIZE**                           | This value represents the size of the log pool. |
| **UX_ENABLE_ASSERT**                            | This enables the assert checks inside USBX. |
| **UX_ENABLE_ERROR_CHECKING**                    | This option enables the basic USBX error checking. This define is typically used when the application is debugging and removed after the application is fully debugged. |
