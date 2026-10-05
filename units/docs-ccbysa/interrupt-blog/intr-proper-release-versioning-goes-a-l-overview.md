---
id: "intr-proper-release-versioning-goes-a-l-overview"
type: "concept"
domain: "debug"
title: "Proper Release Versioning Goes a Long Way: Overview"
summary: "Versions don't exist just to differentiate one release from another. They serve other purposes! Such purposes include, but are not limited to:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-01-19-release-versioning.md"
doc_source: "https://interrupt.memfault.com/blog/release-versioning#overview"
license: "CC-BY-SA-4.0"
mode: "V"
---

Versions don't exist just to differentiate one release from another. They serve other purposes! Such purposes include, but are not limited to:

- Providing an ordering to versions (e.g. 1.1 > 1.0)
- Encode compatibility information, breaking changes, and upgrade/downgrade restrictions
- Reference a specific revision of the software
- Reference a specific build of the software
- Tell users when *major* changes took place (e.g. Windows 8 → Windows 10)

If a project chooses to use just a Git SHA, or a build timestamp, or a random ASCII name, then many or all of the above benefits that versions typically provide are lost. We can do better!

Throughout this article, we'll talk about the various pieces that I believe provide a holistic picture of the software that is packaged into a release and running on a device. First, let's talk about Semantic Versioning.
