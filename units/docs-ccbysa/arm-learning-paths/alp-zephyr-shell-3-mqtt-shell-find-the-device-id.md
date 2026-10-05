---
id: "alp-zephyr-shell-3-mqtt-shell-find-the-device-id"
type: "concept"
domain: "rtos"
title: "Create an interactive shell for Zephyr RTOS on Arm Cortex-M: Build and run the Zephyr MQTT shell on Arm Cortex-M: Find the device ID"
summary: "The MQTT shell backend derives its client ID from the board's hardware UID, so each board connects with topics under <device_id>/sh/rx and <device_id>/sh/tx."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell/#find-the-device-id"
license: "CC-BY-SA-4.0"
mode: "V"
---

The MQTT shell backend derives its client ID from the board's hardware UID, so each board connects with topics under `<device_id>/sh/rx` and `<device_id>/sh/tx`. 

There are two ways to read this ID:

### Read from the board's serial console

If you have a serial terminal open on the board's UART, the MQTT backend logs the topics it subscribes to and publishes from at boot. 

A typical FRDM-MCXN947 boot log looks like this:

```output
*** Booting Zephyr OS build v4.4.0 ***
[00:00:01.654,000] <inf> phy_mii: PHY (0) Link speed 100 Mb, full duplex
[00:00:01.654,000] <inf> eth_nxp_enet_qos_mac: Link is up
[00:00:01.656,000] <wrn> shell_mqtt: Network connected
[00:00:01.656,000] <inf> app_main: MQTT shell backend demo on frdm_mcxn947
[00:00:02.656,000] <inf> shell_mqtt: DNS resolved for 192.168.1.31:1883
[00:00:02.656,000] <err> shell_mqtt: mqtt_connect error: -22
[00:00:03.656,000] <inf> shell_mqtt: DNS resolved for 192.168.1.31:1883
[00:00:03.656,000] <err> shell_mqtt: mqtt_connect error: -22
[00:00:04.656,000] <inf> shell_mqtt: DNS resolved for 192.168.1.31:1883
[00:00:04.656,000] <err> shell_mqtt: mqtt_connect error: -22
[00:00:05.656,000] <inf> shell_mqtt: DNS resolved for 192.168.1.31:1883
[00:00:05.656,000] <err> shell_mqtt: mqtt_connect error: -22
[00:00:06.656,000] <inf> shell_mqtt: DNS resolved for 192.168.1.31:1883
[00:00:06.818,000] <wrn> shell_mqtt: MQTT client connected!
[00:00:07.823,000] <wrn> shell_mqtt: MQTT subscribe: ok
[00:00:07.823,000] <inf> shell_mqtt: Logs will be published to: 1a2b3c/sh/tx
[00:00:07.823,000] <inf> shell_mqtt: Subscribing shell cmds from: 1a2b3c/sh/rx
```

The two `<inf> shell_mqtt:` lines in the last two lines of the log give you the device ID directly. In this example, it's `1a2b3c`.

**Note:**
The `mqtt_connect error: -22` lines you see during the first few seconds are expected. The Zephyr MQTT client retries the connect handshake until the broker accepts it, usually within a few attempts. The connection completes when you see `MQTT client connected!`, followed by `MQTT subscribe: ok`.


### Read from the broker side

If you don't have a serial terminal open, watch every shell-output topic with a wildcard:

```bash
docker exec -it mosquitto-mqtt mosquitto_sub -h localhost -t "+/sh/tx" -v
```

When the board connects, it publishes its shell prompt to `<device_id>/sh/tx`. The topic prefix on the first message is the device ID:

```output
1a2b3c/sh/tx mqtt:~$
```

You can also confirm the same value from the broker's connection log:

```bash
docker logs mosquitto-mqtt | grep "New client connected"
```

The device ID appears in the client connection entry:

```output
New client connected from 192.168.65.1:65496 as 1a2b3c (p4, c0, k60).
```
