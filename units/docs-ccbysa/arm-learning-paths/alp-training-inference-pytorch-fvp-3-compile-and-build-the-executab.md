---
id: "alp-training-inference-pytorch-fvp-3-compile-and-build-the-executab"
type: "concept"
domain: "edge-ai"
title: "Edge AI on Arm: PyTorch and ExecuTorch rock-paper-scissors: Run the model on Corstone-320 FVP: Compile and build the executable"
summary: "Use the Ahead-of-Time (AoT) Arm compiler to convert your PyTorch model to an ExecuTorch program optimized for Arm and the Ethos-U NPU. This process (delegation) offloads supported parts of the neural network to the NPU for efficient inference."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/training-inference-pytorch/fvp-3.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/training-inference-pytorch/fvp-3/#compile-and-build-the-executable"
license: "CC-BY-SA-4.0"
mode: "V"
---

Use the Ahead-of-Time (AoT) Arm compiler to convert your PyTorch model to an ExecuTorch program optimized for Arm and the Ethos-U NPU. This process (delegation) offloads supported parts of the neural network to the NPU for efficient inference.

Set up environment variables:

```bash
export ET_HOME=$HOME/executorch
export executorch_DIR=$ET_HOME/build
```

Use the AOT Arm compiler to generate the optimized `.pte` file. This command delegates the model to the Ethos-U85 NPU, applies quantization to reduce model size and improve performance, and specifies the memory configuration. Run it from the ExecuTorch root directory.

```bash
cd $ET_HOME
python -m examples.arm.aot_arm_compiler --model_name=examples/arm/rps_tiny.py \
--delegate --quantize --target=ethos-u85-128 \
--system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Dedicated_Sram
```

You should see:

```output
PTE file saved as rps_tiny_arm_delegate_ethos-u85-128.pte
```

Next, build the Ethos-U runner - a bare-metal executable that includes the ExecuTorch runtime and your compiled model. Configure the build with CMake:

```bash
cd $HOME/executorch/examples/arm/executor_runner

cmake -DCMAKE_BUILD_TYPE=Release \
      -S "$ET_HOME/examples/arm/executor_runner" \
      -B "$ET_HOME/examples/arm/executor_runner/cmake-out" \
      -DCMAKE_TOOLCHAIN_FILE="$ET_HOME/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake" \
      -DTARGET_CPU=cortex-m85 \
      -DET_DIR_PATH="$ET_HOME" \
      -DET_BUILD_DIR_PATH="$ET_HOME/arm_test/cmake-out" \
      -DET_PTE_FILE_PATH="$ET_HOME/rps_tiny_arm_delegate_ethos-u85-128.pte" \
      -DETHOS_SDK_PATH="$ET_HOME/examples/arm/ethos-u-scratch/ethos-u" \
      -DETHOSU_TARGET_NPU_CONFIG=ethos-u85-128 \
      -DSYSTEM_CONFIG=Ethos_U85_SYS_DRAM_Mid
```

You should see configuration output similar to:

```bash
-- *******************************************************
-- PROJECT_NAME                           : ethos-u-corstone-320
-- TR_ARENA_SIZE                          :
-- MESSAGE_HANDLER_ARENA_SIZE             :
-- *******************************************************
-- ET_ARM_BAREMETAL_SCRATCH_TEMP_ALLOCATOR_POOL_SIZE = 0x200000
-- ET_ARM_BAREMETAL_FAST_SCRATCH_TEMP_ALLOCATOR_POOL_SIZE =
-- Configuring done (17.1s)
-- Generating done (0.2s)
-- Build files have been written to: ~/executorch/examples/arm/executor_runner/cmake-out
```

Build the executable:

```bash
cmake --build "$ET_HOME/examples/arm/executor_runner/cmake-out" -j --target arm_executor_runner
```
