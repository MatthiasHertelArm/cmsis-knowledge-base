---
id: "zep-kernel-objects-initialization-state"
type: "concept"
domain: "rtos"
title: "Kernel Objects: Initialization State"
summary: "Most operations on kernel objects will fail if the object is considered to be in an uninitialized state. The appropriate init function for the object must be performed first."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/kernelobjects.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/kernelobjects.rst"
license: "Apache-2.0"
mode: "V"
---

Most operations on kernel objects will fail if the object is considered to be
in an uninitialized state. The appropriate init function for the object must
be performed first.

Some objects will be implicitly initialized at boot:

* Kernel objects that were declared with static initialization macros
  (such as `K_SEM_DEFINE` for semaphores) will be in an initialized
  state at build time.

* Device driver objects are considered initialized after their init function
  is run by the kernel early in the boot process.

If a kernel object is initialized with a private static initializer, the object
must have `k_object_init` called on it at some point by a supervisor
thread, otherwise the kernel will consider the object uninitialized if accessed
by a user thread. This is very uncommon, typically only for kernel objects that
are embedded within some larger struct and initialized statically.

```c

struct foo {
    struct k_sem sem;
    ...
};

struct foo my_foo = {
    .sem = Z_SEM_INITIALIZER(my_foo.sem, 0, 1),
    ...
};

...
k_object_init(&my_foo.sem);
...
```
