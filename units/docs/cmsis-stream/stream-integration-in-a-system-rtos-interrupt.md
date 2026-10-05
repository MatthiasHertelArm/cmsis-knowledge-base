---
id: "stream-integration-in-a-system-rtos-interrupt"
type: "concept"
domain: "cmsis-stream"
title: "Integration in a system: RTOS / Interrupt"
summary: "In this case, there is possibility to sleep the CMSIS-Stream scheduler and wake-it up in reaction to an event."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Integration.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Integration.md#rtos-interrupt"
license: "Apache-2.0"
mode: "V"
---

In this case, there is possibility to sleep the CMSIS-Stream scheduler and wake-it up in reaction to an event.

With an RTOS, CMSIS-Stream scheduler would be in a thread and  would be waiting on a semaphore, a queue etc ... Generally the synchronization is responsibility of the sink and source nodes.

With an interrupt based system with no RTOS, the CMSIS-Stream loop would sleep and wait for an interrupt.
