---
id: "intr-a-shallow-dive-into-gnu-make"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make"
summary: "GNU Make is a popular and commonly used program for building C language software. It is used when building the Linux kernel and other frequently used GNU/Linux programs and software libraries."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines"
license: "CC-BY-SA-4.0"
mode: "V"
---

GNU Make is a popular and commonly used program for building C language software. It is used when [building the Linux
kernel](https://wiki.archlinux.org/index.php/Kernel/Traditional_compilation#Compilation)
and other frequently used GNU/Linux programs and software libraries.

Most embedded software developers will work with GNU Make at some point in their career, either using it to compile small libraries or building an entire project. Though there are [many, many
alternatives to Make](https://en.wikipedia.org/wiki/List_of_build_automation_software),
it's still commonly chosen as the build system for new software given its feature set and wide support.



This article explains general concepts and features of GNU Make and includes
recommendations for getting the most out of a Make build! Consider it a brief
guided tour through some of my favorite/most used Make concepts and features 🤗.



If you feel like you already know Make pretty well, feel free to skip the tutorial portion and [jump to my personal recommendations](#recommendations).
