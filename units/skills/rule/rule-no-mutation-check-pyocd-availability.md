---
type: "rule"
title: "No mutation"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-no-mutation-check-pyocd-availability"
constrains: ["proc-check-pyocd-availability"]
refines: ["rule-no-install"]
delta_of: "rule-no-install"
---

Do not install pyOCD or an extension, change `PATH`, activate an environment, or alter Visual Studio Code settings.

## Delta zu rule-no-install

pyOCD or an extension, change `PATH`, activate an environment, or alter Visual Studio Code settings
