---
id: "zep-tracing-serialization-formats"
type: "concept"
domain: "debug"
title: "Tracing: Serialization Formats"
summary: "Common Trace Format, CTF, is an open format and language to describe trace formats. This enables tool reuse, of which line-textual (babeltrace) and graphical (TraceCompass) variants already exist."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

### Common Trace Format (CTF) Support


Common Trace Format, CTF, is an open format and language to describe trace
formats. This enables tool reuse, of which line-textual (babeltrace) and
graphical (TraceCompass) variants already exist.

CTF should look familiar to C programmers but adds stronger typing.
See `CTF - A Flexible, High-performance Binary Trace Format
<https://diamon.org/ctf/>`_.


CTF allows us to formally describe application specific payload and the
serialization format, which enables common infrastructure for host tools
and parsers and tools for filtering and presentation.



#### A Generic Interface


In CTF, an event is serialized to a packet containing one or more fields.
As seen from *I/O taxonomy* section below, a bottom layer may:

- perform actions at transaction-start (e.g. mutex-lock),
- process each field in some way (e.g. sync-push emit, concat, enqueue to
  thread-bound FIFO),
- perform actions at transaction-stop (e.g. mutex-release, emit of concat
  buffer).


#### CTF Top-Layer Example


The CTF_EVENT macro will serialize each argument to a field::
```
/* Example for illustration */
static inline void ctf_top_foo(uint32_t thread_id, ctf_bounded_string_t name)
{
  CTF_EVENT(
    CTF_LITERAL(uint8_t, 42),
    thread_id,
    name,
    "hello, I was emitted from function: ",
    __func__  /* __func__ is standard since C99 */
  );
}
```
How to serialize and emit fields as well as handling alignment, can be done
internally and statically at compile-time in the bottom-layer.


The CTF top layer is enabled using the configuration option
`CONFIG_TRACING_CTF` and can be used with the different transport
backends both in synchronous and asynchronous modes.
