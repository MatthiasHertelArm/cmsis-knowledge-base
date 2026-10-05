---
id: "intr-firmware-testing-with-renode-and-g-automation-testing-for-firmware"
type: "concept"
domain: "debug"
title: "Firmware Testing with Renode and GitHub Actions: Automation Testing for Firmware"
summary: "Test automation is the practice of testing software and/or hardware in a repeatable and scalable way where expected values are compared against actual values."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-07-test-automation-renode.md"
doc_source: "https://interrupt.memfault.com/blog/test-automation-renode#automation-testing-for-firmware"
license: "CC-BY-SA-4.0"
mode: "V"
---

Test automation is the practice of testing software and/or hardware in a
repeatable and scalable way where expected values are compared against actual
values.

There are various forms of test automation, and they are usually run under a
continuous integration system, such as Jenkins, GitHub Actions, or CircleCI.

- Software Unit Tests - Isolated tests that exercise a single module. Usually
  run on the host machine and sometimes on an emulator or real device.
- Integration Tests - Tests that exercise a collection of modules that interact
  with each other
- End-to-end Tests - Tests that exercise an entire technical stack end-to-end.
  These tests would usually communicate with some sort of backend in the cloud
  or a mobile phone.

These testing approaches are not limited entirely to software, as hardware can
be tested in similar ways. "Hardware unit testing" is a concept where individual
pieces of the larger hardware board are put under test to ensure the chip itself
behaves correctly. Integration tests and end-to-end tests can also be performed
on hardware, but the complexity increases exponentially as more hardware is
thrown into the mix.

A middle ground between host-run tests and hardware tests is testing on an
emulator which emulates the real hardware as much as possible. Renode, by
Antmicro, has become our favorite emulator at Memfault, and its list of support
boards is continually growing[^renode_boards]. Renode emulates many peripherals
of the board, including the UART, SPI, I2C, RAM, ROM, and GPIO's.

Renode has a built-in integration with the open-source testing framework called
Robot Framework[^robot_framework]. Robot Framework is most popular in the web
world, but it is generic and powerful enough to be used for many more use-cases.
It provides the glue between various test scripts, test reporting, and multiple
machines under test.
