---
id: "zep-executing-time-functions-usage"
type: "concept"
domain: "rtos"
title: "Executing Time Functions: Usage"
summary: "2. Call timing_start to signal the start of gathering of timing information. This usually starts the timer."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/timing_functions/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/timing_functions/index.rst"
license: "Apache-2.0"
mode: "V"
---

To gather timing information:

1. Call `timing_init` to initialize the timer.

2. Call `timing_start` to signal the start of gathering of
   timing information. This usually starts the timer.

3. Call `timing_counter_get` to mark the start of code
   execution.

4. Call `timing_counter_get` to mark the end of code
   execution.

5. Call `timing_cycles_get` to get the number of timer cycles
   between start and end of code execution.

6. Call `timing_cycles_to_ns` with total number of cycles
   to convert number of cycles to nanoseconds.

7. Repeat from step 3 to gather timing information for other
   blocks of code.

8. Call `timing_stop` to signal the end of gathering of
   timing information. This usually stops the timer.


### Example


This shows an example on how to use the timing functions:

```c

#include <zephyr/timing/timing.h>

void gather_timing(void)
{
    timing_t start_time, end_time;
    uint64_t total_cycles;
    uint64_t total_ns;

    timing_init();
    timing_start();

    start_time = timing_counter_get();

    code_execution_to_be_measured();

    end_time = timing_counter_get();

    total_cycles = timing_cycles_get(&start_time, &end_time);
    total_ns = timing_cycles_to_ns(total_cycles);

    timing_stop();
}
```
