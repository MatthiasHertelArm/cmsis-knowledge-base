---
id: "alp-zephyr-shell-4-uart-shell-connect-with-a-uart-terminal"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Build and run the Zephyr UART shell on Arm Cortex-M: Connect with a UART terminal"
summary: "After flashing, the board resets and starts running. Open a UART terminal application and connect to the board's serial port over USB."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/4_uart_shell.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/4_uart_shell/#connect-with-a-uart-terminal"
license: "CC-BY-SA-4.0"
mode: "V"
---

After flashing, the board resets and starts running. Open a UART terminal application and connect to the board's serial port over USB.

### Windows with PuTTY

Configure PuTTY with:

- **Connection type**: `Serial`
- **Serial line**: your board's COM port (for example, `COM5`)
- **Speed**: `115200`

After configuring, select **Open** to connect to the UART shell.

(figure: PuTTY configuration window with Connection type set to Serial, Serial line set to the board's COM port, and Speed set to 115200, ready to connect to the Zephyr UART shell#center)

### macOS with screen

Open a terminal window and identify the serial device:

```bash
ls /dev/tty.*
```

Connect to the UART shell, replacing `/dev/tty.usbmodemXXXX` with the serial device shown on your system:

```bash
screen /dev/tty.usbmodemXXXX 115200
```
To exit `screen`, press the `Ctrl` key and `A`, then `K`, then `Y` to confirm.

### Linux with screen

List available serial devices:

```bash
ls /dev/ttyACM* /dev/ttyUSB*
```

If you see a permission error, add your user to the `dialout` group, then log out and back in:

```bash
sudo usermod -aG dialout $USER
```

Connect to the UART shell, replacing `/dev/ttyACM0` with the device shown on your system:

```bash
screen /dev/ttyACM0 115200
```
To exit `screen`, press the `Ctrl` key and `A`, then `K`, then `Y` to confirm.

### Check the shell prompt

In your UART terminal application, you'll see the boot log followed by the shell prompt:

```output
uart:~$ *** Booting Zephyr OS build v4.4.0 ***
uart:~$ [00:00:00.001,037] <inf> app_main: UART shell backend demo on frdm_mcxn947
uart:~$ [00:00:00.001,037] <inf> app_main: Connect a serial terminal at 115200 baud and use the uart:~$ prompt
uart:~$
```

The `uart:~$` prompt confirms that the UART shell backend is active.

The boot banner and the `<inf>` log lines are prefixed with `uart:~$` because `SHELL_LOG_BACKEND` is enabled by default when `CONFIG_SHELL=y` and `CONFIG_LOG=y` are both set. Log output is routed through the active shell backend.
