---
id: "intr-embedded-c-c-unit-testing-with-moc-stubs-mocks-and-fakes-review"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: Stubs, Mocks, and Fakes Review"
summary: "As a quick review, let's summarize the differences between fakes, stubs, and mocks."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#stubs-mocks-and-fakes-review"
license: "CC-BY-SA-4.0"
mode: "V"
---

As a quick review, let's summarize the differences between **fakes**, **stubs**,
and **mocks**.

- **Fakes** are a working implementation, but usually substitute their
  dependencies with something simpler and easier for a test environment.
  Example: an in-memory key/value store vs a NOR-flash backed Key/Value store.
- **Stubs** are a trivial implementation that returns canned values, generally
  always returning valid or invalid values.
- **Mocks** are an implementation that is controlled by the unit test. They can
  be pre-programmed with return values, check values of arguments, and help
  verify that functions are called.

Each one serves a purpose in unit testing. Although each type might not be
utilized in every unit test you write, I can guarantee you that there's a place
for all of them within the suite of tests for your firmware.
