---
id: "zep-logging-dictionary-based-logging"
type: "concept"
domain: "debug"
title: "Logging: Architecture / Dictionary-based Logging"
summary: "Dictionary-based logging, instead of human readable text, outputs the log messages in binary format. This binary format encodes arguments to formatted strings in their native storage formats which can be more compact than their text equivalents."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Architecture_

Dictionary-based logging, instead of human readable text, outputs the log
messages in binary format. This binary format encodes arguments to formatted
strings in their native storage formats which can be more compact than their
text equivalents. For statically defined strings (including the format
strings and any string arguments), references to the ELF file are encoded
instead of the whole strings. A dictionary created at build time contains
the mappings between these references and the actual strings. This allows
the offline parser to obtain the strings from the dictionary to parse
the log messages. This binary format allows a more compact representation
of log messages in certain scenarios. However, this requires the use of
an offline parser and is not as intuitive to use as text-based log messages.

Note that `long double` is not supported by Python's `struct` module.
Therefore, log messages with `long double` will not display the correct
values.



#### Configuration


Here are kconfig options related to dictionary-based logging:

- `CONFIG_LOG_DICTIONARY_SUPPORT` enables dictionary-based logging
  support. This should be selected by the backends which require it.

- The UART backend can be used for dictionary-based logging. These are
  additional config for the UART backend:

  - `CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_HEX` tells
    the UART backend to output hexadecimal characters for dictionary based
    logging. This is useful when the log data needs to be captured manually
    via terminals and consoles.

  - `CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_BIN` tells
    the UART backend to output binary data.

- The RTT backend can also be used for dictionary-based logging:

  - `CONFIG_LOG_BACKEND_RTT` enables the RTT backend.

  - `CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY` enables
    dictionary-based output for the RTT backend. Use together with
    `CONFIG_USE_SEGGER_RTT`.

  - `CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY_HEX` tells
    the RTT backend to output hexadecimal characters for dictionary based
    logging.



#### Usage


When dictionary-based logging is enabled via enabling related logging backends,
a JSON database file, named `log_dictionary.json`, will be created
in the build directory. This database file contains information for the parser
to correctly parse the log data. Note that this database file only works
with the same build, and cannot be used for any other builds.


##### Offline Parsing


To parse a previously captured log file:

```console

./scripts/logging/dictionary/log_parser.py <build dir>/log_dictionary.json <log data file>
```
The parser takes two required arguments, where the first one is the full path
to the JSON database file, and the second part is the file containing log data.
Add an optional argument `--hex` to the end if the log data file contains
hexadecimal characters
(e.g. when `CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_HEX=y`). This tells
the parser to convert the hexadecimal characters to binary before parsing.


##### Live Parsing


For real-time decoding of dictionary-based log output, use the live log parser.
It connects to a running device and continuously decodes binary log data as it
arrives. Note that the live parser only supports binary dictionary output
(not hex-encoded). The live parser supports three input modes:

**Serial (UART):**

```console

./scripts/logging/dictionary/live_log_parser.py <build dir>/log_dictionary.json serial <port> <baudrate>
```
For example, to read from `/dev/ttyACM0` at 115200 baud:

```console

./scripts/logging/dictionary/live_log_parser.py build/zephyr/log_dictionary.json serial /dev/ttyACM0 115200
```
**JLink RTT:**

```console

./scripts/logging/dictionary/live_log_parser.py <build dir>/log_dictionary.json jlink-rtt <device_name>
```
For example, to read RTT output from an nRF5340:

```console

./scripts/logging/dictionary/live_log_parser.py build/zephyr/log_dictionary.json jlink-rtt nrf5340_xxaa_app
```
The JLink RTT mode requires the `pylink-square` Python package
(`pip install pylink-square`). Optional arguments include `--channel` to
select the RTT channel (default: 0), `--speed` to set the connection speed,
and `--block-address` to specify the RTT control block address in hex.

**File / stdin:**

```console

./scripts/logging/dictionary/live_log_parser.py <build dir>/log_dictionary.json file <filepath>
```
When `<filepath>` is omitted, the parser reads from stdin, which allows piping
binary data directly into it.

Please refer to the logging-dictionary sample for more
examples on using the log parsers.
