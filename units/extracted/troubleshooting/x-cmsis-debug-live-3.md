---
id: "x-cmsis-debug-live-3"
type: "troubleshooting"
domain: "debug"
title: "Serial port held by MS Serial Monitor"
status: "draft"
symptoms: ["PORT_HELD"]
extracted_from: "proc-cmsis-debug-live"
source: "cmsis-debug-live/SKILL.md"
license: "Apache-2.0"
---

If the user has the MS Serial Monitor open on the same device, the OS will not give you the tty (PORT_HELD). serial_subscribe_monitor reads that session only where the Serial Monitor's API exposes a data event; API version 0 has none, so the call is refused and says why. Then ask the user to stop monitoring the port there, and read it with serial_capture once it is free.
