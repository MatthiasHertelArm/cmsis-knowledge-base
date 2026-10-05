---
id: "intr-pocket-article-debug-vs-release-bu"
type: "concept"
domain: "debug"
title: "Pocket article: Debug vs. Release Builds Considered Harmful"
summary: "Separate \"debug\" and \"release\" builds are very common in embedded development. Typically the notion is improved debug capabilities (less aggressive compiler optimizations, more debugging information like logs) vs. highly optimized and hardened production release builds."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-04-25-debug-vs-release-builds.md"
doc_source: "https://interrupt.memfault.com/blog/debug-vs-release-builds"
license: "CC-BY-SA-4.0"
mode: "V"
---

Separate "debug" and "release" builds are very common in embedded development.
Typically the notion is improved debug capabilities (less aggressive compiler
optimizations, more debugging information like logs) vs. highly optimized and
hardened production release builds. I'm here to describe disadvantages to this
practice, and why it might make sense to consolidate to a single build!





> 🌶️🔥 Warning! this article is taking a strong position on debug-vs-release
> builds. I'm hoping to highlight a few pitfalls you may run into, but it's not
> intended to be a complete discounting of the reasons we end up with bifurcated
> builds (despite the clickbait title)! Please enjoy and as always comments are
> greatly appreciated 🙏
