---
id: "x-start-zephyr-project-4"
type: "concept"
domain: "project"
title: "What cbuild setup with --update-rte checks and generates"
status: "draft"
extracted_from: "proc-start-zephyr-project"
source: "project/start-zephyr-project/SKILL.md"
license: "Apache-2.0"
---

cbuild setup <solution-name>.csolution.yml --active <target-type> --packs --update-rte

This invokes west's CMake-only setup and helps detect invalid paths, board targets, pack identifiers, and project contexts before compilation. `--update-rte` generates required RTE files, including board debug configuration files.
