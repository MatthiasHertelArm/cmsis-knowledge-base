---
id: "zep-tracing-using-tracing"
type: "concept"
domain: "debug"
title: "Tracing: Using Tracing"
summary: "The sample samples/subsys/tracing demonstrates tracing with different formats and backends."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

The sample `samples/subsys/tracing` demonstrates tracing with
different formats and backends.

To get started, the simplest way is to use the CTF format with the
native_sim port, build the sample as follows:

You can then run the resulting binary with the option `-trace-file` to generate
the tracing data::
```
mkdir data
cp $ZEPHYR_BASE/subsys/tracing/ctf/tsdl/metadata data/
./build/zephyr/zephyr.exe -trace-file=data/channel0_0
```
The resulting CTF output can be visualized using babeltrace or TraceCompass
by pointing the tool to the `data` directory with the metadata and trace files.


### Using RAM backend


For devices that do not have available I/O for tracing such as USB or UART but have
enough RAM to collect trace data, the ram backend can be enabled with configuration
`CONFIG_TRACING_BACKEND_RAM`.
Adjust `CONFIG_RAM_TRACING_BUFFER_SIZE` to be able to record enough traces for your needs.
Then thanks to a runtime debugger such as gdb this buffer can be fetched from the target
to an host computer::
```
(gdb) dump binary memory data/channel0_0 <ram_tracing_start> <ram_tracing_end>
```
The resulting channel0_0 file have to be placed in a directory with the `metadata`
file like the other backend.
