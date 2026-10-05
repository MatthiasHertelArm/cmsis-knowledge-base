---
id: "sds-sdsio-interface-layer-sdsio-network"
type: "concept"
domain: "test"
title: "SDSIO Interface: Layer: sdsio_network"
summary: "The layer/sdsio/network/sdsionetwork.clayer.yml is configured for recording and playback via the Ethernet interface. It uses the MDK-Middleware Network component. Both the target hardware and the SDSIO-Server are connected to a local LAN."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/sdsio.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio-network"
license: "Apache-2.0"
mode: "V"
---

The [`layer/sdsio/network/sdsio_network.clayer.yml`](https://github.com/ARM-software/SDS-Framework/tree/main/layer/sdsio/network) is configured for recording and playback via the Ethernet interface. It uses the  [MDK-Middleware](https://www.keil.arm.com/packs/mdk-middleware-keil) Network component. Both the target hardware and the SDSIO-Server are connected to a local LAN.

(figure: SDS-Firmware with Network interface)

!!! Note
    - The target device and the host computer must be connected to the same network. With a standard network installation, the DHCP server assigns IP addresses automatically.
    - On **Windows**, a firewall may restrict socket connections. To allow the SDSIO-Server through the Windows Defender Firewall:
        - Open **Windows Security - Firewall & network protection - Allow an app through firewall**.
        - Click **Change settings**, then allow your Python runtime (`python.exe`) on the network profile you use (usually Private).
        - On a managed corporate PC, Group Policy or endpoint security may still block connections. Your IT administrator may need to whitelist the IP address and port.

### Using Network Interface

To access [SDS data files](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/theory.md#sds-data-files), configure the `*.sdsio.yml` file with the [`interface - socket:`](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#socket) node for Network interface, and start the [SDSIO-Server](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#sdsio-server) on the host computer with:

```bash
>python sdsio-server.py -c myproject.sdsio.yml
SDSIO-Server v3.1.0
Press 'Ctrl+C' or 'X' to exit.
Working directory: ...\SDS_data
SDSIO configuration YAML: ...\myproject.sdsio.yml
SDSIO command input: R=Record, P=playback, S/s=stop, T/t=reset, X/x=exit, A-H=set flags 0-7, a-h=clear flags 0-7.
SDSIO-Server listening on 192.0.2.10:5050...
```

!!! Note
    The SDSIO-Server prints the IP address on which it is listening. The target hardware must connect to this IP address. Configure the target by updating the `SDSIO_SOCKET_SERVER_IP` macro in `layer/sdsio/network/RTE/SDS/sdsio_client_socket_config.h`.
