---
id: "threadx-chapter-5-device-drivers-for-threa-device-driver-introduction-2"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Device Drivers for ThreadX SMP: Device Driver Introduction"
summary: "Communication with the external environment is an important component of most embedded applications. This communication is accomplished through hardware devices that are accessible to the embedded application software."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter5.md#device-driver-introduction"
license: "MIT"
mode: "V"
---

Communication with the external environment is an important component of most embedded applications. This communication is accomplished through hardware devices that are accessible to the embedded application software. The software components responsible for managing such devices are commonly called *Device Drivers*.

Device drivers in embedded, real-time systems are inherently application dependent. This is true for two principal reasons: the vast diversity of target hardware and the equally vast performance requirements imposed on real-time applications. Because of this, it is virtually impossible to provide a common set of drivers that will meet the requirements of every application. For these reasons, the information in this chapter is designed to help users customize *off-the-shelf* ThreadX SMP device drivers and write their own specific drivers.
