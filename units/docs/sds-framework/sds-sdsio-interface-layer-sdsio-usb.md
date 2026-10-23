---
id: "sds-sdsio-interface-layer-sdsio-usb"
type: "concept"
domain: "test"
title: "SDSIO Interface: Layer: sdsio_usb"
summary: "The layer/sdsio/usb/sdsio_usb.clayer.yml is configured for recording and playback via the USB interface. It uses the MDK-Middleware USB Device component and connects to a host computer through a USB interface."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/sdsio.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md#layer-sdsio-usb"
license: "Apache-2.0"
mode: "V"
---

The [`layer/sdsio/usb/sdsio_usb.clayer.yml`](https://github.com/ARM-software/SDS-Framework/tree/main/layer/sdsio/usb) is configured for recording and playback via the USB interface. It uses the [MDK-Middleware](https://www.keil.arm.com/packs/mdk-middleware-keil) USB Device component and connects to a host computer through a USB interface.

(figure: SDS-Firmware with USB interface)

### Using USB Interface

To access [SDS data files](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/theory.md#sds-data-files), configure the `*.sdsio.yml` file with the [`interface - usb:`](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#usb) node and start the [SDSIO-Server](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sdsio-server) on the host computer with:

```bash
>python sdsio-server.py -c myproject.sdsio.yml
SDSIO-Server v3.1.0
Press 'Ctrl+C' or 'X' to exit.
Working directory: ...\SDS_data
SDSIO configuration YAML: ...\myproject.sdsio.yml
SDSIO command input: R=Record, P=playback, S/s=stop, T/t=reset, X/x=exit, A-H=set flags 0-7, a-h=clear flags 0-7.
SDSIO-Server waiting for USB SDSIO-Client...
SDSIO-Client USB device connected.
```
