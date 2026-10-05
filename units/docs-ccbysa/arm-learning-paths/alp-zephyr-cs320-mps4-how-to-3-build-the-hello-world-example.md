---
id: "alp-zephyr-cs320-mps4-how-to-3-build-the-hello-world-example"
type: "concept"
domain: "rtos"
title: "Port Zephyr RTOS and run applications on the Arm Corstone-320 MPS4 platform: Build and run the hello_world sample on Arm Corstone-320 MPS4: Build the hello_worl"
summary: "The Zephyr hello_world example prints \"Hello World\" to the console. Use it to validate that your board support and toolchain configuration work correctly."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/how-to-3.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/how-to-3/#build-the-hello-world-example-for-mps4"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Zephyr `hello_world` example prints "Hello World" to the console. Use it to validate that your board support and toolchain configuration work correctly.

Activate your Python virtual environment:

```bash
source ~/zephyrproject/.venv/bin/activate
```

If you haven't set the toolchain environment variables in your current terminal, set them now. For full setup steps, see [Set up the Zephyr build environment](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/how-to-1/):

```bash
export ZEPHYR_TOOLCHAIN_VARIANT=gnuarmemb
export GNUARMEMB_TOOLCHAIN_PATH=$HOME/arm-gnu-toolchain-13.2.Rel1-aarch64-arm-none-eabi
```

Replace the path with the path to your toolchain directory. On x86_64, the directory name starts with `x86_64` instead of `aarch64`.

From the `~/zephyrproject/zephyr` directory, build the `hello_world` example for the Corstone-320 FPGA variant:

```bash
west build -p always -b mps4/corstone320/fpga zephyr/samples/hello_world -- -DCONFIG_ROMSTART_RELOCATION_ROM=y
```

The output is similar to:

```output
[xxx/xxx] Linking C executable zephyr/zephyr.elf
Memory region         Used Size  Region Size  %age Used
 ROMSTART_REGION:         xxx B       128 KB      x.xx%
           FLASH:       xxxxx B         4 MB      x.xx%
             RAM:        xxxx B         2 MB      x.xx%
```

Verify that the ELF image was created:

```bash
ls build/zephyr/zephyr.elf
```

The output is similar to:

```output
build/zephyr/zephyr.elf
```

The ELF image contains the application and the Zephyr kernel libraries. You can now load it onto the MPS4 board.
