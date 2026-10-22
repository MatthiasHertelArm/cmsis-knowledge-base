---
id: "tfm-nordic-nrf9161-flashing-and-debugging-with-nordic-nrf-s"
type: "concept"
domain: "security"
title: "Nordic nRF9161: Flashing and debugging with Nordic nRF Segger J-Link"
summary: "nRF9161 DK is equipped with a Debug IC (Atmel ATSAM3U2C) which provides the following functionality:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/nordic_nrf/nrf9161dk_nrf9161/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/nordic_nrf/nrf9161dk_nrf9161/.html#flashing-and-debugging-with-nordic-nrf-segger-j-link"
license: "BSD-3-Clause"
mode: "V"
---

nRF9161 DK is equipped with a Debug IC (Atmel ATSAM3U2C) which provides the
following functionality:

* Segger J-Link firmware and desktop tools
* SWD debug for the nRF9161 IC
* Mass Storage device for drag-and-drop image flashing
* USB CDC ACM Serial Port bridged to the nRFx UART peripheral
* Segger RTT Console
* Segger Ozone Debugger

To install the J-Link Software and documentation pack, follow the steps below:

#. Download the appropriate package from the J-Link Software and documentation pack website
#. Depending on your platform, install the package or run the installer
#. When connecting a J-Link-enabled board such as an nRF9161 DK, a
   drive corresponding to a USB Mass Storage device as well as a serial port should come up


### nRF Util Installation


nRF Util allows you to control your nRF9161 device from the command line,
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

BL2, S, and NS application images can be flashed into nRF9161 separately or may be merged
together into a single binary.


### Flashing the nRF9161 DK


To program the flash with a compiled TF-M image (i.e. S, NS or both) after having
followed the instructions to install the Segger J-Link Software and the nRFx
Command-Line Tools, follow the steps below:

Generate Intel hex files from the output binary (bin) files as follows:

```console

srec_cat build_app/tfm_s_ns_signed.bin -binary --offset 0x10000 \
      -o build_app/tfm_s_ns_signed.hex -intel
```
* Connect the micro-USB cable to the nRF9161 DK and to your computer
* Erase the flash memory in the nRF9161 IC:

```console

nrfutil device erase --all --x-family nrf91
```
* (Optionally) Erase the flash memory and reset flash protection and disable
   the read back protection mechanism if enabled.

```console

nrfutil device recover --x-family nrf91
```
* Flash the BL2 and TF-M image binaries from the sample folder of your choice:

```console

nrfutil device program --x-family nrf91 --firmware build_spe/bin/bl2.hex --options chip_erase_mode=ERASE_RANGES_TOUCHED_BY_FIRMWARE
nrfutil device program --x-family nrf91 --firmware build_app/tfm_s_ns_signed.hex --options chip_erase_mode=ERASE_RANGES_TOUCHED_BY_FIRMWARE
```
* Reset and start TF-M:

```console

nrfutil device reset --x-family nrf91
```

### Secure UART Console on nRF9161 DK


SECURE_UART1 is enabled by default when building TF-M on nRF9161 DK, so the secure firmware console output
is available via USART1.

Non-Secure console output is available via USART0.


**Note:** By default USART0 and USART1 outputs are routed to separate serial ports.

--------------

*Copyright (c) 2023, Nordic Semiconductor. All rights reserved.*
