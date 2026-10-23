---
id: "tflm-tensorflow-lite-for-microcontrolle-design-proposal"
type: "concept"
domain: "edge-ai"
title: "TensorFlow Lite for Microcontrollers Port of 16x8 Quantized Operators: Design Proposal"
summary: "We propose that the 16x8 kernels are ported from the TensorFlow Lite reference kernels to TensorFlow Lite for Microcontrollers following the process in the Porting TensorFlow Lite Ops to Micro guide."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/rfc/002_16x8_quantization_port.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/rfc/002_16x8_quantization_port.md#design-proposal"
license: "Apache-2.0"
mode: "V"
---

We propose that the 16x8 kernels are ported from the TensorFlow Lite reference kernels to
TensorFlow Lite for Microcontrollers following the process in the [Porting TensorFlow Lite Ops to Micro](https://docs.google.com/document/d/1KLJTPWm4TUKB9YyIqFJl9VCP0ZMJDt_P8RNpRmwqMxw/edit#heading=h.5x0d5h95i329)
guide.

We wish to ensure that the following kernels are compatible with 16x8 mode:

- Conv2D
- MaxPool2D
- DepthwiseConv2D
- FullyConnected
- Relu
- Relu6
- Tanh
- Softmax
- Pad
- Reshape
- Pack
- Unpack
- Add
- Mul

Adding the 16x8 kernels directly to TFLM alongside the existing kernels would increase the default code size by an unacceptable amount. Instead, we will make use of the kernel registration API currently under development by the TFLM team. The use of this is demonstrated in the
[Keyword benchmark code](https://github.com/tensorflow/tensorflow/blob/a30d20b632b4ffbfd437ccf8ee205fef0917a3eb/tensorflow/lite/micro/benchmarks/keyword_benchmark.cc#L56).
By doing this, the end user can decide which kernels and dependencies they want to include (e.g. 8 bit, 16x8,
or float32).

For example, the following could be registered:

```
// Support for all datatypes
op_resolver->AddFullyConnected(tflite::Register_FULLY_CONNECTED);
// Support for 8 bit quantized models
op_resolver->AddFullyConnected(tflite::Register_FULLY_CONNECTED_INT8);
// Support for 16x8 quantized models
op_resolver->AddFullyConnected(tflite::Register_FULLY_CONNECTED_INT16X8());
```

This means that kernels not currently using this registration API will need to be refactored to use it. Currently only **FullyConnected** uses the API.

The following associated tasks will be required to support this work:

- Build or port unit tests for the new kernels
- Prove that code memory is not impacted by running benchmarks before and after the port

### Alternatives Considered
* An alternative would be to add the 16x8 kernels without using the new kernel registration API, but this would
  result in a major increase in code size.

### Performance Implications
- Impact on memory usage for current modes (int8 and float32) will be minimal. This will be confirmed by
  benchmarking of current performance against performance of the submitted changes.
- When 16x8 mode is used, RAM usage will be approximately 2x. Latency may change depending on the target
  platform.
- End to end and unit tests will be updated to prove that the new implementations are operating correctly.

### Dependencies
- No additional dependencies will be added to TensorFlow
- No other parts of TensorFlow will be affected

### Engineering Impact
- Impact on binary size should be minimal
- Test times may increase due to additional kernel unit tests
- The reference kernels already exist within TensorFlow Lite so there will be minimal additional maintenance

### Platforms and Environments
- The proposed changes will work on all currently supported platforms

### Best Practices
- TensorFlow Lite for Microcontrollers should be updated to indicate that 16x8 kernels are now available

### Tutorials and Examples
- A benchmark will be added to [`tensorflow/lite/micro/benchmarks`](https://github.com/tensorflow/tensorflow/tree/975335bc83bf3cb80a71a04ed407725508709808/tensorflow/lite/micro/benchmarks) that demonstrates the use of the ops that provide a 16x8 kernel.
- A Colab will be created that demonstrates quantizing a model in 16x8 mode and exporting it as a C header file for use with TensorFlow Lite for Microcontrollers

### Compatibility
- This work will improve compatibility and feature parity between TensorFlow Lite and TensorFlow Lite for Microcontrollers

### User Impact
- Since TFLM does not have a versioning system the feature can be rolled out as any other commit
