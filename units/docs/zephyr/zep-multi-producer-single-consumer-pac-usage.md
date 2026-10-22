---
id: "zep-multi-producer-single-consumer-pac-usage"
type: "concept"
domain: "rtos"
title: "Multi Producer Single Consumer Packet Buffer: Usage"
summary: "Packet header details can be found in include/zephyr/sys/mpsc_packet.h. API functions can be found in include/zephyr/sys/mpsc_pbuf.h. Headers are split to avoid include spam when declaring the packet."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/mpsc_pbuf.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/mpsc_pbuf.rst"
license: "Apache-2.0"
mode: "V"
---

### Packet header definition


Packet header details can be found in `include/zephyr/sys/mpsc_packet.h`.
API functions can be found in `include/zephyr/sys/mpsc_pbuf.h`. Headers
are split to avoid include spam when declaring the packet.

User header structure must start with internal header:

```c

#include <zephyr/sys/mpsc_packet.h>

struct foo_header {
        MPSC_PBUF_HDR;
        uint32_t length: 32 - MPSC_PBUF_HDR_BITS;
};
```

### Packet buffer configuration


Configuration structure contains buffer details, configuration flags and
callbacks. Following callbacks are used by the packet buffer:

* Drop notification - callback called whenever a packet is dropped due to
  overwrite.
* Get packet length - callback to determine packet length


### Packet producing


Standard, two step method:

```c

foo_packet *packet = mpsc_pbuf_alloc(buffer, len, K_NO_WAIT);

fill_data(packet);

mpsc_pbuf_commit(buffer, packet);
```
Performance optimized storing of small packets:

* 32 bit word packet
* 32 bit word with pointer packet

Note that since packets are written by value, they should already contain
`valid` bit set in the header.

```c

mpsc_pbuf_put_word(buffer, data);
mpsc_pbuf_put_word_ext(buffer, data, ptr);
```

### Packet consuming


Two step method:

```c

foo_packet *packet = mpsc_pbuf_claim(buffer);

process(packet);

mpsc_pbuf_free(buffer, packet);
```
