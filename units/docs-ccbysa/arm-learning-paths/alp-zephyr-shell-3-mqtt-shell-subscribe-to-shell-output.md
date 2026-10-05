---
id: "alp-zephyr-shell-3-mqtt-shell-subscribe-to-shell-output"
type: "concept"
domain: "rtos"
title: "3 mqtt shell: Subscribe to shell output"
summary: "Narrow the subscription to your board's response topic only. Replace 1a2b3c with your device ID:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell/#subscribe-to-shell-output"
license: "CC-BY-SA-4.0"
mode: "V"
---

Narrow the subscription to your board's response topic only. Replace `1a2b3c` with your device ID:

```bash
docker exec -it mosquitto-mqtt mosquitto_sub -h localhost -t "1a2b3c/sh/tx" -v
```

Keep this terminal open. Every shell response from the board will print here.
