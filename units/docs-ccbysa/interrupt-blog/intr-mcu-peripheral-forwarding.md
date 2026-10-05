---
id: "intr-mcu-peripheral-forwarding"
type: "concept"
domain: "debug"
title: "MCU Peripheral Forwarding"
summary: "PC applications that interact with MCUs are used by developers for a number of reasons, such as data visualization, monitoring during testing campaigns, and command and control via a GUI."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-10-11-mcu-peripheral-forwarding.md"
doc_source: "https://interrupt.memfault.com/blog/mcu-peripheral-forwarding"
license: "CC-BY-SA-4.0"
mode: "V"
---

PC applications that interact with MCUs are used by developers for a number of reasons, such as data visualization, monitoring during testing campaigns, and command and control via a GUI. In this article, we'll explore mapping an MCU's peripherals to your personal computer to simplify development of PC applications built for embedded systems.







---

Embedded systems development often involves utilizing various microcontroller peripherals such as CAN buses, I2C buses, DACs, ADCs, and more. However, when integrating these functionalities into PC applications, developers are typically required to develop firmware and communication protocols, which can add complexity to the overall software stack. They can avoid this additional work if the chip peripheral registers are directly mapped into the address space of our PC programs. We'll explore two options for instrumenting your PC application to perform this mapping.
