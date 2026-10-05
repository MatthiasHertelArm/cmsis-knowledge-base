---
id: "zep-zyclictest"
type: "concept"
domain: "debug"
title: "Zyclictest"
summary: "The zyclictest module enables estimation of worst case latencies of realtime threads. It can measure the time from the hardware interrupt to the service routine and further to the Zephyr thread."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/debugging/zyclictest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/debugging/zyclictest.rst"
license: "Apache-2.0"
mode: "V"
---

The zyclictest module enables estimation of worst case latencies of realtime
threads. It can measure the time from the hardware interrupt to the service
routine and further to the Zephyr thread.

This module and its name is inspired from the cyclictest program on Linux.
That's why it's a Zephyr cyclictest.

The idea is to use the timer interrupt as interrupt source as we know exactly
the point of time when it occurred. In the interrupt service routine we take
the time and calculate the difference to the programmed time of the timer
interrupt.

Further a thread is also synchronizing itself on the timer and also measures
the difference to the programmed timer.

Both times are put into an array which serves as data source of the histogram
printed out at the end of the measurement.

This measurement is done in a cyclic manner with a certain interval time.

If someone wants to know the worst case latency of a task with priority <p>
then the application needs to be running. While it is running we can start
zyclictest with a priority at least one digit less than the application thread
probed. For example if our application with the thread of interest has the
priority -10 than we need to start zyclictest with a priority of -11 or less.

Another important argument is the interval time. It's not meant to have an
interval less than the measured worst case latency. Therefore it's recommended
to set up an interval with at least double the time of the expected or measured
worst case latency.

If there are overflows indicated at the end of the measurement than this means
that there is no deterministic worst case latency inside the range of the
histogram.

For a meaningful output it's recommended to set up
`CONFIG_SYS_CLOCK_TICKS_PER_SEC` to at least 1000000 as this
means a minimum resolution of 1 microsecond. A tickless kernel is also needed
(`CONFIG_TICKLESS_KERNEL`:).
