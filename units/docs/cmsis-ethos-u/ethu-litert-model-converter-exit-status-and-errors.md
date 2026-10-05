---
id: "ethu-litert-model-converter-exit-status-and-errors"
type: "concept"
domain: "edge-ai"
title: "LiteRT model converter: Exit status and errors"
summary: "The converter validates configuration files, directories, and models before starting Vela. Common errors include:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:examples/Test-Ethos-U/script/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/examples/Test-Ethos-U/script/README.md#exit-status-and-errors"
license: "Apache-2.0"
mode: "V"
---

- `0`: all models were converted.
- `1`: Vela or output generation failed.
- `2`: command-line or YAML configuration is invalid.

The converter validates configuration files, directories, and models before
starting Vela. Common errors include:

- Vela is missing from `PATH`;
- `model.dir`, a model, or the Vela INI file does not exist;
- `model.name` is missing, empty, or malformed; and
- a model path escapes `model.dir`.
