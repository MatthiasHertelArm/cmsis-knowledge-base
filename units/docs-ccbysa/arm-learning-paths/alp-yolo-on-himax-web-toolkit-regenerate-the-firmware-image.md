---
id: "alp-yolo-on-himax-web-toolkit-regenerate-the-firmware-image"
type: "concept"
domain: "edge-ai"
title: "Run a computer vision model on a Himax microcontroller: Run additional models in the web toolkit: Regenerate the firmware image"
summary: "Use the same commands from previous section to regenerate the firmware image:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/yolo-on-himax/web-toolkit.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/yolo-on-himax/web-toolkit/#regenerate-the-firmware-image"
license: "CC-BY-SA-4.0"
mode: "V"
---

Use Make to regenerate the `.elf` file.

```bash
make clean
make
```

Use the same commands from previous section to regenerate the firmware image:

```bash
cd ../we2_image_gen_local/
cp ../EPII_CM55M_APP_S/obj_epii_evb_icv30_bdv10/gnu_epii_evb_WLCSP65/EPII_CM55M_gnu_epii_evb_WLCSP65_s.elf input_case1_secboot/
```

Run the script corresponding to the OS of your host machine.


  **Linux:**
./we2_local_image_gen project_case1_blp_wlcsp.json
  
  **macOS:**
./we2_local_image_gen_macOS_arm64 project_case1_blp_wlcsp.json
  



Finally, use `xmodem` to flash the image.

```bash
python xmodem\xmodem_send.py --port=<COM port> \
--baudrate=921600 --protocol=xmodem \
--file=we2_image_gen_local\output_case1_sec_wlcsp\output.img \
--model=<model argument>
```

Press the reset button when prompted before moving on.
