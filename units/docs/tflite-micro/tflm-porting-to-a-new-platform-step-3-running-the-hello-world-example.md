---
id: "tflm-porting-to-a-new-platform-step-3-running-the-hello-world-example"
type: "concept"
domain: "edge-ai"
title: "Porting to a new platform: Step 3: Running the hello\\_world Example"
summary: "Once you have completed step 2, you should be set up to run the hello_world example and see the output over the UART."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/new_platform_support.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/new_platform_support.md#step-3-running-the-hello-world-example"
license: "Apache-2.0"
mode: "V"
---

Once you have completed step 2, you should be set up to run the `hello_world`
example and see the output over the UART.

```
cp -r /tmp/tflm-tree/examples/hello_world <path-to-platform-specific-hello-world>
```
The `hello_world` example should not need any customization and you should be
able to directly build and run it.
