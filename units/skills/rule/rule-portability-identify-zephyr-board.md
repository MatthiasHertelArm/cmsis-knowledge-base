---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-portability-identify-zephyr-board"
constrains: ["proc-identify-zephyr-board"]
refines: ["rule-portability"]
delta_of: "rule-portability"
---

Keep the installed Zephyr board catalog authoritative for its version; do not introduce CMSIS-pack, toolchain, debugger, or hardware assumptions.

## Delta zu rule-portability

Keep the installed Zephyr board catalog authoritative for its version; do not introduce CMSIS-pack … assumptions.
