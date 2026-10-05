---
id: "zep-zyclictest-example"
type: "concept"
domain: "debug"
title: "Zyclictest: Example"
summary: "In this example we want to know the worst case latency of a thread which is woken up by an interrupt and running as cooperative task with priority -10. We expect a latency of less then 200 us."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/debugging/zyclictest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/debugging/zyclictest.rst"
license: "Apache-2.0"
mode: "V"
---

In this example we want to know the worst case latency of a thread which is
woken up by an interrupt and running as cooperative task with priority -10. We
expect a latency of less then 200 us. We are using the free running mode.

1. Start the zyclictest thread with an interval of 400 us (double of expected
worst case latency) and a priority of -11 (one digit higher than the
application thread):

```console

zyclictest start -i 400 -p -11
```
2. Do whatever should be tested....

3. Stop the measurement:

```console

zyclictest stop
```
   Output from zyclictest:

   :
```
Count: 547329
                   IRQ  Thread
Max-Latency:        21      27
Errors:              0       0
Overflow:            0       0
Histogram:
[...]
 23                  0  547306
 24                  0       2
 25                  0       5
 26                  0       5
 27                  0       2
 28                  0       0
[...]
```
4. Interpret the result:

   Where are no errors and no overflows which means the measurement can be used.
   There were 547329 cycles in the test.
   Worst case interrupt latency is 21 us and for threads it's 27 us.
