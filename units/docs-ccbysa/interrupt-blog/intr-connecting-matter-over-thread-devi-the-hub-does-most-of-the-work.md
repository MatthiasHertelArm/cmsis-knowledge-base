---
id: "intr-connecting-matter-over-thread-devi-the-hub-does-most-of-the-work"
type: "concept"
domain: "debug"
title: "Connecting Matter-over-Thread Devices to the Internet: The Hub Does Most of the Work"
summary: "Matter is designed so that devices rarely need to talk directly to the internet. Instead, internet-facing communication is delegated to the controller (the hub)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-03-24-matter-internet-connectivity.md"
doc_source: "https://interrupt.memfault.com/blog/matter-internet-connectivity#the-hub-does-most-of-the-work"
license: "CC-BY-SA-4.0"
mode: "V"
---

Matter is designed so that devices rarely need to talk directly to the internet.
Instead, internet-facing communication is delegated to the controller (the hub).

A good example is firmware updates. Matter devices do not check a server directly for updates. Instead, manufacturers publish their update on the Distributed Compliance Ledger (DCL)[^dcl], a blockchain (yes! blockchain!) managed by the CSA. Devices regularly ask their hub for updates, and the hub in turn goes and checks the DCL. If a new update is found on the DCL, the hub downloads it and sends it to the device using a standardized Matter cluster (i.e. message format).

This is true for most Matter operations: device control, event reporting, and
scene management all happen locally. The controller handles cloud integration,
voice assistant bridges, and remote access.

(figure: Matter data model for a door lock)
