---
id: "txmw-chapter-5-i-o-drivers-for-filex-i-o-driver-entry"
type: "concept"
domain: "rtos"
title: "Chapter 5 - I/O Drivers for FileX: I/O Driver Entry"
summary: "Each FileX I/O driver has a single entry function that is defined by the fx_media_open service call. The driver entry function has the following format:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter5.md#i-o-driver-entry"
license: "MIT"
mode: "V"
---

Each FileX I/O driver has a single entry function that is defined by the ***fx_media_open*** service call. The driver entry function has the following format:

```c
void my_driver_entry(FX_MEDIA *media_ptr);
```

FileX calls the I/O driver entry function to request all physical media access, including initialization and boot sector reading. Requests made to the driver are done sequentially; i.e., FileX waits for the current request to complete before another request is sent.
