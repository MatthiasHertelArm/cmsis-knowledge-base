---
id: "zep-test-framework-stress-test-framework"
type: "concept"
domain: "test"
title: "Test Framework: Stress test framework"
summary: "Zephyr stress test framework (Ztress) provides an environment for executing user functions in multiple priority contexts. It can be used to validate that code is resilient to preemptions. The framework tracks the number of executions and preemptions for each context."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr stress test framework (Ztress) provides an environment for executing user
functions in multiple priority contexts. It can be used to validate that code is
resilient to preemptions. The framework tracks the number of executions and preemptions
for each context. Execution can have various completion conditions like timeout,
number of executions or number of preemptions.

The framework is setting up the environment by creating the requested number of threads
(each on different priority), optionally starting a timer. For each context, a user
function (different for each context) is called and then the context sleeps for
a randomized amount of system ticks. The framework is tracking CPU load and adjusts sleeping
periods to achieve higher CPU load. In order to increase the probability of preemptions,
the system clock frequency should be relatively high. The default 100 Hz on QEMU x86
is much too low and it is recommended to increase it to 100 kHz.

The stress test environment is setup and executed using `ZTRESS_EXECUTE` which
accepts a variable number of arguments. Each argument is a context that is
specified by `ZTRESS_TIMER` or `ZTRESS_THREAD` macros. Contexts
are specified in priority descending order. Each context specifies completion
conditions by providing the minimum number of executions and preemptions. When all
conditions are met and the execution has completed, an execution report is printed
and the macro returns. Note that while the test is executing, a progress report is
periodically printed.

Execution can be prematurely completed by specifying a test timeout (`ztress_set_timeout`)
or an explicit abort (`ztress_abort`).

User function parameters contains an execution counter and a flag indicating if it is
the last execution.

The example below presents how to setup and run 3 contexts (one of which is k_timer
interrupt handler context). Completion criteria is set to at least 10000 executions
of each context and 1000 preemptions of the lowest priority context. Additionally,
the timeout is configured to complete after 10 seconds if those conditions are not met.
The last argument of each context is the initial sleep time which will be adjusted throughout
the test to achieve the highest CPU load.

```C

ztress_set_timeout(K_MSEC(10000));
ZTRESS_EXECUTE(ZTRESS_TIMER(foo_0, user_data_0, 10000, Z_TIMEOUT_TICKS(20)),
               ZTRESS_THREAD(foo_1, user_data_1, 10000, 0, Z_TIMEOUT_TICKS(20)),
               ZTRESS_THREAD(foo_2, user_data_2, 10000, 1000, Z_TIMEOUT_TICKS(20)));
```

### Configuration


Static configuration of Ztress contains:

 - `CONFIG_ZTRESS_MAX_THREADS` - number of supported threads.
 - `CONFIG_ZTRESS_STACK_SIZE` - Stack size of created threads.
 - `CONFIG_ZTRESS_REPORT_PROGRESS_MS` - Test progress report interval.
