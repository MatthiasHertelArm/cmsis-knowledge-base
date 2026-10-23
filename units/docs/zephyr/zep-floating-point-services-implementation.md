---
id: "zep-floating-point-services-implementation"
type: "concept"
domain: "rtos"
title: "Floating Point Services: Implementation"
summary: "No special coding is required for a thread to use floating point arithmetic if the kernel is properly configured."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/other/float.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/other/float.rst"
license: "Apache-2.0"
mode: "V"
---

### Performing Floating Point Arithmetic


No special coding is required for a thread to use floating point arithmetic
if the kernel is properly configured.

The following code shows how a routine can use floating point arithmetic
to avoid overflow issues when computing the average of a series of integer
values.

```c

int average(int *values, int num_values)
{
    double sum;
    int i;

    sum = 0.0;

    for (i = 0; i < num_values; i++) {
        sum += *values;
        values++;
    }

    return (int)((sum / num_values) + 0.5);
}
```
