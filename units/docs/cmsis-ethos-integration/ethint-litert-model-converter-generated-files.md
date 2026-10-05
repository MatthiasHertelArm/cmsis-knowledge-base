---
id: "ethint-litert-model-converter-generated-files"
type: "concept"
domain: "edge-ai"
title: "LiteRT model converter: Generated files"
summary: "The int8 suffix is removed when naming the C source. For network.tflite, the outputs are network_vela.tflite and network_model.c."
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@529e966:script/README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/script/README.md#generated-files"
license: "Apache-2.0"
mode: "V"
---

Given this input:

```text
Model/tiny_cnn/tiny_cnn_int8.tflite
```

the converter produces:

```text
Model/tiny_cnn/tiny_cnn_int8_vela.tflite
Model/tiny_cnn/tiny_cnn_model.c
Model/tiny_cnn/VELA_SUMMARY.md
```

The `_int8` suffix is removed when naming the C source. For `network.tflite`,
the outputs are `network_vela.tflite` and `network_model.c`.

The C source exports:

```c
const uint8_t tiny_cnn_int8_vela_tflite[];
const uint32_t tiny_cnn_int8_vela_tflite_len;
```

The array is aligned to 16 bytes and placed in the `ethos_model` section.

`VELA_SUMMARY.md` records the effective accelerator, system, and memory
configuration followed by Vela's report. Command-line overrides are reflected
in this file.

Outputs are prepared in temporary storage and replace destination files only
after Vela succeeds.
