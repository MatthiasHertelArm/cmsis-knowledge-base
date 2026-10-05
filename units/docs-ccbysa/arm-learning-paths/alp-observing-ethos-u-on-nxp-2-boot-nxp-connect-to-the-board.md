---
id: "alp-observing-ethos-u-on-nxp-2-boot-nxp-connect-to-the-board"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Boot the NXP FRDM i.MX 93 board: Connect to the board"
summary: "This section walks through powering on the board and establishing a serial console connection. If your board is already running Linux and you can log in, skip ahead to the next section."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/2-boot-nxp.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/2-boot-nxp/#connect-to-the-board"
license: "CC-BY-SA-4.0"
mode: "V"
---

This section walks through powering on the board and establishing a serial console connection. If your board is already running Linux and you can log in, skip ahead to the next section.

You need a serial terminal to see the boot console and log in.

**macOS:**
On macOS as your host, you'll need the following set up before getting started: 

- Install the [Silicon Labs USB-to-UART driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads)
- Install [picocom](https://github.com/npat-efault/picocom)
   ```bash
   brew install picocom
   ```


Connect the board's **DEBUG** USB-C connector to your host machine.

Find the board's serial device:

   ```bash { output_lines = "2-5" }
   ls /dev/tty.*
   ...
   /dev/tty.usbmodem<SERIAL_ID_1>
   /dev/tty.usbmodem<SERIAL_ID_2>
   ...
   ```

   The exact device names vary per board. Look for entries containing `usbmodem`.

Open a serial connection using the first `usbmodem` device:

   ```bash { output_lines = "2-4" }
   sudo picocom -b 115200 /dev/tty.usbmodem<SERIAL_ID_1>
   picocom v3.1
   ...
   Terminal ready
   ```

Connect the board's **POWER** USB-C connector to your host machine. You should see a red and a white LED on the board.

Wait for the boot log to scroll past in the picocom window. When it finishes, you'll see a login prompt:

   ```output
   NXP i.MX Release Distro 6.6-scarthgap imx93frdm ttyLP0

   imx93frdm login:
   ```

**Tip:**
If you miss the login prompt, hold the board's power button for two seconds to power off, then press it again to reboot.
