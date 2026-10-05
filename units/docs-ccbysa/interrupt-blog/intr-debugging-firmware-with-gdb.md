---
id: "intr-debugging-firmware-with-gdb"
type: "concept"
domain: "debug"
title: "Debugging Firmware with GDB"
summary: "If I had to choose one significant aspect that I was not aware of before starting my career as a firmware developer, it would be how much time is spent not actually developing, and instead debugging firmware!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-21-gdb-for-firmware-1.md"
doc_source: "https://interrupt.memfault.com/blog/gdb-for-firmware-1"
license: "CC-BY-SA-4.0"
mode: "V"
---

If I had to choose one significant aspect that I was not aware of before starting my career as a firmware developer, it would be how much time is spent **not actually developing**, and instead **debugging** firmware!


Not convinced?

I'll leave you with a few figures taken from the 2017 Embedded/EETimes **Embedded Markets Study** survey which showcase the significance of debugging in the professional life of a firmware developer.













Let's face it..

Debugging is **generally difficult**, and it gets even more difficult for firmware applications and has more limitations compared with a mobile or web application.

This is due to a few factors, some of which are:

- Limited availability of resources for debugging. For example, some bugs are very difficult to diagnose using software breakpoints. In those scenarios, you would rely on hardware breakpoints and usually there is a limited number of hardware breakpoints for a specific architecture. This makes debugging complex bugs a challenging task.
- Time-dependency in real-time/time-critical applications. For example, setting breakpoints can interfere with the timing of operations. If a bug is timing-related, then the debugging process may even cause the bug to disappear!
- Challenges in setting up the debugging environment (cross-platform development environment). There is a variety of visual IDEs and integrated debuggers available, but for some scenarios you may need an automated debugging setup and this can prove to be a challenging task.
- High cost of some debugging hardware tools.
