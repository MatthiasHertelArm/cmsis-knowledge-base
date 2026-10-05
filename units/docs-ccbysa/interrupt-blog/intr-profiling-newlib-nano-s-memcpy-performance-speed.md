---
id: "intr-profiling-newlib-nano-s-memcpy-performance-speed"
type: "concept"
domain: "debug"
title: "Profiling newlib-nano's memcpy: Performance: speed"
summary: "Let's first take a look at the performance of this implementation by measuring the number of cycles it takes to copy different amounts of data."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-09-07-memcpy-newlib-nano.md"
doc_source: "https://interrupt.memfault.com/blog/memcpy-newlib-nano#performance-speed"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's first take a look at the performance of this implementation by measuring
the number of cycles it takes to copy different amounts of data. We're going to
do our experiment on a Cortex-M4F processor (specific chip was an STM32F407),
using the Cortex-M CYCCNT register (for more information, and the implementation
of the cycle-counting functions, see [this post on profiling](https://interrupt.memfault.com/blog/profiling-firmware-on-cortex-m)).

```c
  struct test_struct {
    char data[4096];
  };
  // instantiate 2 structs. for our purposes, we don't care what data is in
  // there. set them to `volatile` so the compiler won't optimize away what we
  // do with them
  volatile struct test_struct dest, source;

  enable_cycle_counter(); // << Enable Cycle Counter

  // run through powers-of-two memcpy's, printing stats for each test
  for (size_t len = 1; len <= sizeof(dest); len <<= 1) {
    uint32_t start = read_cycle_counter(); // << Start count
    memcpy((void *)&dest, (void *)&source, len);
    uint32_t stop = read_cycle_counter(); // << Stop count

    // print out the cycles consumed
    printf("len = %lu, cyccnt = %lu, cycles/byte = %0.3f\n",
           (uint32_t)len, stop - start,
           (float)(stop - start) / (float)len);
  }
```

The output of this test is:

```plaintext
len = 1, cyccnt = 30, cycles/byte = 30.000
len = 2, cyccnt = 41, cycles/byte = 20.500
len = 4, cyccnt = 63, cycles/byte = 15.750
len = 8, cyccnt = 107, cycles/byte = 13.375
len = 16, cyccnt = 195, cycles/byte = 12.188
len = 32, cyccnt = 371, cycles/byte = 11.594
len = 64, cyccnt = 723, cycles/byte = 11.297
len = 128, cyccnt = 1427, cycles/byte = 11.148
len = 256, cyccnt = 2835, cycles/byte = 11.074
len = 512, cyccnt = 5651, cycles/byte = 11.037
len = 1024, cyccnt = 11283, cycles/byte = 11.019
len = 2048, cyccnt = 22547, cycles/byte = 11.009
len = 4096, cyccnt = 45075, cycles/byte = 11.005
```

To replace the default `memcpy` implementation with an alternative, what we can
do is:

1. copy the newlib `memcpy` function into a file in our project, eg `memcpy.c`
2. add the file to the sources we're compiling
3. we have to make a couple of modifications to get the result we want:
   1. add a line `#undef __OPTIMIZE_SIZE__` to the file; we saw GCC will set
      this flag if we enable `-Os` when compiling
   2. add the following definition (which is present in the newlib build):

      ```c
      # define __inhibit_loop_to_libcall \
        __attribute__ ((__optimize__ ("-fno-tree-loop-distribute-patterns")))
      ```

      This is required to prevent the C compiler from inserting `memcpy` calls
      within the body of memcpy, which will end up recursing repeatedly and
      probably overflowing the stack 😩.

Rebuilding, we should see our version of memcpy present if we examine the `.map`
file.

Running the same experiment, the results are:

```plaintext
len = 1, cyccnt = 44, cycles/byte = 44.000
len = 2, cyccnt = 58, cycles/byte = 29.000
len = 4, cyccnt = 86, cycles/byte = 21.500
len = 8, cyccnt = 142, cycles/byte = 17.750
len = 16, cyccnt = 71, cycles/byte = 4.438
len = 32, cyccnt = 91, cycles/byte = 2.844
len = 64, cyccnt = 131, cycles/byte = 2.047
len = 128, cyccnt = 211, cycles/byte = 1.648
len = 256, cyccnt = 371, cycles/byte = 1.449
len = 512, cyccnt = 691, cycles/byte = 1.350
len = 1024, cyccnt = 1331, cycles/byte = 1.300
len = 2048, cyccnt = 2611, cycles/byte = 1.275
len = 4096, cyccnt = 5171, cycles/byte = 1.262
```

At the larger sizes, this implementation is ~ **8.7** times faster!
