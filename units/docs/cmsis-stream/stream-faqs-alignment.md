---
id: "stream-faqs-alignment"
type: "concept"
domain: "cmsis-stream"
title: "FAQs: Alignment"
summary: "When the memoryOptimization mode is enabled, the memory can be shared between different FIFOs (when the FIFOs are in fact used as simple arrays)."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/FAQ.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/FAQ.md#alignment"
license: "Apache-2.0"
mode: "V"
---

When the `memoryOptimization` mode is enabled, the memory can be shared between different FIFOs (when the FIFOs are in fact used as simple arrays).

In this case, the type of the memory buffers is `uint8_t`. And this memory can be used with FIFOs of different types (`float32_t`, `q31_t`).

So, it is important to align the buffers because the compiler may generate instructions which are requiring an aligned buffer thinking that the type of the buffer is different from `uint8_t`.

This can be achieved by defining `CG_BEFORE_BUFFER` in the global custom header included by the scheduler.

For instance:

`#define CG_BEFORE_BUFFER __ALIGNED(4)`

This is not needed when `memoryOptimization` is `False` in the Python configuration.

The read buffer and write buffers used to interact with a FIFO have the alignment of the FIFO datatype but no more (assuming the underlying memory is aligned in case its type is `uint8_t`)

If the number of samples read is `NR` and the number of samples written if `NW`, the alignments (in number of samples) may be:

* `r0 . NR` for a read buffer in the FIFO (where `r0 ` if an integer with `r0 >= 0`)
* `w . NW - r1 . NR` for a write buffer in the FIFO (where `r1 ` and `w` are integers with `r1 >= 0` and `w >= 0`)

If you need a stronger alignment, you'll need to chose `NR` and `NW` in the right way.

For instance, if you need an alignment on a multiple of `16` bytes with a buffer containing `q31_t`, then `NW` and `NR` need to be multiple of `4`.

If you can't choose freely the values of `NR` and `NW` then you may need to do a copy inside your component to align the buffer (of course only if the overhead due to the lack of alignment is bigger than doing a copy.)
