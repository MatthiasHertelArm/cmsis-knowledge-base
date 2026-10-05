---
id: "alp-yolo-on-himax-flash-and-run-flash-the-firmware-onto-the-mo"
type: "concept"
domain: "edge-ai"
title: "Run a computer vision model on a Himax microcontroller: Flash firmware onto the microcontroller: Flash the firmware onto the module"
summary: "Run the python script below to flash the firmware:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/yolo-on-himax/flash-and-run.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/yolo-on-himax/flash-and-run/#flash-the-firmware-onto-the-module"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the python script below to flash the firmware:

```bash
python xmodem\xmodem_send.py --port=<COM port> \
--baudrate=921600 --protocol=xmodem \
--file=we2_image_gen_local\output_case1_sec_wlcsp\output.img
```

**Note:**
When you run other example models demonstrated in the later section [Run additional models in the web toolkit](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/yolo-on-himax/web-toolkit/), you need to adapt this command with `--model` argument.


After the firmware image flashing is completed, the message `Do you want to end file transmission and reboot system? (y)` is displayed. Press the reset button shown in the image below.

(figure: reset button)
