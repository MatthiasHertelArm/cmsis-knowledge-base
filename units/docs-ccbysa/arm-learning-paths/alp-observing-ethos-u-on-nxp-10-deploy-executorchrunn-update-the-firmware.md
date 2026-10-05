---
id: "alp-observing-ethos-u-on-nxp-10-deploy-executorchrunn-update-the-firmware"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Deploy and test on FRDM-IMX93: Update the firmware"
summary: "To deploy a new version of the firmware:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board/#update-the-firmware"
license: "CC-BY-SA-4.0"
mode: "V"
---

To deploy a new version of the firmware:

1. Build the updated firmware on your development machine
2. Copy to the board:

```bash
scp debug/executorch_runner_cm33.elf root@<board-ip>:/lib/firmware/
```

3. Re-run inference on the board:

```bash { command_line="root@frdm-imx93" }
echo stop > /sys/class/remoteproc/remoteproc0/state
sleep 2
echo start > /sys/class/remoteproc/remoteproc0/state
sleep 15
cat /sys/kernel/debug/remoteproc/remoteproc0/trace0
```

**Troubleshooting:**
**RemoteProc fails to load firmware:**

Check that the file exists and has correct permissions:

```bash { command_line="root@frdm-imx93" }
ls -la /lib/firmware/executorch_runner_cm33.elf
chmod 644 /lib/firmware/executorch_runner_cm33.elf
```

**`Program identifier '' != expected 'ET12'`:**

The `.pte` model is not present at DDR address `0xC0000000`. Reload the model using the `/dev/mem` method or via U-Boot.

**Firmware hangs (no trace output):**

Verify the Ethos-U kernel driver is loaded:

```bash { command_line="root@frdm-imx93" }
ls /dev/ethosu*
dmesg | grep ethosu
```

If `/dev/ethosu0` does not exist, the NPU is not powered and the firmware cannot initialize it.

**Memory allocation failed for planned buffer:**

This occurs when a large model's activation tensors exceed the DTCM method allocator. The firmware automatically uses DDR for models that need more than 12KB of planned buffers. If you see this error, verify the `ethosu_region@A8000000` (128MB) is reserved in the device tree.

**BUS FAULT or vtable corruption:**

The SDK linker script patch has not been applied. Run the patch script and rebuild:

```bash
./patches/apply_patches.sh
cmake --preset debug
cmake --build debug
```

**Firmware crashes after NPU init:**

Check kernel logs:

```bash { command_line="root@frdm-imx93" }
dmesg | grep -i error | tail
```

This might indicate memory configuration issues. Verify that both DDR regions (`0xC0000000`--`0xC03FFFFF` and `0xA8000000`--`0xAFFFFFFF`) are reserved in the device tree.
