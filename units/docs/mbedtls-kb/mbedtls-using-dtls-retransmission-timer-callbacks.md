---
id: "mbedtls-using-dtls-retransmission-timer-callbacks"
type: "concept"
domain: "security"
title: "Using DTLS: Retransmission: timer callbacks"
summary: "The (D)TLS handshake is a lock-step procedure: messages need to arrive in a certain order and cannot be skipped."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/dtls-tutorial.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/dtls-tutorial.md#retransmission-timer-callbacks"
license: "Apache-2.0"
mode: "V"
---

The (D)TLS handshake is a lock-step procedure: messages need to arrive in a certain order and cannot be skipped.

To achieve this on top of UDP, DTLS has its own retransmission mechanism, which needs timers. In Mbed TLS, the SSL module accepts a pair of callbacks for timer functions, which can be set using `mbedtls_ssl_set_timer_cb()`. Example callbacks (for Unix and Windows) are provided in `timing.c`, namely `mbedtls_timing_set_delay()` and `mbedtls_timing_get_delay()`, that are suitable for use with blocking I/O.

The callbacks have the following interface:
```
  void mbedtls_timing_set_delay( void *data, uint32_t int_ms, uint32_t fin_ms );
  int mbedtls_timing_get_delay( void *data );
```
In both cases, `data` is a context shared by the callbacks. The **setting** function accepts two delays: an **intermediate** and a **final** one, and the **getting** function tells the caller which of these delays are expired, if any (see the documentation of [`mbedtls_ssl_set_timer_cb()`](https://github.com/api/ssl_8h.html#a335ee78886daf7f8fb369fa925b3cca8) for details). The final delay is used to indicate when retransmission should happen, while the intermediate delay is an internal implementation detail whose semantic may evolve in future versions.

The interface was designed to allow a variety of implementation strategies, two of which two are:

* Timestamps.
    * The setting function records a timestamp and the values of the delay in the context, and the getting function compares the stored timestamp with the current time.

This is the strategy used by the example callbacks in `timing.c`. It is suitable when you know the application will call `mbedtls_ssl_handshake()` repeatedly until it returns `0` or a fatal error, which is usually the case when using blocking I/O.

* Timers and events.
    * The setting function ensures (for example using a hardware timer or a system call) that a timeout handler will be called when one of the delays expires. This timeout handler needs to at least record the information about which delay expired so that the getting function can return the proper value. For the intermediate delay, this is all you need to do (the information **may** be used internally **if** another event, such as an incoming packet, causes `mbedtls_ssl_handshake()` to be called again before the final delay expires).

For the final delay however, if you are using an event-driven style of programming, the timeout handler needs to generate an event that will cause `mbedtls_ssl_handshake()` to be called again. Our DTLS handshake code will then internally call the `get_delay()` function, notice the delays are expired, and take the appropriate action (either retransmit the last flight of messages or give up on the handshake and return a timeout error).

**Note:** You need to make sure that calling `set_delay()` while a timer is already running cancels it (more precisely, that no event will be generated when the final delay expires). In particular, after a call like `set_delay(0, 0)`, no timer should be running any more. Said otherwise, there should be at most one running timer at any given time.

**Note:** If you have multiple concurrent connections, you need to make sure each has its own independent set of timers, and that, when a timeout event is generated for one connection, `mbedtls_ssl_handshake()` is called with the appropriate `ssl_context` for that connection (the `data` argument for the callbacks can be used to store the required information). You also need to avoid making multiple calls to `mbedtls_ssl_handshake()` with the same `ssl_context` at the same time.

With event-based I/O, **don't** use read timeouts by calling `mbedtls_ssl_conf_read_timeout()` with a non-zero value, for two reasons:

* It's unnecessary, as you only call `mbedtls_ssl_read()` when data is ready to be read.
* It makes your timeout handler more complex, as it would have to know whether the timeout happened during handshake or read in order to schedule the appropriate function.
