---
id: "intr-a-simple-scheduler-via-an-interrup-how-it-works"
type: "concept"
domain: "debug"
title: "A Simple Scheduler via an Interrupt-driven Actor Model: How it Works"
summary: "Let's look at the concept above in more detail. MCUs have a lot of interrupt vectors, but only a few are used in each application. Usually, unused interrupt vectors are disabled and mapped to panics or infinite loops."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-09-13-hardware-actor-scheduler.md"
doc_source: "https://interrupt.memfault.com/blog/hardware-actor-scheduler#how-it-works"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's look at the concept above in more detail. MCUs have a lot of interrupt vectors, but only a few are used in each application. Usually, unused interrupt vectors are disabled and mapped to panics or infinite loops. This approach aims to reuse vectors unused by devices in that given application and map actor priorities to these vectors. In other words, actors with priority N are associated with interrupt vector X, which is adjusted to have priority N. Therefore, when actors activate each other (indirectly, via message passing using queues), they trigger interrupt vectors associated with the target actor's priority. All the work related to preemption, delaying, etc., is done in hardware, and we shouldn't even be concerned about it (this also means that we don't have to write any code). It is up to the user which exact interrupt vector is mapped to each runqueue. Users are responsible for setting appropriate priorities for vectors to reflect their actual preemption priority (for example, runqueue 0 has the lowest priority, so the vector corresponding to runqueue 0 should have the lowest priority among all the other vectors). Simplified pseudocode for push may be written as:
```
push(queue, msg) {
    if no waiting actors
        enqueue msg
    else
        dequeue waiting actor from queue
        save msg pointer into actor object
        request interrupt associated with the actor
}
```

If an actor has been activated, it causes the corresponding interrupt vector to be triggered. As with a thread scheduler, a global context contains runqueues, or ready-to-run lists. Each such runqueue is assigned an interrupt vector. So, the schedule function may be implemented as follows:

```
context_schedule(this_vector) {
    until runqueue associated with this_vector is nonempty
        dequeue next actor
        call actor's function with saved message
}
```

As actors and interrupts, which are utilized by devices and produce messages, constitute the sole executable entities in this design, it implies that no threads are present in this system. Since there are no threads, main() is just an initialization. The second important point is that actors are run-to-completion routines. It means they only need a stack frame when running, so actors can use a common stack.

When a hardware interrupt occurs, it allocates and posts a message to a queue. This causes the subscribed actor to be activated, the message to be moved into its incoming mailbox, the actor to be moved to the list of ready ones, and the interrupt vector corresponding to the actor's priority to be triggered. After the interrupt handler is finished, the CPU hardware automatically transfers control to the activated vector. Its handler then calls a function called 'schedule,' which eventually calls the corresponding actor.

During this process, the system remains fully preemptable and asynchronous: other interrupt handlers may post messages to other queues. If the actors are delayed, then messages will be accumulated in queues. When an actor or interrupt triggers another high-priority actor, preemption is initiated immediately.

It is important to emphasize that the interrupt vector is assigned to a priority level, not an actor, so the total number of actors is unlimited:



It's clear that the number of possible priorities is limited to the number of interrupt vectors and available hardware preemption priorities. Cortex-M microcontrollers can have up to 240 interrupt vectors, but only a few are used in each application. Therefore, there should be no vector shortage. If that's the case, your application may be so complicated that a full-featured RTOS would be a better choice.

The aforementioned concept can be implemented in approximately 200 lines of C code. In the case of software implementation, the framework would have to deal with interrupt frames, their patching to emulate preemption, calls for rescheduling on interrupt return, examining bitmaps to find the most prioritized runqueue, etc. With hardware-assisted implementation, you can get all of this functionality for free.
