---
id: "intr-programming-the-atsamd21-with-ibda-installing-openocd"
type: "concept"
domain: "debug"
title: "Programming the ATSAMD21 with IBDAP: Installing OpenOCD"
summary: "Installing OpenOCD with all the right dependencies to do CMSIS-DAP was once trickier than it ought to be. Today, the Homebrew formula takes care of it all for you:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-04-25-getting-started-with-ibdap-and-atsamd21g18.md"
doc_source: "https://interrupt.memfault.com/blog/getting-started-with-ibdap-and-atsamd21g18#installing-openocd"
license: "CC-BY-SA-4.0"
mode: "V"
---

Installing OpenOCD with all the right dependencies to do CMSIS-DAP was once
trickier than it ought to be. Today, the Homebrew formula takes care of it all
for you:

```terminal
$ brew install openocd
...
$ openocd --version
Open On-Chip Debugger 0.10.0
Licensed under GNU GPL v2
For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html
```
Huzzah!
