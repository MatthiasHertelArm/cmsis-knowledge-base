---
id: "intr-profiling-firmware-on-cortex-m-timing-code-with-the-cycle-counter"
type: "concept"
domain: "debug"
title: "Profiling Firmware on Cortex-M: Timing Code With the Cycle Counter"
summary: "Our sampling profiler is able to tell us the relative time spent in one function versus another. However, it does not tell us anything about absolute time spent."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-02-profiling-firmware-on-cortex-m.md"
doc_source: "https://interrupt.memfault.com/blog/profiling-firmware-on-cortex-m#timing-code-with-the-cycle-counter"
license: "CC-BY-SA-4.0"
mode: "V"
---

Our sampling profiler is able to tell us the relative time spent in one
function versus another. However, it does not tell us anything about absolute
time spent. If we want to optimize our `mandel` function, we will need a way to
measure how long it executes for.

This is where the `CYCCNT` register (address: `0xE0001004`) comes in. As noted
earlier, the cycle counter is a free running 32-bit cycle counter which is used
to tee-off PC sampling events. The cycle counter can also be used to measure
time without needing to use a hardware timer.

To use the `CYCCNT` to time a function, we simply need to read it before and
after the function executes, and compute the delta.

> Note: since the CYCCNT register is 32-bit wide, it can not be used to measure
> time periods longer than `cycle_period` * 2^32. Given our 168MHz clock speed,
> this comes to about ~25 seconds in our case.

We already know how to enable the cycle counter: we set the CYCCNTENA bit in the
DWT Control Register (this was required for PC sampling as well).

```c
void enable_cycle_counter(void) {
    DWT_CTRL |= DWT_CTRL_CYCCNTENA;
}
```

To read the cycle counter we simple read that register:

```c
uint32_t read_cycle_counter(void) {
    return DWT_CYCCNT;
}
```

That's it! Now we can measure the time spent in our `mandel` function as such:

```c
int main(void) {
    ...
    enable_cycle_counter(); // << Enable Cycle Counter
    printf("System initialized.\n");
    while (1) {
        uint32_t start = read_cycle_counter(); // << Start count
        mandel(center_x, center_y, scale);	/* draw mandelbrot */
        uint32_t stop = read_cycle_counter(); // << Stop count
        printf("We spent %lu cycles in mandel\n", stop - start);
        ...
    }

    return 0;
}
```

> Note: libopencm3 has APIs to use the cycle counter already implemented:
> `dwt_enable_cycle_counter` and `dwt_read_cycle_counter`. I chose to implement
> them myself to make it easier to reproduce for those who do not use the
> library.

And here are the results:

```shell
...
We spent 23392491 cycles in mandel
We spent 24345217 cycles in mandel
We spent 25360211 cycles in mandel
We spent 26309694 cycles in mandel
We spent 27019451 cycles in mandel
We spent 27434047 cycles in mandel
We spent 27662784 cycles in mandel
We spent 27868860 cycles in mandel
We spent 28259158 cycles in mandel
We spent 28544329 cycles in mandel
We spent 28927996 cycles in mandel
We spent 29792795 cycles in mandel
We spent 30591276 cycles in mandel
We spent 31332753 cycles in mandel
We spent 32102420 cycles in mandel
We spent 32874457 cycles in mandel
We spent 33490363 cycles in mandel
We spent 33849665 cycles in mandel
We spent 34146071 cycles in mandel
We spent 34523587 cycles in mandel
We spent 34923967 cycles in mandel
We spent 35274893 cycles in mandel
We spent 35667430 cycles in mandel
We spent 36211229 cycles in mandel
We spent 36762744 cycles in mandel
We spent 37389846 cycles in mandel
We spent 37976133 cycles in mandel
We spent 38298322 cycles in mandel
```

We see here that the amount of time spent in the `mandel` function increases
with every iteration. To convert cycles to seconds we simply divide by our clock
frequency. e.g. `38298322` cycles works out to ~23ms at 168MHz.

> Note: You can find libraries on Github that implement a bit more logic on top
> of the cycle counter, so multiple functions can be measured within the same
> run. Here are two that I stumbled upon while researching this article:
> https://github.com/Serj-Bashlayev/STM32_Profiler, and
> https://github.com/esynr3z/profiler-cortex-m4.
