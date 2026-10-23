---
id: "tflm-porting-reference-ops-from-lite-to-4-extract-the-reference-for-the-op-to-a"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: 4. Extract the reference for the op to a standalone header (PR2)"
summary: "Move the reference implementation of the op in [reference_ops.h][] to a standalone header so that Micro can include it without including unrelated dependencies via reference_ops.h."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/porting_reference_ops.md#4-extract-the-reference-for-the-op-to-a-standalone-header-pr2"
license: "Apache-2.0"
mode: "V"
---

Move the reference implementation of the op in [reference_ops.h][] to a standalone header so that
Micro can include it without including unrelated dependencies via
reference_ops.h.

A good example is [PR #45311][].

1.  Copy an existing header from `tensorflow/lite/kernels/internal/reference/`
    to `tensorflow/lite/kernels/internal/reference/NEW_OP.H` to create the
    boilerplate. Replace `NEW_OP.H` with the name of the new operator.

1.  Move the implementation from
    `tensorflow/lite/kernels/internal/reference/reference_ops.h` to
    `tensorflow/lite/kernels/internal/reference/NEW_OP.H`.

1.  Add the new header to the build by adding to the  library definitions
    `reference_base` and `legacy_reference_base` in the file
    `tensorflow/lite/kernels/internal/BUILD`. See, for example,
    [this change for operator FILL](https://github.com/tensorflow/tensorflow/pull/45311/commits/92f459e6b917fa5099ef5317d14c5100d33a86f0#diff-0b0fc9e1affece3c5a141ee9326f882876b6b958bc8b12a7c01d7540dc04983e).

1.  Use the program `clang-format` to make sure the code is properly formatted.

    ```shell
    clang-format --style=google -i $(git ls-files -m | grep -E '\.cc|\.h')
    ```

    Do not clang-format existing code in `BUILD` or `reference_ops.h`.

1.  Make sure your code is lint-free.

    ```shell
    cpplint.py $(git ls-files -m)
    ```

    Do not modify code in `BUILD` or `reference_ops.h` to satisfy `cpplint.py`.

1.  Create a single commit containing the change. Observe the guidelines for
    good commit log messages found in the article [Providing Context][].
    A good example is commit [92f459e](https://github.com/tensorflow/tensorflow/commit/92f459e6b917fa5099ef5317d14c5100d33a86f0).

1.  Since this change modifies the op's implementation in Lite, test the change
    with the relevant Lite unit tests.

    ```shell
    bazel test tensorflow/lite/kernels:all
    ```

1.  Create and submit the PR. Write a [good PR description][], and be sure to
    link to the GitHub issue created to document the port. A good example is
    [PR #45311][].
