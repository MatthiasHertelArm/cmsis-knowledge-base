---
id: "threadx-chapter-1-overview"
type: "concept"
domain: "rtos"
title: "Chapter 1  Overview"
summary: "The ARMv8-M architecture introduces new security features, including TrustZone, which allows memory to be tagged as secure or non-secure. Following ARM's guidelines, ThreadX (and the user application) is designed to be run in non-secure mode."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/user-guide-armv8m/chapter1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/user-guide-armv8m/chapter1.md"
license: "MIT"
mode: "V"
---

The ARMv8-M architecture introduces new security features, including TrustZone, which allows memory to be tagged as secure or non-secure. Following ARM's guidelines, ThreadX (and the user application) is designed to be run in non-secure mode. ThreadX (and the user application) can also be run in secure mode. In order to interface with secure mode software, some new ThreadX APIs are necessary. This document describes these ThreadX services that are specific to the ARMv8-M architecture, including the Cortex-M23, Cortex-M33, Cortex-M35P, and Cortex-M55.
