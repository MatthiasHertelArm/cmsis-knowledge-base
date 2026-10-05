---
id: "intr-defensive-programming-friend-or-fo-handling-external-application-code"
type: "concept"
domain: "debug"
title: "Defensive Programming - Friend or Foe?: Handling External & Application Code"
summary: "There are places where one would not want to use offensive programming practices. Primarily, it's when the developer is not fully in control of the software, hardware, or incoming data. These could be any of the following:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-15-defensive-and-offensive-programming.md"
doc_source: "https://interrupt.memfault.com/blog/defensive-and-offensive-programming#handling-external-application-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are places where one would not want to use offensive programming
practices. Primarily, it's when the developer is not fully in control of the
software, hardware, or incoming data. These could be any of the following:

- Hardware & peripheral drivers
- Contents of flash or persistent storage
- HAL or 3rd-party libraries
- Data or external inputs from comms stacks
- Language interpreters, such as MicroPython[^micropython] or
  JerryScript[^jerryscript]
- 3rd party applications written by external developers

All of these variables or inputs are outside the control of the developer, and
you should not trust any of them! Developers will do the most creative,
beautiful, terrible, abusive, and dangerous things to your platform, unintended
or not, and you should be very cautious of this.

To prevent bugs from stomping on your lawn, you can isolate these outside layers
with a shim layer that uses defensive programming. This ensures that any bad
inputs, corrupted data, and nefarious actors receive error codes instead of
crashing the software.

One important thing, that can't be stressed enough, is that you can almost
always trust and assume that developers and code internal to your organization
or project will be correct or at least _want_ to be correct. With this in mind,
we can assert everything within the **Internal Software** block and crash the
application or system and provide useful data to internal developers.
