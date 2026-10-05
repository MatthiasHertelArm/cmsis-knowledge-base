---
id: "intr-improving-compilation-time-of-c-c-closing"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects: Closing"
summary: "I hope this post has helped uncover some ways that you could try to improve the build time of your firmware projects."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects#closing"
license: "CC-BY-SA-4.0"
mode: "V"
---

I hope this post has helped uncover some ways that you could try to improve the
build time of your firmware projects.

I would argue that it may be more difficult to keep the build time fast than it
is to initially make it fast. For this, I recommend tracking the build times
either in your CI system or in an external database that can be referenced
retroactively. If you notice that your build time somehow slipped from 1 minute
to 2 minutes, you can easily look through all master commits and see where the
build time regression took place.

Do you have any further ideas or ways that you have employed to speed up your
firmware builds? I'd love to hear them!

_All the code used in this blog post is available on
[Github](https://github.com/memfault/interrupt/tree/master/example/faster-compilation/)._


{:.no_toc}
