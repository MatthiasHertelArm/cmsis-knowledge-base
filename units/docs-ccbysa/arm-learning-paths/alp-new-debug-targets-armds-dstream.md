---
id: "alp-new-debug-targets-armds-dstream"
type: "concept"
domain: "debug"
title: "Add new debug targets to Arm Development Studio: Debug connection with Arm DSTREAM"
summary: "The DSTREAM family of debug probes are a scalable solution for debug and trace of Arm based platforms. They are used in conjunction with the Arm Development Studio debugger."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/dstream.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/dstream/"
license: "CC-BY-SA-4.0"
mode: "V"
---

The [DSTREAM](https://developer.arm.com/Tools%20and%20Software/DSTREAM-ST#Editions) family of debug probes are a scalable solution for debug and trace of Arm based platforms. They are used in conjunction with the Arm Development Studio debugger. They can connect to the host machine over high speed USB or Ethernet connections.

The family consists of:
 - [DSTREAM-ST](https://developer.arm.com/Tools%20and%20Software/DSTREAM-ST)
 - [DSTREAM-PT](https://developer.arm.com/Tools%20and%20Software/DSTREAM-PT)
 - [DSTREAM-HT](https://developer.arm.com/Tools%20and%20Software/DSTREAM-HT)
 - [DSTREAM-XT](https://developer.arm.com/Tools%20and%20Software/DSTREAM-XT)

DSTREAM-ST provides full debug capability over JTAG and SWD interfaces, as well as on-chip and low bandwidth (4-bit) external trace. If higher bandwidth trace is necessary, then one of the other solutions can be used, provided the SoC (and platform) support such features.

 - DSTREAM-PT adds the capability to support (up to) 32-bit parallel trace output.
 - DSTREAM-HT adds the capability to support (up to) 6 lanes of High-Speed Serial Trace (HSST)
 - DSTREAM-XT adds the capability to support (debug and) trace over PCIe interface.
