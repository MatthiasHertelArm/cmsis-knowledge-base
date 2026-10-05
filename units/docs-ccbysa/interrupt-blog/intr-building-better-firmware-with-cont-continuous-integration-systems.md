---
id: "intr-building-better-firmware-with-cont-continuous-integration-systems"
type: "concept"
domain: "debug"
title: "Building Better Firmware with Continuous Integration: Continuous Integration Systems"
summary: "Many tools exist today that can be used to implement Continuous Integration. You may have heard of Jenkins, a popular open source tool, but many others exist: TravisCI, CircleCI, TeamCity, Bamboo, Build Bot, …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-17-continuous-integration-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/continuous-integration-for-firmware#continuous-integration-systems"
license: "CC-BY-SA-4.0"
mode: "V"
---

Many tools exist today that can be used to implement Continuous Integration. You
may have heard of Jenkins, a popular open source tool, but many others exist:
TravisCI, CircleCI, TeamCity, Bamboo, Build Bot, …

Fundamentally, continuous integration systems all do roughly the same thing:
1. Monitor your repository for changesets (either pull requests, or merges)
2. For each changeset, execute a set of build & test steps
3. Report the success or failure of build & test steps
4. Save the resulting artifacts (e.g. firmware binary) for future use

A good continuous integration system for firmware development should have the
following features:

* **Windows support**: many firmware engineers work on Windows, so it is important
   that this platform be supported by your CI system.

* **Configuration-as-code**: the build and test steps should be declared in files
   checked-in alongside your code. Imagine the case where multiple branches
   require slightly different build instructions: a build system that saves
   configuration in a database separate from the code would not be able to build
   every branch.

* **A hosted solution**: so you don’t have to set up and maintain your own servers,
   with the ability to go on-premise in the future.

* **VCS Integration**

At Memfault, we use CircleCI[^2] for continuous integration. It ticks all 4 of the
above requirements, has a generous free plan, and in our limited testing runs
much faster than the competition.
