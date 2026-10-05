---
id: "zep-thread-local-storage-tls-declaring-and-using-thread-local-variabl"
type: "concept"
domain: "rtos"
title: "Thread Local Storage (TLS): Declaring and Using Thread Local Variables"
summary: "The macro Z_THREAD_LOCAL can be used to declare thread local variables."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/other/thread_local_storage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/other/thread_local_storage.rst"
license: "Apache-2.0"
mode: "V"
---

The macro `Z_THREAD_LOCAL` can be used to declare thread local variables.

For example, to declare a thread local variable in header files:

```c

extern Z_THREAD_LOCAL int i;
```
And to declare the actual variable in source files:

```c

Z_THREAD_LOCAL int i;
```
Keyword `static` can also be used to limit the variable within a source file:

```c

static Z_THREAD_LOCAL int j;
```
Using the thread local variable is the same as using other variable, for example:

```c

void testing(void) {
    i = 10;
}
```
