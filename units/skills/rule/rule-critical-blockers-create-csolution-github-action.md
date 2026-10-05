---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
shared: false
id: "rule-critical-blockers-create-csolution-github-action"
constrains: ["proc-create-csolution-github-action"]
---

Stop when the loaded solution is ambiguous, the active target is invalid, CI tool provisioning is undefined, a required pack is not public, an FVP configuration is incomplete, or the workflow fails YAML validation.
