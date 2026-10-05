---
id: "alp-training-inference-pytorch-fvp-3-run-the-model-on-the-fvp"
type: "concept"
domain: "edge-ai"
title: "Edge AI on Arm: PyTorch and ExecuTorch rock-paper-scissors: Run the model on Corstone-320 FVP: Run the model on the FVP"
summary: "With the arm_executor_runner executable ready, you can now run it on the Corstone-320 FVP to see the model on a simulated Arm device."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/training-inference-pytorch/fvp-3.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/training-inference-pytorch/fvp-3/#run-the-model-on-the-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

With the `arm_executor_runner` executable ready, you can now run it on the Corstone-320 FVP to see the model on a simulated Arm device.

```bash
FVP_Corstone_SSE-320 \
-C mps4_board.subsystem.ethosu.num_macs=128 \
-C mps4_board.visualisation.disable-visualisation=1 \
-C vis_hdlcd.disable_visualisation=1                \
-C mps4_board.telnetterminal0.start_telnet=0        \
-C mps4_board.uart0.out_file='-'                    \
-C mps4_board.uart0.shutdown_on_eot=1               \
-a "$ET_HOME/examples/arm/executor_runner/cmake-out/arm_executor_runner"
```

**Note:**
`mps4_board.visualisation.disable-visualisation=1` disables the FVP GUI and can reduce launch time


You should see logs indicating that the model file loads and inference begins:

```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003
I [executorch:arm_executor_runner.cpp:489 main()] PTE in 0x70000000 $ Size: 433968 bytes
I [executorch:arm_executor_runner.cpp:514 main()] PTE Model data loaded. Size: 433968 bytes.
I [executorch:arm_executor_runner.cpp:527 main()] Model buffer loaded, has 1 methods
I [executorch:arm_executor_runner.cpp:535 main()] Running method forward
I [executorch:arm_executor_runner.cpp:546 main()] Setup Method allocator pool. Size: 62914560 bytes.
I [executorch:arm_executor_runner.cpp:563 main()] Setting up planned buffer 0, size 3920.
I [executorch:EthosUBackend.cpp:116 init()] data:0x70000070
```

**Note:**
Inference might take longer with a model of this size on the FVP; this does not reflect real device performance.


You have now built, optimized, and deployed a computer vision model on a simulated Arm-based system. In a future Learning Path, you can compare performance and latency before and after optimization and analyze CPU and memory usage during inference for deeper insight into ExecuTorch on edge devices.
