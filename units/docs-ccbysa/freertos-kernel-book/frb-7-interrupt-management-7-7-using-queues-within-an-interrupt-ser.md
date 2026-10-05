---
id: "frb-7-interrupt-management-7-7-using-queues-within-an-interrupt-ser"
type: "concept"
domain: "rtos"
title: "7 Interrupt Management: 7.7 Using Queues within an Interrupt Service Routine"
summary: "Binary and counting semaphores are used to communicate events. Queues are used to communicate events and to transfer data."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch07.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch07.md#7-7-using-queues-within-an-interrupt-service-routine"
license: "CC-BY-SA-4.0"
mode: "V"
---

Binary and counting semaphores are used to communicate events. Queues
are used to communicate events and to transfer data.

`xQueueSendToFrontFromISR()` is the version of `xQueueSendToFront()` that is
safe to use in an interrupt service routine, `xQueueSendToBackFromISR()`
is the version of `xQueueSendToBack()` that is safe to use in an interrupt
service routine, and `xQueueReceiveFromISR()` is the version of
`xQueueReceive()` that is safe to use in an interrupt service routine.
