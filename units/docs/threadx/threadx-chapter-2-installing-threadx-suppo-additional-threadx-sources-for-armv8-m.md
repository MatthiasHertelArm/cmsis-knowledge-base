---
id: "threadx-chapter-2-installing-threadx-suppo-additional-threadx-sources-for-armv8-m"
type: "concept"
domain: "rtos"
title: "Chapter 2  Installing ThreadX support for ARMv8-M: Additional ThreadX Sources for ARMv8-M"
summary: "The additional ThreadX files for the ARMv8-M TrustZone architecture are described below."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/user-guide-armv8m/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/user-guide-armv8m/chapter2.md#additional-threadx-sources-for-armv8-m"
license: "MIT"
mode: "V"
---

The additional ThreadX files for the ARMv8-M TrustZone architecture are described below.

  | **File Name**                            | **Contents**                                                        |
  |------------------------------------------|---------------------------------------------------------------------|
  | ***tx_secure_interface.h***              | Include file that defines the ThreadX non-secure callable functions. |
  | ***txe_thread_secure_stack_allocate.c*** |  Error-checking file for the secure stack allocate API. |
  | ***txe_thread_secure_stack_free.c***     |  Error-checking file for the secure stack free API. |
  | ***tx_thread_secure_stack_initialize.s*** |  Initialize the secure stacks. |
  | ***tx_thread_secure_stack_allocate.s***  |  Non-secure veneer for the secure stack allocate service. |
  | ***tx_thread_secure_stack_free.s***      |  Non-secure veneer for the secure stack free service. |
