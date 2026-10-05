---
id: "intr-separating-unique-parameters-from"
type: "concept"
domain: "debug"
title: "Separating Unique Parameters from Firmware Binaries"
summary: "When writing firmware for embedded systems, the firmware is usually meant to run on many identical devices. These devices often have their own serial number, public and private keys, or some other unique parameters."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-10-06-separating-unique-parameters.md"
doc_source: "https://interrupt.memfault.com/blog/separating-unique-parameters"
license: "CC-BY-SA-4.0"
mode: "V"
---

When writing firmware for embedded systems, the firmware is usually meant to run
on many identical devices. These devices often have their own serial
number, public and private keys, or some other unique parameters. These
parameters need to be provisioned per device, either by generating unique
firmware binaries or by writing the values to the device's persistent storage, like
external flash or the EEPROM.

During the firmware development phase, most of us start out by hardcoding these
parameters and recompiling the code every time a new device needs to be
programmed. While this is fine during the early development stages, it doesn't
scale as the number of devices grows.



In this post, we take a look at a method for separating unique parameters such
as keys and IDs from firmware. This enables us to program these parameters
separately from the firmware, making our setup much more scalable and suitable
for use in production.
