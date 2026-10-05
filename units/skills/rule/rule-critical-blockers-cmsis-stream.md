---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
shared: false
id: "rule-critical-blockers-cmsis-stream"
constrains: ["proc-cmsis-stream"]
---

Stop generation when the component specification or destination folders are missing or ambiguous, or the required API behavior cannot be established. If a Python import check is unavailable, report that limitation and do not claim it passed.
