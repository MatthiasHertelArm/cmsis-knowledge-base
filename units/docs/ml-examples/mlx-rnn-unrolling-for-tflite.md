---
id: "mlx-rnn-unrolling-for-tflite"
type: "concept"
domain: "edge-ai"
title: "RNN unrolling for TFLite"
summary: "This repository contains a Jupyter notebook that will demonstrate how to train a Recurrent Neural Network (RNN) in TensorFlow and then prepare it for exporting to TensorFlow Lite format by unrolling it."
status: "draft"
collection: "ml-examples"
source: "ARM-software/ML-examples@0e45384:rnn-unrolling-tflite/README.md"
doc_source: "https://github.com/ARM-software/ML-examples/blob/0e45384/rnn-unrolling-tflite/README.md"
license: "Apache-2.0"
mode: "V"
---

This repository contains a Jupyter notebook that will demonstrate how to train a Recurrent Neural Network (RNN) in TensorFlow and then prepare it for exporting to [TensorFlow Lite](https://www.tensorflow.org/lite) format by unrolling it.

It also shows how to quantize your unrolled model so that it is ready to be optimized by [Vela](https://pypi.org/project/ethos-u-vela/) in order for the model to be deployed onto [Arm Ethos-U55](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u55) or [Arm Ethos-U65](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65) NPU.
