---
id: "zep-tracing-user-defined-tracing"
type: "concept"
domain: "debug"
title: "Tracing: Tracing Tools / User-Defined Tracing"
summary: "This tracing format lets the application define plain C functions that run on each hook, with no need to author or fork a tracing header."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Tracing Tools_

This tracing format lets the application define plain C functions that run on
each hook, with no need to author or fork a tracing header. Each
`sys_port_trace_* hook is routed to a weak` callback named
`sys_trace_<event>_user()`; the application overrides only the callbacks it
cares about, and any callback it leaves undefined is a no-op.

Examples include:

- simple toggling of GPIO for external scope tracing while minimizing extra cpu load
- generating/outputting trace data in a non-standard or proprietary format that can
  not be supported by the other tracing systems

The callbacks cover thread/scheduler, ISR, idle, system init and sleep events,
GPIO, timers, RTIO, and the kernel objects (semaphores, mutexes, condition
variables, message queues, mailboxes, events, polling, memory slabs and work
queues). The authoritative list, with exact signatures, is the set of
`sys_trace_*_user` declarations in
`subsys/tracing/user/tracing_user.h`. A representative subset:

```c

void sys_trace_thread_create_user(struct k_thread *thread);
void sys_trace_thread_switched_in_user(void);
void sys_trace_thread_switched_out_user(void);
void sys_trace_isr_enter_user(void);
void sys_trace_isr_exit_user(void);
void sys_trace_idle_user(void);
void sys_trace_k_sem_give_enter_user(struct k_sem *sem);
void sys_trace_k_mutex_lock_enter_user(struct k_mutex *mutex, k_timeout_t timeout);
```
Enable this format with the `CONFIG_TRACING_USER` option.
`tests/subsys/tracing/tracing_user_callbacks` shows an application
overriding object callbacks.
