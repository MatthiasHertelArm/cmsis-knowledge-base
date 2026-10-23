---
id: "x-cmsis-debugger-setup-2"
type: "pattern"
domain: "project"
title: "Debugger node in a csolution target set"
status: "draft"
extracted_from: "proc-cmsis-debugger-setup"
source: "cmsis-debugger-setup/SKILL.md"
license: "Apache-2.0"
---

  target-types:
    - type: <target-type>
      board: <vendor>::<board>
      device: <device>
      target-set:
        - set:
          images:
            - project-context: <project>.Debug
          debugger:
            name: <adapter name>
