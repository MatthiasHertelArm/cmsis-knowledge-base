---
id: "tflm-tflm-compression-support-decompressing-a-tensor"
type: "concept"
domain: "edge-ai"
title: "TFLM Compression Support: Decompressing a Tensor"
summary: "Any kernel can have decompression support easily added. Tensor data is decompressed into the designated memory buffer, and is available for the lifetime of the memory buffer."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/compression.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/compression.md#decompressing-a-tensor"
license: "Apache-2.0"
mode: "V"
---

Any kernel can have decompression support easily added.
Tensor data is decompressed into the designated memory buffer, and is available
for the lifetime of the memory buffer.

Only the following methods are required to implement decompression within kernel code:

* `MicroContext::AllocateDecompressionScratchBuffer` ([micro_context.h](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/micro_context.h)):
Allocates a scratch memory buffer within the `MicroInterpreter` to hold the
decompressed tensor data.  The returned scratch memory handle must be retained
(typically through kernel `OpData`) for use during the kernel inference operation.
* `MicroContext::GetTensorCompressionData` ([micro_context.h](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/micro_context.h)):
Retrieves compressed tensor information (see [compression.h](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/compression.h)).
* `tflite::micro::GetTensorData` ([kernel_util.h](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/kernels/kernel_util.h)):
The four parameter version of this method will automatically decompress the
tensor data into the supplied scratch memory buffer.  The lifetime of a scratch
buffer is the same as the lifetime of the current kernel operator being processed.
Each call to the four parameter version of this method will always result in a
decompression operation being performed, if the tensor supplied is compressed.

Please see the [TRANSPOSE_CONV](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/kernels/transpose_conv.cc)
reference kernel code for an example of how to implement tensor decompression
within a kernel.

### Alternate Decompression Memory

Alternate decompression memory regions allow the use of specialized memory
available to the processor, to be used as the target of a tensor decompression
operation.  Such memory is typically mapped by the application through a linker
script.  The application would then use a C++ attribute of the form:
```
__attribute__((section(".your-specialized-memory")))
```
to link one or more application symbols to the specialized memory region.

Only a single API is required to use alternate decompression memory regions in
an application:
* `MicroInterpreter::SetDecompressionMemory` ([micro_interpreter.h](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/micro_interpreter.h)):
Specify the address and size of each alternate decompression
memory region.  This method must be called before the application calls
`MicroInterpreter::AllocateTensors`.  The lifetime of the method parameter must
equal the lifetime of the `MicroInterpreter` instance.  The memory regions
specified by the method parameter must not overlap, and each region is considered
to be non-contiguous with all other regions.

Specifying alternate decompression memory will cause `MicroContext::AllocateDecompressionScratchBuffer`
and `tflite::micro::GetTensorData` (the four parameter version)
to automatically attempt to allocate memory for the decompression destination
buffer from available memory in one of the alternate memory regions.  If no
alternate memory region of sufficient size is available, a scratch buffer will
be allocated within the `MicroInterpreter` arena.

# How to Compress a Model

Compression works best when the targeted tensors in the model have been binned.
Binning of the model tensors will result in a change in model accuracy, but will
also allow for better control of the compression ratio.  For example, by binning
a tensor to just four values among the tensor elements, a fixed-width of two bits
can be used for each element.  This would result in nearly a four-fold decrease
in the size of an INT8 tensor.

Tensors to compress are specified with a `YAML` file.  For example, if tensors
5, 10, 11, 22 of subgraph 0 of the model are to be compressed, the contents of
the file would be as follows:
```
tensors:

  - subgraph: 0
    tensor: 5
    compression:
      - lut:
          index_bitwidth: 4
          per_channel:
            axis: 0

  - subgraph: 0
    tensor: 10
    compression:
      - lut:
          index_bitwidth: 4
          per_channel:
            axis: 0

  - subgraph: 0
    tensor: 11
    compression:
      - lut:
          index_bitwidth: 2
          per_tensor:

  - subgraph: 0
    tensor: 22
    compression:
      - lut:
          index_bitwidth: 2
          per_tensor:
```
Note that each tensor can have a different bit width (1 through 7 bits).

Each `lut` entry states its compression mode, exactly one of `per_channel`
or `per_tensor`. `per_channel` builds one value table per channel, along
the given axis of the tensor's shape. A bare `per_tensor:` builds one
value table for the whole tensor.

Once the `YAML` specification is ready, compress the model using the following:
```
bazel run -s tensorflow/lite/micro/compression:compress -- --input=binned.tflite --output=compressed.tflite --spec=spec.yaml
```

# The Generic Benchmark Application

The Generic Benchmark Application can be used to see the size of the model, the
amount of arena memory used, and the size of the interpreter data structures
including those involved with tensor compression. The benchmark also reports
total inference time, as well as time taken for tensor decompression.

For additional information on the Generic Benchmark Application, please refer to
this [document](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/tools/benchmarking/README.md).
