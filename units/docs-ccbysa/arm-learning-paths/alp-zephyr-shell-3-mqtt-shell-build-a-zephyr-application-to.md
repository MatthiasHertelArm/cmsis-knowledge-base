---
id: "alp-zephyr-shell-3-mqtt-shell-build-a-zephyr-application-to"
type: "concept"
domain: "rtos"
title: "3 mqtt shell: Build a Zephyr application to enable the MQTT shell backend"
summary: "Start by building a minimal Zephyr application that enables the MQTT shell backend."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell/#build-a-zephyr-application-to-enable-the-mqtt-shell-backend"
license: "CC-BY-SA-4.0"
mode: "V"
---

Start by building a minimal Zephyr application that enables the MQTT shell backend.

The application doesn't need networking code in `main.c`. Zephyr starts the shell, network stack, DHCP client, and MQTT shell backend from configuration options in `prj.conf`.

### How the MQTT shell backend works

When `CONFIG_SHELL_BACKEND_MQTT=y` is enabled, Zephyr’s MQTT shell backend connects to a broker and uses MQTT topics to carry shell traffic.

The default topic pattern is:

| Direction | Topic |
|-----------|-------|
| Commands sent to the board | `<device_id>/sh/rx` |
| Responses sent from the board | `<device_id>/sh/tx` |

The backend derives `<device_id>` from the hardware device ID, so each board uses a unique topic prefix. You'll read this ID from the broker after the board connects for the first time.

### Create an application project in Workbench for Zephyr

To create an application project in Workbench for Zephyr:

1. Open the **Workbench for Zephyr** panel.
2. In the panel, select **New Application** to open the **Create a new Zephyr Application Project** wizard. 
3. After opening the wizard, fill in the following fields:
    - For **Select West Workspace**, select your initialized West workspace for Zephyr v4.4.0 (for example, `zephyr`).
    - For **Select Toolchain**, select `zephyr-sdk-1.0.1`.
    - For **Select Board**, select **NXP FRDM-MCXN947 (CPU0)** (Zephyr identifier `frdm_mcxn947/mcxn947/cpu0`).
    - For **Application type**, select **Create new application**.
    - For **Select Sample project**, select `hello_world`.
    - For **Project Name**, enter `mqtt_shell_backend`.
    - For **Project Location**, select the directory where you want to create the project (for example, `zephyr/apps`).
    - Leave **Debug preset** checked.
    - Leave **Advanced options** as the defaults.
4. Select **Create** to generate the project.

(figure: Workbench for Zephyr "Create a new Zephyr Application Project" wizard showing "West Workspace" set to "zephyr", "Toolchain" set to "zephyr-sdk-1.0.1", "Board" set to "NXP FRDM-MCXN947 CPU0", "Application type" set to "Create new application", "Sample project" set to "hello_world", "Project Name" set to "mqtt_shell_backend", and "Project Location" set to "zephyr/apps"#center)

### Configure the application

The `hello_world` sample provides a working `CMakeLists.txt`, `prj.conf`, and `src/main.c`. Leave `CMakeLists.txt` unchanged, and replace `prj.conf` and `src/main.c`.

Replace the contents of `prj.conf` with the following text:

```text
# Shell and MQTT backend
CONFIG_SHELL=y
CONFIG_SHELL_BACKEND_MQTT=y

# Networking
CONFIG_NETWORKING=y
CONFIG_NET_IPV4=y
CONFIG_NET_TCP=y
CONFIG_NET_DHCPV4=y
CONFIG_NET_CONFIG_SETTINGS=y

# MQTT broker address
CONFIG_SHELL_MQTT_SERVER_ADDR="192.168.1.233"

# Optional shell modules and logging
CONFIG_NET_SHELL=y
CONFIG_LOG=y

# Resource tuning
CONFIG_HEAP_MEM_POOL_SIZE=8192
CONFIG_MAIN_STACK_SIZE=2048
CONFIG_NET_PKT_RX_COUNT=16
CONFIG_NET_BUF_RX_COUNT=32
```

Replace `192.168.1.233` with the IP address of the host running Mosquitto, as seen from the board's Ethernet network.

The values under `# Resource tuning` keep the shell footprint small on Cortex-M and allow the network stack and MQTT client to operate reliably.

#### Use a static IPv4 address

DHCP is convenient, but it's not required. To use a static address, remove:

```text
CONFIG_NET_DHCPV4=y
```

Then, add values that match your network:

```text
CONFIG_NET_CONFIG_MY_IPV4_ADDR="192.168.1.50"
CONFIG_NET_CONFIG_MY_IPV4_NETMASK="255.255.255.0"
CONFIG_NET_CONFIG_MY_IPV4_GW="192.168.1.1"
```

Keep `CONFIG_NET_CONFIG_SETTINGS=y` enabled so Zephyr applies the network configuration at boot.

#### Update the main function

The shell and MQTT backend start from Zephyr initialization hooks.

Replace the contents of `main.c` with the following code:

```c
int main(void)
{
    return 0;
}
```

### Build and flash

In the **Workbench for Zephyr** panel, select your project and build configuration. Select **Build**, then select **Flash**.

The FRDM-MCXN947 uses NXP LinkServer as the debug runner. If LinkServer isn't installed, follow the `Workbench for Zephyr` prompt to install or configure it.
