---
id: "intr-building-an-on-device-embedded-tes-controller-is-independent"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Controller is independent"
summary: "Based on the specific project and testing needs, one can use one binary with a controller for multiple reactors. That is something I intend with the actual main project that uses it."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#controller-is-independent"
license: "CC-BY-SA-4.0"
mode: "V"
---

Based on the specific project and testing needs, one can use one binary with a `controller` for multiple `reactors.` That is something I intend with the actual main project that uses it.

As the controller loads most information from the reactor and if the Google Test integration is used, there is not much logic that can be varied.

The sole exception is how data is provided for the tests.
But then it can be implemented in some general way - for example, the `controller` binary would load the data from a JSON file in some generic way.
