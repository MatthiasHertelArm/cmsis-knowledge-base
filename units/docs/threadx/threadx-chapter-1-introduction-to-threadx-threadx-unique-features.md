---
id: "threadx-chapter-1-introduction-to-threadx-threadx-unique-features"
type: "concept"
domain: "rtos"
title: "Chapter 1 - Introduction to ThreadX: ThreadX Unique Features"
summary: "Unlike other real-time kernels, ThreadX is designed to be versatile—easily scaling among small microcontroller-based applications through those that use powerful CISC, RISC, and DSP processors."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter1.md#threadx-unique-features"
license: "MIT"
mode: "V"
---

Unlike other real-time kernels, ThreadX is designed to be versatile—easily scaling among small microcontroller-based applications through those that use powerful CISC, RISC, and DSP
processors.

ThreadX is scalable based on its underlying architecture. Because ThreadX services are implemented as a C library, only those services actually used by the application are brought into the run-time image. Hence, the actual size of ThreadX is completely determined by the application. For most applications, the instruction image of ThreadX ranges between 2 KBytes and 15 KBytes in size.

### Picokernel Architecture_

Instead of layering kernel functions on top of each other like traditional _microkernel_ architectures, ThreadX services plug directly into its core. This results in the fastest possible context switching and service call performance. We call this non-layering design a _picokernel_ architecture.

### ANSI C Source Code

ThreadX is written primarily in ANSI C. A small amount of assembly language is needed to tailor the kernel to the underlying target processor. This design makes it possible to port ThreadX to a new processor family in a very short time—usually within weeks!

### Advanced Technology

The following are highlights of the ThreadX advanced technology.

- Simple _picokernel_ architecture
- Automatic scaling (small footprint)
- Deterministic processing
- Fast real-time performance
- Preemptive and cooperative scheduling
- Flexible thread priority support
- Dynamic system object creation
- Unlimited number of system objects
- Optimized interrupt handling
- Preemption-threshold
- Priority inheritance
- Event-chaining
- Fast software timers
- Run-time memory management
- Run-time performance monitoring
- Run-time stack analysis
- Built-in system trace
- Vast processor support
- Vast development tool support
- Completely endian neutral

### Not A Black Box

Most distributions of ThreadX include the complete C source code as well as the processor-specific assembly language. This eliminates the "black-box" problems that occur with many commercial kernels. With ThreadX, application developers can see exactly what the kernel is doing—there are no mysteries!

The source code also allows for application specific modifications. Although not recommended, it is certainly beneficial to have the ability to modify the kernel if it is absolutely required.

These features are especially comforting to developers accustomed to working with their own _in-house kernels_. They expect to have source code and the ability to modify the kernel. ThreadX is the ultimate kernel for such developers.

### The RTOS Standard

Because of its versatility, high-performance _picokernel_ architecture, advanced technology, and demonstrated portability, ThreadX is deployed in more than two-billion devices today. This effectively makes ThreadX the RTOS standard for deeply embedded applications.
