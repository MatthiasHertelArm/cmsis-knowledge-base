---
type: "rule"
title: "Exactly-one gate"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-exactly-one-gate-identify-cmsis-board-support"
constrains: ["proc-identify-cmsis-board-support"]
---

Do not return a usable support result unless every required board/device identity resolves to exactly one choice. For multiple choices, ask the user to select from the exact candidates before continuing.
