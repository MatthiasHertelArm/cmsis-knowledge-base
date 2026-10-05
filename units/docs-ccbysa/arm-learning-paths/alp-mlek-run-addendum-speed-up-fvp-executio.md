---
id: "alp-mlek-run-addendum-speed-up-fvp-executio"
type: "concept"
domain: "edge-ai"
title: "Build and run the Arm Machine Learning Evaluation Kit examples: Run the examples on the FVP: Addendum: Speed up FVP execution"
summary: "By default, the examples are built with Ethos-U timing enabled. This provides benchmarking information, but the result is that the FVP executes relatively slowly."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/mlek/run.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/mlek/run/#addendum-speed-up-fvp-execution"
license: "CC-BY-SA-4.0"
mode: "V"
---

By default, the examples are built with Ethos-U timing enabled. This provides benchmarking information, but the result is that the FVP executes relatively slowly.

The build system has a macro `-DETHOS_U_NPU_TIMING_ADAPTER_ENABLED` defined to control this.

Modify the command `build_default.py` passes to `cmake` to include this setting (`OFF`). Search for `cmake_command` and modify as follows:

#### build_default.py
```
cmake_command = (
    f"{cmake_path} -B {build_dir} -DTARGET_PLATFORM={target_platform}"
    f" -DTARGET_SUBSYSTEM={target_subsystem}"
    f" -DCMAKE_TOOLCHAIN_FILE={cmake_toolchain_file}"
    f" -DETHOS_U_NPU_ID={ethos_u_cfg.processor_id}"
    f" -DETHOS_U_NPU_CONFIG_ID={ethos_u_cfg.config_id}"
    " -DTENSORFLOW_LITE_MICRO_CLEAN_DOWNLOADS=ON"
    " -DETHOS_U_NPU_TIMING_ADAPTER_ENABLED=OFF"
)
```

Rebuild the applications as before, for example:
```
./build_default.py --npu-config-name ethos-u85-256 --toolchain gnu --make-jobs 8
```

Add additional configuration option (`mps4_board.subsystem.ethosu.extra_args`) to the FVP command line:

#### config.txt
```
mps4_board.subsystem.ethosu.num_macs=256
mps4_board.visualisation.disable-visualisation=1
vis_hdlcd.disable_visualisation=1
mps4_board.subsystem.ethosu.extra_args="--fast"
```

Run the application again, and notice how much faster execution completes.

```console
FVP_Corstone_SSE-320 -f config.txt -a ethos-u-kws.axf
```

**Note:**
Do not use fast execution mode whilst benchmarking performance.
