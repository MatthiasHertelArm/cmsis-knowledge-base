---
id: "alp-zephyr-cs320-mps4-how-to-3-run-the-hello-world-applicatio"
type: "concept"
domain: "rtos"
title: "Port Zephyr RTOS and run applications on the Arm Corstone-320 MPS4 platform: Build and run the hello_world sample on Arm Corstone-320 MPS4: Run the hello_world "
summary: "To run the application on the MPS4 board, follow these steps:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/how-to-3.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/how-to-3/#run-the-hello-world-application-on-the-mps4-board"
license: "CC-BY-SA-4.0"
mode: "V"
---

To run the application on the MPS4 board, follow these steps:

1. Download the board files from [FI101](https://developer.arm.com/downloads/view/FI101?sortBy=availableBy&revision=r1p0-00eac0-2).
2. Set up the MPS4 platform according to the [Using the FI101 on MPS4 board](https://developer.arm.com/documentation/109762/0100/?lang=en).

3. For the hello_world application, place the vector table in the FPGA boot ROM at address `0x11000000`, and place the remaining code and data in SRAM at address `0x31000000`. Use `arm-none-eabi-objcopy` to extract these two regions from `build/zephyr/zephyr.elf`:

```bash
arm-none-eabi-objcopy  -O binary --only-section=rom_start zephyr.elf vector.bin
arm-none-eabi-objcopy  -O binary --remove-section=rom_start zephyr.elf app.bin
```

4. Update `images.txt` under `/MB/HBI0376B/FI101` to load the two images. The paths use the `\SOFTWARE\` folder on the MPS4 SD card, which is where you will copy the binary files:

```text
IMAGE0PORT: 2
IMAGE0ADDRESS: 0x00_1100_0000           ; Address to load into
IMAGE0UPDATE: RAM
IMAGE0FILE: \SOFTWARE\vector.bin        ; Image/data to be loaded

IMAGE1PORT: 1
IMAGE1ADDRESS: 0x31000000               ; Address to load into
IMAGE1UPDATE: RAM
IMAGE1FILE: \SOFTWARE\app.bin           ; Image/data to be loaded
```

5. Copy `vector.bin` and `app.bin` to the `\SOFTWARE\` folder on the MPS4 SD card, then power on the board.
If the setup is correct, the UART console prints the “Hello World” message, similar to the following example:

(figure: UART console output showing "Hello World! arm" from Zephyr running on the Corstone-320 MPS4 board#center)
