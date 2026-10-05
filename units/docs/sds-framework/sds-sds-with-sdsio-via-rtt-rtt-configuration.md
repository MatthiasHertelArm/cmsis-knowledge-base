---
id: "sds-sds-with-sdsio-via-rtt-rtt-configuration"
type: "concept"
domain: "test"
title: "SDS with SDSIO via RTT: RTT Configuration"
summary: "The following SEGGER RTT software components are required:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:layer/sdsio/rtt/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/layer/sdsio/rtt/README.md#rtt-configuration"
license: "Apache-2.0"
mode: "V"
---

The following SEGGER RTT software components are required:

```yml
  - component: SEGGER:RTT
```

The RTT channel number used for SDSIO is configured in
`./RTE/SDS/sdsio_client_rtt_config.h` with the `SDSIO_RTT_CHANNEL` define (default: `1`).
