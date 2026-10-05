---
id: "intr-building-better-firmware-with-cont-what-is-continuous-integration"
type: "concept"
domain: "debug"
title: "Building Better Firmware with Continuous Integration: What is Continuous Integration?"
summary: "Strictly speaking, Continuous Integration is the practice of regularly integrating code into a mainline repository. In other words: merging your work into master as often as possible."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-17-continuous-integration-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/continuous-integration-for-firmware#what-is-continuous-integration"
license: "CC-BY-SA-4.0"
mode: "V"
---

Strictly speaking, Continuous Integration is the practice of regularly
integrating code into a mainline repository. In other words: merging your work
into master as often as possible.

To achieve Continuous Integration, teams rely on a well established set of
techniques:

1. Revision Control: Continuous Integration depends on a solid Version Control
   System. Nowadays, it often is a git repository, but mercurial (hg), perforce,
   or SVN are fine options.

2. Automated Builds: If anything, a project must compile. This is often easier
   said than done! As the set of build configurations grows, running through
   each of them can be both time consuming, and error prone. Builds must
   therefore be automated.

3. Automated Tests: Engineers do not always anticipate the impact their change
   can have on other part of the codebase. As the pace of changes increase,
   testing everything manually becomes intractable and automated tests must be put
   in place.

These techniques have become synonymous with Continuous Integration, as they are
universally implemented by teams who want to integrate code regularly. In this
blog post, we use Continuous Integration, or "CI" to mean the use of these
techniques to integrate code on an ongoing basis.
