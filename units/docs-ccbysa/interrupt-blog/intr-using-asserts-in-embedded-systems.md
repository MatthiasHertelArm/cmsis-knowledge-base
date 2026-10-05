---
id: "intr-using-asserts-in-embedded-systems"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems"
summary: "The use of asserts is one of the best ways to find bugs, unintended behavior, programmatic errors, and to catch when systems are no longer 100% functional and need to be reset to recover."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems"
license: "CC-BY-SA-4.0"
mode: "V"
---

The use of asserts is one of the best ways to find bugs, unintended behavior,
programmatic errors, and to catch when systems are no longer 100% functional and
need to be reset to recover. If instrumented correctly, an assert can give a
developer context about when and where in the code an issue took place. Despite
the numerous benefits, the practice of using asserts in firmware is not common
or agreed upon.



By using asserts proactively in embedded systems on debug **and production**
builds, developers can both prevent more bugs before shipping and quickly
surface and fix them after shipping. Proper assert handling is also the safest
way to handle issues and undefined behavior that occur in production. In this
post, we'll go over best practices with asserts, when to use asserts, and then
come up with a production ready custom assert implementation for an ARM Cortex-M
device, all while keeping the code size usage to a minimum.



> **Why you shouldn't compile asserts out in production builds**
> Many of the popular embedded platforms have options to
> [compile](https://github.com/aws/amazon-freertos/blob/master/vendors/nordic/nRF5_SDK_15.2.0/components/libraries/util/nrf_assert.h#L78-L115)
> [out](https://github.com/espressif/esp-idf/blob/master/components/esp_common/include/esp_err.h#L104-L124)
> [error](https://github.com/ARMmbed/mbed-os/blob/master/platform/mbed_error.h#L191-L202)
> [handling](https://github.com/zephyrproject-rtos/zephyr/blob/master/include/sys/__assert.h#L34-L89)
> and assertions. In our opinion, this is a mistake. In the event of
> inconsistent behavior or memory corruption, crashing the device is often the
> safest thing you could do. Embedded systems can often reboot quickly, getting
> the system back to a known good state. Over time, it will also be noticed and
> provide valuable feedback back to your engineering teams. The alternative is
> worse: the system could behave in unpredictable way and perform poorly, lose
> customer information, …etc.



### Article Disclaimers

- This post is about runtime asserting, not compile time asserting, such as
  [`static_assert`](https://en.wikichip.org/wiki/c/assert.h/static_assert).
- This post is targeting the ever-growing number of **non-safety-critical**
  embedded systems, such as consumer electronics, Class 1 medical devices, home
  automation devices, etc.
- The above types of embedded systems are primarily constrained by memory and
  code space limitations, so the information below takes this into account.
- The examples below are implemented for the ARM Cortex-M series of MCUs. Many
  of the concepts can be generalized to other architectures.
