---
id: "devt-ctrace-constraints-build-and-ci-constraints"
type: "concept"
domain: "trace"
title: "ctrace Constraints: Build and CI constraints"
summary: "Changes to these contracts require corresponding unit or integration coverage. Update the architecture document only when the implementation structure or data flow changes."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/constraints.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/constraints.md#build-and-ci-constraints"
license: "Apache-2.0"
mode: "V"
---

- Keep the ctrace workflow's `push.paths` and `pull_request.paths` filters identical. They are limited to the ctrace
  workflow and matrix, the root and ctrace CMake configuration, and ctrace source and tests. Changes made only to
  `.gitmodules` or paths below `external/` must not trigger this workflow.
- Changes to the input, routing, or output-profile contracts require the supported-platform CI, portable unit and
  integration suite, native-Linux Babeltrace consumer gate, source-line coverage gate, and branch-report review
  described in the [build and CI architecture](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/architecture.md#build-and-ci-structure). XML-shape changes additionally
  follow the golden-update and external-acceptance requirements in the [CTF profile](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/ctf-format.md#maintaining-the-profile).

Changes to these contracts require corresponding unit or integration coverage. Update the architecture document only
when the implementation structure or data flow changes.
