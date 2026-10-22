---
id: "zep-tracing-future-lttng-inspiration"
type: "concept"
domain: "debug"
title: "Tracing: Future LTTng Inspiration"
summary: "Currently, the top-layer provided here is quite simple and bare-bones, and needlessly copied from Zephyr's Segger SystemView debug module."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

Currently, the top-layer provided here is quite simple and bare-bones,
and needlessly copied from Zephyr's Segger SystemView debug module.

For an OS like Zephyr, it would make sense to draw inspiration from
Linux's LTTng and change the top-layer to serialize to the same format.
Doing this would enable direct reuse of TraceCompass' canned analyses
for Linux.  Alternatively, LTTng-analyses in TraceCompass could be
customized to Zephyr.  It is ongoing work to enable TraceCompass
visibility of Zephyr in a target-agnostic and open source way.



### I/O Taxonomy


- Atomic Push/Produce/Write/Enqueue:

  - synchronous:
                  means data-transmission has completed with the return of the
                  call.

  - asynchronous:
                  means data-transmission is pending or ongoing with the return
                  of the call. Usually, interrupts/callbacks/signals or polling
                  is used to determine completion.

  - buffered:
                  means data-transmissions are copied and grouped together to
                  form a larger ones. Usually for amortizing overhead (burst
                  dequeue) or jitter-mitigation (steady dequeue).

  Examples:
    - sync  unbuffered
        E.g. PIO via GPIOs having steady stream, no extra FIFO memory needed.
        Low jitter but may be less efficient (can't amortize the overhead of
        writing).

    - sync  buffered
        E.g. `fwrite()` or enqueuing into FIFO.
        Blockingly burst the FIFO when its buffer-waterlevel exceeds threshold.
        Jitter due to bursts may lead to missed deadlines.

    - async unbuffered
        E.g. DMA, or zero-copying in shared memory.
        Be careful of data hazards, race conditions, etc!

    - async buffered
        E.g. enqueuing into FIFO.



- Atomic Pull/Consume/Read/Dequeue:

  - synchronous:
                  means data-reception has completed with the return of the call.

  - asynchronous:
                  means data-reception is pending or ongoing with the return of
                  the call. Usually, interrupts/callbacks/signals or polling is
                  used to determine completion.

  - buffered:
                  means data is copied-in in larger chunks than request-size.
                  Usually for amortizing wait-time.

  Examples:
    - sync  unbuffered
        E.g. Blocking read-call, `fread()` or SPI-read, zero-copying in shared
        memory.

    - sync  buffered
        E.g. Blocking read-call with caching applied.
        Makes sense if read pattern exhibits spatial locality.

    - async unbuffered
        E.g. zero-copying in shared memory.
        Be careful of data hazards, race conditions, etc!

    - async buffered
        E.g. `aio_read()` or DMA.



Unfortunately, I/O may not be atomic and may, therefore, require locking.
Locking may not be needed if multiple independent channels are available.

  - The system has non-atomic write and one shared channel
        E.g. UART. Locking required.

        `lock(); emit(a); emit(b); emit(c); release();`

  - The system has non-atomic write but many channels
        E.g. Multi-UART. Lock-free if the bottom-layer maps each Zephyr
        thread+ISR to its own channel, thus alleviating races as each
        thread is sequentially consistent with itself.

        `emit(a,thread_id); emit(b,thread_id); emit(c,thread_id);`

  - The system has atomic write     but one shared channel
        E.g. `native_sim` or board with DMA. May or may not need locking.

        `emit(a ## b ## c); /* Concat to buffer */`

        `lock(); emit(a); emit(b); emit(c); release(); /* No extra mem */`

  - The system has atomic write     and many channels
        E.g. native_sim or board with multi-channel DMA. Lock-free.

        `emit(a ## b ## c, thread_id);`
