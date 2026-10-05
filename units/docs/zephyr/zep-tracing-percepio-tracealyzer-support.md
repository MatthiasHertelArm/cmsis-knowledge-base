---
id: "zep-tracing-percepio-tracealyzer-support"
type: "concept"
domain: "debug"
title: "Tracing: Tracing Tools / Percepio Tracealyzer Support"
summary: "Zephyr includes support for Percepio Tracealyzer that offers trace visualization for simplified analysis, report generation and other analysis features. Tracealyzer allows for trace streaming over various interfaces and also snapshot tracing, where the events are kept in a RAM buffer."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Tracing Tools_

Zephyr includes support for Percepio Tracealyzer that offers trace visualization for
simplified analysis, report generation and other analysis features. Tracealyzer allows for trace
streaming over various interfaces and also snapshot tracing, where the events are kept in a RAM
buffer.

Zephyr kernel events are captured automatically when Tracealyzer tracing is enabled.
Tracealyzer also provides extensive support for application logging, where you call the tracing
library from your application code. This lets you visualize kernel events and application events
together, for example as data plots or state diagrams on logged variables.
Learn more in the Tracealyzer User Manual provided with the application.


#### Percepio TraceRecorder and Stream Ports

The tracing library for Tracealyzer (TraceRecorder) is included in the Zephyr manifest and
provided under the same license (Apache 2.0). This is enabled by adding the following
configuration options in your prj.conf:

```cfg

CONFIG_TRACING=y
CONFIG_PERCEPIO_TRACERECORDER=y
```
Or using menuconfig:

* Enable `Subsystems and OS Services --> Tracing Support`
* Under `Subsystems and OS Services --> Tracing Support --> Tracing Format`, select
  `Percepio Tracealyzer`

Some additional settings are needed to configure TraceRecorder. The most important configuration
is to select the right "stream port". This specifies how to output the trace data.
As of July 2024, the following stream ports are available in the Zephyr configuration system:

* **Ring Buffer**: The trace data is kept in a circular RAM buffer.
* **RTT**: Trace streaming via Segger RTT on J-Link debug probes.
* **ITM**: Trace streaming via the ITM function on Arm Cortex-M devices.
* **Semihost**: For tracing on QEMU. Streams the trace data to a host file.

Select the stream port in menuconfig under
`Modules --> percepio --> TraceRecorder --> Stream Port`.

Or simply add one of the following options in your prj.conf:

```cfg

CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER=y
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT=y
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM=y
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ZEPHYR_SEMIHOST=y
```
Make sure to only include ONE of these configuration options.

The stream port modules have individual configuration options. In menuconfig these are found
under `Modules --> percepio --> TraceRecorder --> (Stream Port) Config`.
The most important options for each stream port are described below.


#### Tracealyzer Snapshot Tracing (Ring Buffer)


The "Ring Buffer" stream port keeps the trace data in a RAM buffer on the device.
By default, this is a circular buffer, meaning that it always contains the most recent data.
This is used to dump "snapshots" of the trace data, e.g. by using the debugger. This usually only
allows for short traces, unless you have megabytes of RAM to spare, so it is not suitable for
profiling. However, it can be quite useful for debugging in combination with breakpoints.
For example, if you set a breakpoint in an error handler, a snapshot trace can show the sequence
of events leading up to the error. Snapshot tracing is also easy to begin with, since it doesn't
depend on any particular debug probe or other development tool.

To use the Ring Buffer option, make sure to have the following configuration options in your
prj.cnf:

```cfg

CONFIG_TRACING=y
CONFIG_PERCEPIO_TRACERECORDER=y
CONFIG_PERCEPIO_TRC_START_MODE_START=y
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER=y
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_SIZE=<size in bytes>
```
Or if using menuconfig:

* Enable `Subsystems and OS Services --> Tracing Support`
* Under `Subsystems and OS Services --> Tracing Support --> Tracing Format`, select
  `Percepio Tracealyzer`
* Under `Modules --> percepio --> TraceRecorder --> Recorder Start Mode`, select
  `Start`
* Under `Modules --> percepio --> TraceRecorder --> Stream Port`, select
  `Ring Buffer`
* Under `Modules --> percepio --> TraceRecorder --> Ring Buffer Config --> Buffer Size`,
  set the buffer size in bytes.

The default buffer size can be reduced if you are tight on RAM, or increased if you have RAM to
spare and want longer traces. You may also optimize the Tracing Configuration settings to get
longer traces by filtering out less important events.
In menuconfig, see
`Subsystems and OS Services --> Tracing Support --> Tracing Configuration`.

To view the trace data, the easiest way is to start your debugger (west debug) and run the
following GDB command::
```
dump binary value trace.bin *RecorderDataPtr
```
The resulting file is typically found in the root of the build folder, unless a different path is
specified. Open this file in Tracealyzer by selecting `File --> Open --> Open File`.


#### Tracealyzer Streaming with SEGGER RTT


Tracealyzer has built-in support for SEGGER RTT to receive trace data using a J-Link probe.
This allows for recording very long traces. To configure Zephyr for RTT streaming to Tracealyzer,
add the following configuration options in your prj.cnf:

```cfg

CONFIG_TRACING=y
CONFIG_PERCEPIO_TRACERECORDER=y
CONFIG_PERCEPIO_TRC_START_MODE_START_FROM_HOST=y
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT=y
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_UP_BUFFER_SIZE=<size in bytes>
```
Or if using menuconfig:

* Enable `Subsystems and OS Services --> Tracing Support`
* Under `Subsystems and OS Services --> Tracing Support --> Tracing Format`, select
  `Percepio Tracealyzer`
* Under `Modules --> percepio --> TraceRecorder --> Recorder Start Mode`, select
  `Start From Host`
* Under `Modules --> percepio --> TraceRecorder --> Stream Port`, select
  `RTT`
* Under `Modules --> percepio --> TraceRecorder --> RTT Config`, set the size of the
  RTT "up" buffer in bytes.

The setting `RTT buffer size up` sets the size of the RTT transmission buffer. This is important
for throughput. By default this buffer is quite large, 5000 bytes, to give decent performance
also on onboard J-Link debuggers (they are not as fast as the stand-alone probes).
If you are tight on RAM, you may consider reducing this setting. If using a regular J-Link probe
it is often sufficient with a much smaller buffer, e.g. 1 KB or less.

Learn more about RTT streaming in the Tracealyzer User Manual.
See Creating and Loading Traces -> Percepio TraceRecorder -> Using TraceRecorder v4.6 or later ->
Stream ports (or search for RTT).


#### Tracealyzer Streaming with Arm ITM


This stream port is for Arm Cortex-M devices featuring the ITM unit. It is recommended to use a
fast debug probe that allows for SWO speeds of 10 MHz or higher. To use this stream port,
apply the following configuration options:

```cfg

CONFIG_TRACING=y
CONFIG_PERCEPIO_TRACERECORDER=y
CONFIG_PERCEPIO_TRC_START_MODE_START=y
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM=y
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM_PORT=1
```
Or if using menuconfig:

* Enable `Subsystems and OS Services --> Tracing Support`
* Under `Subsystems and OS Services --> Tracing Support --> Tracing Format`, select
  `Percepio Tracealyzer`
* Under `Modules --> percepio --> TraceRecorder --> Recorder Start Mode`, select
  `Start`
* Under `Modules --> percepio --> TraceRecorder --> Stream Port`, select
  `ITM`
* Under `Modules --> percepio --> TraceRecorder --> ITM Config`, set the ITM port to
  1.

The main setting for the ITM stream port is the ITM port (0-31). A dedicated channel is needed
for Tracealyzer. Port 0 is usually reserved for printf logging, so channel 1 is used by default.

The option `Use internal buffer` should typically remain disabled. It buffers the data in RAM
before transmission and defers the data transmission to the periodic TzCtrl thread.

The host-side setup depends on what debug probe you are using. Learn more in the Tracealyzer
User Manual.
See `Creating and Loading Traces --> Percepio TraceRecorder --> Using TraceRecorder v4.6 or later --> Stream ports (or search for ITM)`.


#### Tracealyzer Streaming from QEMU (Semihost)


This stream port is designed for Zephyr tracing in QEMU. This can be an easy way to get started
with tracing and try out streaming trace without needing a fast debug probe. The data is streamed
to a host file using semihosting. To use this option, apply the following configuration options:

```cfg

CONFIG_SEMIHOST=y
CONFIG_TRACING=y
CONFIG_PERCEPIO_TRACERECORDER=y
CONFIG_PERCEPIO_TRC_START_MODE_START=y
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ZEPHYR_SEMIHOST=y
```
Using menuconfig

* Enable `General Architecture Options --> Semihosting support for Arm and RISC-V targets`
* Enable `Subsystems and OS Services --> Tracing Support`
* Under `Subsystems and OS Services --> Tracing Support --> Tracing Format`, select
  `Percepio Tracealyzer`
* Under `Modules --> percepio --> TraceRecorder --> Recorder Start Mode`, select
  `Start`
* Under `Modules --> percepio --> TraceRecorder --> Stream Port`, select
  `Semihost`

By default, the resulting trace file is found in `./trace.psf` in the root of the build folder,
unless a different path is specified. Open this file in Percepio Tracealyzer by selecting
`File --> Open --> Open File`.


#### Recorder Start Mode


You may have noticed the `Recorder Start Mode` option in the Tracealyzer examples above.
This decides when the tracing starts. With the option `Start`, the tracing begins directly
at startup, once the TraceRecorder library has been initialized. This is recommended when using the
Ring Buffer and Semihost stream ports.

For streaming via RTT or ITM you may also use `Start From Host` or
`Start Await Host`. Both listens for start commands from the Tracealyzer application. The
latter option, `Start Await Host`, causes the TraceRecorder initialization to block until
the start command is received from the Tracealyzer application.


#### Custom Stream Ports for Tracealyzer


The stream ports are small modules within TraceRecorder that define what functions to call to
output the trace data and (optionally) how to read start/stop commands from Tracealyzer.
It is fairly easy to make custom stream ports to implement your own data transport and
Tracealyzer can receive trace streams over various interfaces, including files, sockets,
COM ports, named pipes and more. Note that additional stream port modules are available in the
TraceRecorder repo (e.g. lwIP), although they might require modifications to work with Zephyr.


#### Learning More


Learn more about how to get started in the Tracealyzer Getting Started Guides.
