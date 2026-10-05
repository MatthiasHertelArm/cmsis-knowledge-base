---
id: "alp-zephyr-shell-1-installation-network-requirements-for-the-m"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Set up the Zephyr shell development environment: Network requirements for the MQTT shell example"
summary: "For the MQTT shell example, the board needs access to an MQTT broker over Ethernet. You'll run Mosquitto locally and use the Mosquitto command-line tools to send and receive shell messages."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/1_installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/1_installation/#network-requirements-for-the-mqtt-shell-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

For the MQTT shell example, the board needs access to an MQTT broker over Ethernet. You'll run Mosquitto locally and use the Mosquitto command-line tools to send and receive shell messages.

Make sure that:

- The board is connected to the same network as the host computer.
- The network provides DHCP, or you configure a static IPv4 address in `prj.conf`.
- The board can reach the MQTT broker on port `1883`.

**Note:**
The example configuration uses IPv4. If your network doesn't provide DHCP, use the static IPv4 settings shown in the next section.
