---
id: "alp-observing-ethos-u-on-nxp-9-build-executorch-runne-build-the-firmware"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Build Cortex-M33 firmware for ExecuTorch: Build the firmware"
summary: "Build the project from VS Code. In the left sidebar, open Explorer, then in the MCUXpresso Projects view select the build icon next to executorch_runner_cm33."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33/#build-the-firmware"
license: "CC-BY-SA-4.0"
mode: "V"
---

Build the project from VS Code. In the left sidebar, open **Explorer**, then in the MCUXpresso **Projects** view select the build icon next to `executorch_runner_cm33`.

(figure: VS Code explorer showing project structure with build icon in the Projects tab#center)

The build output shows the progress:

```output
[build] Scanning dependencies of target executorch_runner_cm33.elf
[build] [ 25%] Building CXX object source/arm_executor_runner.cpp.obj
[build] [ 50%] Building CXX object source/arm_memory_allocator.cpp.obj
[build] [ 75%] Linking CXX executable executorch_runner_cm33.elf
[build] [100%] Built target executorch_runner_cm33.elf
[build] Build finished with exit code 0
```

Verify the memory usage to ensure the firmware fits in the Cortex-M33:

```output
Memory region         Used Size  Region Size  %age Used
    m_interrupts:        1140 B       1144 B     99.65%
          m_text:      103476 B     129928 B     79.64%
          m_data:       61984 B       108 KB     56.05%
```

The text section uses approximately 80% of the 128KB ITCM, and data uses approximately 56% of the 108KB DTCM.

You now have everything you need to deploy the `.elf` binary on your NXP board.

**Troubleshooting:**
**SDK patches not applied:**

If you see a BUS FAULT during `load_method` or vtable corruption errors, the GOT linker script patch has not been applied. Run:

```bash
./patches/apply_patches.sh
```

Then rebuild the project.

**Region `m_text` overflowed:**

The 128KB ITCM is nearly full. Verify that `CMakeLists.txt` links `libquantized_ops_lib_selective.a` (not the full `libquantized_ops_lib.a`). The selective library registers only the two operators needed for NPU delegation.

**`resolve_operator` error for `quantized_decomposed::*`:**

The quantized operator kernels are not linked. Verify that `CMakeLists.txt` links `libquantized_ops_lib_selective.a` with `--whole-archive` and that `libquantized_kernels.a` and `libkernels_util_all_deps.a` are also listed.
