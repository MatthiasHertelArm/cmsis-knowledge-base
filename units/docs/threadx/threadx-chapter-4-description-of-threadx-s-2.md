---
id: "threadx-chapter-4-description-of-threadx-s-2"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX SMP Services"
summary: "This chapter contains a description of all ThreadX SMP services in alphabetic order. Their names are designed so all similar services are grouped together."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter4.md"
license: "MIT"
mode: "V"
---

This chapter contains a description of all ThreadX SMP services in alphabetic order. Their names are designed so all similar services are grouped together. In the "Return Values" section in the following descriptions, values in **BOLD** are not affected by the **TX_DISABLE_ERROR_CHECKING** define used to disable API error checking; while values shown in nonbold are completely disabled. In addition, a "**Yes**" listed under the "**Preemption Possible**" heading indicates that calling the service may resume a higher-priority thread, thus preempting the calling thread.

The Threadx SMP API functions available to the application are as follows.
