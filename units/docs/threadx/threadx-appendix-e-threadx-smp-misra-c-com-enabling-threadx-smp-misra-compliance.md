---
id: "threadx-appendix-e-threadx-smp-misra-c-com-enabling-threadx-smp-misra-compliance"
type: "concept"
domain: "rtos"
title: "Appendix E - ThreadX SMP MISRA C compliance: MISRA C Overview / Enabling ThreadX SMP MISRA Compliance"
summary: "Full MISRA compliance is achieved by building the ThreadX SMP library with TX_MISRA_ENABLE defined."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/appendix-e.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/appendix-e.md#enabling-threadx-smp-misra-compliance"
license: "MIT"
mode: "V"
---

_Part of: MISRA C Overview_

Full MISRA compliance is achieved by building the ThreadX SMP library
with **_TX_MISRA_ENABLE_** defined.

It is important to note that **_TX_MISRA_ENABLE_** must be defined on
the command line or within project settings of the IDE, i.e., it isn't
sufficient for this to be defined in **_tx_port.h_** or **_tx_user.h_**.
All other defines can be added to the header files. It's also important
that **_TX_INLINE_INITIALIZATION_** must not be defined. By default,
this is defined in most distribution's **_tx_port.h_** file.

> **Note:** Some versions of ThreadX SMP might require changes to project and/or **_tx_port.h_**. Please see the end of this document for additional information.
