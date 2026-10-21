---
id: "x-check-cmsis-environment-1"
type: "concept"
domain: "project"
title: "Structure of the generated .cmsis/tools-environment.yml"
status: "draft"
extracted_from: "proc-check-cmsis-environment"
source: "project/check-cmsis-environment/SKILL.md"
license: "Apache-2.0"
---

Require one `cmsis-tools-environment` mapping containing string `version`, `generated-by`, and `solution` values; an `environment` mapping with a string array `path` and a string-to-string mapping `variables`; and a `tools` array whose consumed entries contain string `name`, `origin`, and `directory` values plus a `provider` mapping.
