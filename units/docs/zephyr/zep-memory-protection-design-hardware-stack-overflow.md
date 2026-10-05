---
id: "zep-memory-protection-design-hardware-stack-overflow"
type: "concept"
domain: "rtos"
title: "Memory Protection Design: Hardware Stack Overflow"
summary: "CONFIG_HW_STACK_PROTECTION is an optional feature which detects stack buffer overflows when the system is running in supervisor mode. This catches issues when the entire stack buffer has overflowed, and not individual stack frames, use compiler-assisted CONFIG_STACK_CANARIES for that."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/usermode/memory_domain.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/usermode/memory_domain.rst"
license: "Apache-2.0"
mode: "V"
---

`CONFIG_HW_STACK_PROTECTION` is an optional feature which detects stack
buffer overflows when the system is running in supervisor mode. This
catches issues when the entire stack buffer has overflowed, and not
individual stack frames, use compiler-assisted `CONFIG_STACK_CANARIES`
for that.

Like any crash in supervisor mode, no guarantees can be made about the overall
health of the system after a supervisor mode stack overflow, and any instances
of this should be treated as a serious error. However it's still very useful to
know when these overflows happen, as without robust detection logic the system
will either crash in mysterious ways or behave in an undefined manner when the
stack buffer overflows.

Some systems implement this feature by creating at runtime a 'guard' MPU region
which is set to be read-only and is at either the beginning or immediately
preceding the supervisor mode stack buffer.  If the stack overflows an
exception will be generated.

This feature is optional and is not required to catch stack overflows in user
mode; disabling this may free 1-2 MPU regions depending on the MPU design.

Other systems may have dedicated CPU support for catching stack overflows
and no extra MPU regions will be required.
