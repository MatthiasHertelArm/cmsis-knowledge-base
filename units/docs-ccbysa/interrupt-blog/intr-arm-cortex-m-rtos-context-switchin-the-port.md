---
id: "intr-arm-cortex-m-rtos-context-switchin-the-port"
type: "concept"
domain: "debug"
title: "ARM Cortex-M RTOS Context Switching: Demystifying the FreeRTOS Context Switcher / The Port"
summary: "Part of: Demystifying the FreeRTOS Context Switcher"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-30-cortex-m-rtos-context-switching.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#the-port"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Demystifying the FreeRTOS Context Switcher_

**FreeRTOS** has excellent documentation[^10] about creating a new project. If you are trying to
port FreeRTOS to your own platform, I'd strongly recommend reading through those docs. For context,
the approximate steps I followed for the minimal port to the Cortex-M4 are:

1. Set up a build system and startup sequence for your MCU. Extensive details about what these
   steps look like can be found in our [zero to main() series]().
2. Compile the core source files included in the **FreeRTOS Kernel**[^11] (`tasks.c`, `queue.c`, `list.c`, `timers.c`)
3. Choose a "port". A port is the platform specific files needed for the architecture in use. Since
   ports often wind up having assembly and assembly syntax is compiler specific there will often be
   ports per compiler for a given architecture. The **FreeRTOS Kernel** [^11] already has a default
   port for pretty much any architecture imaginable so usually you can just choose one from there. In our
   case, we want a port for a Cortex-M4F which can be found in `portable/GCC/ARM_CM4F/`. Once you
   find the "port" you will need to add `port.c` to your compilation list.
4. Chose a **FreeRTOS** heap implementation[^12]. I went with the most basic one for the example,
   `portable/MemMang/heap_1.c`
5. Add the port directory (in our case `portable/GCC`) and the root directory of the kernel as
   include paths to the build system.
6. Create a `FreeRTOSConfig.h`[^13] with the configuration settings for your particular application
7. Create some tasks (`xTaskCreate`), start the scheduler (`vTaskStartScheduler`), and you are
   ready to go!
