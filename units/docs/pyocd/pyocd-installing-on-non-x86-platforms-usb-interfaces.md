---
id: "pyocd-installing-on-non-x86-platforms-usb-interfaces"
type: "concept"
domain: "debug"
title: "Installing on non-x86 platforms: USB interfaces"
summary: "The other dependencies that might be problematic are those for USB communications. pyOCD uses three USB libraries:"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/installing_on_non_x86.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/installing_on_non_x86.md#usb-interfaces"
license: "Apache-2.0"
mode: "V"
---

The other dependencies that might be problematic are those for USB communications. pyOCD uses
three USB libraries:

- pyusb and libusb: CMSIS-DAPv1 on Linux, CMSIS-DAPv2 and STLink on all OSes
- hidapi: CMSIS-DAPv1 on macOS
- pywinusb: CMSIS-DAPv1 on Windows

Thankfully, libusb is provided by default on most Linux systems, including Raspberry Pi and similar
platforms. So on almost all platforms, USB is not a real problem.

If you are using an alternative OS, you may have trouble finding a functional USB library. In this
case, the options would be to port libusb and/or hidapi to your OS, or even to extend pyOCD with
support for another USB interface package.
