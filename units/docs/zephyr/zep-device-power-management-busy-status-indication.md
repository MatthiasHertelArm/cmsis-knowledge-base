---
id: "zep-device-power-management-busy-status-indication"
type: "concept"
domain: "optimization"
title: "Device Power Management: Busy Status Indication"
summary: "When the system is idle and the SoC is going to sleep, the power management subsystem can suspend devices, as described in pm-device-system-pm. This can cause device hardware to lose some states."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/pm/device.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/pm/device.rst"
license: "Apache-2.0"
mode: "V"
---

When the system is idle and the SoC is going to sleep, the power management
subsystem can suspend devices, as described in pm-device-system-pm. This
can cause device hardware to lose some states. Suspending a device which is in
the middle of a hardware transaction, such as writing to a flash memory, may
lead to undefined behavior or inconsistent states. This API guards such
transactions by indicating to the kernel that the device is in the middle of an
operation and should not be suspended.

When `pm_device_busy_set` is called, the device is marked as busy and
the system will not do power management on it. After the device is no
longer doing an operation and can be suspended, it should call
`pm_device_busy_clear`.
