---
id: "alp-introduction-to-tinyml-on-arm-4-build-model-run-the-model-on-the-corstone"
type: "concept"
domain: "edge-ai"
title: "Introduction to TinyML on Arm using PyTorch and ExecuTorch: Build a simple PyTorch model: Run the model on the Corstone-320 FVP"
summary: "The final step is to take the Python-defined model and run it on the Corstone-320 FVP. This was done upon running the run.sh script in a previous section."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/4-build-model.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/4-build-model/#run-the-model-on-the-corstone-320-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

The final step is to take the Python-defined model and run it on the Corstone-320 FVP. This was done upon running the `run.sh` script in a previous section. To wrap up the Learning Path, you will perform these steps separately to better understand what happened under the hood. Start by setting some environment variables that are used by ExecuTorch.

```bash
export ET_HOME=$HOME/executorch
export executorch_DIR=$ET_HOME/build
```

Generate a model in ExecuTorch `.pte` format using the Arm examples. The AoT Arm compiler enables optimizations for devices such as the Grove Vision AI Module V2 and the Corstone-320 FVP. Run the compiler from the ExecuTorch root directory:

```bash
cd $ET_HOME
python -m examples.arm.aot_arm_compiler --model_name=examples/arm/simple_nn.py --delegate --quantize --target=ethos-u85-256 --system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Sram_Only
```

From the Arm Examples directory, you can build an embedded Arm runner with the `.pte` included. This allows you to optimize the performance of your model, and ensures compatibility with the CPU kernels on the FVP. Finally, build the ExecuTorch libraries and generate the executable `arm_executor_runner`.

```bash
cmake -S "${ET_HOME}" \
      -B "${executorch_DIR}" \
      --preset arm-baremetal \
      -DCMAKE_BUILD_TYPE=Release

cmake --build "$executorch_DIR" --target install --parallel

cd $HOME/executorch/examples/arm/executor_runner

cmake -S "${ET_HOME}/examples/arm/executor_runner" \
      -B "${ET_HOME}/examples/arm/executor_runner/cmake-out" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_TOOLCHAIN_FILE=$ET_HOME/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake \
      -DTARGET_CPU=cortex-m85 \
      -DET_PTE_FILE_PATH:PATH=$ET_HOME/simple_nn_arm_delegate_ethos-u85-256.pte \
      -DETHOS_SDK_PATH:PATH=$ET_HOME/examples/arm/ethos-u-scratch/ethos-u \
      -DETHOSU_TARGET_NPU_CONFIG=ethos-u85-256 \
      -DPYTHON_EXECUTABLE=$HOME/executorch-venv/bin/python3 \
      -DSYSTEM_CONFIG=Ethos_U85_SYS_DRAM_Mid \

cmake --build $ET_HOME/examples/arm/executor_runner/cmake-out --parallel -- arm_executor_runner

```

Run the model on Corstone-320:

```bash
FVP_Corstone_SSE-320 \
-C mps4_board.subsystem.ethosu.num_macs=256 \
-C mps4_board.visualisation.disable-visualisation=1 \
-C vis_hdlcd.disable_visualisation=1                \
-C mps4_board.telnetterminal0.start_telnet=0        \
-C mps4_board.uart0.out_file='-'                    \
-C mps4_board.uart0.shutdown_on_eot=1               \
-a "$ET_HOME/examples/arm/executor_runner/cmake-out/arm_executor_runner"
```

**Note:**
The argument `mps4_board.visualisation.disable-visualisation=1` disables the FVP GUI and can speed up launch time


Observe that the FVP loads the model file.
```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003
I [executorch:arm_executor_runner.cpp:412] Model in 0x70000000 $
I [executorch:arm_executor_runner.cpp:414] Model PTE file loaded. Size: 3360 bytes.
```

You have now set up your environment for TinyML development on Arm and tested a small PyTorch model with ExecuTorch on the Corstone-320 FVP. In the next Learning Path, you learn how to optimize neural networks to run efficiently on Arm.
