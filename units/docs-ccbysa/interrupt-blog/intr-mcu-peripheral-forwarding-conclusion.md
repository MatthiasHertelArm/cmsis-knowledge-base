---
id: "intr-mcu-peripheral-forwarding-conclusion"
type: "concept"
domain: "debug"
title: "MCU Peripheral Forwarding: Conclusion"
summary: "In conclusion, we've explored the fundamentals of Chip Peripheral Forwarding technology, laying down the basis for its understanding and implementation."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-10-11-mcu-peripheral-forwarding.md"
doc_source: "https://interrupt.memfault.com/blog/mcu-peripheral-forwarding#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

In conclusion, we've explored the fundamentals of Chip Peripheral Forwarding technology, laying down the basis for its understanding and implementation.
This approach emerges as a versatile technology, simplifying the expansion of peripherals for both PC and embedded systems, such as the Raspberry Pi. Moreover, it significantly bolsters hardware equipment testing, harnessing the capabilities of PC program tools such as high-level languages like Python and interactive shells like Jupyter Notebook, and it eliminates the need for firmware and communication protocol development.

To witness this technology in action, look no further than the [**REMCU examples repository**](https://github.com/remotemcu/remcu_examples). Here, a diverse array of practical examples is offered, specifically crafted for various MCUs.

*In the GIF demonstration below, we offer a vivid glimpse into the capabilities of the QT example application. This software charts gyroscope data along three distinct axes, providing visual insight into the device's orientation and motion. The gyroscope sensor,  mounted on the STM32F3 Discovery board, communicates via the I2C protocol. In this application, the I2C port of the STM32F3 microcontroller serves as a direct conduit to the PC environment. This connection is established effortlessly by using the STM32 Standard Peripheral Library, instrumented with REMCU.
More detail in [Plotter of Gyroscope example](https://github.com/remotemcu/remcu_examples/tree/master/stm32f3_discovery/gyro_graph)*
(figure: REMCU MEMS STM32 Example)

These examples, combined with accompanying [video tutorials](https://remotemcu.com/tutorials), offer hands-on insights into effectively integrating REMCU into your own projects.

In [this](https://ser-mk.github.io/remcu/tutorial-preparing-nrf51-sdk/) guide, we will lead you through the procedure of preparing drivers for the nRF51422 MCU. The prime objective of this guide is to empower you to fabricate your very own REMCU shared/dynamic library, meticulously tailored to your distinct MCU and its SDK.







{:.no_toc}
