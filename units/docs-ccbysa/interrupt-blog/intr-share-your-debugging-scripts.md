---
id: "intr-share-your-debugging-scripts"
type: "concept"
domain: "debug"
title: "Share Your Debugging Scripts"
summary: "One of my favorite ways to debug is to let GDB and a set of previously written Python scripts do all the work for me."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-04-21-sharing-gdb-scripts.md"
doc_source: "https://interrupt.memfault.com/blog/sharing-gdb-scripts"
license: "CC-BY-SA-4.0"
mode: "V"
---

One of my favorite ways to debug is to let GDB and a set of previously written Python scripts do all the work for me. These scripts could parse the heap and data structures, investigate fault registers, and paint an accurate picture of a system at the time of a crash.

Did I know how to assemble and make sense of all this knowledge myself using the debugger and a raw GDB prompt? Maybe 5-10%. What made this possible was a common set of GDB scripts that the team of firmware engineers improved constantly, and the project automatically loaded them into GDB when we launched the debugger. It was wonderful.



In this short-form post, I want to share how you can go about keeping a central `gdbinit` file that you can commit into your project's repo and automatically source it in the popular editor and IDE environments that firmware engineers find themselves in today.
