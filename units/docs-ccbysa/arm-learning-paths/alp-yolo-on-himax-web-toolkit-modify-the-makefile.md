---
id: "alp-yolo-on-himax-web-toolkit-modify-the-makefile"
type: "concept"
domain: "edge-ai"
title: "Run a computer vision model on a Himax microcontroller: Run additional models in the web toolkit: Modify the makefile"
summary: "Change to the directory where the makefile is located."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/yolo-on-himax/web-toolkit.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/yolo-on-himax/web-toolkit/#modify-the-makefile"
license: "CC-BY-SA-4.0"
mode: "V"
---

Change to the directory where the `makefile` is located. 

```bash
cd $HOME/Seeed_Grove_Vision_AI_Module_V2/EPII_CM55M_APP_S/
```

The table shows the different options available to use with the web toolkit. 

Use a text editor to open `makefile` and modify the `APP_TYPE` field to one of the values in the table. 

You will use the model argument value with the `--model` option to the `xmodem` command.

|APP_TYPE           |Description        | Model argument |
|---                |---                |---
|tflm_yolov8_od     |Object detection   | model_zoo\tflm_yolov8_od\yolov8n_od_192_delete_transpose_0xB7B000.tflite 0xB7B000 0x00000 |
|tflm_fd_fm         |Face detection     | model_zoo\tflm_fd_fm\0_fd_0x200000.tflite 0x200000 0x00000 model_zoo\tflm_fd_fm\1_fm_0x280000.tflite 0x280000 0x00000 model_zoo\tflm_fd_fm\2_il_0x32A000.tflite 0x32A000 0x00000 |

**Note:**
For `tflm_fd_fm`, you need to pass all three models as separate `--model` arguments.
