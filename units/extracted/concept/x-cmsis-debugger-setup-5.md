---
id: "x-cmsis-debugger-setup-5"
type: "concept"
domain: "project"
title: "When the CMSIS Solution extension rewrites launch.json and tasks.json"
status: "draft"
extracted_from: "proc-cmsis-debugger-setup"
source: "cmsis-debugger-setup/SKILL.md"
license: "Apache-2.0"
---

The CMSIS Solution extension rewrites both files when the csolution changes, as long as its setting `cmsis-csolution.autoDebugLaunch` is on (the default). Do not write them by hand.
A launch configuration whose `cmsis` node says `"updateConfiguration": "manual"` is never rewritten; leave it alone and tell the user.
