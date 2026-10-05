---
id: "intr-building-a-tiny-cli-shell-for-tiny-when-not-to-build-a-cli-shell"
type: "concept"
domain: "debug"
title: "Building a Tiny CLI Shell for Tiny Firmware: When Not To Build a CLI Shell"
summary: "No article would be useful without the counter-arguments. I've seen a few times where having a CLI shell over serial was not the tool for the job. It might be worth the time to invest in building something else if:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-09-firmware-shell.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-shell#when-not-to-build-a-cli-shell"
license: "CC-BY-SA-4.0"
mode: "V"
---

No article would be useful without the counter-arguments. I've seen a few times
where having a CLI shell over serial was **not** the tool for the job. It might
be worth the time to invest in building something else if:

- The connection to the device is not reliable. You'll need to be able to detect
  dropped bytes and attempt retries.
- The footprint and breadth of the CLI has gotten too big, and it would be
  better to have most of the strings, help menus, argument parsing, and error
  checking be contained with a host-side application.
- You need to maintain multiple connections to a single device over a single
  serial port.
- You are sure that any consumer of the interface (developers, QA, factory
  harnesses) will use the tools your team builds. In this case, I would
  definitely go for the binary protocol route.
