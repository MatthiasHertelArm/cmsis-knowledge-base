---
id: "intr-balancing-test-coverage-vs-overhea-what-is-test-coverage"
type: "concept"
domain: "debug"
title: "Balancing Test Coverage vs. Overhead: What is Test Coverage?"
summary: "Test coverage refers to how extensively software is covered by its test suite. Exactly how extensive a test suite should be is a matter of debate within software testing."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-03-23-testing-vs-overhead.md"
doc_source: "https://interrupt.memfault.com/blog/testing-vs-overhead#what-is-test-coverage"
license: "CC-BY-SA-4.0"
mode: "V"
---

Test coverage refers to how extensively software is covered by its test suite. Exactly how extensive a test suite should be is a matter of debate within software testing. For example, a comprehensive test suite would not only test each component in a codebase but would also cover branch conditions and ideally every possible configuration of conditionals. As you can imagine, the number of test cases would be enormous!

Tests can also take forms outside of directly testing the codebase, such as end-to-end (E2E) testing. This involves testing the entire process of using software from an end-user's perspective, from the very beginning to the very end of the end-user experience. If your end-product that your customers use is a set of API endpoints, then your E2E tests should use the API endpoints directly with the standard authentication methods that your app expects.

For hardware and firmware, end-to-end tests would likely be initiated through an [on-device shell or CLI](https://interrupt.memfault.com/blog/building-a-cli-for-firmware-projects) through the UART or over USB. The E2E test result could be determined by validating the responses from the CLI command or by checking the environment after the test case, such as ensuring a file exists or flash region is written with a particular value.
