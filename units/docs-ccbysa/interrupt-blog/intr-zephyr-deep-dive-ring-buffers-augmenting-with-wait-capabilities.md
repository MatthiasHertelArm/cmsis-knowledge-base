---
id: "intr-zephyr-deep-dive-ring-buffers-augmenting-with-wait-capabilities"
type: "concept"
domain: "debug"
title: "Zephyr Deep Dive: Ring Buffers: Augmenting With Wait Capabilities"
summary: "In the simplest case of a single producer and consumer, the producer can use a semaphore to signal to the consumer data is available."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-24-zephyr-ring-buffers.md"
doc_source: "https://interrupt.memfault.com/blog/zephyr-ring-buffers#augmenting-with-wait-capabilities"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the simplest case of a single producer and consumer, the producer can use a
semaphore to signal to the consumer data is available. Let’s take a look at the
`eswifi` driver, but this time at the function that wraps
`eswifi_uart_get_resp`:

```c
static int eswifi_uart_wait_prompt(struct eswifi_uart_data *uart)
{
  unsigned int max_retries = 60 * 1000; /* 1 minute */
  int err;

  while (--max_retries) {
    err = eswifi_uart_get_resp(uart);
    if (err) {
      LOG_DBG("Err: 0x%08x - %d", err, err);
      return err;
    }

    if (uart->fsm == ESWIFI_UART_FSM_END) {
      LOG_DBG("Success!");
      return uart->rx_count;
    }

    /* allow other threads to be scheduled */
    k_sleep(K_MSEC(1));
  }

  LOG_DBG("Timeout");
  return -ETIMEDOUT;
}
```

We can see that this function relies on the response being sent within 60
seconds of the call to wait for the response. In the worst case, this code will
require a context-switch 60,000 times as each call to `k_sleep` allows a ready
thread to take over. Additionally, many short sleeps like this introduce more
jitter than a single timeout. So not only does this cause many more context
switches, but it is also less accurate in terms of timing. A semaphore signaled
from `eswifi_iface_uart_isr` would only require a single switch after timing
out. Here is an example of what this improvement could look like:

```c
// Initialize the semaphore with an initial count of 0 and a max of 1
K_SEM_DEFINE(response_sem, 0, 1);

static void eswifi_iface_uart_isr(const struct device *uart_dev,
        void *user_data)
{
  // ... rest of code
  ring_buf_put_finish(&uart->rx_rb, total_size);

  // Raise signal to eswifi_uart_wait_prompt
  k_sem_give(&response_sem);
}

static int eswifi_uart_wait_prompt(struct eswifi_uart_data *uart) {
  int err;

  // Wait for the UART state machine to reach end state
  // Timeout occurs after 10 seconds since last data received
  while (uart->fsm != ESWIFI_UART_FSM_END) {
    // Returns non-zero value on timeout
    if (k_sem_take(&response_sem, K_SECONDS(10))) {
      return -ETIMEDOUT;
    }

    err = eswifi_uart_get_resp(uart);
    if (err) {
      LOG_DBG("Err: 0x%08x - %d", err, err);
      return err;
    }
  }

  LOG_DBG("Success");
  return uart->rx_count;
}
```

The reworked code has several advantages:

- A more responsive driver when waiting for responses (pun intended)
- `eswifi_uart_wait_prompt` has simpler logic. It fails quickly if it does not
  receive data
- We reduce the number of unnecessary context switches
- The macro, `K_SEM_DEFINE`[^4], prevents annoying race conditions if the kernel
  object has not yet been initialized before the UART interrupt is enabled

The only disadvantage here is a small hit to RAM due to the new semaphore. I
think this is a worthwhile trade-off.
