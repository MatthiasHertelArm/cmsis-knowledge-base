---
id: "threadx-appendix-e-threadx-smp-misra-c-com-misra-high-level-compliance"
type: "concept"
domain: "rtos"
title: "Appendix E - ThreadX SMP MISRA C compliance: MISRA C Overview / MISRA High-Level Compliance"
summary: "There are several areas in MISRA C:2012 that are not easily determined by static analysis tools such as IAR's C-STAT. These areas are addressed in this section, as follows:"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/appendix-e.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/appendix-e.md#misra-high-level-compliance"
license: "MIT"
mode: "V"
---

_Part of: MISRA C Overview_

There are several areas in MISRA C:2012 that are not easily determined
by static analysis tools such as IAR's C-STAT. These areas are addressed
in this section, as follows:

|Directive|ThreadX SMP Compliance Support|
|---------|------------------------------|
|Dir 1.1|IEC 61508 certification indicates this directive is met.|
|Dir 3.1|IEC 61508 certification indicates this directive is met.|
|Dir 4.1|IEC 61508 certification indicates this directive is met.|
|Dir 4.2|There are eight assembly language files – each effectively a function in size – comprising a typical ThreadX SMP port. The assembly files are:

**_txinitialize_low_level.s_**
**_txthread_context_save.s_**
**_txthread_context_restore.s_**
**_txthread_interrupt_control.s_**
**_txthread_schedule.s_**
**_txthread_smp_core_get.s_**
**_txthread_smp_core_preempt.s_**
**_txthread_smp_current_state_get.s_**
**_txthread_smp_current_thread_get.s_**
**_txthread_smp_initialize_wait.s_**
**_txthread_smp_low_level_initialize.s_**
**_txthread_smp_protect.s_**
**_txthread_smp_time_get.s_**
**_txthread_smp_unprotect.s_**
**_txthread_stack_build.s_**
**_txthread_system_return.s_**
**_txtimer_interrupt.s_**

When **_TX_MISRA_ENABLE_** is used to build the ThreadX SMP library, another assembly file **_tx_misra.s_** is present that encapsulates all pointer arithmetic/manipulation.|
