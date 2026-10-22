---
id: "zep-system-calls-verifier-definition"
type: "concept"
domain: "rtos"
title: "System Calls: Verification Function / Verifier Definition"
summary: "All system calls are dispatched to a verifier function with a prefixed z_vrfy name based on the system call. They have exactly the same return type and argument types as the wrapped system call."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/syscalls.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/syscalls.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Verification Function_

All system calls are dispatched to a verifier function with a prefixed
`z_vrfy_` name based on the system call.  They have exactly the same
return type and argument types as the wrapped system call.  Their job
is to execute the system call (generally by calling the implementation
function) after having validated all arguments.

The verifier is itself invoked by an automatically generated
unmarshaller function which takes care of unpacking the register
arguments from the architecture layer and casting them to the correct
type.  This is defined in a header file that must be included from
user code, generally somewhere after the definition of the verifier in
a translation unit (so that it can be inlined).

For example:

```c

static int z_vrfy_k_sem_take(struct k_sem *sem, int32_t timeout)
{
    K_OOPS(K_SYSCALL_OBJ(sem, K_OBJ_SEM));
    return z_impl_k_sem_take(sem, timeout);
}
#include <zephyr/syscalls/k_sem_take_mrsh.c>
```
