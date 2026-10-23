---
id: "ethint-litert-model-converter-basic-usage"
type: "concept"
domain: "edge-ai"
title: "LiteRT model converter: Basic usage"
summary: "The path to the .cbuild-mlops.yml file may be absolute or relative. Example:"
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:script/README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/script/README.md#basic-usage"
license: "Apache-2.0"
mode: "V"
---

```console
python script/model-converter.py <project.cbuild-mlops.yml>
```

The path to the *.cbuild-mlops.yml file may be absolute or relative. Example:

```console
python script/model-converter.py Test-Ethos-U55.cbuild-mlops.yml
```

### C source output directory

By default, each generated C source is written beside its input model. Use
`--out-dir` when the build system expects generated sources in a separate
directory:

```console
python script/model-converter.py Test-Ethos-U55.cbuild-mlops.yml --out-dir source/model
```

An absolute path is used as given. A relative path is resolved from the
directory containing the `*.cbuild-mlops.yml` input file, independently of the
shell's current working directory. The converter creates the output directory
when necessary.

Only generated `*_model.c` files are redirected. The Vela-optimized
`*_vela.tflite` files and `VELA_SUMMARY.md` reports remain beside their input
models. If multiple input models would produce the same C filename, conversion
is rejected instead of overwriting one model with another.
