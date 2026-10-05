---
id: "intr-practical-zephyr-zephyr-basics-par"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1)"
summary: "This is the start of a new article series about Zephyr's basics: It will walk you through Zephyr's build and configuration systems West, Kconfig and devicetree."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics"
license: "CC-BY-SA-4.0"
mode: "V"
---

This is the start of a new article series about _Zephyr's basics_: It will walk you through Zephyr's [build and configuration systems](https://docs.zephyrproject.org/latest/build/index.html) _West_, _Kconfig_ and _devicetree_.

**Yet another Zephyr series?**

[Zephyr's documentation](https://docs.zephyrproject.org/latest/develop/getting_started/index.html) aside, several very good article series exist already, e.g., the _"Getting Started with Zephyr"_ series by [Mohammed Billoo](https://www.embeddedrelated.com/blogs-1/nf/Mohammed_Billoo.php), or the Zephyr notes by [Abhijit Boseji](https://boseji.com/docs/zephyr/). Nordic Semiconductor also launched its [DevAcademy](https://academy.nordicsemi.com/), which contains a great course on the [nRF Connect SDK Fundamentals](https://academy.nordicsemi.com/courses/nrf-connect-sdk-fundamentals/): Since the _nRF Connect SDK_ is based on Zephyr, this course also teaches about Zephyr.

So why another article series, and what's different in this one?

When I first started looking into Zephyr, the learning curve felt overwhelming. Even as an embedded developer with a decent amount of experience, understanding key concepts and tools like _Kconfig_ or _devicetree_ for creating even a simple application had me chasing down the rabbit hole, following link after link after link, night after night - and it was exhausting. The existing article series would only brush over core concepts like _Kconfig_ and _devicetree_ and leave me with more questions than answers; I still needed to understand those tools since I had no previous experience with them.

What I'm trying to achieve with this article series is the following:



If you're working a full-time job and would still like to get started with Zephyr but don't have the energy to set up your environment to dive deeper into the docs, this article series will guide you through the __Zephyr basics__. Of course, you'll learn most if you follow along with programming, but all code, including snippets of generated code and build logs, are included in the articles of this series. Thus, even just reading this series should give you a good idea about how Zephyr works.



After this series, you should understand Zephyr's build and configuration tools. The learning curve flattens, and you can continue learning without getting lost in Zephyr's documentation.

👉 Find the other parts of the *Practical Zephyr* series [here](https://interrupt.memfault.com/tags#practical-zephyr-series).

> **Note:** This series is **not** for you if you're not interested in details and how things work but instead want to _use_ Zephyr. We'll go through _generated code and configuration files and learn _devicetree_ from first principles! Also, if you're experienced with Linux and already know how _Kconfig_ and _devicetree_ work, the articles of this series are just not for you.

> 🎬
> [Listen to Martin on Interrupt Live](https://www.youtube.com/watch?v=ls_Y45WsTiA?feature=share)
> talk about the content and motivations behind writing this article.
