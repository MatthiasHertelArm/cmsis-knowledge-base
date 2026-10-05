---
id: "intr-balancing-test-coverage-vs-overhea-how-to-reduce-coverage-testing-overhead"
type: "concept"
domain: "debug"
title: "Balancing Test Coverage vs. Overhead: How to Reduce Coverage Testing Overhead"
summary: "Testing is costly in terms of the time it takes to develop, maintain, and ultimately run the tests. How long it takes to run an extensive test suite can fluctuate wildly depending on the software and the tests involved."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-03-23-testing-vs-overhead.md"
doc_source: "https://interrupt.memfault.com/blog/testing-vs-overhead#how-to-reduce-coverage-testing-overhead"
license: "CC-BY-SA-4.0"
mode: "V"
---

Testing is costly in terms of the time it takes to develop, maintain, and ultimately run the tests. How long it takes to run an extensive test suite can fluctuate wildly depending on the software and the tests involved. To add to this, regression testing advocates for testing each new change against the entire existing codebase to ensure that no new bugs are introduced. When developing using a methodology that advocates for the continuous integration of small, rapidly developed commits, an extensive suite can quickly develop into a testing bottleneck.

Several different methods can be used to mitigate this and reduce the overhead of extensive test coverage. The tests themselves could be analyzed and refactored to reduce the time it takes for them to run as much as possible. Some tests will unavoidably take longer to run than others though, so certain groups of tests can be placed into categories so that they are not run as frequently as other tests or at all under certain conditions.

Other options, such as continuous testing and parallel testing, are available. These methods either run your tests as you write them or run your test suite in parallel, so you do not have to wait for some of the longer tests to finish before moving on to other tests. Both methods deliver results as they happen, cutting down on the waiting time required when running tests, which can be on the order of magnitude of hours to days for sufficiently mature regression tests run in series.
