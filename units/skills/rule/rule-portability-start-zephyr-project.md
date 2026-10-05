---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
shared: false
id: "rule-portability-start-zephyr-project"
constrains: ["proc-start-zephyr-project"]
---

Do not add a device-, board-, compiler-, debugger-, or RTOS-specific setting unless the verified inputs require it; retain the conditional GCC-only configuration below.
