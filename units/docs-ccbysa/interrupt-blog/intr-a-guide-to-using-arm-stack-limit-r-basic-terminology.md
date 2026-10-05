---
id: "intr-a-guide-to-using-arm-stack-limit-r-basic-terminology"
type: "concept"
domain: "debug"
title: "A Guide to Using ARM Stack Limit Registers: Basic Terminology"
summary: "The ARM Cortex-M33 introduced two new stack limit registers, PSPLIM and MSPLIM [^m33-psplim_msplim]. ARM has included this in its ARMv8 specification, so any processors before this will not have support."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-02-14-using-psp-msp-limit-registers-for-stack-overflow.md"
doc_source: "https://interrupt.memfault.com/blog/using-psp-msp-limit-registers-for-stack-overflow#basic-terminology"
license: "CC-BY-SA-4.0"
mode: "V"
---

The ARM Cortex-M33 introduced two new stack limit registers, PSPLIM and MSPLIM
[^m33-psplim_msplim]. ARM has included this in its ARMv8 specification, so any
processors before this will not have support.
