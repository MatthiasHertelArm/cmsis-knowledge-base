---
id: "tflm-error-handling-defensive-programmi"
type: "concept"
domain: "edge-ai"
title: "Error Handling & Defensive Programming Guide"
summary: "Balancing defensiveness with the extreme constraints of microcontrollers (where every byte of Flash/RAM and every clock cycle matters) is a core design tension in TFLM."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/error_handling_guide.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/error_handling_guide.md"
license: "Apache-2.0"
mode: "V"
---

Balancing defensiveness with the extreme constraints of microcontrollers (where
every byte of Flash/RAM and every clock cycle matters) is a core design tension
in TFLM. Since TFLM targets environments that often lack memory protection (no
MMU), don't support C++ exceptions, and run on bare metal or simple RTOSs, a
"standard" defensive posture would result in unacceptable binary bloat and
performance degradation.

This guide provides an architectural framework for writing safe kernels and
offers recommendations for code reviews for contributors.

--------------------------------------------------------------------------------
