---
id: "intr-mcuboot-walkthrough-and-porting-gu"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide"
summary: "In previous articles such as How to Write a Bootloader from Scratch, device firmware update strategies, & how to securely sign firmware updates, we have explored the various parts that make up a bootloader and DFU subsystem."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview"
license: "CC-BY-SA-4.0"
mode: "V"
---

In previous articles such as [How to Write a Bootloader from Scratch](https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch), [device firmware update strategies](https://interrupt.memfault.com/blog/device-firmware-update-cookbook), & [how to securely sign firmware updates](https://interrupt.memfault.com/blog/secure-firmware-updates-with-code-signing), we have explored the various parts that make up a bootloader and DFU subsystem. We have seen there are a lot of pieces that need to come together for the system to work reliably and be secure.

Over the last few years, an interesting open-source project, [MCUboot](https://github.com/mcu-tools/mcuboot), has surfaced seeking to
simplify and standardize the approach to these problems.  MCUboot was chosen as the bootloader to
be used with the Zephyr RTOS[^2]. Implementations using MCUboot have even been incorporated in
semiconductor provided SDKs such as Nordic's nRF Connect SDK [^2] for the NRF91 & NRF53 MCUs.

If you are working on a new project, MCUboot is worth a look! At the very least, some of the design
decisions can be used to help guide your own solution.



In this article, we will explore the feature set of MCUboot and how it works. We will walk through
step-by-step how to port it to a custom platform and test our port out on a Cortex-M based development board.



> Note: While the focus of this article is about MCUboot, the general strategy outlined for porting
> MCUboot to a new platform can be used as a guide for incorporating other third-party libraries
> into an embedded project.
