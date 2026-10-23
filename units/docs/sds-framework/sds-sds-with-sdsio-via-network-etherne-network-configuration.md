---
id: "sds-sds-with-sdsio-via-network-etherne-network-configuration"
type: "concept"
domain: "test"
title: "SDS with SDSIO via Network (Ethernet): Network Configuration"
summary: "The following MDK-Middleware Network software components are required:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:layer/sdsio/network/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/layer/sdsio/network/README.md#network-configuration"
license: "Apache-2.0"
mode: "V"
---

The following MDK-Middleware Network software components are required:

```yml
  - component: Network&MDK:CORE
  - component: Network&MDK:Interface:ETH
  - component: Network&MDK:Service:DNS Client
  - component: Network&MDK:Socket:BSD
  - component: Network&MDK:Socket:TCP
  - component: Network&MDK:Socket:UDP
```

The communication does not use the **IPv6** protocol, therefore the variant `IPv4 only` can be selected in `Net_Config.h`:

```c
#define NET_CORE_VARIANT        0
```

You can leave the other configuration settings at their default values.
