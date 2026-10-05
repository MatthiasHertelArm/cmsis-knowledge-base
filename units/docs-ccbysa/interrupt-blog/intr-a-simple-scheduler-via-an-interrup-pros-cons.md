---
id: "intr-a-simple-scheduler-via-an-interrup-pros-cons"
type: "concept"
domain: "debug"
title: "A Simple Scheduler via an Interrupt-driven Actor Model: Pros & Cons"
summary: "Interrupts are often used as a simple 'execution engine' in RTOS-less embedded systems. While it is better than loop-based solutions because of preemption, it may lead to worse latencies when complex processing is done in handlers directly."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-09-13-hardware-actor-scheduler.md"
doc_source: "https://interrupt.memfault.com/blog/hardware-actor-scheduler#pros-cons"
license: "CC-BY-SA-4.0"
mode: "V"
---

Interrupts are often used as a simple 'execution engine' in RTOS-less embedded systems. While it is better than loop-based solutions because of preemption, it may lead to worse latencies when complex processing is done in handlers directly. Many devices use interrupts for various reasons; for example, communication devices use them to signal transmission completion, new data receiving, errors, and so on. When the data is processed in handlers, it may block responses to other events, which may be undesirable, especially when communication protocol has timing constraints, like USB, where the host pings devices periodically. It's a good idea to split interrupt handlers into several parts and keep interrupt code as short as possible to be able to respond to other incoming events. This approach may be a way to achieve such a split. Also, actors may be put in another environment, like a host computer, for testing purposes.

Furthermore, it may also help with processing events from multiple sources and utilizing multiple CPUs. For example, interrupt controllers for multi-core chips (i.e. ARM GIC, see [GICD_SGIR](https://developer.arm.com/documentation/ddi0601/2023-06/External-Registers/GICD-SGIR--Software-Generated-Interrupt-Register?lang=en)) can trigger interrupts on other cores too (while also enforcing priorities and all the other things described above). Thus, the target CPU core may easily augment an actor's associated vector. In this design, each core has its own run queues, just like threads do. Posting messages to a queue may activate subscribed actors running on different cores, enabling true parallel message processing. While 'big' multi-core chips usually run Linux, they are not the ideal target hardware for such a simple framework, but this case is possible. It's worth considering when ultra-low latency is crucial, and every tick counts.

The most significant disadvantage of the model is its requirement to redefine the task in terms of actors and messages (publish-subscribe model), which may be difficult. Consider implementing timeouts or waiting for a response before further message processing. Since the actor model relies on message allocations, it is less deterministic than fixed-memory solutions, like threads and semaphores. When message pools are exhausted, it is still being determined how the handler should proceed. In other words, design patterns for the actor model are less known and may be more complex than their threading-based counterparts. Nevertheless, this may be fixed sometimes by utilizing 'async/await' features of modern languages like Rust and C++20. With async functions, the actor's code may be expressed more naturally and sequentially without manually creating state machines.
