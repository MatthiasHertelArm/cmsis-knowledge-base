---
id: "alp-deploy-ml-model-to-npu-with-topo-deploy-open-the-web-application"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Clone and deploy the application with Topo: Open the web applicati"
summary: "(figure: Screenshot of the web interface running on an Arm-based target, showing an image and the model response. This confirms successful deployment and provides a visual reference for the expected result.#center)"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/deploy.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/deploy/#open-the-web-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

Open the web application in a browser:

```
http://<target-ip>:3001
```

**Note:**
If you need to use a different target port, set `WEBAPP_PORT` when deploying. For example:

```bash
WEBAPP_PORT=3002 topo deploy --target <user>@<target-ip>
```

Then open:

```output
http://<target-ip>:3002
```


The application shows:

- an image selector
- a **Classify** button
- board prerequisite checks
- classification results
- an expandable analysis section with runtime details

(figure: Screenshot of the web interface running on an Arm-based target, showing an image and the model response. This confirms successful deployment and provides a visual reference for the expected result.#center)

When you choose an image in the browser and select **Classify**, the web application:

1. Resizes and normalizes the image to classify into an input tensor compatible with the [MobileNetV2](https://arxiv.org/abs/1801.04381) model.
2. Writes the ExecuTorch `.pte` program and input tensor into reserved physical memory.
3. Sends a `RUN` command to the Cortex-M33 runner over `RPMsg`.
4. Waits for the Cortex-M33 firmware to run inference using Ethos-U65 acceleration.
5. Displays the top-1 and top-5 ImageNet classification results in the browser.

Try this out with an image from an ImageNet-supported class.
