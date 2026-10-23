---
id: "zep-zyclictest-mode-of-operation"
type: "concept"
domain: "debug"
title: "Zyclictest: Mode of operation"
summary: "Zyclictest can be started free running without a fixed number of cycles. This is the default. When stopped the result so far is printed out."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/zyclictest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/zyclictest.rst"
license: "Apache-2.0"
mode: "V"
---

Zyclictest can be started free running without a fixed number of cycles. This
is the default. When stopped the result so far is printed out.

In the loop mode (option start with -l <loops>) zyclictest is running for a
predefined number of cycles. When the number of cycles is reached there is a
message on the shell indicating the end of the test. But the test can be
canceled prematurely with zyclictest stop -c.
