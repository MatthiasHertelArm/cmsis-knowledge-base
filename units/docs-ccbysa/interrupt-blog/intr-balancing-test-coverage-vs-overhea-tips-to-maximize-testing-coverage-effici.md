---
id: "intr-balancing-test-coverage-vs-overhea-tips-to-maximize-testing-coverage-effici"
type: "concept"
domain: "debug"
title: "Balancing Test Coverage vs. Overhead: Tips To Maximize Testing Coverage/Efficient Testing"
summary: "All of this testing takes time. Maximizing available testing resources effectively is generally done by categorizing potential bugs. This can be done in a number of ways."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-03-23-testing-vs-overhead.md"
doc_source: "https://interrupt.memfault.com/blog/testing-vs-overhead#tips-to-maximize-testing-coverage-efficient-testing"
license: "CC-BY-SA-4.0"
mode: "V"
---

All of this testing takes time. Maximizing available testing resources effectively is generally done by categorizing potential bugs. This can be done in a number of ways.

### Categorizing Test Cases

One such way would be by *feature usage*: features that are used more commonly and extensively should receive a greater proportion of testing time and resources than other features.

Another categorization is by *risk*, or how severely a bug impacts a product or end-user. In the example above, a bug in the battery driver that could potentially lead to a failure would be a high-risk bug and should receive much more time and resources than a simple, low-risk UI bug of little consequence.

*Feature criticality* is another category for test development. This involves testing features in order of how critical they are for the product to work successfully. If a feature breaking has little impact on the user experience, then it should receive fewer resources than a feature that is integral to the user experience.

Two parts of the codebase that should be rigorously tested no matter what are [firmware update](https://interrupt.memfault.com/blog/device-firmware-update-cookbook) and factory reset. Firmware update will allow your devices to update from one firmware to another, and factory reset will bring the device back to the state it was in when it was first provisioned. Factory reset will typically involve zeroing external flash memory, deleting all user preferences, removing bonding information, wiping the filesystem, and ideally loading the original firmware that the device started with. The only things that should remain between factory resets are the device provisioning information and maybe some logs to determine what caused the factory reset in the first place.

### Testing Without Hardware

Testing with hardware-in-the-loop is a necessary evil of device manufacturers, but it can be done only for a few basic test cases, such as firmware update, factory reset, power monitoring, and basic hardware functionality. Beyond that, most of the firmware can be tested without hardware with either unit tests or emulators! Emulators, such as Renode and QEMU, provide a perfect platform to run tests on with mostly-original firmware images. Emulators don't require teams to purchase extra hardware, they scale infinitely, you'll experience fewer hardware test flakes, and the performance of hardware does not degrade over time.

In today's silicon shortage, emulators also provide a team with a way to start or continue building firmware without hardware in hand. For example, the Zephyr RTOS[^zephyr] has support for the Cortex-M0 and Cortex-M3 MCU's in QEMU, which should provide a solid platform to start building some applications that run within the Zephyr environment.

The Memfault team is also a big fan of Renode[^renode] for MCU emulation ([quick start guide](https://interrupt.memfault.com/blog/intro-to-renode)), and it even has support for the nRF52 and STM32F4. Emulators really shine when they are hooked up to continuous integration systems and tests are run with them in an [automated fashion](https://interrupt.memfault.com/blog/test-automation-renode).

### Use Unit Tests Where Possible

Unit tests are the fastest way to test a single module of code and prevent it from regressing through constant modifications and refactoring. Unit tests generally run on the host machine and will run in seconds or minutes, providing developers with the quickest build-deploy-test cycles. Use them wherever possible and when a proper integration test combining multiple modules or hardware isn't required.
