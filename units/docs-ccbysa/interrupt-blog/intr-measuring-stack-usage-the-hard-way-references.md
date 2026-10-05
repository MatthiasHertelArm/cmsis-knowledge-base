---
id: "intr-measuring-stack-usage-the-hard-way-references"
type: "concept"
domain: "debug"
title: "Measuring Stack Usage the Hard Way: References"
summary: "Measuring Stack Usage the Hard Way: References"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-06-14-measuring-stack-usage.md"
doc_source: "https://interrupt.memfault.com/blog/measuring-stack-usage#references"
license: "CC-BY-SA-4.0"
mode: "V"
---

- Overview of stack and heap:
  <https://courses.engr.illinois.edu/cs225/fa2022/resources/stack-heap/>
- Tutorial on FreeRTOS memory usage:
  <https://www.digikey.com/en/maker/projects/introduction-to-rtos-solution-to-part-4-memory-management/6d4dfcaa1ff84f57a2098da8e6401d9c>
- Nice strategy for stack overflow protection via a 2-pass link, without using
  an MPU: <https://blog.japaric.io/stack-overflow-protection/>
- Static stack analysis for rust programs:
  <https://blog.japaric.io/stack-analysis/>
- Useful compiler flags around stack usage:
  <https://embeddedartistry.com/blog/2020/08/17/three-gcc-flags-for-analyzing-memory-usage/>
- Very cool tracing system (requires some tinkering to use on an unhosted target
  though): <https://justine.lol/ftrace/>
- FreeRTOS stack overview:
  <https://moji1.github.io/EEE499/assets/docs/freertos1.pdf>
