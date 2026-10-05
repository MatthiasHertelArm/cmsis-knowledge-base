---
id: "cda-troubleshooting-c-and-c-debug-sess-checklist"
type: "concept"
domain: "debug"
title: "Troubleshooting C and C++ debug sessions: Checklist"
summary: "Troubleshooting C and C++ debug sessions: Checklist"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@7db44ba:docs/agent-resources/troubleshooting/cpp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/cpp.md#checklist"
license: "Apache-2.0"
mode: "V"
---

- [ ] The session runs a debug build (`-g`, `-Og` or `-O0`; `debug: on`, `optimize: debug`).
- [ ] Breakpoints on lines with code; `-exec info breakpoints` when one never stops.
- [ ] Aggregates read by member and element, or with `-exec print`.
- [ ] The wrong value traced to the store that wrote it, in the types the program uses.
- [ ] Watchpoints and catchpoints deleted by number; `clear_all_breakpoints` once the cause is confirmed.
