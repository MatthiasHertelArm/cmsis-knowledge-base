---
id: "txmw-chapter-5-i-o-drivers-for-filex-i-o-driver-introduction"
type: "concept"
domain: "rtos"
title: "Chapter 5 - I/O Drivers for FileX: I/O Driver Introduction"
summary: "FileX supports multiple media devices. The FX_MEDIA structure defines everything required to manage a media device. This structure contains all media information, including the media-specific I/O driver and associated parameters for passing information and status between the driver and FileX."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter5.md#i-o-driver-introduction"
license: "MIT"
mode: "V"
---

FileX supports multiple media devices. The FX_MEDIA structure defines everything required to manage a media device. This structure contains all media information, including the media-specific I/O driver and associated parameters for passing information and status between the driver and FileX. In most systems, there is a unique I/O driver for each FileX media instance.
