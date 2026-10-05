---
id: "ethint-litert-model-converter-overwrite-mlops-settings"
type: "concept"
domain: "edge-ai"
title: "LiteRT model converter: Overwrite MLOps settings"
summary: "Three optional arguments override settings from the .cbuild-mlops.yml file:"
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@529e966:script/README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/script/README.md#overwrite-mlops-settings"
license: "Apache-2.0"
mode: "V"
---

Three optional arguments override settings from the `*.cbuild-mlops.yml` file:

```text
--system <name>    Vela system configuration
--memory <name>    Vela memory mode
--misc <options>   Complete miscellaneous option string
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
