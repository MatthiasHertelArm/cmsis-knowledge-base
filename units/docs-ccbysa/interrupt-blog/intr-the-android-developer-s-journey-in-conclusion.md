---
id: "intr-the-android-developer-s-journey-in-conclusion"
type: "concept"
domain: "debug"
title: "The Android Developer's Journey into Hardware Observability: Conclusion"
summary: "There's a ton of content on what observability means for Android apps, but content and tooling for AOSP device observability is sparse in comparison, leading many AOSP developers to build their own internal tools."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-28-aosp-observability.md"
doc_source: "https://interrupt.memfault.com/blog/aosp-observability#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

There's a ton of content on what observability means for Android apps, but
content and tooling for AOSP device observability is sparse in comparison,
leading many AOSP developers to build their own internal tools. And most AOSP
developers end on a similar journey: they discover the limits of their apps
observability tools, then they figure out they want to pull Android bugreports
and [logcat device logs](https://interrupt.memfault.com/blog/device-logging),
then they find a way to push the logs from the device instead of pull, and then
they discover even more Android data they want to include, but would rather
parse the data automatically, and do it for every device, not just the one
they're working on, and then they fight to build a team that could do all of
this sustainably.

One of the reasons I joined Memfault was to build the tooling I wish we had
previously because I ran through all the same roadblocks I described above, and
helping other developers to learn the same lessons I had, in less time. And
there are still many more lessons in AOSP observability to learn, so if you have
experience with observability at scale, I'd love to hear from you.









{:.no_toc}
