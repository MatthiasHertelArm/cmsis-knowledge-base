---
id: "intr-zephyr-deep-dive-ring-buffers-zephyr-ring-buffers"
type: "concept"
domain: "debug"
title: "Zephyr Deep Dive: Ring Buffers: Zephyr Ring Buffers"
summary: "Ring buffers[^1] in Zephyr provide a way to pass data through a shared memory buffer. Ring buffers are safely used in single-consumer, single-producer scenarios. Their usage generally follows the diagram below:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-24-zephyr-ring-buffers.md"
doc_source: "https://interrupt.memfault.com/blog/zephyr-ring-buffers#zephyr-ring-buffers"
license: "CC-BY-SA-4.0"
mode: "V"
---

Ring buffers[^1] in Zephyr provide a way to pass data through a shared memory
buffer. Ring buffers are safely used in single-consumer, single-producer
scenarios. Their usage generally follows the diagram below:

(figure: General usage of a ring buffer in Zephyr)

The producer writes to the ring buffer via the `ring_buf_put` functions, while
the reader reads from the ring buffer with the `ring_buf_get` functions. Next,
we will explore the two interfaces provided: the bytes-based API and the
items-based API.

### Bytes API

The ring buffer bytes API is often used in driver implementations, where a piece
of hardware needs to send chunks of data up to a higher layer for further
processing. We will look at the `eswifi` driver[^2] as a guide for ring buffer
bytes API operation and walk through some of the driver code to understand its
use. This driver uses AT commands to interface with a WiFi module over a UART.
Let’s start with the initialization code:

```c
struct eswifi_uart_data {
  // ... rest of code
  uint8_t iface_rb_buf[ESWIFI_RING_BUF_SIZE];
  struct ring_buf rx_rb;
};

int eswifi_uart_init(struct eswifi_dev *eswifi)
{
  // ... rest of code
  ring_buf_init(&uart->rx_rb, sizeof(uart->iface_rb_buf),
          uart->iface_rb_buf);
  // ... rest of code
}
```

We can see from this initialization that we have two components to set up. The
structure containing the state of the ring buffer object,
`eswifi_uart_data.rx_rb`, and the underlying shared buffer,
`eswifi_uart_data.iface_rb_buf`. Next, let’s examine how the driver writes to
the ring buffer:

```c
static void eswifi_iface_uart_isr(const struct device *uart_dev,
        void *user_data)
{
struct eswifi_uart_data *uart = &eswifi_uart0; /* Static instance */
  int rx = 0;
  uint8_t *dst;
  uint32_t partial_size = 0;
  uint32_t total_size = 0;

  ARG_UNUSED(user_data);

  while (uart_irq_update(uart->dev) &&
          uart_irq_rx_ready(uart->dev)) {
    if (!partial_size) {
      partial_size = ring_buf_put_claim(&uart->rx_rb, &dst,
                UINT32_MAX);
    }
    if (!partial_size) {
      LOG_ERR("Rx buffer doesn't have enough space");
      eswifi_iface_uart_flush(uart);
      break;
    }

    rx = uart_fifo_read(uart->dev, dst, partial_size);
    if (rx <= 0) {
      continue;
    }

    dst += rx;
    total_size += rx;
    partial_size -= rx;
  }

  ring_buf_put_finish(&uart->rx_rb, total_size);
}
```

When the MCU receives data over the UART from the WiFi module, the UART
peripheral runs the interrupt handler, `eswifi_iface_uart_isr`. Next, the
interrupt handler repeatedly checks for available data. If data is available,
the driver calls `ring_buf_put_claim`. The `put_claim` operation reserves up to
the provided size in the ring buffer for writing and returns the number of bytes
claimed. A return of 0 indicates the ring buffer is full. The write operation
then becomes a simple copy into the shared buffer. After copying the data, the
handler calls `ring_buf_put_finish` to signal completion.

If the ring buffer is full (i.e. the `put_claim` returns 0), the driver drops
the current batch of data received because we cannot block to wait for new data
in this interrupt. Resolving this issue may require increasing the ring buffer
size to account for pressure on the ring buffer. It is difficult to trace the
specific instance when the buffer completely filled. One way to determine the
proper size is to add an assertion when the `put_claim` fails to reserve any
data. Asserting in this manner is a technique of offensive programming[^3], as
this modification proactively looks for an issue and fails purposefully.

The main driver work is done within the context of a dedicated driver workqueue.
The workqueue operates as a dedicated cooperative thread that sleeps until new
work is submitted. In our case, the work starts with requests sent to the WiFi
module and ends with responses sent back. The code below shows how the function,
`eswifi_uart_get_resp` reads data from the ring buffer to parse responses from
the WiFi module:

```c
static int eswifi_uart_get_resp(struct eswifi_uart_data *uart)
{
  uint8_t c;

  while (ring_buf_get(&uart->rx_rb, &c, 1) > 0) {
      LOG_DBG("FSM: %c, RX: 0x%02x : %c",
        get_fsm_char(uart->fsm), c, c);

      if (uart->rx_buf_size > 0) {
        uart->rx_buf[uart->rx_count++] = c;

        if (uart->rx_count == uart->rx_buf_size) {
          return -ENOMEM;
        }
      }
    // ... rest of code
  }
// ... rest of code
}
```

Two things stand out compared to the code that wrote data to the ring buffer.
The first is the usage of `ring_buf_get` instead of the claim-based API. When the
interrupt handler receives UART data, the handler does not immediately know how
much to write into the ring buffer. The claim-based function allows the handler
to use the buffer directly, minimizing copying operations. However, the driver
function, `eswifi_uart_get_resp`, must copy the data for later processing. There
is a bit of an asymmetry by design here. The interrupt handler does not do any
processing on the data. It simply hands the data off to the workqueue and moves
on to the next read. The workqueue, on the other hand, does need to keep this
data around to complete processing the response! The utility of the ring buffer
is that it supports both cases and allows for clear code.

The second thing to note is that the interrupt handler writes in variable
lengths while read operations are a constant length. The ring buffer offers
flexibility in the amount of data being written to or read from the buffer.

### Items API

In addition to the standard bytes-based API, there is the ring buffer items
API. In this version, data is written to and read from the ring buffer as an
item with three components:

1. An application-defined type
2. An application-defined integer value
3. An optional array of associated data

This metadata adds some structure to the data. The type helps identify what the
item contains. The integer value represents either additional metadata or the
value of the item. We can view ring-buffers using this API as better suited to
passing data with some structure rather than a raw array of bytes (e.g.
packet-oriented protocols). For instance, we could parse different items by type
to produce different messages, or route data to different destinations based on
the integer value.
