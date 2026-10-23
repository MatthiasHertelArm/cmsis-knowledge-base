---
id: "tflm-pre-allocated-tensors-performance-overview"
type: "concept"
domain: "edge-ai"
title: "Pre-allocated tensors: Performance overview"
summary: "In this section we try to estimate the number of clock cycles one memcpy() takes in relation to the total inference time for the person_detection model."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/rfc/001_preallocated_tensors.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/rfc/001_preallocated_tensors.md#performance-overview"
license: "Apache-2.0"
mode: "V"
---

### Cycle aspect

In this section we try to estimate the number of clock cycles one memcpy() takes
in relation to the total inference time for the person_detection model. The
reason for looking closer at this model is that it has a relatively large input
data size, which should make the cycle consumption of a memcpy() relatively
large. Please note that these numbers are approximate and based on calculations,
not actual benchmarking numbers.

A word aligned memcpy() consumes somewhere between 1 - 4 bytes per cycle
depending on which CPU is used. The input size for the person_detection model
is 96x96 = 9216 bytes. On a reference system without accelerators one memcpy()
of 9216 bytes corresponds to, in order of magnitudes, ~0.01% of the total amount
of clock cycles for one inference. The ratio will differ depending on the input
size and the number of inferences/second.

When using an accelerator, the total inference time will be significantly less
which means that the memcpy()-call will consume a larger part of the total
inference time. Approximations show that one memcpy() of 9216 bytes will consume
~1% of the total execution time for a reference system utilizing an ML HW
accelerator.

### Memory aspect

In this section we'll look at memory savings aspects of pre-allocating tensors
outside the tensor arena. The default memory planner in TFLu is
[GreedyPlanner](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/memory_planner/greedy_memory_planner.h)
(see
[RFC](https://docs.google.com/document/d/1akpqu0uiPQshmCrnV6dOEFgYM4tCCnI8Zce85PnjHMI)).
One good tool for understanding tensor layout in the tensor arena is using
[PrintMemoryPlan API](https://github.com/tensorflow/tflite-micro/blob/73c5fa4d2bfbfd974552957818de2ab18ff42f39/tensorflow/lite/micro/memory_planner/greedy_memory_planner.h#L84).
If we print the calculated memory layout for the
[person detection model](https://storage.googleapis.com/download.tensorflow.org/data/tf_lite_micro_person_data_int8_grayscale_2020_06_23.zip),
the tensor arena looks like this at each layer:

`Layer 1:
00000000000000000000000000tttttttttttttt........................................
Layer 2:
00000000000000000000000000...........................999999999999999999999999999
Layer 3:
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999
Layer 4:
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbb..............
Layer 5:
cccccccccccccccccccccccccc...........................bbbbbbbbbbbbb..............
Layer 6:
ccccccccccccccccccccccccccddddddddddddddddddddddddddd...........................`

The horizontal axis shows offset from the start of the tensor arena. The
vertical axis shows execution order. The dots are "unused" memory for that
specific layer. The letters and numbers represent the EvalTensor index, mapped
to 0-9, then a-z. 't' is the input tensor of layer 1 (equivalent to the input
data to the model) and '0' is the output tensor of layer 1. Hence, '0' is also
the input tensor to layer 2, and '9' is the output tensor of layer 2. And so on.

The reason for showing this illustration is that it becomes obvious that it is
**the largest combination of simultaneously used tensors, of your model, that
defines how large the tensor arena needs to be.** In this example, it's Layer 3.

The combined size of tensors 'a' and '9' defines the size needed for the tensors
arena. As a consequence, to save tensor arena memory by pre-allocation, we must
start by pre-allocating tensor 'a' or '9' outside the arena. This will make the
total size of the tensor arena smaller, which will reduce the total memory
footprint of TensorFlow Lite Micro if the pre-allocated tensor is already
allocated outside of the memory arena, like in the examples given in the
Background section.
