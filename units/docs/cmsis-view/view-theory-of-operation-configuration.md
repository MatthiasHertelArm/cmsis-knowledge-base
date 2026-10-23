---
id: "view-theory-of-operation-configuration"
type: "concept"
domain: "trace"
title: "Theory of operation: Configuration"
summary: "Adding the software component CMSIS-View:Event Recorder to a project will copy the file EventRecorderConf.h into the project that is used to define the configuration parameters of the Event Recorder."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/event_recorder.md#configuration"
license: "Apache-2.0"
mode: "V"
---

Adding the software component **CMSIS-View:Event Recorder** to a project will copy the file *EventRecorderConf.h* into the project that is used to define the configuration parameters of the **Event Recorder**. It uses [Configuration Wizard Annotations](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/configWizard.html), so 
IDEs that support this can also show a graphical representation of the file:

(figure: EventRecorderConf.h in Configuration Wizard View)

Following configuration parameters are defined in the *EventRecorderConf.h* file:

|Option                              |\#define                 |Description
|------------------------------------|-------------------------|-----------
|Number of Records                   |`EVENT_RECORD_COUNT`     |Specifies the number or records stored in the Event Record Buffer. Each record is 16 bytes.
|Time Stamp Source                   |`EVENT_TIMESTAMP_SOURCE` |Specifies the timer that is used as time base. Refer to TimeStampSource below for more information.
|Time Stamp Clock Frequency [Hz]     |`EVENT_TIMESTAMP_FREQ`   |Specifies the initial timer clock frequency.

> **Note**
> - Set the time stamp clock frequency to your target's core clock frequency to avoid problems in determining the correct frequency.

### Time stamp source

The following time stamp sources can be selected:
| Source                     | Description |
|----------------------------|-------------|
| DWT Cycle Counter          | Default setting. The DWT cycle counter is part of the CoreSight debug interface. DWT is not available with Cortex-M0/M0+/M23. uVision can simulate DWT using a script. |
| SysTick                    | System tick timer is available on most Cortex-M processors. But in power-down modes it might be disabled. |
| CMSIS-RTOS2 System Timer   | The system tick counter provided by a CMSIS-RTOS2 compliant real-time operating system. |
| User Timer (Normal Reset)  | User-defined timer that stops by any system reset. Refer to EventRecorder_Time for more information. |
| User Timer (Power-On Reset)| User-defined timer that stops only by power-on reset. Refer to EventRecorder_Time for more information. |

> **Note**
> - When **DWT Cycle Counter** is selected on Cortex-M0/M0+/M23, a warning is issued at compile time:
>  ```
>  Invalid Time Stamp Source selected in EventRecorderConf.h!
>  ```
> - When using the **CMSIS-RTOS2 System Timer**, it is strongly recommended to set up the **Time Stamp Clock Frequency [Hz]** (see above) to the correct value to avoid display problems in the Event Recorder and System Analyzer windows.

### Configure for targets without DWT Cycle Counter

Arm Cortex-M0/M0+/M23 processors do not offer the DWT Cycle Counter and require therefore alternative time-stamp sources.

**SysTick**

For applications that do not use the SysTick timer, you may configure EventRecorderConf.h with:

```c
#define EVENT_TIMESTAMP_SOURCE  1             // use SysTick
#define EVENT_TIMESTAMP_FREQ    25000000U     // processor core clock (input frequency to SysTick)
```

**CMSIS-RTOS2 System Timer**

For applications that use a CMSIS-RTOS2 compliant RTOS (SysTick timer used by RTOS), you may configure EventRecorderConf.h with:

```
#define EVENT_TIMESTAMP_SOURCE  2             // use CMSIS-RTOS2 System Timer
#define EVENT_TIMESTAMP_FREQ    25000000U     // processor core clock (input frequency to SysTick)
```

### DWT Cycle Counter with µVision simulator

The DWT Cycle Counter can be simulated with the following debug initialization file, for example Debug_Sim.ini:

```
MAP 0xE0001000, 0xE0001007 READ WRITE

signal void DWT_CYCCNT (void) {
  while (1) {
    rwatch(0xE0001004);
    _WWORD(0xE0001004, states);
  }
}

DWT_CYCCNT()
```
