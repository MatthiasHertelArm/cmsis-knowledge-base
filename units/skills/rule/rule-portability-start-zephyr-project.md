---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-portability-start-zephyr-project"
constrains: ["proc-start-zephyr-project"]
refines: ["rule-portability"]
delta_of: "rule-portability"
---

Do not add a device-, board-, compiler-, debugger-, or RTOS-specific setting unless the verified inputs require it; retain the conditional GCC-only configuration below.

## Delta zu rule-portability

RTOS-specific setting unless the verified inputs require it; retain the conditional GCC-only configuration below.
