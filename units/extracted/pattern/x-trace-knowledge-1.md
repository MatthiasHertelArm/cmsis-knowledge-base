---
id: "x-trace-knowledge-1"
type: "pattern"
domain: "bring-up"
title: "Source-to-sink route table per trace mode"
status: "draft"
extracted_from: "proc-trace-knowledge"
source: "bring-up/trace-knowledge/SKILL.md"
license: "Apache-2.0"
---

For each trace mode, build the required source-to-sink route table: record the ordered route and classify every participating component as `source-side`, `funnel/glue`, or `sink/output`. Establish the route-specific components, addresses and access path, trace-clock source and enablement, pin-function and electrical configuration, path-selection controls, and sink operating mode plus device-specific lifecycle constraints.
