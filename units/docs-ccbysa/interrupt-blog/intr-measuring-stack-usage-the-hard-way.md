---
id: "intr-measuring-stack-usage-the-hard-way"
type: "concept"
domain: "debug"
title: "Measuring Stack Usage the Hard Way"
summary: "Embedded systems often require a careful eye to where memory resources are being spent, especially runtime memory utilization like stack and heap memories."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-06-14-measuring-stack-usage.md"
doc_source: "https://interrupt.memfault.com/blog/measuring-stack-usage"
license: "CC-BY-SA-4.0"
mode: "V"
---

Embedded systems often require a careful eye to where memory resources are being
spent, especially runtime memory utilization like stack and heap memories.



This article is intended to shed some light on strategies for measuring stack
memory usage on a small embedded system.
