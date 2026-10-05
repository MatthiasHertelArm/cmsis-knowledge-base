---
id: "txmw-chapter-11-format-of-event-trace-b-event-trace-entries"
type: "concept"
domain: "trace"
title: "Chapter 11 - Format of event trace buffer: Event Trace Entries"
summary: "The event trace entries are found in the bottom portion of the event trace buffer. The entries are maintained in a circular list, with the current entry pointer pointing to the oldest entry."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter11.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter11.md#event-trace-entries"
license: "MIT"
mode: "V"
---

The event trace entries are found in the bottom portion of the event trace buffer. The entries are maintained in a circular list, with the current entry pointer pointing to the oldest entry. The number of entries in the list is calculated by the ***tx_trace_enable*** call.

Each object register entry contains information about a specific ThreadX trace event. The following data structure defines each trace event entry:

```c
typedef struct TX_TRACE_BUFFER_ENTRY_STRUCT
{
    ULONG     tx_trace_buffer_entry_thread_pointer;
    ULONG     tx_trace_buffer_entry_thread_priority;
    ULONG     tx_trace_buffer_entry_event_id;
    ULONG     tx_trace_buffer_entry_time_stamp;
    ULONG     tx_trace_buffer_entry_information_field_1;
    ULONG     tx_trace_buffer_entry_information_field_2;
    ULONG     tx_trace_buffer_entry_information_field_3;
    ULONG     tx_trace_buffer_entry_information_field_4;
} TX_TRACE_BUFFER_ENTRY;
```

### Thread Pointer

The thread pointer contains the address of the thread running at the time of this event. If the event occurred during
initialization (no thread running), the value of this pointer is 0xF0F0F0F0. If the event occurred during an Interrupt Service Routine (ISR), the value of this pointer is 0xFFFFFFFF. If the entry has not yet been used, the value of this pointer is 0.

### Thread Priority

The thread priority field contains the thread priority and preemption-threshold of the thread that was running at the time of this event. If an interrupt context is present (thread pointer is 0xFFFFFFFF), the value of this field is not the priority but instead the value of ***_tx_thread_current_ptr*** at the time of the event. Otherwise, the value of this field is 0.

### Event ID

The event ID specifies the event that took place. Valid ThreadX trace event IDs range from 1 through 1024. Values starting at 1025 and above are reserved for user-specific events. Please refer to the ***tx_trace.h*** file for the complete definition of ThreadX event IDs. | 

### Information Fields (1-4)

The information fields contain additional information about the specific event. Please refer to the ***tx_trace.h*** file for the complete description of the information fields for each of the defined ThreadX event IDs.
