---
id: "intr-building-an-on-device-embedded-tes-requirements"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Requirements"
summary: "Based on my experience and opinions, I decided to specify the following requirements:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#requirements"
license: "CC-BY-SA-4.0"
mode: "V"
---

Based on my experience and opinions, I decided to specify the following requirements:

- **emlabcpp Integration**

   The test library is tightly integrated into my personal C++20 library, [emlapcpp](https://github.com/emlab-fi/emlabcpp).
   That is: it can't be used without the library.
   This eases the development of the testing framework as I reuse functionality from the library, specifically: the protocol library inside emlabcpp.

- **Simplicity**

   The library should be simple and should not try to provide the entire set of functionalities that Catch/Google Test offers.

- **Integration into existing testing tools**

   A wide set of tools exist that can work with the test results of Catch/Google Test. For example, GitLab has the integration of test results from these tools.
   The library should be compatible with these integrations.

- **Small footprint**

   Since we are running tests on the device, and the application code itself will take a big percentage of the available memory of the microchip, the library needs to have a small footprint.

- **No dynamic memory. No exceptions.**

   Both are C++ features that we may want to avoid in the firmware since embedded firmware often does not have dynamic memory.

- **No platform requirements**

   The library should not be tied to any specific platform.
