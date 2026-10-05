---
id: "x-cmsis-debugger-setup-2"
type: "concept"
domain: "project"
title: "Load runs the firmware before the debugger attaches"
status: "draft"
extracted_from: "proc-cmsis-debugger-setup"
source: "cmsis-debugger-setup/SKILL.md"
---

**Load runs the firmware before the debugger attaches.** In `load_and_debug` the pre-launch `CMSIS Load` task programs and starts the image; the session then restarts it and halts at `main`. A complete run's output can already be in the serial buffer at the first stop. Do not count that run twice.
