---
id: "tflm-porting-reference-ops-from-lite-to-can-i-use-global-static-variable-constru"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: Can I use global/static variable constructors in my operator code?"
summary: "Global constructors are not allowed. This is due to the call ordering of C++ global constructors being platform/compiler dependent. Some platforms do not support global constructors at all, and will silently fail."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/porting_reference_ops.md#can-i-use-global-static-variable-constructors-in-my-operator-code"
license: "Apache-2.0"
mode: "V"
---

Global constructors are not allowed. This is due to the call ordering of C++
global constructors being platform/compiler dependent.  Some platforms do not
support global constructors at all, and will silently fail.

Static variables that use constructors are safe to declare within methods.  This
is because the static variable executes its call-once sequence only when the
encapsulating method is called.
