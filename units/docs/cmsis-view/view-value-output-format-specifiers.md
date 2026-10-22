---
id: "view-value-output-format-specifiers"
type: "concept"
domain: "trace"
title: "Value output: Format Specifiers"
summary: "A format specifier starts with a percent sign followed by a format selector followed by an expression enclosed in brackets."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

A format specifier starts with a percent sign followed by a format selector followed by an expression enclosed in brackets.

**Examples:**
```
  <item property="State=%d[TCB.state]"  value="delay=%x[time_ticks/10]" />
 
  <item property="%S [TCB[i].Entry] : %d[i]" 
           value="ThreadId=%d[TCB[i].Task_ID] | State=%E[TCB[i].State] | Priority=%E[TCB[i].Priority] | Delay=%d[TCB[i].DelaySum]">
```

The following format specifiers are available:

Format specifier       | Description
:----------------------|:------------------------------------------------
\%d      | Integer value as a signed decimal number
\%u      | Integer value as an unsigned decimal number
\%t      | Text output from ASCII characters
\%x      | Integer value as hexadecimal number
\%C      | Address value as symbolic name with file context, if fails in hexadecimal format
\%E      | Symbolic enumerator value, if fails in decimal format
\%I      | IPv4 address, example: `192.168.150.99`
\%J      | IPv6 address, example: `2a00:ee0:d::13`
\%N      | String address (name), example: `Instance 1`
\%M      | MAC address, example: `1E-30-6C-A2-45-5F`
\%S      | Address value as symbolic name, if fails in hexadecimal format
\%T      | Value in format derived from expression type (hexadecimal or floating number)
\%U      | Text output from USB descriptor
\%\%     | Output \% character

**Note:**
- Format specifiers are only used by the Component Viewer. Event Recorder does not support
  format specifiers and displays all values as is. 
- You may emphasis output values using alert_bold attributes to emphasis the displayed output values.
- print_spec are supported using the 
 element.
