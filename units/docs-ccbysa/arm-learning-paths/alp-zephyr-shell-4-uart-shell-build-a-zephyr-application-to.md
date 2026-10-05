---
id: "alp-zephyr-shell-4-uart-shell-build-a-zephyr-application-to"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Build and run the Zephyr UART shell on Arm Cortex-M: Build a Zephyr application to enable the UART "
summary: "Start by building a Zephyr application that enables the UART shell backend."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/4_uart_shell.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/4_uart_shell/#build-a-zephyr-application-to-enable-the-uart-shell-backend"
license: "CC-BY-SA-4.0"
mode: "V"
---

Start by building a Zephyr application that enables the UART shell backend.

The example uses the FRDM-MCXN947 because it provides an onboard CMSIS-DAP/LinkServer debug interface together with a USB UART connection. These can be accessed from a serial terminal application such as PuTTY on Windows, or `screen` on macOS and Linux.

UART shell access uses the board's USB serial interface and doesn't require additional debug hardware or network connectivity. The Zephyr UART shell backend maps shell input and output to the active UART console. 

### Create an application project in Workbench for Zephyr

To create an application project in Workbench for Zephyr:

1. Open the **Workbench for Zephyr** panel.
2. In the panel, select **New Application** to open the **Create a new Zephyr Application Project** wizard. 
3. After opening the wizard, fill in the following fields:
    - For **Select West Workspace**, select your initialized West workspace for Zephyr v4.4.0.
    - For **Select Toolchain**, select `zephyr-sdk-1.0.1`.
    - For **Select Board**, select **FRDM-MCXN947** (Zephyr identifier `frdm_mcxn947/mcxn947/cpu0`).
    - For **Application type**, select **Create new application**.
    - For **Select Sample project**, select `hello_world`.
    - For **Project Name**, enter `frdm_uart_shell`.
    - For **Project Location**, select the directory where you want to create the project.
    - Leave **Debug preset** checked.
    - Leave **Advanced options** as the defaults.
4. Select **Create** to generate the project.

### Configure the application

The `hello_world` sample provides a working `CMakeLists.txt`, `prj.conf`, and `src/main.c`. Leave `CMakeLists.txt` unchanged, and replace `prj.conf` and `src/main.c` with the following contents.

Edit the `prj.conf` file and replace the contents with the following text:

```text
CONFIG_SHELL=y
CONFIG_LOG=y

CONFIG_SERIAL=y
CONFIG_CONSOLE=y
CONFIG_UART_CONSOLE=y
CONFIG_SHELL_BACKEND_SERIAL=y

CONFIG_MAIN_STACK_SIZE=2048
```

The UART shell backend routes shell input and output through the board's USB serial interface.

#### Update the main function

Edit the `main.c` file and replace the contents with the following code:

```c
#include <zephyr/logging/log.h>

LOG_MODULE_REGISTER(app_main, LOG_LEVEL_INF);

int main(void)
{
    LOG_INF("UART shell backend demo on %s", CONFIG_BOARD);
    LOG_INF("Connect a serial terminal at 115200 baud and use the uart:~$ prompt");
    return 0;
}
```

No shell initialization code is required in `main.c`. Zephyr registers and starts the UART shell backend from the Kconfig options in `prj.conf`.

### Build and flash the application

Connect the FRDM-MCXN947 board to your host computer over USB.

In the **Workbench for Zephyr** panel, select your project and build configuration. Select **Build**, then select **Flash**.

The FRDM-MCXN947 uses the onboard CMSIS-DAP/LinkServer interface for flashing and debugging.
