---
id: "zep-system-calls"
type: "concept"
domain: "rtos"
title: "System Calls"
summary: "User threads run with a reduced set of privileges than supervisor threads: certain CPU instructions may not be used, and they have access to only a limited part of the memory map."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/syscalls.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/syscalls.rst"
license: "Apache-2.0"
mode: "V"
---

User threads run with a reduced set of privileges than supervisor threads:
certain CPU instructions may not be used, and they have access to only a
limited part of the memory map. System calls (may) allow user threads to
perform operations not directly available to them.

When defining system calls, it is very important to ensure that access to the
API's private data is done exclusively through system call interfaces.
Private kernel data should never be made available to user mode threads
directly. For example, the `k_queue` APIs were intentionally not made
available as they store bookkeeping information about the queue directly
in the queue buffers which are visible from user mode.

APIs that allow the user to register callback functions that run in
supervisor mode should never be exposed as system calls. Reserve these
for supervisor-mode access only.

This section describes how to declare new system calls and discusses a few
implementation details relevant to them.
