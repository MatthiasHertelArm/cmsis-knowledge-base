---
id: "intr-a-shallow-dive-into-gnu-make-what-is-gnu-make"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: What is GNU Make?"
summary: "GNU Make is a program that automates the running of shell commands and helps with repetitive tasks. It is typically used to transform files into some other form, e.g. compiling source code files into programs or libraries."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#what-is-gnu-make"
license: "CC-BY-SA-4.0"
mode: "V"
---

[GNU Make](https://www.gnu.org/software/make/) is a program that automates the
running of shell commands and helps with repetitive tasks. It is typically used to transform files into some other form, e.g. compiling
source code files into programs or libraries.

It does this by tracking **prerequisites** and executing a hierarchy of commands to
produce **targets**.

Although the GNU Make manual is lengthy, I suggest giving it a read as it is the best reference I've found:
[https://www.gnu.org/software/make/manual/html_node/index.html](https://www.gnu.org/software/make/manual/html_node/index.html)

Let's dive in!
