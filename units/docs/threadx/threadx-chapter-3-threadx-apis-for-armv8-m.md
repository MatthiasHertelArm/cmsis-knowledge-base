---
id: "threadx-chapter-3-threadx-apis-for-armv8-m"
type: "concept"
domain: "rtos"
title: "Chapter 3  ThreadX APIs for ARMv8-M"
summary: "This chapter contains a description of the ARMv8-M-specific ThreadX services in alphabetic order. Their names are designed so all similar services are grouped together."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/user-guide-armv8m/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/user-guide-armv8m/chapter3.md"
license: "MIT"
mode: "V"
---

This chapter contains a description of the ARMv8-M-specific ThreadX services in alphabetic order. Their names are designed so all similar services are grouped together. In the "Return Values" section in the following descriptions, values in **BOLD** are not affected by the **TX_DISABLE_ERROR_CHECKING** define used to disable API error checking; while values shown in non-bold are completely disabled.

- [tx_thread_secure_stack_allocate](#tx_thread_secure_stack_allocate) Allocate a thread stack in secure memory.
- [tx_thread_secure_stack_free](#tx_thread_secure_stack_free) Free thread stack in secure memory
