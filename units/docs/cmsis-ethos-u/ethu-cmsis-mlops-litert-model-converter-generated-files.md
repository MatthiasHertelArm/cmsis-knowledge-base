---
id: "ethu-cmsis-mlops-litert-model-converter-generated-files"
type: "concept"
domain: "edge-ai"
title: "CMSIS MLOps LiteRT model converter specification: Generated files"
summary: "For every input model, the converter produces:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:examples/Test-Ethos-U/script/model-converter-specification.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/script/model-converter-specification.md#generated-files"
license: "Apache-2.0"
mode: "V"
---

For every input model, the converter produces:

```text
<input-stem>_vela.tflite
<model-name>_model.c
VELA_SUMMARY.md
```

For `tiny_cnn/tiny_cnn_int8.tflite`, these files are:

```text
tiny_cnn_int8_vela.tflite
tiny_cnn_model.c
VELA_SUMMARY.md
```

`model-name` is the input stem with a trailing `_int8` removed. Without that
suffix, the input stem is used unchanged.

By default, all three files are written beside the input model. When
`--out-dir` is specified, only the generated C source is written to that
directory. The optimized flatbuffer and Vela summary remain beside the input
model.

An absolute `--out-dir` path is used as given. A relative path is resolved from
the directory containing the `*.cbuild-mlops.yml` file, not from the process
working directory. The script creates the directory when required. If multiple
inputs map to the same generated C filename, the script rejects the
configuration instead of overwriting an output.

The C source embeds the Vela output using:

```c
const uint8_t <input-stem>_vela_tflite[];
const uint32_t <input-stem>_vela_tflite_len;
```

The byte array is aligned to 16 bytes and placed in the `ethos_model` section:

```c
__attribute__((aligned(16), section("ethos_model")))
```

The source includes `<stdint.h>`, uses LF line endings, and contains a
generated-file notice and Apache-2.0 SPDX identifier.

`VELA_SUMMARY.md` contains the model name, effective accelerator, system
configuration, memory mode, and Vela textual report in a fenced code block.
Effective values include `--system` and `--memory` overrides.

Vela first writes into temporary storage. Only after successful conversion and
output generation does the script replace destination files. A failure does
not leave a partial flatbuffer, C source, or summary.
