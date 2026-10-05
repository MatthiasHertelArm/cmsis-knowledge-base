---
id: "intr-why-std-this-thread-sleep-for-is-b"
type: "concept"
domain: "debug"
title: "Why std::this_thread::sleep_for() is broken on ESP32"
summary: "A curious bug appearing after upgrading to IDF v5 led me into a deep dive of how std::this_thread::sleep_for() is implemented on the ESP32. I discuss how the IDF implements pthreads and newlib to provide C++ threading functionality."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-20-why-sleep-for-is-broken-on-esp32.md"
doc_source: "https://interrupt.memfault.com/blog/why-sleep-for-is-broken-on-esp32"
license: "CC-BY-SA-4.0"
mode: "V"
---

A curious bug appearing after upgrading to IDF v5 led me into a deep dive of how
`std::this_thread::sleep_for()` is implemented on the ESP32. I discuss how the
IDF implements `pthreads` and `newlib` to provide C++ threading functionality.
The results are surprising: a simple 10 millisecond sleep was killing
performance, but only in the new version of IDF due to an interaction between
`libstdc++` and `usleep()`.



> 🎬
> [Listen to Steve on Interrupt Live](https://youtube.com/live/dwL-PI7TuDY?feature=share)
> talk about the content and motivations behind writing this article.
