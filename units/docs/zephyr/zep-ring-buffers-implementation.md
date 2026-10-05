---
id: "zep-ring-buffers-implementation"
type: "concept"
domain: "rtos"
title: "Ring Buffers: Implementation"
summary: "A ring buffer is defined using a variable of type ring_buf. It must then be initialized by calling ring_buf_init."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/data_structures/ring_buffers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/data_structures/ring_buffers.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining a Ring Buffer


A ring buffer is defined using a variable of type `ring_buf`.
It must then be initialized by calling `ring_buf_init`.

A ring buffer can be defined and initialized at compile time
using the macros at file scope. The macro defines the ring buffer
itself and its data buffer.

The following code defines a ring buffer:

```c

#define MY_RING_BUF_BYTES 93
RING_BUF_DECLARE(my_ring_buf, MY_RING_BUF_BYTES);
```

### Enqueuing Data


Bytes are copied to a ring buffer by calling
`ring_buf_put`.

```c

uint8_t my_data[MY_RING_BUF_BYTES];
uint32_t ret;

ret = ring_buf_put(&ring_buf, my_data, MY_RING_BUF_BYTES);
if (ret != MY_RING_BUF_BYTES) {
    /* not enough room, partial copy. */
...
}
```
Data can be added to a ring buffer by directly accessing the
ring buffer's memory.  For example:

```c

uint32_t size;
uint32_t rx_size;
uint8_t *data;

/* Get pointer to writable area within the ring buffer memory. */
size = ring_buf_put_ptr(&ring_buf, &data, 0);

/* Work directly on a ring buffer memory. */
rx_size = uart_rx(data, size);

/* Indicate amount of valid data. rx_size must be equal or less than size. */
ring_buf_commit(&ring_buf, rx_size);
```

### Retrieving Data


Data bytes are copied out from a ring buffer by calling
`ring_buf_get`. For example:

```c

uint8_t my_data[MY_DATA_BYTES];
size_t  ret;

ret = ring_buf_get(&ring_buf, my_data, sizeof(my_data));
if (ret != sizeof(my_data)) {
    /* Fewer bytes copied. */
} else {
    /* Requested amount of bytes retrieved. */
    ...
}
```
Data can be retrieved from a ring buffer by direct
operations on the ring buffer's memory.  For example:

```c

uint32_t size;
uint32_t proc_size;
uint8_t *data;

/* Get pointer to readable data within the ring buffer memory. */
size = ring_buf_get_ptr(&ring_buf, &data, 0);

/* Work directly on a ring buffer memory. */
proc_size = process(data, size);

/* Indicate amount of data that has been consumed. proc_size must be equal
 * or less than size.
 */
ring_buf_consume(&ring_buf, proc_size);
```
