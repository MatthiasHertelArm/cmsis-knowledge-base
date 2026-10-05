---
id: "zep-shell-backends"
type: "concept"
domain: "debug"
title: "Shell: Backends"
summary: "The module can be connected to any transport for command input and output. At this point, the following transport layers are implemented:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

The module can be connected to any transport for command input and output.
At this point, the following transport layers are implemented:

* MQTT
* Segger RTT
* SMP
* Telnet
* UART
* USB
* Bluetooth LE (NUS)
* RPMSG
* DUMMY - not a physical transport layer.


### Telnet


Enabling `CONFIG_SHELL_BACKEND_TELNET` will allow users to use telnet
as a shell backend. Connecting to it can be done using PuTTY or any `telnet` client.
For example:

```none

telnet <ip address> <port>
```
By default the telnet client won't handle telnet commands and configuration. Although
command support can be enabled with `CONFIG_SHELL_TELNET_SUPPORT_COMMAND`.
This will give the telnet client access to a very limited set of supported commands but
still can be turned on if needed. One of the command options it supports is the `ECHO`
option. This will allow the client to be in character mode (character at a time),
similar to a UART backend in that regard. This will make the client send a character
as soon as it is typed having the effect of increasing the network traffic
considerably. For that cost, it will enable the line editing,
tab completion <tab-feature_>, and history <history-feature_>
features of the shell.


### USB CDC ACM


To configure Shell USB CDC ACM backend, simply add the snippet `cdc-acm-console`
to your build:

```console

west build -S cdc-acm-console [...]
```
Details on the configuration settings are captured in the following files:

- `snippets/cdc-acm-console/cdc-acm-console.conf`.
- `snippets/cdc-acm-console/cdc-acm-console.overlay`.


### Bluetooth LE (NUS)


To configure Bluetooth LE (NUS) backend, simply add the snippet `nus-console`
to your build:

```console

west build -S nus-console [...]
```
Details on the configuration settings are captured in the following files:

- `snippets/nus-console/nus-console.conf`.
- `snippets/nus-console/nus-console.overlay`.


### Segger RTT


To configure Segger RTT backend, add the following configurations to your build:

- `CONFIG_USE_SEGGER_RTT`
- `CONFIG_SHELL_BACKEND_RTT`
- `CONFIG_SHELL_BACKEND_SERIAL`

Details on additional configuration settings are captured in:
`samples/subsys/shell/shell_module/prj_minimal_rtt.conf`.


#### Using west


Attach to and configure RTT with:

```console

$ west rtt
```

**Note:** If your default runner does not have support for RTT, check your board's documentation page for any other runners that support RTT. You may then use the `--runner` option to specify a different runner. .. code-block:: console $ west rtt --runner <runner>


#### Using PuTTY


Use following procedure:

* Open debug session and continue running the application.

```none

west attach
```
* Open `PuTTY`. Use telnet port 19021 and specific Terminal configuration. Set `Local echo`
  to `Force off` and `Local line editing` to `Force off` (see image below).


* Now you should have a network connection to RTT that will let you enter input
  to the shell.


#### Connecting to Segger RTT via TCP (on macOS, for example)


On macOS JLinkRTTClient won't let you enter input. Instead, please use following
procedure:

* Open up a first Terminal window and enter:

```none

JLinkRTTLogger -Device NRF52840_XXAA -RTTChannel 1 -if SWD -Speed 4000 ~/rtt.log
```
  (change device if required)

* Open up a second Terminal window and enter:

```none

nc localhost 19021
```
* Now you should have a network connection to RTT that will let you enter input
  to the shell. However, contrary to PuTTY <shell_rtt_putty_> some features like
  `Tab` completion do not work.
