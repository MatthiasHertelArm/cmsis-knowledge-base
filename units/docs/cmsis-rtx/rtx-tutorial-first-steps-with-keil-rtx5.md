---
id: "rtx-tutorial-first-steps-with-keil-rtx5"
type: "concept"
domain: "rtos"
title: "tutorial: First Steps with Keil RTX5"
summary: "The RTOS itself consists of a scheduler which supports round-robin, pre-emptive and co-operative multitasking of program threads, as well as time and memory management services."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#first-steps-with-keil-rtx5"
license: "Apache-2.0"
mode: "V"
---

The RTOS itself consists of a scheduler which supports round-robin, pre-emptive and co-operative multitasking of program threads, as well as time and memory management services. Inter-thread communication is supported by additional RTOS objects, including signal thread and event flags, semaphores, mutex, message passing and a memory pool system. As we will see, interrupt handling can also be accomplished by prioritized threads which are scheduled by the RTOS kernel.

(figure: RTOS Components)
