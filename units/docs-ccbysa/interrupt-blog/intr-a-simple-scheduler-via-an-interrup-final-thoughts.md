---
id: "intr-a-simple-scheduler-via-an-interrup-final-thoughts"
type: "concept"
domain: "debug"
title: "A Simple Scheduler via an Interrupt-driven Actor Model: Final Thoughts"
summary: "The actor model has been around since 1973. It can help with modularity, testability, power efficiency, and configurability in embedded systems. Using hardware-implemented scheduling allows for further simplified source code while also speeding up scheduling operations."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-09-13-hardware-actor-scheduler.md"
doc_source: "https://interrupt.memfault.com/blog/hardware-actor-scheduler#final-thoughts"
license: "CC-BY-SA-4.0"
mode: "V"
---

The actor model has been around since 1973. It can help with modularity, testability, power efficiency, and configurability in embedded systems. Using hardware-implemented scheduling allows for further simplified source code while also speeding up scheduling operations. Suppose your application uses a few interrupt vectors, and your implementation of an interrupt controller allows you to use others. Reusing these vectors for your needs may be a good decision. However, remember that this is largely dependent on the implementation. For example, the NVIC spec is fixed, but the count of available priorities and vectors may vary from one vendor to another. So, while not all systems are suitable for the actor model, it may be a good choice for some, and hardware implementation of model parts in widely available MCUs makes it even more attractive.








{:.no_toc}
