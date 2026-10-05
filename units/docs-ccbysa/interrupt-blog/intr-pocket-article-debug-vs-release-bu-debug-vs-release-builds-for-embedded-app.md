---
id: "intr-pocket-article-debug-vs-release-bu-debug-vs-release-builds-for-embedded-app"
type: "concept"
domain: "debug"
title: "Pocket article: Debug vs. Release Builds Considered Harmful: Debug vs. Release Builds for Embedded Applications"
summary: "Many embedded development IDEs provide separate \"Debug\" and \"Release\" build configurations out of the box. Generally the differences between those can be summarized as:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-04-25-debug-vs-release-builds.md"
doc_source: "https://interrupt.memfault.com/blog/debug-vs-release-builds#debug-vs-release-builds-for-embedded-applications"
license: "CC-BY-SA-4.0"
mode: "V"
---

Many embedded development IDEs provide separate "Debug" and "Release" build
configurations out of the box. Generally the differences between those can be
summarized as:

| Build config | Debug info enabled?          | Compiler optimization?      | `NDEBUG` preprocessor definition?          |
| ------------ | ---------------------------- | --------------------------- | ------------------------------------------ |
| **Debug**    | ✅ enabled (`-g` or similar) | low (`-O0` or `-Og`)        | `DEBUG` is set, or `#define NDEBUG 0`, etc |
| **Release**  | ❌ disabled                  | high (`-O3` or `-Os`/`-Oz`) | `NDEBUG` is set                            |

Let's go one-by-one through these items!
