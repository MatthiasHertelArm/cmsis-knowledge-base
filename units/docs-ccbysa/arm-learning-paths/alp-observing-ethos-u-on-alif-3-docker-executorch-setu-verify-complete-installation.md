---
id: "alp-observing-ethos-u-on-alif-3-docker-executorch-setu-verify-complete-installation"
type: "concept"
domain: "edge-ai"
title: "3 docker executorch setup: Verify complete installation"
summary: "3. Then, run a minimal export test to verify the complete setup:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup/#verify-complete-installation"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run all verification checks:

<!-- Check Arm GCC Toolchain

```bash
arm-none-eabi-gcc --version
```

Expected output:
```output
arm-none-eabi-gcc (Arm GNU Toolchain 13.3.Rel1 (Build arm-13.24)) 13.3.1 20240614
Copyright (C) 2023 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
``` -->

1. Check Vela compiler

    ```bash
    vela --version
    ```

    The output is similar to:

    ```output
    4.4.1
    ```
2. Check ExecuTorch:

    ```bash
    python3 -c "from executorch.exir import to_edge; print('ExecuTorch OK')"
    ```

    The output is similar to:

    ```output
    ExecuTorch OK
    ```

3. Then, run a minimal export test to verify the complete setup:

    ```bash
    cd $ET_HOME
    python3 -m examples.arm.aot_arm_compiler --model_name=add --delegate --quantize   --target=ethos-u85-256 --output=/home/developer/output/add_ethos_u85.pte
    ```

    The output is similar to:

    ```output
    Exporting model add...
    Lowering to TOSA...
    Compiling with Vela...
    PTE file saved as add_ethos_u85.pte
    ```

    Verify the `.pte` file was created:

    ```bash
    ls -lh /home/developer/output/add_ethos_u85.pte
    ```

    The `output` directory is mounted from your host machine, so the file is also available at `~/mnist_alif/executorch-alif/output/`.
