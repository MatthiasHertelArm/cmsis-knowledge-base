---
id: "view-expressions-predefined-variables"
type: "concept"
domain: "trace"
title: "Expressions: Predefined variables"
summary: "Predefined variables can be used without a declaration or definition."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Predefined variables can be used without a declaration or definition.

 Predefined Variable | Description
---------------------|-------------------------------------------------------------
 __Running           | Indicates program execution at target: `1=run, 0=stop`
 _count              | Counts the number of items in `<readlist>` and `<read>` elements.
 _addr               | Returns the memory address of a `<readlist>` member. 


\page Symbol_Access Symbol Access

The SCVD interpreter can access symbol information from the user application that is loaded into the debugger.
This symbol information is used to:
  - generate address for reading memory content from the target system with the elements `<read>` and `<readlist>`
  - map member offsets in the element `<typedef>` using the \attr{import}.
  
Symbols can be referenced with:
  - _test.c/MySymbol_  - to access a static symbol in a specific file.
  - **MySymbol** - to access a public symbol.

This symbol information is used to read the content of static and public variables. 

The SCVD interpreter supports the scalar and complex data types. Complex data types such as struct and enum are defined using the element `<typedef>`.
The element `<read>` accesses variables or arrays from the target system. The element `<readlist>` accesses linked lists or dynamic arrays from the target system.

**Example:**

The following example code is an excerpt from the FreeRTOS source code. The CMSIS-RTOS compliant FreeRTOS implementation is available as a **Software Pack**.
 
C Code:
```
// Module Device::tasks.c
// file private variables
...
   static volatile BaseType_t  xSchedulerRunning    = pdFALSE;
   static volatile UBaseType_t uxPendedTicks        = ( UBaseType_t ) 0U;
   static volatile TickType_t  xTickCount           = ( TickType_t ) 0U;
...
 
 
// module Device::timers.c
...
  // definition; Value is  set in a function.
  static TaskHandle_t xTimerTaskHandle = NULL;
 
  // definition; Queue to send commands to the timer service task. Value is  set in a function.
  static QueueHandle_t xTimerQueue = NULL;
...  
```

.SCVD file XML elements:
```
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyFirstComponent" version="0.0.1"/>    <!-- name and version of the component  -->
 
  <objects>
    <object name="FreeRTOS Object">
      <var name="i"  type="uint32_t" value="0"/>
      <var name="j"  type="uint32_t" value="0"/>
      <var name="sp" type="uint32_t" value="0"/>
  
      <read name="xSchedulerRunning"      type="uint32_t" symbol="tasks.c/xSchedulerRunning"/>
      <read name="uxPendedTicks"          type="uint32_t" symbol="tasks.c/uxPendedTicks"/>
      <read name="xTickCount"             type="uint32_t" symbol="tasks.c/xTickCount"/>
   
      <read name="xTimerTaskHandle"       type="uint32_t" symbol="timers.c/xTimerTaskHandle"/>
      <read name="xTimerQueue"            type="uint32_t" symbol="timers.c/xTimerQueue"/>
    </object>
  </objects>
 
</component_viewer>
```

 
\page builtin_function Built-in functions

The SCVD interpreter has the following built-in functions for calculation of stack memory usage, access to CPU registers and application program symbols. 

Function Name        | Description
---------------------|-------------------------------
__CalcMemUsed   | Provide memory usage information for stack area in user application program.
__FindSymbol    | Get address value of a symbol in user application program.
__GetRegVal     | Read the value of processor register from the target processor.
__Offset_of     | Get offset of type member defined with the `<typedef>`.
__size_of       | Number of elements of an array defined by a symbol in user application.
__Symbol_exists | Check if a specific symbol exists in the user application program.
