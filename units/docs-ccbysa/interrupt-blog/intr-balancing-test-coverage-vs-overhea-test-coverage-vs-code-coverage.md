---
id: "intr-balancing-test-coverage-vs-overhea-test-coverage-vs-code-coverage"
type: "concept"
domain: "debug"
title: "Balancing Test Coverage vs. Overhead: Test Coverage vs Code Coverage"
summary: "Test coverage refers to the wider scope of testing and how much of a product is tested. This includes not just the underlying code but how the user experiences it."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-03-23-testing-vs-overhead.md"
doc_source: "https://interrupt.memfault.com/blog/testing-vs-overhead#test-coverage-vs-code-coverage"
license: "CC-BY-SA-4.0"
mode: "V"
---

Test coverage refers to the wider scope of testing and how much of a product is tested. This includes not just the underlying code but how the user experiences it. UI/UX testing across different devices and platforms, user story testing, and E2E testing all fall under the umbrella of test coverage.

Thus, it is sometimes advocated that 100% *test coverage* in tests is not necessarily desirable or is seen as a misuse of available time and energy. Development teams need to balance testing with other demands, such as regularly updating the software to add new features to attract more customers, improve reviews and ratings, and prolong the life of the device.

On the contrary, it is generally desirable to reach 100% *code coverage*, but it can not be confused with 100% *test coverage*. Code coverage only points out the percentage of code units that were cycling over when running a single or a suite of tests. It can not be confused with testing every branch and set of arguments, which would be *test coverage*.
