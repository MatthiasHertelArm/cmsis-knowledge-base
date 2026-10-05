---
id: "txmw-chapter-3-functional-components-of-system-information"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional components of FileX: System Information"
summary: "FileX system information consists of keeping track of the open media instances and maintaining the global system time and date."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter3.md#system-information"
license: "MIT"
mode: "V"
---

FileX system information consists of keeping track of the open media instances and maintaining the global system time and date.

(figure: File with Contiguous Clusters vs. File Requiring FAT Link)

**FIGURE 3. File with Contiguous Clusters vs. File Requiring FAT Link**

By default, the system date and time are set to the last release date of FileX. To have accurate system date and time, the application must call ***fx_system_time_set*** and ***fx_system_date_set*** during initialization.

### System Date

The FileX system date is maintained in the global ***_fx_system_date*** variable. Bits 15 through 9 contain the year offset from 1980, bits 8 through 5 contain the month offset, and bits 4 through 0 contain the day.

### System Time

The FileX system time is maintained in the global ***_fx_system_time*** variable. Bits 15 through 11 contain the hours, bits 10 through 5 contain the minutes, and bits 4 through 0 contain the half seconds.

### Periodic Time Update

During system initialization, FileX creates a ThreadX application timer to periodically update the system date and time. The rate at which the system date and time update is determined by two constants used by the ***_fx_system_initialize*** function.

The constants **FX_UPDATE_RATE_IN_SECONDS** and **FX_UPDATE_RATE_IN_TICKS** represent the same period of time. The constant **FX_UPDATE_RATE_IN_TICKS** is the number of ThreadX timer ticks that represents the number of seconds specified by the constant **FX_UPDATE_RATE_IN_SECONDS**. The **FX_UPDATE_RATE_IN_SECONDS** constant specifies how many seconds between each FileX time update. Therefore, the internal FileX time increments in intervals of **FX_UPDATE_RATE_IN_SECONDS**. These constants may be supplied during compilation of ***fx_system_initialize***, or the developer may modify the defaults found in the ***fx_port.h*** file of the FileX release.

The periodic FileX timer is used only for updating the global system date and time, which is used solely for file time-stamping. If time-stamping is not necessary, simply define **FX_NO_TIMER** when compiling ***fx_system_initialize.c*** to eliminate the creation of the FileX periodic timer.

(figure: FileX FAT-16 File Example)

**FIGURE 4. FileX FAT-16 File Example**
