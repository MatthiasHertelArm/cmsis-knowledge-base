---
id: "txmw-chapter-2-usbx-device-stack-instal-source-code-tree"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Device Stack Installation: Source Code Tree"
summary: "The USBX files are provided in several directories."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-device-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-device-stack-2.md#source-code-tree"
license: "MIT"
mode: "V"
---

The USBX files are provided in several directories.

(figure: Source Code Tree)

In order to make the files recognizable by their names, the following convention has been adopted:

| File Suffix Name  | File description                          |
| ----------------- | ----------------------------------------- |
| ux_host_stack     | usbx host stack core files                |
| ux_host_class     | usbx host stack classes files             |
| ux_hcd            | usbx host stack controller driver files   |
| ux_device_stack   | usbx device stack core files              |
| ux_device_class   | usbx device stack classes files           |
| ux_dcd            | usbx device stack controller driver files |
| ux_otg            | usbx otg controller driver related files  |
| ux_pictbridge     | usbx pictbridge files                     |
| ux_utility        | usbx utility functions                    |
| demo_usbx         | demonstration files for USBX              |
