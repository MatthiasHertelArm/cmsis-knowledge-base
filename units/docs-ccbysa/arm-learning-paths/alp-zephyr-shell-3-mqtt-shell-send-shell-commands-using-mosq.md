---
id: "alp-zephyr-shell-3-mqtt-shell-send-shell-commands-using-mosq"
type: "concept"
domain: "rtos"
title: "3 mqtt shell: Send shell commands using Mosquitto"
summary: "You'll now send shell commands to the board using the Mosquitto command-line tools."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell/#send-shell-commands-using-mosquitto"
license: "CC-BY-SA-4.0"
mode: "V"
---

You'll now send shell commands to the board using the Mosquitto command-line tools.

Open a second terminal to publish commands to the board:

```bash
printf 'kernel version\n' | docker exec -i mosquitto-mqtt mosquitto_pub -h localhost -t "1a2b3c/sh/rx" -s
```

The command is published to Mosquitto and the board executes it. 

The response appears in the first terminal:

```output
1a2b3c/sh/tx Zephyr version 4.4.0
```

Try the following commands:

| Command | Description |
|---------|-------------|
| `kernel version` | Print the Zephyr version string. |
| `kernel uptime` | Print the time since boot. |
| `kernel thread list` | Print the thread list and stack usage. |
| `net iface` | Print network interface configuration, including the assigned IPv4 address. |
| `net ping <ip>` | Send ICMP echo requests to a reachable host (for example, your gateway). |
| `device list` | Print registered Zephyr devices. |
| `help` | Print available shell modules and commands. |

The `net` commands are available because you set `CONFIG_NET_SHELL=y` in `prj.conf`. Without that option, only the `kernel`, `device`, and `shell` modules are exposed.

Example output for `kernel uptime`:

```output
1a2b3c/sh/tx Uptime: 55310 ms
```

Truncated example output for `kernel thread list` on the FRDM-MCXN947 (the full list shows the network and Ethernet driver threads):

```output
1a2b3c/sh/tx Scheduler: 1046 since last call
Threads:
*0x300015d0 shell_mqtt
	options: 0x0, priority: 14 timeout: 0
	state: queued, entry: 0x100069e5
	stack size 2048, unused 1096, usage 952 / 2048 (46 %)

 0x30001c30 sh_mqtt_workq
	options: 0x0, priority: -9 timeout: 800
	state: pending, entry: 0x100223cd
	stack size 2048, unused 1160, usage 888 / 2048 (43 %)

 0x30002688 conn_mgr_monitor
	options: 0x0, priority: -1 timeout: 0
	state: pending, entry: 0x1001ea0d
	stack size 512, unused 264, usage 248 / 512 (48 %)

 0x300027c0 ENETQOS_RX
	options: 0x0, priority: -13 timeout: 0
	state: pending, entry: 0x100223cd
	stack size 1024, unused 752, usage 272 / 1024 (26 %)

 0x300028b0 idle
	options: 0x1, priority: 15 timeout: 0
	state: , entry: 0x1003a335
	stack size 320, unused 256, usage 64 / 320 (20 %)
```

The `*` next to `shell_mqtt` marks the running thread, which is the shell that executed the command. Note that responses larger than the MQTT buffer are split across multiple publishes. `mosquitto_sub -v` reassembles them sequentially under the `1a2b3c/sh/tx` topic prefix.

Example output for `net iface` on the FRDM-MCXN947, truncated to the IPv4 section:

```output
1a2b3c/sh/tx Default interface: 1

Interface eth0 (0x30000c70) (Ethernet) [1]
===================================
Link addr : XX:XX:XX:XX:XX:XX
MTU       : 1500
Flags     : AUTO_START,IPv4,IPv6
Status    : oper=UP, admin=UP, carrier=ON
Ethernet link speed: 100 Mbits full-duplex
IPv4 unicast addresses (max 1):
	192.168.1.41/255.255.255.0 DHCP preferred
IPv4 gateway : 192.168.1.1
DHCPv4 state      : bound
DHCPv4 server     : 192.168.1.1
```
Next, run `net ping` with the gateway address shown by `net iface`. The board sends three ICMP echo requests by default. 

Example output for `net ping 192.168.1.1` (board pinging its gateway):

```output
1a2b3c/sh/tx PING 192.168.1.1
28 bytes from 192.168.1.1 to 192.168.1.41: icmp_seq=1 ttl=64 time=0 ms
28 bytes from 192.168.1.1 to 192.168.1.41: icmp_seq=2 ttl=64 time=0 ms
28 bytes from 192.168.1.1 to 192.168.1.41: icmp_seq=3 ttl=64 time=0 ms
```

**Note:**
The MQTT shell backend executes a command after it receives a newline character. The `printf 'kernel version\n' | ... mosquitto_pub -s` form sends the command with the required newline.
