---
id: "frb-12-developer-support-12-5-1-task-run-time-statistics"
type: "concept"
domain: "rtos"
title: "12 Developer Support: 12.5 Viewing Run-time and Task State Information / 12.5.1 Task Run-Time Statistics"
summary: "Part of: 12.5 Viewing Run-time and Task State Information"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch12.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch12.md#12-5-1-task-run-time-statistics"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 12.5 Viewing Run-time and Task State Information_

Task run-time statistics provide information on the amount of processing
time each task has received. A task's *run time* is the total time the
task has been in the Running state since the application booted.

Run-time statistics are intended to be used as a profiling and debugging
aid during the development phase of a project. The information they
provide is only valid until the counter used as the run-time statistics
clock overflows. Collecting run-time statistics will increase the task
context switch time.

To obtain binary run-time statistics information, call the
`uxTaskGetSystemState()` API function. To obtain run-time statistics
information as a human readable ASCII table, call the
`vTaskGetRunTimeStatistics()` helper function.
