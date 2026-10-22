---
id: "tflm-porting-reference-ops-from-lite-to-can-i-use-malloc-free-or-new-delete-in-m"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: Can I use malloc/free or new/delete in my operator code?"
summary: "No. All memory allocation in TensorFlow Lite Micro (TFLM) is done using C++ stack based automatic allocation, or through specialized TFLM persistent and temporary allocation methods. The only use of new in TFLM is through the use of placement new."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/porting_reference_ops.md#can-i-use-malloc-free-or-new-delete-in-my-operator-code"
license: "Apache-2.0"
mode: "V"
---

No.  All memory allocation in TensorFlow Lite Micro (TFLM) is done using C++
stack based automatic allocation, or through specialized TFLM persistent
and temporary allocation methods. The only use of `new` in TFLM is through the
use of [placement new](https://en.cppreference.com/w/cpp/language/new.html#Placement_new).
