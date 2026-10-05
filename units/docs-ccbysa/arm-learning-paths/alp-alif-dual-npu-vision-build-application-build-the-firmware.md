---
id: "alp-alif-dual-npu-vision-build-application-build-the-firmware"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Build the dual-NPU application: Build the firmware"
summary: "A successful build ends with messages showing that Zephyr linked the ELF file and generated the binary."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/build-application.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/build-application/#build-the-firmware"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the complete build command:

```bash
west build \
  -b alif_e8_dk/ae822fa0e5597xx0/rtss_hp \
  -d build-dual-npu-vision \
  "$APP" --pristine -- \
  -DZEPHYR_MODULES="$MODULES" \
  -DPYTHON_EXECUTABLE="$PWD/.venv-executorch/bin/python" \
  -DPython3_EXECUTABLE="$PWD/.venv-executorch/bin/python" \
  -DCMSIS_NN_LOCAL_PATH="$PWD/modules/cmsis-nn-src" \
  -DDTC_OVERLAY_FILE="$APP/boards/dual_npu_e8.overlay;$OD/boards/alif_e8_dk_ae822fa0e5597xx0_rtss_hp.overlay;$OD/serial_camera.overlay;$OD/serial_camera_mt9m114.overlay;$OD/serial_camera_isp.overlay;$OD/serial_camera_mt9m114_isp.overlay;$APP/isp_route.overlay" \
  -DOVERLAY_CONFIG="$APP/vision.conf"
```

A successful build ends with messages showing that Zephyr linked the ELF file and generated the binary.

Confirm that the three expected outputs exist:

```bash
ls -lh build-dual-npu-vision/zephyr/zephyr.bin \
  build-dual-npu-vision/zephyr/zephyr.elf \
  build-dual-npu-vision/model_assets.bin
```

The files have the following roles:

| File | Purpose |
| --- | --- |
| `zephyr.bin` | Cortex-M55 Zephyr application |
| `zephyr.elf` | Symbols and debug information |
| `model_assets.bin` | U85 PTE, U55 PTE, startup image, and ImageNet labels |

You can use the checked-in PTE files to build and flash the application without installing TensorFlow, TOSA Tools, or Vela. CMake packages those files directly into `model_assets.bin`.

**Note:**
If model preparation reports an allocation failure, the PTE files don't match the memory-pool sizes in the checked-out sample. Confirm that the workspace is at the validated SDK revision and run a pristine build.

If you regenerated the PTE files, use the supplied scripts, model inputs, and `ensemble_vela.ini` file.
