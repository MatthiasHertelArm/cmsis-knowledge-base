---
id: "intr-a-guide-to-using-arm-stack-limit-r"
type: "concept"
domain: "debug"
title: "A Guide to Using ARM Stack Limit Registers"
summary: "Stack overflows have notoriously plagued the development processes. They often can go undetected and can present themselves in obscure ways. We have implemented software mechanisms to protect against them, but these have limitations and still don't protect against all conditions."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-02-14-using-psp-msp-limit-registers-for-stack-overflow.md"
doc_source: "https://interrupt.memfault.com/blog/using-psp-msp-limit-registers-for-stack-overflow"
license: "CC-BY-SA-4.0"
mode: "V"
---

Stack overflows have notoriously plagued the development processes. They often
can go undetected and can present themselves in obscure ways. We have
implemented software mechanisms to protect against them, but these have
limitations and still don't protect against all conditions.

With the maturity of the ARM architecture, wouldn't it be better to have a
fool-proof mechanism for detecting overflows?



We will explore using the MSP Limit and the PSP Limit Registers on the ARM
Cortex-M33 architecture to detect stack overflows. We will walk through an
implementation on the Renesas DA1469x and look at practical examples of
detecting stack overflows. Additionally, we will look at supplementary options
for scenarios that the MSPLIM and PSPLIM features fall short.
