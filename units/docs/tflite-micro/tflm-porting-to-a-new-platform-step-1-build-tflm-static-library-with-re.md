---
id: "tflm-porting-to-a-new-platform-step-1-build-tflm-static-library-with-re"
type: "concept"
domain: "edge-ai"
title: "Porting to a new platform: Step 1: Build TFLM Static Library with Reference Kernels"
summary: "Use the TFLM project generation script to create a directory tree containing only the sources that are necessary to build the code TFLM library."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/new_platform_support.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/new_platform_support.md#step-1-build-tflm-static-library-with-reference-kernels"
license: "Apache-2.0"
mode: "V"
---

Use the TFLM project generation script to create a directory tree containing
only the sources that are necessary to build the code TFLM library.

```bash
python3 tensorflow/lite/micro/tools/project_generation/create_tflm_tree.py \
  -e hello_world \
  -e micro_speech \
  -e person_detection \
  /tmp/tflm-tree
```

This will create a folder that looks like the following at the top-level:
```bash
examples  LICENSE  tensorflow  third_party
```

All the code in the `tensorflow` and `third_party` folders can be compiled into
a single static library (for example `libtflm.a`) using your platform-specific
build system.

TFLM's third party dependencies are separated out in case there is a need to
have shared libraries for the third party code to avoid symbol collisions.

Note that for IDEs, it might be sufficient to simply include the
folder created by the TFLM project generation script into the overall IDE tree.
