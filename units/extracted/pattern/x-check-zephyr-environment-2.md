---
id: "x-check-zephyr-environment-2"
type: "pattern"
domain: "project"
title: "Confirm that a Python executable runs inside a virtual environment"
status: "draft"
extracted_from: "proc-check-zephyr-environment"
source: "project/check-zephyr-environment/SKILL.md"
license: "Apache-2.0"
---

Run the selected Python executable with `-c "import sys; print(sys.prefix); print(sys.base_prefix)"`. Confirm that `sys.prefix` differs from `sys.base_prefix`.
