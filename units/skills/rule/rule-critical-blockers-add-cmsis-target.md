---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-critical-blockers-add-cmsis-target"
constrains: ["proc-add-cmsis-target"]
---

Stop on a failed CMSIS environment check, mixed or incompatible CMSIS-Toolbox executables, an active `csolution` older than `created-for`, a board/device identity with zero choices, an `AMBIGUOUS` identity awaiting the user's choice, an invalid or duplicate required target-type name, unavailable required packs, no compatible layer when the project requires one, a conflicting destination, or failed schema/semantic validation.
