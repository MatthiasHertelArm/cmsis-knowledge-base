---
id: "rtx-operation-thread-stack-management"
type: "concept"
domain: "rtos"
title: "operation: Thread Stack Management"
summary: "For Cortex-M processors without floating point unit the thread context requires 64 bytes on the local stack."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/operation.md#thread-stack-management"
license: "Apache-2.0"
mode: "V"
---

For Cortex-M processors without floating point unit the thread context requires 64 bytes on the local stack.

> **Note**
>
> - For Cortex-M4/M7 with FP the thread context requires 200 bytes on the local stack. For these devices the default stack space should be increased to a minimum of 300 bytes.

Each thread is provided with a separate stack that holds the thread context and stack space for automatic variables and return addresses for function call nesting. The stack sizes of RTX threads are flexibly configurable as explained in the section threadConfig. RTX offers a configurable checking for stack overflows and stack utilization.
