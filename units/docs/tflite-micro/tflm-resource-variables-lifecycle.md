---
id: "tflm-resource-variables-lifecycle"
type: "concept"
domain: "edge-ai"
title: "Resource Variables: Lifecycle"
summary: "When the ResourceVariables class is created in the application, it contains an array of N ResourceVariable handles. The index into this array is the Resource ID."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/resource_variables.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/resource_variables.md#lifecycle"
license: "Apache-2.0"
mode: "V"
---

When the ResourceVariables class is created in the application, it contains an
array of N ResourceVariable handles. The index into this array is the Resource
ID.

On the first call to Prepare in the VAR_HANDLE op, a new resource ID is reserved
and the resource ID value is referenced from within the output tensor of
VAR_HANDLE. On the first call to Prepare in ASSIGN_VARIABLE, the specified ID
found in the input index tensor is updated based on the size of the input value
tensor, and its resource buffer is allocated.

Future invocations of READ_VARIABLE and ASSIGN_VARIABLE read and write to and
from the allocated resource buffer.

The lifecycle must follow the pattern:
VAR_HANDLE Prepare() -> ASSIGN_VARIABLE Prepare() -> Other calls

Note that VAR_HANDLE Prepare() and ASSIGN_VARIABLE Prepare() may be called more
that once, across multiple subgraphs. Only the first call to each will generate
a new resource ID or allocate a resource buffer.
