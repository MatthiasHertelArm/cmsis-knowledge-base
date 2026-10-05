---
id: "zep-atomic-services-suggested-uses"
type: "concept"
domain: "rtos"
title: "Atomic Services: Suggested Uses"
summary: "Use an atomic variable to implement critical section processing that only requires the manipulation of a single 32-bit value."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/other/atomic.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/other/atomic.rst"
license: "Apache-2.0"
mode: "V"
---

Use an atomic variable to implement critical section processing that only
requires the manipulation of a single 32-bit value.

Use multiple atomic variables to implement critical section processing
on a set of flag bits in a bit array longer than 32 bits.


**Note:** Using atomic variables is typically far more efficient than using other techniques to implement critical sections such as using a mutex or locking interrupts.
