---
id: "intr-c-17-s-useful-features-for-embedde-conclusion"
type: "concept"
domain: "debug"
title: "C++17’s Useful Features for Embedded Systems: Conclusion"
summary: "As opposed to C++14, C++17 came with many new features. Some of those features are beneficial in the world of embedded systems and some of them are not."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-17-cpp-17-for-embedded.md"
doc_source: "https://interrupt.memfault.com/blog/cpp-17-for-embedded#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

As opposed to C++14, C++17 came with many new features. Some of those features are beneficial in the world of embedded systems and some of them are not. I inspected the ones that I liked the most by directly utilizing them in my current designs.

The computation power range of embedded devices varies considerably between different products. Some of the features that I chose might not be appropriate in your firmware due to several reasons such as CPU performance, lack of compiler support, verification necessity, etc. Migration to C++17 might cost you a severe amount of time and effort. It’s better to know whether you require the migration or not.










{:.no_toc}
