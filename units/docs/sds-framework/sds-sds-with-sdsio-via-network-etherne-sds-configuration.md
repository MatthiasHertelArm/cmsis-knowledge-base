---
id: "sds-sds-with-sdsio-via-network-etherne-sds-configuration"
type: "concept"
domain: "test"
title: "SDS with SDSIO via Network (Ethernet): SDS Configuration"
summary: "The following SDS software components are required:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:layer/sdsio/network/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/layer/sdsio/network/README.md#sds-configuration"
license: "Apache-2.0"
mode: "V"
---

The following SDS software components are required:

```yml
  - component: SDS:Stream&CMSIS-RTOS2
  - component: SDS:IO:Socket
```

The IP address of the SDSIO-Server must be updated in `sdsio_client_socket_config.h` with the
(`Socket server listing`) address reported by the SDSIO-Server at startup:

```c
#define SDSIO_SOCKET_SERVER_IP    "0.0.0.0"
```

You can leave the other configuration settings at their default values.
