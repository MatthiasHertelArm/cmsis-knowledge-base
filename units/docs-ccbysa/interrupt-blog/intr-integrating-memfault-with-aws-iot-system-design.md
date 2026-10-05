---
id: "intr-integrating-memfault-with-aws-iot-system-design"
type: "concept"
domain: "debug"
title: "Integrating Memfault With AWS IoT Core and ExpressLink: System Design"
summary: "First, let's take a look at the high-level architecture. This article will cover the primary components identified along with how they fit together."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-30-memfault-aws-iot-expresslink.md"
doc_source: "https://interrupt.memfault.com/blog/memfault-aws-iot-expresslink#system-design"
license: "CC-BY-SA-4.0"
mode: "V"
---

First, let's take a look at the high-level architecture.
This article will cover the primary components identified along
with how they fit together. The device side is primarily hardware, but
will also include your custom firmware as well as any specific device
configuration. The cloud side leverages AWS services as a bridge to
Memfault.



In this design, the STM32G0 Nucleo board serves as a versatile
development platform based on the
[STM32G0 series](https://www.st.com/en/microcontrollers-microprocessors/stm32g0-series.html)
of microcontrollers. The STM32G0 is a low-cost, low-power, 32-bit MCU based
on the Arm Cortex-M0+. It offers a solid foundation for prototyping and
developing embedded applications. Peripherals such as sensors and actuators can
be easily attached to suit the intended behavior of the device.
STMicroelectronics has a rich and extensible development environment with
[STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html)
and [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html)
that can be used for the STM32G0. In conjunction with these tools,
STMicroelectronics also developed the
[I-CUBE-ExpressLink](https://github.com/stm32-hotspot/I-CUBE-ExpressLink)
expansion to make developing firmware with AWS IoT ExpressLink connectivity
modules incredibly easy. The board comes complete with Arduino headers, which
is a perfect interface to plug in the
[AWS IoT ExpressLink development kit from Espressif](https://www.espressif.com/en/solutions/device-connectivity/esp-aws-iot-expresslink).
