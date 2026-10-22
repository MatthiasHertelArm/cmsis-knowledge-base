---
id: "sds-utilities-usage"
type: "concept"
domain: "test"
title: "Utilities: SDSIO-Server / Usage"
summary: "The SDSIO-Server accepts directly on the console the following keyboard entries:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/utilities.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#usage"
license: "Apache-2.0"
mode: "V"
---

_Part of: SDSIO-Server_

- [Setup](#setup) the Python environment.
- Configure via a YAML control file (`-c *.sdsio.yml`) or specify the interface directly on the command line.
- Terminate the server by pressing `Ctrl+C` or the `X` key in the server application window.

```txt
usage: sdsio-server.py [-h] [-V] [{socket | serial | usb} [interface-opts]] [-c sdsio.yml] [general-opts]

SDSIO-Server: record and playback SDS data stream files over USB, socket, or serial interface.
Configure via *.sdsio.yml file or specify the interface parameters directly on the command line.

options:
  --help, -h                       Show this help message and exit
  --version, -V                    Show program's version number and exit

interface (optional, default: usb; overrides interface specified in *.sdsio.yml):
  {socket | serial | usb}
    socket                         Run SDSIO-Server using socket interface
    serial                         Run SDSIO-Server using serial interface
    usb                            Run SDSIO-Server using USB interface

configuration:
  --control, -c <*.sdsio.yml>      Configure interface, SDS file directories, and playback steps

general-opts:
  --playback, -p <step|"*">        Start SDSIO-Server in playback mode; optionally select a zero-based play step or "*" for all steps
  --exit-after-playback, -x        Terminate when playback is completed
  --no-progress-info, -n           Disable dynamic progress indicator
  --workdir <path>                 Directory for SDS files (overrides *.sdsio.yml setting; default: current directory)
  --mon-port, -m <port>            Monitor control interface port
  --log, -l <file>                 Redirect console output to a log file (typically for CI use)
  --write-flush-records <records>  Force recorded SDS data to disk after this many records (overrides *.sdsio.yml setting; 0 = after every record; default: disabled)
  --verbose, -v                    Enable debug messages
  --high-priority                  Increase process priority when using USB interface (requires elevated privileges)
```

**Console input for SDSIO-Server:**

The SDSIO-Server accepts directly on the console the following keyboard entries:

Key | Action
:--:|:------------------
R/r | Start recording
P/p | Start playback
S/s | Stop recording/playback
T/t | Reset target
A-H | Set user flags 0-7
a-h | Clear user flags 0-7
X/x | Terminate server

#### SDSIO Control File

It is recommended to use a [SDSIO control file (`*.sdsio.yml`)](#sdsio-control-file-sdsioyml) that configures project parameters such as interface, workdir and steps for playback mode. With command line options the parameters of the `*.sdsio.yml` file can be overwritten.  It is also possible to use additional [general options](#using-general-options).

Start SDSIO-Server using a control file:

```bash
python sdsio-server.py -c myproject.sdsio.yml
```

Start SDSIO-Server automatically starting playback of all configured `play:` steps:

```bash
python sdsio-server.py -c sdsio.yml --playback "*"
```

Start SDSIO-Server automatically starting only the first configured `play:` step:

```bash
python sdsio-server.py -c sdsio.yml --playback 0
```

The numeric `--playback` value selects a `play:` step by its number, with `0` selecting the first step.

Start SDSIO-Server and override the `workdir:` node.

```bash
python sdsio-server.py -c myproject.sdsio.yml --workdir ./mytest2
```

#### USB Mode (command line)

```txt
usage: sdsio-server.py usb [-h] [-V] [general-opts]

options:
  --help, -h                       Show this help message and exit
  --version, -V                    Show program's version number and exit
```

**Example:**

```bash
python sdsio-server.py usb --workdir ./work_dir
```

#### Socket Mode (command line)

The socket server can operate in two modes:

- **Listen mode** (default): SDSIO-Server binds to a local IP address and waits for the target device to connect. The listen mode is used with the [Layer: SDSIO-Network](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md#layer-sdsio_network). This mode requires network configuration.
- **Connect mode** (`--connect`): SDSIO-Server actively connects to the specified IP address. The connect mode is used with the [Layer: SDSIO-RTT](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md#layer-sdsio_rtt), where the debug adapter (J-Link or pyOCD) exposes RTT data over a local TCP socket. No network configuration is required.

```txt
usage: sdsio-server.py socket [-h] [-V] [--ipaddr <IP> | --netif <Interface>] [--port <TCP Port>] [--connect [<message>]] [--connect-time <ms>] [general-opts]

options:
  --help, -h                       Show this help message and exit
  --version, -V                    Show program's version number and exit

interface-opts (optional):
  --ipaddr <IP>                    Server IP address; cannot be combined with 'netif',
                                   or host IP address in connect mode (default: 127.0.0.1 / localhost)
  --netif <Interface>              Network interface (example: eth0), cannot be combined with '--ipaddr' or '--connect'
  --port <TCP Port>                TCP port number (default: 5050)
  --connect <message>              Connect to existing IP port instead of listening for incoming connections;
                                   optionally send <message> to establish the connection
  --connect-time <ms>              Duration in milliseconds to discard incoming data after the connection is established (default: 50)
```

!!! Note
    - The `--ipaddr` and `--netif` options are mutually exclusive.
    - SDSIO-Server only supports IPv4 addresses.
    - `--connect` requires `--ipaddr` and cannot be combined with `--netif`.

**Examples:**

Start in listen mode with default IP address of the host computer:

```bash
python sdsio-server.py socket --workdir ./work_dir
```

Start in listen mode with a specific interface (for Linux or macOS):

```bash
python sdsio-server.py socket --netif eth0 --workdir ./work_dir
```

Start in `connect` mode using local host (default setting) and message for SEGGER J-Link:

```bash
python sdsio-server.py socket --port 19021 --connect "$$SEGGER_TELNET_ConfigStr=RTTCh;1$$"
```

Start in `connect` mode with a connection to a specific IP address and IP port.

```bash
python sdsio-server.py socket --ipaddr 192.168.0.1 --port 5050 --connect
```

#### Serial Mode (command line)

```txt
usage: sdsio-server.py serial [-h] [-V] --port <Serial Port> [--baudrate <Baudrate>] [--parity <Parity>] [--stopbits <Stop bits>] [--connect-timeout <Timeout>] [general-opts]

options:
  --help, -h                       Show this help message and exit
  --version, -V                    Show program's version number and exit

interface-opts (required):
  --port <Serial Port>             Serial port (required)

interface-opts (optional):
  --baudrate <Baudrate>            Baudrate (default: 115200)
  --parity <Parity>                Parity: none, even, odd, mark, space (default: none)
  --stopbits <Stop bits>           Stop bits: 1, 1.5, 2 (default: 1)
  --connect-timeout <Timeout>      Serial port connection timeout in seconds (default: no timeout)
```

**Example:**

```bash
python sdsio-server.py serial --port COM0 --baudrate 115200 --workdir ./work_dir
```

#### Using general options

Start SDSIO-Server with monitor server waiting on the port `6060`:

```bash
python sdsio-server.py -c sdsio.yml --mon-port 6060
```

Start SDSIO-Server using a user-specified working directory:

```bash
python sdsio-server.py usb --workdir ./data
```

Start SDSIO-Server, forcing SDS file write flushes to disk after each new record:

```bash
python sdsio-server.py usb --write-flush-records 0
```

!!! Note
    - For more reliable operation at higher data transfer rates, it is recommended to enable the `--high-priority` general option. This increases the thread priority of the SDSIO-Server process.
    - When using `--high-priority`, elevated privileges are required depending on your operating system:
        - **Windows**: Run the Python script as an administrator.
        - **macOS/Linux**: Execute the script with `sudo` or ensure the user has sufficient permissions.

On **macOS**, the **libusb** system library is required. If not already installed, you can install it with [Homebrew](https://brew.sh/): `>brew install libusb`

On **Linux**, access to USB devices from user space requires a udev rule by default. Create a udev rule file (e.g. `/etc/udev/rules.d/99-sdsio.rules`) with the vendor and product ID of the SDSIO-Client device.

```bash
SUBSYSTEM=="usb", ATTRS{idVendor}=="XXXX", ATTRS{idProduct}=="XXXX", MODE="0666"
```

Then reload rules with `sudo udevadm control --reload && sudo udevadm trigger`.  Use `dmesg` before and after plugging in the device to find the vendor/product IDs.
