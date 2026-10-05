---
id: "txmw-chapter-2-installation-and-use-of-configuration-options-3"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options"
summary: "There are several configuration options when building the NetX Duo library and the application using NetX Duo. The configuration options can be defined in the application source, on the command line, or within the nx_user.h include file, unless otherwise specified."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#configuration-options"
license: "MIT"
mode: "V"
---

There are several configuration options when building the NetX Duo library and the application using NetX Duo. The configuration options can be defined in the application source, on the command line, or within the ***nx_user.h*** include file, unless otherwise specified.

> **Note:** *Options defined in **nx_user.h** are applied only if the application and NetX Duo library are built with* **NX_INCLUDE_USER_DEFINE_FILE** *defined.*

The following sections list the configuration options available in NetX Duo. General options applicable to both IPv4 and IPv6 are listed first, followed by IPv6-specific options.
