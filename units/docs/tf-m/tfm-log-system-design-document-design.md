---
id: "tfm-log-system-design-document-design"
type: "concept"
domain: "security"
title: "Log system design document: Design"
summary: "To allow customizable configurations, the log interfaces are defined as macros. The macros are easy to be forwarded or even empty."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/tfm_log_system_design_document.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_log_system_design_document.html#design"
license: "BSD-3-Clause"
mode: "V"
---

To allow customizable configurations, the log interfaces are defined as macros.
The macros are easy to be forwarded or even empty. When SPM trying to output
message and a value, it relies on a wrapper function, and finally output the
formatted message by the HAL API.

The design principles of TF-M log system:

  - Configurable log levels.
  - Separated SPM and SP log implementations.
  - Platforms provide log HAL implementations.


### SPM Log System



#### Level Control

Three log levels for SPM log system are defined:

  - LOG_LEVEL_NONE
  - LOG_LEVEL_ERROR
  - LOG_LEVEL_NOTICE
  - LOG_LEVEL_WARNING
  - LOG_LEVEL_INFO
  - LOG_LEVEL_VERBOSE

Then a macro `TFM_SPM_LOG_LEVEL` is defined as an indicator, it should
be equal to one of the six log levels.


#### API Definition

The following APIs output the string with optional format specifiers.
The _RAW forms of the macros, output the string directly, without
adding a prefix identifying the log level of the print:

  VERBOSE_RAW(...);
  VERBOSE(...);

  INFO_RAW(...);
  INFO(...);

  WARN(...);
  WARN_RAW(...);

  NOTICE(...);
  NOTICE_RAW(...);

  ERROR(...);
  ERROR_RAW(...);

Here is a table about the effective APIs with different SPM log level.

+--------------------+--------+------+-------+------+
|                    | DEBUG  | INFO | ERROR | NONE |
+====================+========+======+=======+======+
| VERBOSE_RAW        |  Yes   |  No  |  No   |  No  |
| VERBOSE            |        |      |       |      |
+--------------------+--------+------+-------+------+
| INFO_RAW           |  Yes   | Yes  |  No   |  No  |
| INFO               |        |      |       |      |
+--------------------+--------+------+-------+------+
| NOTICE_RAW         |  Yes   | Yes  |  No   |  No  |
| NOTICE             |        |      |       |      |
+--------------------+--------+------+-------+------+
| WARN_RAW           |  Yes   | Yes  |  No   |  No  |
| WARN               |        |      |       |      |
+--------------------+--------+------+-------+------+
| ERROR_RAW          |  Yes   | Yes  |  Yes  |  No  |
| ERROR              |        |      |       |      |
+--------------------+--------+------+-------+------+


### Partition Log System

Partition log outputting required rich formatting in particular cases. There is
a customized print inside TF-M(`tfm_log_unpriv`), and it is wrapped as macro.


#### Level Control

Three log levels for partition log system are defined:

  - LOG_LEVEL_NONE
  - LOG_LEVEL_ERROR
  - LOG_LEVEL_NOTICE
  - LOG_LEVEL_WARNING
  - LOG_LEVEL_INFO
  - LOG_LEVEL_VERBOSE

Then a macro `TFM_PARTITION_LOG_LEVEL` is defined as an indicator. It should
be equal to one of the six log levels and it is an overall setting for all
partitions.


#### Log Format

Compared to SPM, SP log API supports formatting. Similar to `printf`, these
log APIs use a format outputting to output various type of data:

```c

%d - decimal signed integer
%u - decimal unsigned integer
%x - hex(hexadecimal)
%s - string
```

#### API Definition

Define partition log APIs:

  VERBOSE_UNPRIV_RAW(...);
  VERBOSE_UNPRIV(...);

  INFO_UNPRIV_RAW(...);
  INFO_UNPRIV(...);

  WARN_UNPRIV(...);
  WARN_UNPRIV_RAW(...);

  NOTICE_UNPRIV(...);
  NOTICE_UNPRIV_RAW(...);

  ERROR_UNPRIV(...);
  ERROR_UNPRIV_RAW(...);

Here is a table about the effective APIs with different partition log level.

+--------------------+--------+------+-------+------+
|                    | DEBUG  | INFO | ERROR | NONE |
+====================+========+======+=======+======+
| VERBOSE_UNPRIV_RAW |  Yes   |  No  |   No  |  No  |
| VERBOSE_UNPRIV     |        |      |       |      |
+--------------------+--------+------+-------+------+
| INFO_UNPRIV_RAW    |  Yes   | Yes  |   No  |  No  |
| INFO_UNPRIV        |        |      |       |      |
+--------------------+--------+------+-------+------+
| NOTICE_UNPRIV_RAW  |  Yes   | Yes  |   No  |  No  |
| NOTICE_UNPRIV      |        |      |       |      |
+--------------------+--------+------+-------+------+
| WARN_UNPRIV_RAW    |  Yes   | Yes  |   No  |  No  |
| WARN_UNPRIV        |        |      |       |      |
+--------------------+--------+------+-------+------+
| ERROR_UNPRIV_RAW   |  Yes   | Yes  |  Yes  |  No  |
| ERROR_UNPRIV       |        |      |       |      |
+--------------------+--------+------+-------+------+



#### HAL API

Please refers to the HAL design document.
