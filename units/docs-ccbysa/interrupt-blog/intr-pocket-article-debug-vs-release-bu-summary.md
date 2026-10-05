---
id: "intr-pocket-article-debug-vs-release-bu-summary"
type: "concept"
domain: "debug"
title: "Pocket article: Debug vs. Release Builds Considered Harmful: Summary"
summary: "Avoid separate \"Debug\" and \"Release\" builds at all costs!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-04-25-debug-vs-release-builds.md"
doc_source: "https://interrupt.memfault.com/blog/debug-vs-release-builds#summary"
license: "CC-BY-SA-4.0"
mode: "V"
---

🙅🙅🙅🙅

Avoid separate "Debug" and "Release" builds at all costs!

More seriously, there are many downsides(complexity, wasted time, etc) if a
different build is used during development vs. production. There are
few cases where this is actually required!

My advice is to consider very carefully if you need a separate Release build,
and make sure you're ready to commit to supporting it.

Often it's sufficient to enable or disable a few small features via a
compilation flag for production builds. This can be done, for example, in your
CI server, when preparing a tag for release. That build can also be where
production keys/signing is performed, so it's all in one place and can be
audited later. Avoid "Noah's laptop" builds making it to manufacturing 😅!









{:.no_toc}
