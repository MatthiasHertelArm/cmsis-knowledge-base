---
id: "zep-memory-protection-design-thread-stack"
type: "concept"
domain: "rtos"
title: "Memory Protection Design: Thread Stack"
summary: "Any thread running in user mode will need access to its own stack buffer."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/memory_domain.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/memory_domain.rst"
license: "Apache-2.0"
mode: "V"
---

Any thread running in user mode will need access to its own stack buffer.
On context switch into a user mode thread, a dedicated MPU region or MMU
page table entries will be programmed with the bounds of the stack buffer.
A thread exceeding its stack buffer will start pushing data onto memory
it doesn't have access to and a memory access violation exception will be
generated.

Note that user threads have access to the stacks of other user threads in
the same memory domain. This is the minimum required for architectures to
support memory domains. Architecture can further restrict access to stacks
so each user thread only has access to its own stack if such architecture
advertises this capability via
`CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS`.
This behavior is enabled by default if supported and can be selectively
disabled via `CONFIG_MEM_DOMAIN_ISOLATED_STACKS` if
architecture supports both operating modes. However, some architectures
may decide to enable this all the time, and thus this option cannot be
disabled. Regardless of these kconfigs, user threads cannot access
the stacks of other user threads outside of their memory domains.
