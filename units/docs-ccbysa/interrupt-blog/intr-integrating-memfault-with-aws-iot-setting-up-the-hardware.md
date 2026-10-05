---
id: "intr-integrating-memfault-with-aws-iot-setting-up-the-hardware"
type: "concept"
domain: "debug"
title: "Integrating Memfault With AWS IoT Core and ExpressLink: Setting up the Hardware"
summary: "In this article, we are using the Espressif dev kit with Wi-Fi connectivity. You can follow the links above to discover various procurement options. Configuration of the dev kit is straightforward by following the steps in this guide from Espressif."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-30-memfault-aws-iot-expresslink.md"
doc_source: "https://interrupt.memfault.com/blog/memfault-aws-iot-expresslink#setting-up-the-hardware"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this article, we are using the Espressif dev kit with Wi-Fi connectivity.
You can follow the links above to discover various procurement options.
Configuration of the dev kit is straightforward by following the steps in
[this guide](https://github.com/espressif/esp-aws-expresslink-eval) from
Espressif. At a minimum, AWS IoT Core must be provided the device certificate
and name, and the module must be provided the MQTT endpoint along with the
Wi-Fi credentials. Once you finish the configuration, simply plug in the
dev kit to the STM32G0 Nucleo board as shown in the setup below.



To program the firmware of the device, you can leverage the
I-CUBE-ExpressLink expansion mentioned earlier in the article. To set up
your development environment, follow the instructions from
STMicroelectronics in [this guide](https://github.com/stm32-hotspot/I-CUBE-ExpressLink).
The steps include the installation of several packs in your development
environment. There are examples and code provided so you can get your
device connected to AWS IoT Core and publish data over MQTT topics. Of
course, you can connect different kinds of sensors to the device and
capture the readings within your code to send as data to the cloud for
processing as well.


