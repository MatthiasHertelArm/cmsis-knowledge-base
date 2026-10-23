---
id: "cda-troubleshooting-c-and-c-debug-sess-starting-a-host-program"
type: "concept"
domain: "debug"
title: "Troubleshooting C and C++ debug sessions: Starting a host program"
summary: "Troubleshooting C and C++ debug sessions: Starting a host program"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@29d444c:docs/agent-resources/troubleshooting/cpp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/29d444c/docs/agent-resources/troubleshooting/cpp.md#starting-a-host-program"
license: "Apache-2.0"
mode: "V"
---

- Start it from a `launch.json` entry that names the executable: `start_debugging` with `configurationName`. "Default Configuration" launches `cppdbg` with `program` set to the source path ending in `.exe` instead of `.c`, `.cc` or `.cpp`, which is rarely the program.
- `testName` does not filter C or C++ tests. Put the filter into the entry's `args` instead, such as `--gtest_filter=Parser.Empty` for GoogleTest.
- Firmware sessions start with `cmsis_action load_and_debug`, or with `start_debugging` and the `gdbtarget` entry to attach without flashing.
