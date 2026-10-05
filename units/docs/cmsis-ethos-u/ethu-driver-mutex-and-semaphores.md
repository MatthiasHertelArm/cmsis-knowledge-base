---
id: "ethu-driver-mutex-and-semaphores"
type: "concept"
domain: "edge-ai"
title: "Driver: Mutex and semaphores"
summary: "The driver uses the following synchronization objects to reserve an NPU instance and wait for inference completion:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/driver/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/driver/src/main.md#mutex-and-semaphores"
license: "Apache-2.0"
mode: "V"
---

The driver uses the following synchronization objects to reserve an NPU instance
and wait for inference completion:

| Synchronization object | Used by | Purpose |
| --- | --- | --- |
| Global driver mutex | Driver registration, deregistration, reservation, and release | Protects the registered-driver list and each driver's `reserved` flag. It ensures that concurrent threads cannot reserve the same NPU instance. |
| Global availability semaphore | Driver registration, deregistration, reservation, and release | Counts the number of driver instances currently available. `ethosu_reserve_driver()` waits on this semaphore when every NPU is reserved. |
| Per-driver completion semaphore | `ethosu_wait()` and `ethosu_irq_handler()` | Blocks a thread while its NPU is running. The NPU interrupt gives the semaphore after recording successful completion or a fault. |

> [!Note]
> Reserving a driver grants exclusive use of that instance until
> `ethosu_release_driver()` is called. Each instance supports one outstanding
> inference.

The default synchronization functions support a single-threaded bare-metal
application. An RTOS or multicore application must provide the platform-specific
mutex and semaphore functions. The pack provides code templates for CMSIS-RTOS2
and native FreeRTOS implementations. See
Platform-specific functions for
the hook signatures.
