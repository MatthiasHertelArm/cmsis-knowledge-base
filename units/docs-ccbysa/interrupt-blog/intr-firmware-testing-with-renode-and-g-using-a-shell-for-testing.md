---
id: "intr-firmware-testing-with-renode-and-g-using-a-shell-for-testing"
type: "concept"
domain: "debug"
title: "Firmware Testing with Renode and GitHub Actions: Using a Shell for Testing"
summary: "Whether tests are being run within Renode or on real hardware, there should be a way to easily run tests on a device."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-07-test-automation-renode.md"
doc_source: "https://interrupt.memfault.com/blog/test-automation-renode#using-a-shell-for-testing"
license: "CC-BY-SA-4.0"
mode: "V"
---

Whether tests are being run within Renode or on real hardware, there should be a
way to easily run tests on a device.

A common approach is to use a CLI-based shell over serial, which we wrote about
in our post [Building a Tiny CLI Shell for Tiny
Firmware](https://interrupt.memfault.com/blog/firmware-shell#integration--automated-tests).

The idea is relatively simple.

1. Create a test that will execute a series of shell commands on a device.
2. After each command or series of commands, the results will be compared
   against expected values.
3. At the end of the test run, the harness determines whether the test was
   successful or not.

Thankfully for us, Renode has several utilities and helpers built-in that we can
take advantage of.
