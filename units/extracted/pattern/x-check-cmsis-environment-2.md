---
id: "x-check-cmsis-environment-2"
type: "pattern"
domain: "project"
title: "Import the generated CMSIS tools environment process-locally"
status: "draft"
extracted_from: "proc-check-cmsis-environment"
source: "project/check-cmsis-environment/SKILL.md"
license: "Apache-2.0"
---

Treat `environment.path`, `environment.variables`, and `tools` as the extension-resolved source of truth. Do not rediscover precedence from the vcpkg artifact store or choose another installation when this file is valid.

Prepend the listed `environment.path` entries to the current process `PATH` in their listed order, preserving their precedence, and export every `environment.variables` entry process-locally. Do not persist variables or edit the generated file; the CMSIS Solution extension is its sole writer.
