---
id: "intr-integrating-memfault-with-aws-iot-what-is-aws-iot-expresslink"
type: "concept"
domain: "debug"
title: "Integrating Memfault With AWS IoT Core and ExpressLink: What is AWS IoT ExpressLink?"
summary: "Before we dive into the specifics of the aforementioned connectivity module available from Espressif, let's cover some basic information about AWS IoT ExpressLink."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-30-memfault-aws-iot-expresslink.md"
doc_source: "https://interrupt.memfault.com/blog/memfault-aws-iot-expresslink#what-is-aws-iot-expresslink"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before we dive into the specifics of the aforementioned connectivity module
available from Espressif, let's cover some basic information about AWS
IoT ExpressLink. AWS IoT ExpressLink is a hardware and software solution
available through qualified AWS partners to provide connectivity to AWS
with very little coding and very few dependencies. This comes in the
form of a hardware module with software built in that can connect to AWS
IoT Core securely with pre-provisioned keys and certificates. The
interface to the module is a serial UART and implements a small
[AT command set](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg.html).
In this way, the module acts like a "cloud modem." To date,
several AWS IoT ExpressLink
[modules](https://devices.amazonaws.com/search?page=1&sv=iotxplnk)
are in production with cellular and Wi-Fi connectivity available from
these AWS partners: Espressif, Infineon, Realtek, Telit Cinterion, and
u-blox.
