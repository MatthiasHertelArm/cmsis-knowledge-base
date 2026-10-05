---
id: "alp-yolo-on-himax-flash-and-run-find-the-com-port"
type: "concept"
domain: "edge-ai"
title: "Run a computer vision model on a Himax microcontroller: Flash firmware onto the microcontroller: Find the COM port"
summary: "To flash the image, you need to provide the communication port (COM) which the board is connected to."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/yolo-on-himax/flash-and-run.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/yolo-on-himax/flash-and-run/#find-the-com-port"
license: "CC-BY-SA-4.0"
mode: "V"
---

To flash the image, you need to provide the communication port (COM) which the board is connected to. 

On your machine, you can find commands that you can use to list all COMs available to use. Once your board is connected through USB, it will appear on this list of available COMs. 

The COM identifier is prefixed with **tty**, so you can use this to help you identify which COM it is. You can also run the command before and after plugging in the board if you are unsure, and look for the change in the list.



  **Linux:**
sudo grep -i 'tty' /var/log/dmesg
  
  **macOS:**
ls /dev/tty.*
  



**Note:**
If the port appears to be unavailable, try changing the permissions temporarily using the `chmod` command. Be sure to reset the permissions again afterwards, as otherwise this can pose a computer security vulnerability.

```bash
chmod 0777 <COM port>
```


You will require the full path to the port in the next step, so be sure to save it.
