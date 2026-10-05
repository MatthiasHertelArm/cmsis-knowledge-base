---
id: "intr-seamless-firmware-development-with-conclusion"
type: "concept"
domain: "debug"
title: "Seamless firmware development with PlatformIO: Conclusion"
summary: "There's a lot to like about PlatformIO. It's an open source cross platform tool that makes it easy to setup, build, and test an embedded project no matter what IDE you use or what OS you run on your laptop."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-08-seamless-firmware-with-platformio.md"
doc_source: "https://interrupt.memfault.com/blog/seamless-firmware-with-platformio#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

There's a lot to like about PlatformIO. It's an open source cross platform tool
that makes it easy to setup, build, and test an embedded project no matter what
IDE you use or what OS you run on your laptop.

Best of all, having a package manager for embedded project is fantastic and
will I hope further encourage people to collaborate and leverage excellent open
source libraries like mbedTLS.

At the same time, the low number of supported vendor SDKs ("frameworks") makes
PlatformIO impractical for many professional projects. Unless you are on an
STM32 or an Espressif chip, you likely will need to do a lot of extra work to
add support for your platform of choice to PlatformIO.

Last but not least while the nomenclature is a bit wonky, the PlatformIO
documentation is excellent with tons of examples. The engineers behind the
projects are also very active on twitter and on their discussion board. Props to
them for excellent support!

I look forward to watching PlatformIO grow over the next few years, and cannot
wait to use it for a future project. Look our for `platformio.ini` files in
future Interrupt examples!







{:.no_toc}
