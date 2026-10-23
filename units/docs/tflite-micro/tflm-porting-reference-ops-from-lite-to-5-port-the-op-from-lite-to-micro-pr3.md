---
id: "tflm-porting-reference-ops-from-lite-to-5-port-the-op-from-lite-to-micro-pr3"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: 5. Port the op from Lite to Micro (PR3)"
summary: "In the first commit of this PR, copy the kernel and test from Lite to Micro without making any modifications and without adding them to the build."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/porting_reference_ops.md#5-port-the-op-from-lite-to-micro-pr3"
license: "Apache-2.0"
mode: "V"
---

1.  Copy the kernel and test from Lite to Micro.

    In the first commit of this PR, copy the kernel and test from Lite to Micro
    without making any modifications and without adding them to the build.

    A good example is commit [a2ca1fd](https://github.com/tensorflow/tensorflow/commit/a2ca1fd7a174438f736c0435dd3e4e618612fdee).

    This copy action is in its own commit in order to create readable, reviewable diffs
    when modifications are made in later commits. If the files were copied and
    modified in one step, the modifications would not appear as a diff of the Lite
    version. Instead, the files would simply appear at the destination path in
    their final form.


1.  Remove Lite-specific code from copies

    In the second commit of this PR, remove the bulk of Lite-specific code from
    the files copied to micro in the previous step.

    A good example is commit [a5a87b4](https://github.com/tensorflow/tensorflow/commit/a5a87b420b87a1f832e241db3a5b724207ea700a).

    This bulk-delete action is in its own commit for reasons similar to
    those given in the step above: to produce a more readable, reviewable diff in this
    step and in the next. Because the files are not yet added to the build, they
    need not (and obviously won't) compile or function. What to delete now as
    opposed to deleting in the next commit is somewhat subjective, but make    deletes in order to:

    -   Flatten the namespace down to `tflite`.
    -   Stop resizing output tensors.
    -   Remove input and output types other than `int8`, `int16`, and `float32`.
    -   Stop using gmock and gtest.
    -   etc.

1.  Port the op and the test

    Make the necessary changes to the micro kernel, header, and test to make the op
    implementation suitable for micro. Include these in the build.

    This step requires the most creativity, and may receive the most feedback
    during review. Maintain good atomicity in your commits. Considering its
    scope, this step will consist of more than one commit. A good example is
    the changes made in [PR #45647][].

1.  Use `clang-format` to make sure the code is properly formatted.

    ```shell
    $ clang-format --style=google -i $(git ls-files -m | grep -E '\.cc|\.h')
    ```

    Do not clang-format existing code in `BUILD` or `reference_ops.h`.

1.  Make sure the code is lint-free.

    ```shell
    $ cpplint.py $(git ls-files -m)
    ```

    Do not modify code in `BUILD` or `reference_ops.h` to satisfy `cpplint.py`.

1.  Make sure the port passes all applicable tests.

    ```shell
    $ bazel test tensorflow/lite/micro/kernels:${op}_test
    $ bazel test tensorflow/lite/micro/kernels:all
    $ make -f tensorflow/lite/micro/tools/make/Makefile test_kernel_${op}_test
    $ make -f tensorflow/lite/micro/tools/make/Makefile test
    ```

    See the general [Micro Contributing Guidelines][] for other testing ideas,
    including the use of address sanitizers.

1.  Create and submit the PR. Write a [good PR description][], and be sure to
    link to the GitHub issue created to document the port. A good example is
    [PR #45647][].

# General Guidelines
