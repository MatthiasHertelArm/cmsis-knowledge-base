---
type: "rule"
title: "Hardware identity"
severity: "must"
status: "draft"
shared: false
id: "rule-hardware-identity-add-cmsis-target"
constrains: ["proc-add-cmsis-target"]
---

A target may be added only after each required board/device identity resolves to exactly one verified choice. Installed-pack results alone cannot prove uniqueness because they may omit online catalog candidates. Ask the user to resolve an `AMBIGUOUS` candidate list before editing.
