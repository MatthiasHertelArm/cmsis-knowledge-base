---
id: "intr-building-a-tiny-cli-shell-for-tiny-why-build-a-device-shell"
type: "concept"
domain: "debug"
title: "Building a Tiny CLI Shell for Tiny Firmware: Why Build a Device Shell?"
summary: "During all phases of development, you need a way to interact with the device."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-09-firmware-shell.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-shell#why-build-a-device-shell"
license: "CC-BY-SA-4.0"
mode: "V"
---

During all phases of development, you need a way to interact with the device.
You need to be able to query the device for its configuration, state, and
information for debugging purposes, as well as send commands for setup and
operation. For most devices, the easiest way is to have a direct serial
connection. However, just having a serial connection is not enough. There needs
to be a structured protocol on top of the serial port, and having a shell could
meet those criteria.

There are alternatives to building a CLI over serial that should be mentioned.
I've worked on projects that use binary protocols and interfaces on top of a
serial connection, either by using custom byte-packing, Protobuf, or CBOR. I've
also heard of projects not use a serial connection at all, and instead use an
existing Bluetooth or Wi-Fi connection to channel data over. The problem with
both of these alternatives is that to make these connections and protocols
_useful_ and _reliable_ to the developer and automated systems, many extra
layers need to be built on top of them, including a shell. Bluetooth and Wi-Fi
may also fail due to software bugs or radio interference. This is not the case
with serial over UART.
