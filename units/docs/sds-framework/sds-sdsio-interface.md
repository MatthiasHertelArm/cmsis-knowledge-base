---
id: "sds-sdsio-interface"
type: "concept"
domain: "test"
title: "SDSIO Interface"
summary: "The SDSIO components offer flexible SDS communication interfaces. You may choose between these interface components that are stored in the folders: sds/sdsio/client, sds/sdsio/fs or sds/sdsio/vsi."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/sdsio.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md"
license: "Apache-2.0"
mode: "V"
---

The SDSIO components offer flexible SDS communication interfaces. You may choose between these interface components that are stored in the folders: `sds/sdsio/client`, `sds/sdsio/fs` or `sds/sdsio/vsi`. You may use one of the following CMSIS software components for integration of the SDSIO interface into the target system:

```yml
  - component: SDS:IO:Socket                     # IoT Socket Interface (Ethernet or WiFi)
  - component: SDS:IO:USB&MDK USB                # USB Interface
  - component: SDS:IO:RTT                        # RTT Interface
  - component: SDS:IO:Serial&CMSIS USART         # USART Interface
  - component: SDS:IO:File System&MDK FS         # Memory card
  - component: SDS:IO:VSI                        # VSI Simulation interface of an AVH FVP
  - component: SDS:IO:Custom                     # Source code template for custom implementation
```

To simplify usage further, pre-configured SDS interface layers in *csolution project format* are available. These connect via various interfaces to the SDSIO-Server, which provides read/write access to SDS data files. The following SDS interface layers are available in the pack [`ARM::SDS`](https://www.keil.arm.com/packs/sds-arm):

- [Ethernet Interface](#layer-sdsio_network) using the MDK-Middleware Network component.
- [USB Bulk Interface](#layer-sdsio_usb) using the MDK-Middleware USB component.
- [RTT Interface](#layer-sdsio_rtt) using the SEGGER RTT component.
- [Memory Card Interface](#layer-sdsio_fs) using the MDK-Middleware File System component.
- [VSI Interface](#layer-sdsio_fvp) using the ARM FVP simulation VSI interface.
