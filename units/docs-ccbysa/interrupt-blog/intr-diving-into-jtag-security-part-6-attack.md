---
id: "intr-diving-into-jtag-security-part-6-attack"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Security (Part 6): Attack"
summary: "Naturally, if there are defense mechanisms against the use of debugging interfaces, there are also well-known vulnerabilities in these defense mechanisms. Let's consider the main and most well-known of them."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-08-14-diving-into-jtag-part-6.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-6#attack"
license: "CC-BY-SA-4.0"
mode: "V"
---

Naturally, if there are defense mechanisms against the use of debugging
interfaces, there are also well-known vulnerabilities in these defense
mechanisms. Let's consider the main and most well-known of them.

In general, all attacks can be divided into the following types:

- Software attacks are carried out in particular by exploiting bugs, weaknesses
  in protocols or untrusted code fragments. Attacks on communication channels
  (interception or usurpation) fall into this category. Software attacks account
  for the vast majority of cases. Their cost can be very low. They can be
  widespread and repeatable with tremendous damage. It is not necessary to have
  physical access to the device. The attack can be performed remotely.
- Hardware attacks require physical access to the device. The most obvious one
  uses the debug port if it is not secured. In general, however, hardware
  attacks are complex and expensive. They are carried out with specialized
  materials and require electronics skills. There is a distinction between
  non-invasive attacks (carried out at the board or chip level without
  destroying the device) and invasive attacks (carried out at the device and
  silicon level with the destruction of the package).

Attacks on the JTAG interface belong to the hardware non-invasive attack type.
