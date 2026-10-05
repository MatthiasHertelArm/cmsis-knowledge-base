---
id: "stream-readme-cmsisstream-tensor-max-dimensions"
type: "concept"
domain: "cmsis-stream"
title: "README: CMSISSTREAM_TENSOR_MAX_DIMENSIONS"
summary: "It defines the maximum number of dimensions for tensors used in the CMSIS Stream library. The default value of 3 is suitable for image oriented applications (height, width, channels)."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:platform/cmsis_rtos_runtime/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/platform/cmsis_rtos_runtime/README.md#cmsisstream-tensor-max-dimensions"
license: "Apache-2.0"
mode: "V"
---

Maximum number of tensor dimensions.

It defines the maximum number of dimensions for tensors used in the CMSIS Stream library.
The default value of 3 is suitable for image oriented applications (height, width, channels).

Default value:
```C
#define CMSISSTREAM_TENSOR_MAX_DIMENSIONS 3
```
