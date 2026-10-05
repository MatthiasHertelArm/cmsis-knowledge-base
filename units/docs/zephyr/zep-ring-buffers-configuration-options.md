---
id: "zep-ring-buffers-configuration-options"
type: "concept"
domain: "rtos"
title: "Ring Buffers: Configuration Options"
summary: "Ring Buffers: Configuration Options"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/data_structures/ring_buffers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/data_structures/ring_buffers.rst"
license: "Apache-2.0"
mode: "V"
---

Related configuration options:

* `CONFIG_RING_BUFFER`: Restore the deprecated legacy ring
  buffer APIs (the claim/finish and fixed-size item APIs). The ring buffer
  itself is header-only and always available, so this option is not required
  for normal use.
* `CONFIG_RING_BUFFER_LARGE`: Increase the maximum buffer size
  from 32KB to 1GB.
