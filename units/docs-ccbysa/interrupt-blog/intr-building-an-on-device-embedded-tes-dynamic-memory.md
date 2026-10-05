---
id: "intr-building-an-on-device-embedded-tes-dynamic-memory"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Dynamic Memory"
summary: "Both the reactor and the controller contain data structures with dynamic size. To avoid dynamic memory, I wanted to use std::pmr: the internal containers would use an allocator and expect memory resource as an input argument."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#dynamic-memory"
license: "CC-BY-SA-4.0"
mode: "V"
---

Both the `reactor` and the `controller` contain data structures with dynamic size.
To avoid dynamic memory, I wanted to use `std::pmr`: the internal containers would use an allocator and expect memory resource as an input argument.
This implements the behavior: "The central objects expect a memory resource they should use for data allocation."

I think that this fits the use case quite nicely, as both types require dynamic data structures, but in the same way, I want them to be usable without dynamic memory itself. The compromise is an interface that can be provided with static buffers.

However, `std::pmr` does not feel usable, as the default construction of the allocator uses a default memory instance that exists as a global object that can be changed only at runtime.
The default instance uses new/delete.
That means that it is easy for code that uses `std::pmr` to include in the firmware the entire stack for dynamic allocation - something that I want to avoid.

I decided to re-implement `std::pmr` in my custom library with a few changes in the API that are more fitting to the embedded library.
The key change is that memory resource with new/delete operators simply does not exist.
The user has to instantiate a memory resource also provided by `emlabcpp` and give it to the object.

As a simple alternative, there exists `emlabcpp::testing_basic_reactor,` which inherits from the `reactor` and provides it with a basic memory resource that can be used by it. A sane default.
