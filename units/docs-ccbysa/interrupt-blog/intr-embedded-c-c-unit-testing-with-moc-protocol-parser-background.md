---
id: "intr-embedded-c-c-unit-testing-with-moc-protocol-parser-background"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: Real World Unit Test Example / Protocol Parser Background"
summary: "The protocol we are going to make a parser for is very simple. Each message has a Command, a payload Size, and a Payload."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#protocol-parser-background"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

The protocol we are going to make a parser for is very simple. Each message has
a **Command**, a payload **Size**, and a **Payload**.



We added the **command** field because we want to build a flexible protocol that
can tell the device to do more things than just read and write key/value ("kv")
pairs.

Some other common remote commands I've seen implemented include:

- Reading the version of the firmware loaded on the device
- Ping/Pong command to ensure the device is awake and functional
- A way to remotely reboot or factory reset devices (ensure this endpoint is
  secured in some way)

All of these are possible using the **command** field, but today, we are going
to focus on reading and writing key/value pairs on the device.
