---
id: "intr-diving-into-jtag-debugging-part-2-jtag-access-to-the-stm32f407vg-controlle"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Debugging (Part 2): JTAG Access to the STM32F407VG Controller"
summary: "Before connecting to the STM32F407VG controller via the JTAG protocol, we need to determine the following: the length of the IR register and the number of TAP controllers connected to the JTAG chain."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-29-diving-into-jtag-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-2#jtag-access-to-the-stm32f407vg-controller"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before connecting to the STM32F407VG controller via the JTAG protocol, we need to determine the following: the length of the `IR` register and the number of TAP controllers connected to the JTAG chain. The official documentation, specifically the [RM0090: Reference manual](https://www.st.com/resource/en/reference_manual/rm0090-stm32f405415-stm32f407417-stm32f427437-and-stm32f429439-advanced-armbased-32bit-mcus-stmicroelectronics.pdf), can assist us in this.

According to this document, the STM32F407VG has two TAP controllers: the STM32 Boundary Scan and the CoreSight JTAG-DP. The first in the chain is the Boundary Scan TAP with a `IR` register size of 5 bits. Following it is the CoreSight JTAG-DP TAP with a `IR` register size of 4 bits.



This knowledge is crucial for us because it determines how many bits to send in the JTAG chain and in what sequence to do so when accessing different TAP controllers. According to this information, we can connect to the CoreSight JTAG-DP TAP controller and attempt to read its `IDCODE`.
