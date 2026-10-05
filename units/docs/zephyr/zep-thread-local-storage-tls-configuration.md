---
id: "zep-thread-local-storage-tls-configuration"
type: "concept"
domain: "rtos"
title: "Thread Local Storage (TLS): Configuration"
summary: "To enable thread local storage in Zephyr, CONFIG_THREAD_LOCAL_STORAGE needs to be enabled."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/other/thread_local_storage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/other/thread_local_storage.rst"
license: "Apache-2.0"
mode: "V"
---

To enable thread local storage in Zephyr, `CONFIG_THREAD_LOCAL_STORAGE`
needs to be enabled. Note that this option may not be available if
the architecture or the SoC does not have the hidden option
`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE` enabled, which means
the architecture or the SoC does not have the necessary code to support
thread local storage and/or the toolchain does not support TLS.

`CONFIG_ERRNO_IN_TLS` can be enabled together with
`CONFIG_ERRNO` to let the variable `errno` be a thread local
variable. This allows user threads to access the value of `errno` without
making a system call.
