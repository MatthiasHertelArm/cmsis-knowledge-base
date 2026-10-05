---
id: "tflm-software-emulation-with-renode"
type: "concept"
domain: "edge-ai"
title: "Software Emulation with Renode"
summary: "TensorFlow Lite Micro makes use of Renode for software emulation."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/renode.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/renode.md"
license: "Apache-2.0"
mode: "V"
---

TensorFlow Lite Micro makes use of [Renode](https://github.com/renode/renode) for
software emulation.

Here, we document how Renode is used as part of the TFLM project. For more
general use of Renode, please refer to the [Renode
documentation](https://renode.readthedocs.io/en/latest/).

You can also read more about Renode from a [publicly available slide deck](https://docs.google.com/presentation/d/1j0gjI4pVkgF9CWvxaxr5XuCKakEB25YX2n-iFxlYKnE/edit).

# Installation

Renode can be installed and used in a variety of ways, as documented in the
[Renode README](https://github.com/renode/renode/blob/master/README.rst#installation/). For the purpose of Tensorflow
Lite Micro, we make use of the portable version for Linux.

Portable renode will be automatically installed when using the TfLite Micro
Makefile to `tensorflow/lite/micro/tools/make/downloads/renode`.

The Makefile internally calls the `renode_download.sh` script:

```
tensorflow/lite/micro/tools/make/renode_download.sh tensorflow/lite/micro/tools/make/downloads
```

# Running Unit Tests

All the tests for a specific platform (e.g. bluepill) can be run with:

```
make -f tensorflow/lite/micro/tools/make/Makefile TARGET=bluepill test
```

 * This makes use of the robot framework from Renode.
 * Note that the tests can currently not be run in parallel.
 * It takes about 25 second to complete all tests, including around 3 seconds for suite startup/teardown and average 0.38 second per test.
