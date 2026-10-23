---
id: "tflm-pre-allocated-tensors-current-status"
type: "concept"
domain: "edge-ai"
title: "Pre-allocated tensors: Current status"
summary: "The purpose of pre-allocating tensors is to reduce the number of clock cycles, and our initial motivation for this feature was that avoiding the copying of the buffer described in the Background section would reduce the number of …"
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/rfc/001_preallocated_tensors.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/rfc/001_preallocated_tensors.md#current-status"
license: "Apache-2.0"
mode: "V"
---

The purpose of pre-allocating tensors is to reduce the number of clock cycles,
and our initial motivation for this feature was that avoiding the copying of the
buffer described in the Background section would reduce the number of cycles
consumed by the application.

Our second motivation was that by using a buffer outside of the memory arena,
there was an opportunity to significantly reduce the required size of the memory
arena.

An initial investigation into these matters, using the person detection model as
an example, indicates that the performance gain might not be very significant in
many use cases. The reduction in the number of clock cycles looks to be ~1%.
Details regarding this can be found in the Performance overview section.

The reduction in the size of the memory arena is not straightforward to
estimate. As described in the Performance overview section, it depends on the
size of other tensors in the network. In the worst case scenario it might not
reduce the memory arena size at all. If the pre allocated buffer is much larger
than the second largest buffer, then the reduction in size may be significant.

Therefore, our current position is that the performance gain expected from pre
allocating the tensors does not motivate the increased complexity that this
feature would introduce to the TensorFlow Lite Micro framework.
