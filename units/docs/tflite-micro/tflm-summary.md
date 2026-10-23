---
id: "tflm-summary"
type: "concept"
domain: "edge-ai"
title: "Summary"
summary: "This guide describes the recommended high-level architecture and steps to add hardware-specific optimized kernels to TfLite Micro."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/optimized_kernel_implementations.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/optimized_kernel_implementations.md"
license: "Apache-2.0"
mode: "V"
---

This guide describes the recommended high-level architecture and steps to add
hardware-specific optimized kernels to TfLite Micro.

The goal with these optimizations and the process that we recommend to getting
them merged into the TfLite Micro codebase is to have a measurable and
documented performance improvement on a benchmark of interest.

Once the optimizations are merged, they will indeed be used for more than the
benchmark but the context for why the optimizations were added is still very
important.

# High-Level Steps

1.  Pick a benchmark that you would like to measure the performance for.

    *   Existing benchmarks are in the [benchmarks directory](https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/../benchmarks).
    *   If none of the existing benchmarks capture your use-case, then please
        create a github issue or start a thread on micro@tensorflow.org to
        figure out how to add in a new benchmark.
    *   If adding a publicly-available benchmark to the TFLM codebase is
        determined to be infeasible, then a fall-back would be to have an
        internal benchmark that can be used to document the benefits of adding
        in the optimizations via PR descriptions.
    *   Adding optimized code without any associated benchmarks will need very
        strong justification and will most likely not be permitted.

1.  Do the groundwork and architecture needed to be able to add in optimizations
    for your target (more details in the
    [software architecture](#software-architecture) section).

1.  Create one pull request for each optimized kernel with the PR description
    clearly stating the commands that were used to measure the performance
    improvement.

    *   This context is important even if the toolchain is proprietary and there
        are currently a small number of users.
        *   See [this PR](https://github.com/tensorflow/tensorflow/pull/47098)
            as an example.
        *   At minimum the latency with and without the particular optimized
            kernel should be documented.
            [Additional context](https://github.com/tensorflow/tensorflow/pull/46746)
            may also be desirable.
    *   Here is some
        [general guidance](https://testing.googleblog.com/2017/09/code-health-providing-context-with.html)
        on writing
        [good PR descriptions](https://google.github.io/eng-practices/review/developer/cl-descriptions.html)
