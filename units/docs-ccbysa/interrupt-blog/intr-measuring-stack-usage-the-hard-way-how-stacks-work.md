---
id: "intr-measuring-stack-usage-the-hard-way-how-stacks-work"
type: "concept"
domain: "debug"
title: "Measuring Stack Usage the Hard Way: How stacks work"
summary: "Before we dive into the measurement techniques, let's take a quick look at how stacks usually behave on these types of small embedded chips (skip to \"Measuring stack usage\" if this is old news)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-06-14-measuring-stack-usage.md"
doc_source: "https://interrupt.memfault.com/blog/measuring-stack-usage#how-stacks-work"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before we dive into the measurement techniques, let's take a quick look at how
stacks usually behave on these types of small embedded chips (skip to
["Measuring stack usage"](#measuring-stack-usage) if this is old news). For this
article, we'll be assuming an ARM Cortex-M embedded device with "full
descending" stacks, but similar techniques will apply to other systems.

### Stack grows down, heap grows up

In a "full descending" stack, objects are "allocated" into stack memory in
decreasing memory order.

If our code is allocating a 32-bit value on stack:

```c
int foo(int a) {
  uint32_t var;  // the compiler may choose to allocate this on stack
  ...
}
```

First the "stack pointer" is decremented by 32 bits (4 bytes), then the address
for `var` is set to the new stack pointer address. Loads and stores of the `var`
variable will then access the stack-allocated 32-bit region.

In a typical single-threaded embedded program that uses both stack and heap
(`malloc` and friends), the memory ordering might look like this:



You can find some more explanation here:

<https://courses.engr.illinois.edu/cs225/fa2022/resources/stack-heap/>

> Side note, there's an interesting strategy for single-threaded programs that
> involves a two-pass linking step, and results in this memory layout:
>
> 
>
> Read more about that here:
>
> <https://blog.japaric.io/stack-overflow-protection/>

### RTOS stacks



Things get a little more complicated when there's an RTOS involved: each thread
(in a pre-emptive RTOS) usually has its own dedicated stack. See this link for a
great description:

<https://www.digikey.com/en/maker/projects/introduction-to-rtos-solution-to-part-4-memory-management/6d4dfcaa1ff84f57a2098da8e6401d9c>

When a thread is running, stack allocations occur just as in a single-threaded
system, only the stack is set up (by the RTOS kernel) specifically for the
thread.

Alright, let's jump into the stack usage measurement techniques!

---
