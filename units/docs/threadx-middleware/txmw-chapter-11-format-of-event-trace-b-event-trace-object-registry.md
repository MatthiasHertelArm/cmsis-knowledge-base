---
id: "txmw-chapter-11-format-of-event-trace-b-event-trace-object-registry"
type: "concept"
domain: "trace"
title: "Chapter 11 - Format of event trace buffer: Event Trace Object Registry"
summary: "The event trace object registry contains n object registry entries that correspond to the objects created by the application."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter11.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter11.md#event-trace-object-registry"
license: "MIT"
mode: "V"
---

The event trace object registry contains ***n*** object registry entries that correspond to the objects created by the application. The main purpose of the object registry is for external analysis tools to correlate actual object names with the object addresses of the trace buffer entries. The number of registry entries is specified by the application in the ***tx_trace_enable*** call.

Each object register entry contains information about a specific ThreadX object previously created by the application. The following data structure defines each object registry entry:

```c
typedef struct TX_TRACE_OBJECT_REGISTRY_ENTRY_STRUCT
{
    UCHAR    tx_trace_object_registry_entry_object_available**;
    UCHAR    tx_trace_object_registry_entry_object_type**;
    UCHAR    tx_trace_object_registry_entry_object_reserved1;
    UCHAR    tx_trace_object_registry_entry_object_reserved2;
    ULONG    tx_trace_thread_registry_entry_object_pointer;
    ULONG    tx_trace_object_registry_entry_object_parameter_1;
    ULONG    tx_trace_object_registry_entry_object_parameter_2;
    UCHAR    tx_trace_thread_registry_entry_object_name[TX_TRACE_OBJECT_REGISTRY_NAME];

} TX_TRACE_OBJECT_REGISTRY_ENTRY;
```

### Object Available Flag

The object available flag is set to 1 if the object registry entry is available. Otherwise, if the value is
not 1, the object registry entry is not available. Note that the entry could still contain valid information even though it is available.

### Object Entry Type

The object entry type identifies the type of object in this entry. The following is a list of the valid object types:

| **Value**	| **Object Type** |
|---------- | --------------- |
| 0         | Not Valid       |
| 1         | Thread          |
| 2         | Timer |
| 3         | Queue |
| 4         | Semaphore |
| 5         | Mutex |
| 6         | Event Flags Group |
| 7         | Block Pool |
| 8         | Byte Pool |
| 9         | ../media |
| 10        | File |
| 11        | IP |
| 12        | Packet Pool |
| 13        | TCP Socket |
| 14        | UDP Socket |
| 15-20     | Reserved |  
| 21        | USB Host Stack Device |
| 22        | USB Host Stack Interface |
| 23        | USB Host Endpoint |
| 24        | USB Host Class |
| 25        | USB Device |
| 26        | USB Device Interface |
| 27        | USB Device Endpoint |
| 28        | USB Device Class |

### Object Pointer

The object pointer specifies the object address that is used for accessing the object using the ThreadX API.

### Object Reserved Fields

For all objects other than threads, these reserved fields should be 0. For threads, the priority of the thread at the time it is entered into the registry is placed in these two reserved fields.

### Object Parameters

The object parameters contain supplemental information about the object. The following describes the supplemental information for each ThreadX object:

| **Object Type**        | **Parameter 1**  | **Parameter 2** |
|----------------------- | ---------------- | --------------- |
| Thread                 | Stack Start      | Stack Size |
| Timer                  | Initial Ticks | Reschedule Ticks |
| Queue                  | Queue Size | Message Size |
| Semaphore              | Initial Instances | - |
| Mutex                  | Inheritance Flag | - |
| Event Flags Group      | - | - |
| Block Pool             | Total Blocks | Block Size |
| Byte Pool              | Total Bytes | - |
| ../media                  | Fat Cache Size | Sector Cache Size |
| File                   | - | - |
| IP                     | Stack Start | Stack Size |
| Packet Pool            | Packet Size | Number of Packets |
| TCP Socket             | IP address | Window Size |
| UDP Socket             | IP address | RX Queue Max |

### Object Name

The object name contains the name of the ThreadX object. The name is the name provided to ThreadX at the time the object was created. By default, the object name has a maximum of 32 characters. Actual names greater than 32 characters are truncated.
