---
id: "tflm-porting-reference-ops-from-lite-to-check-each-commit-for-formatting-lint-an"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: Check each commit for formatting, lint, and unit-test passage"
summary: "Check each commit against the [pre-submit checklist][] in the micro Contributing Guidelines. Specifically, make sure your code:"
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/porting_reference_ops.md#check-each-commit-for-formatting-lint-and-unit-test-passage"
license: "Apache-2.0"
mode: "V"
---

Check each commit against the [pre-submit checklist][] in the micro
Contributing Guidelines. Specifically, make sure your code:

1.  Is formatted with clang-format.
1.  Passes a lint check.
1.  Passes all unit tests.

    ```shell
    $ make -s -j8 -f tensorflow/lite/micro/tools/make/Makefile test
    ```

CI runs these checks on all PRs, and will hold up your PR if any of these checks fail.
