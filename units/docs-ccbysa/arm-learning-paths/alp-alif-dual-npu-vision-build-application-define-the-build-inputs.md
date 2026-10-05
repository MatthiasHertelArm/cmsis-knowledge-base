---
id: "alp-alif-dual-npu-vision-build-application-define-the-build-inputs"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Build the dual-NPU application: Define the build inputs"
summary: "The sample application includes compiled PTE models for Ethos-U55 and Ethos-U85. It also includes a startup image that verifies both inference pipelines before the application starts the live camera."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/build-application.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/build-application/#define-the-build-inputs"
license: "CC-BY-SA-4.0"
mode: "V"
---

The sample application includes compiled PTE models for Ethos-U55 and Ethos-U85. It also includes a startup image that verifies both inference pipelines before the application starts the live camera.

Start by defining build inputs.

From the `west` workspace root, activate the Python environment and define the sample paths:

```bash
cd $HOME/alif-dual-npu
source .venv/bin/activate
APP=$PWD/sdk-alif/samples/modules/executorch/dual_npu_vision
OD=$PWD/sdk-alif/samples/modules/tflite-micro/alif_object_detection
MODULES=$(west list -f '{abspath}' | grep -v '/modules/lib/executorch$' | paste -sd';' -)
MODULES="$MODULES;$PWD/modules/lib/executorch;$PWD/modules/ethos-u-core-driver-src"
```

The overlay order is important. The final `isp_route.overlay` file disables the CPI memory endpoint and routes camera frames exclusively through the image signal processor (ISP).

**Note:**
If the ISP reports that it has no empty video buffer, confirm that `isp_route.overlay` is the final device-tree overlay in the build command. The application circulates five buffers and must return each processed buffer to the ISP queue. Don't remove the ISP configuration fragments from `vision.conf`.
