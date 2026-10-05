---
id: "alp-visualizing-ethos-u-performance-7-configure-fvp-gui-deploy-the-model"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Enable GUI and deploy a model on Corstone-320 FVP: Deploy the model"
summary: "Now run the Mobilenet V2 computer vision model, using executorch/examples/arm/run.sh:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/7-configure-fvp-gui.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/7-configure-fvp-gui/#deploy-the-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now run the Mobilenet V2 computer vision model, using [executorch/examples/arm/run.sh](https://github.com/pytorch/executorch/blob/main/examples/arm/run.sh):
```bash
./examples/arm/run.sh \
--aot_arm_compiler_flags="--delegate --quantize --intermediates mv2_u85/ --debug --evaluate" \
--output=mv2_u85 \
--target=ethos-u85-128 \
--model_name=mv2
```

Observe that the FVP loads the model file, compiles the PyTorch model to ExecuTorch `.pte` format and then shows an instruction count in the top right of the GUI:

(figure: Terminal and FVP output#center)

**Note:**

For macOS users, follow these instructions:

- Start Docker. FVPs run inside a Docker container. 
- Make sure to use an [official version of Docker](https://www.docker.com/products/docker-desktop/) and not a free version like the [Colima](https://github.com/abiosoft/colima?tab=readme-ov-file) Docker container runtime
 - `run.sh` assumes Docker Desktop style networking (`host.docker.internal`) which breaks with Colima
  - Colima then breaks the FVP GUI

- **Start XQuartz:** on macOS, the FVP GUI runs using XQuartz.

  Start the xquartz.app and then configure XQuartz so that the FVP will accept connections from your Mac and localhost:
  ```bash
  xhost + <YOUR_IP_ADDRESS>
  xhost + 127.0.0.1 # The Docker container seems to proxy through localhost
  ```
