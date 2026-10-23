---
id: "tflm-porting-reference-ops-from-lite-to-3-extract-lite-s-code-for-parsing-op-par"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: 3. Extract Lite's code for parsing op parameters to a function (PR1)"
summary: "Now we begin changing, testing, and submitting code. This step will result in the first pull request, PR1."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/porting_reference_ops.md#3-extract-lite-s-code-for-parsing-op-parameters-to-a-function-pr1"
license: "Apache-2.0"
mode: "V"
---

Now we begin changing, testing, and submitting code. This step will result in
the first pull request, PR1.

1.  Extract the code for parsing op parameters out of the switch statement in
    [`ParseOpDataTfLite()`][] in `lite/core/api/flatbuffer_conversions.cc` into
    a standalone function, and call that function from the switch statement.
    This standalone function is now available to be called by the Micro op
    resolver, which also needs to parse the op parameters, in a future change.
    A simple example is [PR #45307][], and a more complicated example is [PR
    #46021][].

1.  Use `clang-format` to make sure the code is properly formatted.

    ```shell
    clang-format --style=google -i $(git ls-files -m | grep -E '\.cc|\.h')
    ```

1.  Make sure your code is lint-free.

    ```shell
    cpplint.py $(git ls-files -m)
    ```

1.  Create a single commit containing the change. Observe the guidelines for
    good commit log messages found in the article [Providing Context][].
    A good example is commit [0664214](https://github.com/tensorflow/tensorflow/pull/45307/commits/0664214792ad2357f6224e7002661894775cb512).

1.  Since this change modifies the op's implementation in Lite, test the change
    with the relevant Lite unit tests.

    ```shell
    bazel test tensorflow/lite/kernels:all
    ```

1.  Create and submit the PR. Write a [good PR description][], and be sure to
    link to the GitHub issue created to document the port. A good example is
    [PR #45307][].

    [good PR description]: https://google.github.io/eng-practices/review/developer/cl-descriptions.html
