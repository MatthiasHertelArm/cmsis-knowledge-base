---
id: "zep-semaphores-user-mode-semaphore-api-reference"
type: "concept"
domain: "rtos"
title: "Semaphores: User Mode Semaphore API Reference"
summary: "The sys_sem exists in user memory, working as counter semaphore for user mode threads, when user mode is enabled. When user mode isn't enabled, sys_sem behaves like k_sem."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/synchronization/semaphores.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/synchronization/semaphores.rst"
license: "Apache-2.0"
mode: "V"
---

The `sys_sem` exists in user memory, working as counter semaphore for user mode
threads, when user mode is enabled. When user mode isn't enabled, `sys_sem` behaves
like `k_sem`.
