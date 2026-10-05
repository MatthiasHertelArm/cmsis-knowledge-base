---
id: "txmw-chapter-11-format-of-event-trace-b-event-trace-format"
type: "concept"
domain: "trace"
title: "Chapter 11 - Format of event trace buffer: Event Trace Format"
summary: "The format of the ThreadX event trace buffer is divided into three sections, namely the control header, object registry, and the trace entries. The following describes the general layout of the ThreadX event trace buffer:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter11.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter11.md#event-trace-format"
license: "MIT"
mode: "V"
---

The format of the ThreadX event trace buffer is divided into three sections, namely the control header, object registry, and the trace entries. The following describes the general layout of the ThreadX event trace buffer:

**Control Header**

**Object Registry Entry 0**

**…**

**Object Register Entry "n"**

**Event Trace Entry 0**

**…**

**Event Trace Entry "n"**

### Event Trace Control Header

The control header defines the exact layout of the event trace buffer. This includes how many ThreadX objects can be registered as well as how many events can be recorded. In addition, the control header defines where each of the elements of the trace buffer resides. The following data structure defines the control header:

```c
typedef struct TX_TRACE_CONTROL_HEADER_STRUCT
{
    ULONG    tx_trace_control_header_id;
    ULONG    tx_trace_control_header_timer_valid_mask;
    ULONG    tx_trace_control_header_trace_base_address;
    ULONG    tx_trace_control_header_object_registry_start_pointer;
    USHORT   tx_trace_control_header_reserved1;
    USHORT   tx_trace_control_header_object_registry_name_size;
    ULONG    tx_trace_control_header_object_registry_end_pointer;
    ULONG    tx_trace_control_header_buffer_start_pointer;
    ULONG    tx_trace_control_header_buffer_end_pointer;
    ULONG    tx_trace_control_header_buffer_current_pointer;
    ULONG    tx_trace_control_header_reserved2;
    ULONG    tx_trace_control_header_reserved3;
    ULONG    tx_trace_control_header_reserved4;
} TX_TRACE_CONTROL_HEADER;
```

### Control Header ID

The control header ID consists of the 32-bit HEX value of 0x54585442, which corresponds to the ASCII characters ***TXTB***. Since this value is written as a 32-bit unsigned variable, it can also be used to detect the endianness of the event trace buffer. For example, if the value in the first four byes of memory is 0x54, 0x58, 0x54, 0x42, the event trace buffer was written in big endian format. Otherwise, the event trace buffer was written in little endian format.

### Timer Valid Mask

The timer valid mask defines how many bits of the timestamp in the actual event trace entries are valid. For example, if the time-stamp source has 16-bits, the value in this field should be 0xFFFF. A 32-bit time-stamp source would have a value of 0xFFFFFFFF. This value is defined by the ***TX_TRACE_TIME_MASK*** constant in ***tx_port.h***.

### Trace Base Address

The trace buffer base address is the address the application specified as the start of the trace buffer in the ***tx_trace_enable*** call. This address is maintained for the sole use of the analysis tool to derive bufferrelative offsets for the various elements in the buffer. For example, the buffer relative offset of the current event in the trace buffer is calculated by simple subtraction of the base address from the current event address.

### Registry Start and End Pointers

The registry start pointer points to the address of the first object registry entry, while the registry end pointer points to the address im../mediately following the last register entry. These values are setup during the *tx_trace_enable* processing and are not changed throughout the duration of tracing.

### Registry Name Size

The registry name size defines maximum size in bytes for each object name in the registry entry and is defined by the symbol
***TX_TRACE_OBJECT_REGISTRY_NAME***. The default value is 32 and is defined in ***tx_trace.h***. The object name corresponds to the name given by the application when the object was created. For example, the object registry name for a thread is the name supplied by the application to the ***tx_thread_create***call.

### Buffer Start and End Pointers

The event trace buffer start pointer points to the address of the first trace entry, while the registry end pointer points to the address im../mediately following the last trace entry. These values are setup during the ***tx_trace_enable</*** processing and are not changed throughout the duration of tracing.

### Current Buffer Pointer

The event trace buffer current pointer points to the address of the oldest trace entry. Since the trace entries are maintained in a circular list, the current buffer pointer is also represents the next trace entry to be written. |
