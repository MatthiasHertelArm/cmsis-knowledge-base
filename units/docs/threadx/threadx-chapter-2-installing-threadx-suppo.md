---
id: "threadx-chapter-2-installing-threadx-suppo"
type: "concept"
domain: "rtos"
title: "Chapter 2  Installing ThreadX support for ARMv8-M"
summary: "There are additional ThreadX source code files to support the ARMv8-M architecture."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/user-guide-armv8m/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/user-guide-armv8m/chapter2.md"
license: "MIT"
mode: "V"
---

There are additional ThreadX source code files to support the ARMv8-M architecture.

If ThreadX is to be run in *secure mode*, these additional files and APIs are not needed. To run ThreadX in secure mode, define the symbol **TX_SINGLE_MODE_SECURE** at the top of ***tx_port.h*** or on the command line or project settings. Ensure **TX_SINGLE_MODE_SECURE** is defined for all c and assembly files. ThreadX and the user application will execute in secure mode.

If ThreadX and the user application are to run only in *non-secure mode*, define the symbol **TX_SINGLE_MODE_NON_SECURE** at the top of ***tx_port.h*** or on the command line or project settings. Ensure **TX_SINGLE_MODE_NON_SECURE** is defined for all c and assembly files. ThreadX and the user application will execute in non-secure mode with no support for making secure function calls.

By default, ThreadX and the user application are designed to run in non-secure mode with support for non-secure callable secure functions.
To run ThreadX and the user application in non-secure mode and support non-secure callable secure functions, please do the following:

The file ***tx_thread_secure_stack.c*** must be added to the secure application.

The following files must be added to the ThreadX library:

- ***tx_secure_interface.h***
- ***txe_thread_secure_stack_allocate.c***
- ***txe_thread_secure_stack_free.c***
- ***tx_thread_secure_stack_allocate.s***
- ***tx_thread_secure_stack_free.s***
