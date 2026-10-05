---
id: "threadx-overview-of-threadx-memory-protection-via-threadx-modules"
type: "concept"
domain: "rtos"
title: "Overview of ThreadX: Memory protection via ThreadX Modules"
summary: "An add-on product called ThreadX Modules enables one or more application threads to be bundled into a \"Module\" that can be dynamically loaded and run (or executed in place) on the target."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/overview-threadx.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/overview-threadx.md#memory-protection-via-threadx-modules"
license: "MIT"
mode: "V"
---

An add-on product called ThreadX Modules enables one or more application threads to be bundled into a "Module" that can be dynamically loaded and run (or executed in place) on the target.

Modules enable field upgrade, bug fixing, and program partitioning to allow large applications to occupy only the memory needed by active threads.

Modules also have a separate address space from ThreadX itself. This enables ThreadX to place memory protection (via MPU or MMU) around the Module such that accidental access outside the module will not be able to corrupt any other software component.
