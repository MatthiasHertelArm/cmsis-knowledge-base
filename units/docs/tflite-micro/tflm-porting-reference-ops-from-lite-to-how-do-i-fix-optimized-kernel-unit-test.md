---
id: "tflm-porting-reference-ops-from-lite-to-how-do-i-fix-optimized-kernel-unit-test"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: How do I fix optimized kernel unit test failures?"
summary: "Kernel unit tests for all optimized kernels should pass. It should be noted that optimized kernels may not handle all tensor types or operator parameters. In this case, the optimized kernel should fallback on calling the reference kernel methods."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/porting_reference_ops.md#how-do-i-fix-optimized-kernel-unit-test-failures"
license: "Apache-2.0"
mode: "V"
---

Kernel unit tests for all optimized kernels should pass.
It should be noted that optimized kernels may not handle all tensor types or
operator parameters.
In this case, the optimized kernel should fallback on calling the reference
kernel methods. The following code snippet example can be found [here](https://github.com/tensorflow/tflite-micro/blob/a1eb0480ed9f98e9ea5f5fb9b8e3da98ec512caf/tensorflow/lite/micro/kernels/cmsis_nn/softmax.cc#L98C1-L123C6):
```
    case kTfLiteFloat32: {
      tflite::reference_ops::Softmax(
          op_data.softmax_params, tflite::micro::GetTensorShape(input),
          tflite::micro::GetTensorData<float>(input),
          tflite::micro::GetTensorShape(output),
          tflite::micro::GetTensorData<float>(output));
      return kTfLiteOk;
    }
    case kTfLiteInt8: {
      if (output->type == kTfLiteInt8) {
        arm_softmax_s8(tflite::micro::GetTensorData<int8_t>(input),
                       op_data.num_rows, op_data.row_size,
                       op_data.softmax_params.input_multiplier,
                       op_data.softmax_params.input_left_shift,
                       op_data.softmax_params.diff_min,
                       tflite::micro::GetTensorData<int8_t>(output));
      } else {
        arm_softmax_s8_s16(tflite::micro::GetTensorData<int8_t>(input),
                           op_data.num_rows, op_data.row_size,
                           op_data.softmax_params.input_multiplier,
                           op_data.softmax_params.input_left_shift,
                           op_data.softmax_params.diff_min,
                           tflite::micro::GetTensorData<int16_t>(output));
      }
      return kTfLiteOk;
    }
```
