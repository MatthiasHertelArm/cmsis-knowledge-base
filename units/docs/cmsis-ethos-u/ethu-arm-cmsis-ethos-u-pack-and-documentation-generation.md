---
id: "ethu-arm-cmsis-ethos-u-pack-and-documentation-generation"
type: "concept"
domain: "edge-ai"
title: "Arm CMSIS Ethos-U: Pack and Documentation Generation"
summary: "Generate the documentation from a Bash shell with:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/README.md#pack-and-documentation-generation"
license: "Apache-2.0"
mode: "V"
---

Generate the documentation from a Bash shell with:

```bash
./documentation/doxygen/gen_doc.sh
```

Generate the CMSIS-Ethos-U software pack with:

```bash
./gen_pack.sh
```

The pack script builds the documentation as a preprocessing step and writes the resulting archive to `output` by default. See the [documentation authoring guide](https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/./documentation/README.md) for prerequisites and document structure.
