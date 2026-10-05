---
id: "intr-balancing-test-coverage-vs-overhea-how-much-testing-is-too-much"
type: "concept"
domain: "debug"
title: "Balancing Test Coverage vs. Overhead: How Much Testing Is Too Much?"
summary: "There is an argument that chasing 100% code coverage is a fool’s errand. This is because development teams have limited resources and must distribute them in the most efficient manner possible to develop the product and remain profitable."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-03-23-testing-vs-overhead.md"
doc_source: "https://interrupt.memfault.com/blog/testing-vs-overhead#how-much-testing-is-too-much"
license: "CC-BY-SA-4.0"
mode: "V"
---

There is an argument that chasing 100% code coverage is a fool’s errand. This is because development teams have limited resources and must distribute them in the most efficient manner possible to develop the product and remain profitable. How severe a bug adversely affects a product is also heavily dependent on the type of bug, the area of the application the bug might appear in, and the target market of the product in question. A bug with the UI in a rarely used section of a UI could be overlooked by many users, but a bug that results in a connected battery to ignite or the firmware to reboot at an inopportune time could be catastrophic. Thus, it is important to triage errors and prioritize test coverage effectively, given the time and resources available.
