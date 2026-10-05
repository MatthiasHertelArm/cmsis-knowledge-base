---
id: "intr-mcuboot-walkthrough-and-porting-gu-porting-a-library-phases"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide: Porting MCUboot / Porting a Library Phases"
summary: "I typically like to breakdown a port of a library into several incremental steps:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview#porting-a-library-phases"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Porting MCUboot_

I typically like to breakdown a port of a library into several incremental steps:

1. Add C sources from the library to the project and get everything to compile.
2. Add a call to the library from the application to force the dependencies to be pulled in. Upon completion of this
   step, you will see many "undefined references" at link time.
3. Fix the link-time issues by adding stub implementations for all the dependencies to a port file
   (i.e `mcuboot_port.c`). At this point, we have an application that links but doesn't yet do
   anything. We can ballpark the code size impact of the library by taking a look at the size of our
   image at this point.
4. Walk through and fill in the stub implementations we used to get a link with a real implementation.

With that in mind, let's begin!
