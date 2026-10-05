---
id: "intr-a-deep-dive-into-arm-cortex-m-debu-tracing-a-transaction"
type: "concept"
domain: "debug"
title: "A Deep Dive into ARM Cortex-M Debug Interfaces: Tracing a Transaction"
summary: "Now that we understand a bit about the software stack in play. Let's trace through a transaction to better understand what's happening end to end."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-06-a-deep-dive-into-arm-cortex-m-debug-interfaces.md"
doc_source: "https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces#tracing-a-transaction"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we understand a bit about the software stack in play. Let's trace through a transaction to better understand what's happening end to end.

For this setup we will use:

- A nRF52840-DK running the blinky demo application from our [MPU blog post](https://interrupt.memfault.com/blog/fix-bugs-and-secure-firmware-with-the-mpu#mpu-usage-examples)
- A saleae logic analyzer[^18]
