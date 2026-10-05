---
id: "alp-yolo-on-himax-build-firmware-generate-the-firmware-image"
type: "concept"
domain: "edge-ai"
title: "Run a computer vision model on a Himax microcontroller: Build the firmware: Generate the firmware image"
summary: "The examples repository contains scripts to generate the image file."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/yolo-on-himax/build-firmware.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/yolo-on-himax/build-firmware/#generate-the-firmware-image"
license: "CC-BY-SA-4.0"
mode: "V"
---

The examples repository contains scripts to generate the image file. 

Copy the `.elf` file to the `input_case1_secboot` directory:

```bash
cd ../we2_image_gen_local/
cp ../EPII_CM55M_APP_S/obj_epii_evb_icv30_bdv10/gnu_epii_evb_WLCSP65/EPII_CM55M_gnu_epii_evb_WLCSP65_s.elf input_case1_secboot/
```

Run the script on your OS as shown below. This creates a file named `output.img` in the `output_case1_sec_wlcsp` directory:



  **Linux:**
./we2_local_image_gen project_case1_blp_wlcsp.json
  
  **macOS:**
./we2_local_image_gen_macOS_arm64 project_case1_blp_wlcsp.json
  


The script output ends with the following:

```output
Output image: output_case1_sec_wlcsp/output.img
Output image: output_case1_sec_wlcsp/output.img

IMAGE GEN DONE
```

You are now ready to flash the image onto the Himax development board.
