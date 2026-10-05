---
id: "intr-beyond-error-codes-debugging-ill-d-step-8-mcu-errata-and-application-notes"
type: "concept"
domain: "debug"
title: "Beyond Error Codes - Debugging Ill-Defined Problems: Steps / Step 8 - MCU Errata and Application Notes"
summary: "The reason checking the eratta and application notes is so far down the list is that this assumes at one point you did at least glance through the errata section of your MCU's datasheet."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-04-18-debugging-steps.md"
doc_source: "https://interrupt.memfault.com/blog/debugging-steps#step-8-mcu-errata-and-application-notes"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps_

The reason checking the eratta and application notes is so far down the list is
that this assumes at one point you _did_ at least glance through the errata
section of your MCU's datasheet. Now, we're digging back through errata and
application notes, hoping that we missed something during the first readthrough
and that we could attribute our odd behavior to a silicon bug or a known issue.
Application notes can be extremely helpful to read through, especially for some
of the more complicated/mission-critical peripherals listed above. Using the
same STM32 example as for the MPU, ST has
[provided an application note](https://www.st.com/resource/en/application_note/an4031-using-the-stm32f2-stm32f4-and-stm32f7-series-dma-controller-stmicroelectronics.pdf)
specifically on using the DMA. There's even a specific section with "Tips and
Warnings"!
