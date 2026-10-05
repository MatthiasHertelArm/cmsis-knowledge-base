---
id: "tfm-nordic-nrf5340-flashing-and-debugging-with-nordic-nrf-s"
type: "concept"
domain: "security"
title: "Nordic nRF5340: Flashing and debugging with Nordic nRF Segger J-Link"
summary: "nRF5340 DK is equipped with a Debug IC (Atmel ATSAM3U2C) which provides the following functionality:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/nordic_nrf/nrf5340dk_nrf5340_cpuapp/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/nordic_nrf/nrf5340dk_nrf5340_cpuapp/.html#flashing-and-debugging-with-nordic-nrf-segger-j-link"
license: "BSD-3-Clause"
mode: "V"
---

nRF5340 DK is equipped with a Debug IC (Atmel ATSAM3U2C) which provides the
following functionality:

* Segger J-Link firmware and desktop tools
* SWD debug for the nRF5340 IC
* Mass Storage device for drag-and-drop image flashing
* USB CDC ACM Serial Port bridged to the nRFx UART peripheral
* Segger RTT Console
* Segger Ozone Debugger

To install the J-Link Software and documentation pack, follow the steps below:

#. Download the appropriate package from the J-Link Software and documentation pack website
#. Depending on your platform, install the package or run the installer
#. When connecting a J-Link-enabled board such as an nRF5340 DK, a drive
   corresponding to a USB Mass Storage device as well as a serial port should come up


### nRF Util Installation


nRF Util allows you to control your nRF5340 device from the command line,
including resetting it, erasing or programming the flash memory and more.

To install nRF Util:

1. Visit nRF Util product page.
2. Download the executable.
3. Follow the nRF Util installation instructions.
4. Install `nrfutil device` subcommand for programming, flashing, and erasing devices:

```console

nrfutil install device
```
After installing, make sure that `nrfutil.exe` is somewhere in your executable
path to be able to invoke it from anywhere.

BL2, S, and NS application images can be flashed into nRF5340 separately or may be merged
together into a single binary.


### Flashing the nRF5340 DK


To program the flash with a compiled TF-M image (i.e. S, NS or both) after having
followed the instructions to install the Segger J-Link Software and the nRF
Command-Line Tools, follow the steps below:

Generate Intel hex files from the output binary (bin) files as follows:

```console

srec_cat build_app/tfm_s_ns_signed.bin -binary --offset 0x10000 \
      -o build_app/tfm_s_ns_signed.hex -intel
```
* Connect the micro-USB cable to the nRF5340 DK and to your computer
* Erase the flash memory in the nRF5340 IC:

```console

nrfutil device erase --all --x-family nrf53
```
* (Optionally) Erase the flash memory and reset flash protection and disable
   the read back protection mechanism if enabled.

```console

nrfutil device recover --x-family nrf53
```
* Flash the BL2 and the TF-M image binaries from the sample folder of your choice:

```console

nrfutil device program --x-family nrf53 --firmware build_spe/bin/bl2.hex --options chip_erase_mode=ERASE_RANGES_TOUCHED_BY_FIRMWARE
nrfutil device program --x-family nrf53 --firmware build_app/tfm_s_ns_signed.hex --options chip_erase_mode=ERASE_RANGES_TOUCHED_BY_FIRMWARE
```
* Reset and start TF-M:

```console

nrfutil device reset --x-family nrf53
```

### Secure UART Console on nRF5340 DK


SECURE_UART1 is enabled by default when building TF-M on nRF5340 DK, so the secure firmware console output
is available via USART1.
When using the nRF5340 network MCU make sure to configure different UART pins or disable SECURE_UART1.

Non-Secure console output is available via USART0.


**Note:** By default USART0 and USART1 outputs are routed to separate serial ports.

--------------

*Copyright (c) 2020, Nordic Semiconductor. All rights reserved.*
