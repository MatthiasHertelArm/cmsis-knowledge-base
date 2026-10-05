---
id: "alp-alif-dual-npu-vision-flash-application-stage-the-images"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Package and flash the application: Stage the images"
summary: "The Alif boot flow uses a table of contents to load and start each processor image. The sample provides an Alif Security Toolkit (SETOOLS) JSON file that assigns the application and model payload to their validated MRAM addresses."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/flash-application.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/flash-application/#stage-the-images"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Alif boot flow uses a table of contents to load and start each processor image. The sample provides an Alif Security Toolkit (SETOOLS) JSON file that assigns the application and model payload to their validated MRAM addresses.

Set `ALIF_SE_TOOLS_DIR` to your SETOOLS 1.10 application directory. This example uses the macOS package name:

```bash
cd $HOME/alif-dual-npu
export ALIF_SE_TOOLS_DIR=$HOME/Alif/alif_se_toolkit_110/app-release-exec-macos
APP=$PWD/sdk-alif/samples/modules/executorch/dual_npu_vision
```

Confirm that SETOOLS and the support objects referenced by the sample's package configuration are present:

```bash
test -x "$ALIF_SE_TOOLS_DIR/app-gen-toc"
test -x "$ALIF_SE_TOOLS_DIR/app-write-mram"
test -f "$ALIF_SE_TOOLS_DIR/build/config/app-device-config.json"
test -f "$ALIF_SE_TOOLS_DIR/build/images/a32_stub_0.bin"
test -f "$ALIF_SE_TOOLS_DIR/build/images/m55_stub_he.bin"
```

**Note:**
If the display D-PHY doesn't lock, confirm that the board runs SERAM 1.110.0 and that SETOOLS 1.10 generated the package. Rebuild with the full overlay list from [Build the dual-NPU application](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/build-application/).


Each command completes without output when the file is present. Obtain the validated SETOOLS and firmware updates through the [Alif E8 DevKit support page](https://alifsemi.com/support/kits/ensemble-e8devkit/) if any check fails.

Copy the images and package configuration into SETOOLS:

**Warning:**
To avoid an invalid MRAM payload, don't combine `zephyr.bin` and `model_assets.bin` from different builds. If the logs report an invalid MRAM payload, remove the old build output, rebuild with `--pristine`, and copy both newly generated files into SETOOLS before running `app-gen-toc` again.


```bash
cp build-dual-npu-vision/zephyr/zephyr.bin \
  build-dual-npu-vision/model_assets.bin \
  "$ALIF_SE_TOOLS_DIR/build/images/"
cp "$APP/flash/dual-npu-vision.json" \
  "$ALIF_SE_TOOLS_DIR/build/config/"
```
