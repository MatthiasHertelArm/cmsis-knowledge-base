---
id: "ethu-cmsis-mlops-litert-model-converter-acceptance-criteria"
type: "concept"
domain: "edge-ai"
title: "CMSIS MLOps LiteRT model converter specification: Acceptance criteria"
summary: "CMSIS MLOps LiteRT model converter specification: Acceptance criteria"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:examples/Test-Ethos-U/script/model-converter-specification.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/script/model-converter-specification.md#acceptance-criteria"
license: "Apache-2.0"
mode: "V"
---

- A string-valued `model.name` converts one model.
- A sequence-valued `model.name` converts every listed model in one invocation.
- Each model produces a Vela flatbuffer, C array, and Vela summary.
- Default Vela settings come entirely from `*.cbuild-mlops.yml`.
- `--system` and `--memory` override only their corresponding Vela settings.
- Miscellaneous Vela options are preserved by default.
- `--misc` replaces rather than appends to miscellaneous Vela options.
- `--out-dir` redirects only generated C source files.
- The generated `*.cbuild-mlops.yml` file is never modified.
- Relative paths work when invoked from a different working directory.
- Missing files, invalid YAML, unsafe paths, and Vela failures are reported
  clearly and return a nonzero status.
