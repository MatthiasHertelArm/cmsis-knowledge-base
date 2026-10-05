---
id: "intr-practical-zephyr-zephyr-basics-par-conclusion"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1): Conclusion"
summary: "In this article, we installed Zephyr and its tools using Nordic's nrfutil, and with it have a base environment that we'll use in this series."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this article, we installed Zephyr and its tools using Nordic's [`nrfutil`](https://docs.nordicsemi.com/bundle/nrfutil/page/README.html), and with it have a base environment that we'll use in this series. Since your preference for development environments and installation for sure greatly varies, finding the matching solution will always be your own task. With the contents of the `setup.sh` script that we created in this article, you should have a good idea about what's involved when creating your own setup.

> **Note:** The example application skeleton created throughout this article is available in the [`00_basics` folder of the accompanying GitHub repository](https://github.com/lmapii/practical-zephyr/tree/main/00_basics).

We then had a quick look at Zephyr's application types and created a skeleton _freestanding_ application, which we've compiled using CMake directly, and via Zephyr's meta-tool _West_. We've seen how we can parameterize our build to pick a certain _board_ and concluded, that it might be beneficial to use _West_ over plain CMake - but you can always pick your preference.

We then brushed over the extension commands `flash` and `debug` that allow us to program the application to our board and debug it using `gdb`. Finally, we've had a quick look at a possible `VS Code` debugging integration.

Next up in line for this article series is _Kconfig_, which we briefly encountered when we created the minimum set of files for a freestanding application - which included a `prj.conf` file.









{:.no_toc}
