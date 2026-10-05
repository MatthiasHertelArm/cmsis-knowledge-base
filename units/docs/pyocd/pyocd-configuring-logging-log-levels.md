---
id: "pyocd-configuring-logging-log-levels"
type: "concept"
domain: "debug"
title: "Configuring logging: Log levels"
summary: "There are multiple log levels, in order from least to most verbose: - CRITICAL - ERROR - WARNING - INFO - DEBUG"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/configuring_logging.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/configuring_logging.md#log-levels"
license: "Apache-2.0"
mode: "V"
---

There are multiple log levels, in order from least to most verbose:
- CRITICAL
- ERROR
- WARNING
- INFO
- DEBUG

The CRITICAL level is used only by the `pyocd` tool for reporting fatal errors.

Each subcommand for the `pyocd` tool has a default logging level.

Subcommand     | Default level
---------------|--------------
`commander`    | WARNING
`erase`        | WARNING
`flash`        | WARNING
`gdbserver`    | INFO
`json`         | Logging fully disabled
`list`         | INFO
`pack`         | INFO
`reset`        | WARNING
`rtt`          | INFO
`server`       | INFO
