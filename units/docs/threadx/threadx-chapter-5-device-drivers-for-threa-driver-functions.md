---
id: "threadx-chapter-5-device-drivers-for-threa-driver-functions"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Device Drivers for ThreadX: Driver Functions"
summary: "ThreadX device drivers are composed of eight basic functional areas, as follows."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter5.md#driver-functions"
license: "MIT"
mode: "V"
---

ThreadX device drivers are composed of eight basic functional areas, as follows.

- **Driver Initialization**
- **Driver Control**
- **Driver Access**
- **Driver Input**
- **Driver Output**
- **Driver Interrupts**
- **Driver Status**
- **Driver Termination**

With the exception of initialization, each driver functional area is optional. Furthermore, the exact processing in each area is specific to the device driver.

### Driver Initialization
This functional area is responsible for initialization of the actual hardware device and the internal data structures of the driver. Calling other driver services is not allowed until initialization is complete.

> **Note:** *The driver's initialization function component is typically called from the ***tx_application_define*** function or from an initialization thread.*

### Driver Control

After the driver is initialized and ready for operation, this functional area is responsible for run-time control. Typically, run-time control consists of making changes to the underlying hardware device. Examples include changing the baud rate of a serial device or seeking a new sector on a disk.

### Driver Access

Some device drivers are called only from a single application thread. In such cases, this functional area is not needed. However, in applications where multiple threads need simultaneous driver access, their interaction must be controlled by adding assign/ release facilities in the device driver. Alternatively, the application may use a semaphore to control driver access and avoid extra overhead and complication inside the driver.

### Driver Input

This functional area is responsible for all device input. The principal issues associated with driver input usually involve how the input is buffered and how threads wait for such input.

### Driver Output

This functional area is responsible for all device output. The principal issues associated with driver output usually involve how the output is buffered and how threads wait to perform output.

### Driver Interrupts

Most real-time systems rely on hardware interrupts to notify the driver of device input, output, control, and error events. Interrupts provide a guaranteed response time to such external events. Instead of interrupts, the driver software may periodically check the external hardware for such events. This technique is called *polling*. It is less real-time than interrupts, but polling may make sense for some less real-time applications.

### Driver Status

This function area is responsible for providing run-time status and statistics associated with the driver operation. Information managed by this function area typically includes the following.

- Current device status
- Input bytes
- Output bytes
- Device error counts

### Driver Termination

This functional area is optional. It is only required if the driver and/or the physical hardware device need to be shut down. After being terminated, the driver must not be called again until it is reinitialized.
