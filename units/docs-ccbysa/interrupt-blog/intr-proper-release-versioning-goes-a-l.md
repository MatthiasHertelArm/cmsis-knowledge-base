---
id: "intr-proper-release-versioning-goes-a-l"
type: "concept"
domain: "debug"
title: "Proper Release Versioning Goes a Long Way"
summary: "Release versioning might seem like a boring topic. Honestly, it should be."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-01-19-release-versioning.md"
doc_source: "https://interrupt.memfault.com/blog/release-versioning"
license: "CC-BY-SA-4.0"
mode: "V"
---

Release versioning might seem like a boring topic. Honestly, it should be. There should only be a couple of right ways to do versioning, and each project should pick one of the agreed-upon methods (SemVer[^semver], CalVer[^calver], etc.) that makes the most sense to the project. We don't live in this ideal world unfortunately and many projects choose to deviate from versioning standards. I'm not here to say they are wrong, but I'd like to discuss what they might be missing out on.

Along with a typical release version, it is useful to include extra metadata, such as the Git revision, [GNU Build ID](https://interrupt.memfault.com/blog/gnu-build-id-for-firmware), build timestamp, and other related items. With all of this in place, both machines and developers can quickly figure out *exactly* which release is running on a given device, what the source is, where it came from, and how to rebuild it if necessary.



In this article, we are going to talk through all the various pieces of metadata to be included in your firmware binaries, debug symbols, and build artifacts so that developers and machines can quickly and easily know **exactly** which build is which and how to fetch associated files for the debug, test, and release pipeline.



This post builds upon many of our previous posts and brings all the relevant information together under one post.
