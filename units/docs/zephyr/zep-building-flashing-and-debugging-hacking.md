---
id: "zep-building-flashing-and-debugging-hacking"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Hacking"
summary: "This section documents the runners.core module used by the flash and debug commands. This is the core abstraction used to implement support for these features."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

This section documents the `runners.core` module used by the
flash and debug commands. This is the core abstraction used to implement
support for these features.

Developers can add support for new ways to flash and debug Zephyr programs by
implementing additional runners. To get this support into upstream Zephyr, the
runner should be added into a new or existing `runners` module, and imported
from `runners/__init__.py`.


**Note:** The test cases in `scripts/west_commands/tests` add unit test coverage for the runners package and individual runner classes. Please try to add tests when adding new runners. Note that if your changes break existing test cases, CI testing on upstream pull requests will fail.
