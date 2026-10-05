---
id: "txmw-chapter-2-installation-and-use-of-using-filex"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and use of FileX: Using FileX"
summary: "Using FileX is easy. Basically, the application code must include fx_api.h during compilation and link with the FileX run-time library fx.a (or fx.lib). Of course, the ThreadX files, namely tx_api.h and tx.a (or tx.lib), are also required."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter2.md#using-filex"
license: "MIT"
mode: "V"
---

Using FileX is easy. Basically, the application code must include ***fx_api.h*** during compilation and link with the FileX run-time library ***fx.a*** (or ***fx.lib***). Of course, the ThreadX files, namely ***tx_api.h*** and ***tx.a*** (or ***tx.lib***)*,* are also required.

> **Important:** When using FileX in Standalone mode (**FX_STANDALONE_ENABLE** must be defined), ThreadX files/libraries are not required.

Assuming you are already using ThreadX, there are four steps required to build a FileX application:

1. Include the ***fx_api.h*** file in all application files that use FileX services or data structures.
1. Initialize the FileX system by calling ***fx_system_initialize*** from the ***tx_application_define*** function or an application thread.

   > **Important:** When using FileX in Standalone mode, ***fx_system_initialize*** should be directly called from application code.

1. Add one or more calls to ***fx_media_open*** to set up the FileX media. This call must be made from the context of an application thread.

   > **Important:** *Remember that the **fx_media_open** call requires enough RAM to store data for one sector.*

1. Compile application source and link with the FileX and ThreadX run-time libraries, ***fx.a*** (or ***fx.lib***) and ***tx.a*** (or ***tx.lib***). The resulting image can be downloaded to the target and executed!
