---
id: "sds-sdsio-interface-layer-sdsio-rtt"
type: "concept"
domain: "test"
title: "SDSIO Interface: Layer: sdsio_rtt"
summary: "The layer/sdsio/rtt/sdsio_rtt.clayer.yml is configured for recording and playback using the SEGGER RTT component for I/O via a debug adapter."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/sdsio.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio-rtt"
license: "Apache-2.0"
mode: "V"
---

The [`layer/sdsio/rtt/sdsio_rtt.clayer.yml`](https://github.com/ARM-software/SDS-Framework/tree/main/layer/sdsio/rtt) is configured for recording and playback using the SEGGER RTT component for I/O via a debug adapter.

(figure: SDS-Firmware with RTT interface)

### Using RTT Interface

The SDSIO layer communicates with the host computer via an RTT socket exposed by the
debug probe software. The [SDSIO-Server](https://arm-software.github.io/SDS-Framework/main/utilities.html#sdsio-server)
runs on the host and connects to the debug probe socket using
[socket connect mode](https://arm-software.github.io/SDS-Framework/main/utilities.html#socket-mode-command-line).

#### Connect with SEGGER J-Link

Configure `interface:` in the [`*.sdsio.yml` control file](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#sdsio-control-file-sdsioyml) as shown below:

```yml
sdsio:
  interface:
    socket:
      ipaddr: 127.0.0.1
      port: 19021
      connect: "$$SEGGER_TELNET_ConfigStr=RTTCh;1$$"
      connect-time: 100
```

Then start the SDSIO-Server with:

```bash
python sdsio-server.py -c myproject.sdsio.yml
```

**How it works:**

J-Link exposes RTT data via a TELNET-like TCP socket on `localhost`, port **19021** (default), while a J-Link connection is active (typically during a debug session). After connecting to this TCP socket, the SDSIO-Server (sends within the 100 ms time limit) the [SEGGER TELNET Config String](https://kb.segger.com/J-Link_RTT_TELNET_Channel) that selects the RTT channel. The SDSIO-Server sends this string automatically via `--connect`, and discards any initial response from J-Link during the `--connect-time` window.

#### Connect with pyOCD

pyOCD can expose each RTT channel as a TCP socket server. RTT is configured under the `debugger:` node of the `*.csolution.yml` file as shown below. Refer to [CMSIS-Toolbox - pyOCD - RTT](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#rtt) for further details.

```yml
  target-types:
    - type: MyHardware
      target-set:
        - set:
          images:
            - project-context: DataTest.Debug
          debugger:
            name: CMSIS-DAP@pyOCD
            clock: 10000000
            protocol: swd
            rtt:
              channel:
                - number: 1     # must match SDSIO_RTT_CHANNEL in sdsio_client_rtt_config.h
                  mode: server
                  port: 5100    # any free TCP port on localhost
```

Configure `interface:` in the [`*.sdsio.yml` control file](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#sdsio-control-file-sdsioyml) as shown below:

```yml
sdsio:
  interface:
    socket:
      ipaddr: 127.0.0.1
      port: 5100       # must match the port configured in *.csolution.yml
      connect:         # no connect string required; channel is configured with `rtt:` node above
```

The CMSIS-Toolbox includes all project configuration in the file `*.cbuild-run.yml`. Once this file is up-to-date, run pyOCD and SDSIO-Server with:

```bash
pyocd run --cbuild-run out/<name>+<target-type>.cbuild-run.yml --eot
python sdsio-server.py -c myproject.sdsio.yml
```

**How it works:**

pyOCD does not require a connect message. Instead the RTT channel configuration is part of the `*.cbuild-run.yml` file that also specifies project files and other hardware related parameters. Refer to [CMSIS-Toolbox - Run and Debug Configuration](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#run-and-debug-configuration) for further information.

For CI runs that should stop automatically after SDS playback, start pyOCD with `--eot` and run SDSIO-Server with `--playback --exit-after-playback`. After playback completes, SDSIO-Server sets `SDS_FLAG_TERMINATE`. The target application can then write EOT (`0x04`). pyOCD can terminate on this character only when it receives the target standard output stream, for example through semihosting or RTT stdio. If standard output is retargeted directly to UART, the character bypasses pyOCD and `--eot` will not stop the pyOCD run.
