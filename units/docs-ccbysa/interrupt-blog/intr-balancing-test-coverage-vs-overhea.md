---
id: "intr-balancing-test-coverage-vs-overhea"
type: "concept"
domain: "debug"
title: "Balancing Test Coverage vs. Overhead"
summary: "In a perfect world, all software and firmware are given precisely the time and budget it needs to be successful, code is uniformly well-written to industry best practices, and the code is complemented with a complete test suite …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-03-23-testing-vs-overhead.md"
doc_source: "https://interrupt.memfault.com/blog/testing-vs-overhead"
license: "CC-BY-SA-4.0"
mode: "V"
---

> This article is written by an external contributor, [Erik Fogg](https://interrupt.memfault.com/blog/authors/erikfogg) of [ProdPerfect](https://prodperfect.com/), along with Tyler Hoffman representing the firmware side of the story. Enjoy!



In a perfect world, all software and firmware are given precisely the time and budget it needs to be successful, code is uniformly well-written to industry best practices, and the code is complemented with a complete test suite instrumenting all aspects of the software.

In practice, this rarely, if ever, happens! Development teams and organizations continually have to re-prioritize tasks to meet deadlines and avoid going over budget. In this article, we'll cover how you can think about rapidly modifying and updating firmware, testing these changes, all the while allowing you to get the product out the door.



If you are working at a hardware company right now, which I assume many of you are, you are **undeniably struggling** to procure various hardware components. We've heard that prices of STM32's have sky-rocketed from $1-2 to $10-20! While rapidly modifying and updating the firmware to accommodate different hardware components, a balance between testing and getting s*** out the door needs to be found. We'll dive into some ways that might help you.
