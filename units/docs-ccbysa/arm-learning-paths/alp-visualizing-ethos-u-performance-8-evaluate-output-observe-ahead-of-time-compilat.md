---
id: "alp-visualizing-ethos-u-performance-8-evaluate-output-observe-ahead-of-time-compilat"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Evaluate Ethos-U Performance: Observe Ahead-of-Time Compilation"
summary: "In the examples below, /path/to/executorch represents the directory where you cloned your local copy of the ExecuTorch repo. Replace it with your actual path when running commands or reviewing output."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/8-evaluate-output.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/8-evaluate-output/#observe-ahead-of-time-compilation"
license: "CC-BY-SA-4.0"
mode: "V"
---

- The following output from [run.sh](https://github.com/pytorch/executorch/blob/main/examples/arm/run.sh) confirms that Ahead-of-Time (AOT) compilation was successful.
- Specifically you want to confirm that the original PyTorch model was compiled into an ExecuTorch `.pte` file
- For the MobileNet V2 example, the compiled ExecuTorch file will be output as `mv2_arm_delegate_ethos-u85-128.pte`

**Note:**

In the examples below, `/path/to/executorch` represents the directory where you cloned your local copy of the [ExecuTorch repo](https://github.com/pytorch/executorch/tree/main). Replace it with your actual path when running commands or reviewing output.



**Ahead-of-Time Compiler Start:**
```bash { output_lines = "1-4" }
--------------------------------------------------------------------------------
Running e2e flow for model 'mv2' with flags '--delegate --quantize --delegate --quantize --intermediates mv2_u85/ --debug --evaluate'
--------------------------------------------------------------------------------
CALL python3 -m examples.arm.aot_arm_compiler --model_name=mv2 --target=ethos-u85-128 --delegate --quantize --delegate --quantize --intermediates mv2_u85/ --debug --evaluate --intermediate=/path/to/executorch/mv2_u85 --output=/path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte --system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Sram_Only
```

**.pte File Build Completion:**
```bash { output_lines = "1-3" }
PTE file saved as /path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte
pte_data_size:  3809584 /path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte
pte_file: /path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte
```

**Ethos-U Delegate Build Start:**
```bash{ output_lines = "1-5" }
+ backends/arm/scripts/build_executor_runner.sh --et_build_root=/path/to/executorch/arm_test --pte=/path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte --build_type=Release --target=ethos-u85-128 --system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Sram_Only --extra_build_flags= --ethosu_tools_dir=/path/to/executorch/examples/arm/ethos-u-scratch
--------------------------------------------------------------------------------
Build Arm Baremetal executor_runner for ethos-u85-128 with /path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte using Ethos_U85_SYS_DRAM_Mid Sram_Only  to '/path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128/cmake-out'
--------------------------------------------------------------------------------
```

**Ethos-U Delegate Build Completion:**
```bash { output_lines = "1" }
[100%] Built target arm_executor_runner
```
