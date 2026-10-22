---
id: "ethint-litert-model-converter-overwrite-mlops-settings"
type: "concept"
domain: "edge-ai"
title: "LiteRT model converter: Overwrite MLOps settings"
summary: "Four optional arguments control outputs or override settings from the .cbuild-mlops.yml file:"
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:script/README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/script/README.md#overwrite-mlops-settings"
license: "Apache-2.0"
mode: "V"
---

Four optional arguments control outputs or override settings from the
`*.cbuild-mlops.yml` file:

```text
--system <name>    Vela system configuration
--memory <name>    Vela memory mode
--misc <options>   Complete miscellaneous option string
--out-dir <path>   Explicit path for generated C source files
```

Change the system or memory configuration:

```console
python script/model-converter.py Test-Ethos-U55.cbuild-mlops.yml --system Ethos_U55_High_End_Embedded
python script/model-converter.py Test-Ethos-U55.cbuild-mlops.yml --memory Shared_Sram
```

Replace all miscellaneous Vela options:

```console
python script/model-converter.py Test-Ethos-U55.cbuild-mlops.yml --misc="--verbose-all --timing"
```

An empty value removes them:

```console
python script/model-converter.py Test-Ethos-U55.cbuild-mlops.yml --misc=""
```

`--misc` replaces `vela.misc`; it does not append to it.
