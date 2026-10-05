---
id: "intr-tracing-logging-with-the-trice-lib-trice-features"
type: "concept"
domain: "debug"
title: "Tracing & Logging with the `TRICE` Library (Interrupts too!): _Trice_ features"
summary: "This last section of the article is digging deeper into the parts of Trice which I believe developers will care most about when it comes to instrumenting embedded software."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-01-12-trice.md"
doc_source: "https://interrupt.memfault.com/blog/trice#trice-features"
license: "CC-BY-SA-4.0"
mode: "V"
---

This last section of the article is digging deeper into the parts of _Trice_ which I believe developers will care most about when it comes to instrumenting embedded software.

### Open source

Target code and PC tool are open source. The MIT license gives full usage freedom. Users are invited to support further _Trice_ development.

### Easy-to-use

Making it [facile](https://github.com/rokath/trice/tree/master/docs/TriceUserGuide.md) for a user to use _Trice_ was the driving point just to have one **trice** tool and an additional source file with a project-specific simple to use `triceConfig.h` and to get away with the one macro `TRICE` for most situations. _Trice_ understands itself as a silent helper in the background to give the developer more focus on its real task. If, for example, `trice log` is running and you re-flash the target, there is **_no need to restart_** the **trice** tool. When [til.json](https://github.com/rokath/trice/tree/master/til.json) was updated in a pre-build step, the **trice** tool automatically reloads the new data during logging.

The **trice** tool comes with many command-line switches (`trice help -all`) for tailoring various needs, but mostly these are not needed. Usually, only type `trice l -p COMn` for logging with a 115200 bit/s baud rate.

### Small Size - using _Trice_ frees FLASH memory

Compared to a printf-library code which occupies [1](https://github.com/mludvig/mini-printf) to over [20](https://github.com/mpaland/printf#a-printf--sprintf-implementation-for-embedded-systems) KB FLASH memory, the _Trice_ code is really [small](https://github.com/rokath/trice/tree/master/docs/TriceSpace.md) - less 1 KB will do already but provide full support.

### Performance

[Can it get faster](https://github.com/rokath/trice/tree/master/docs/TriceSpeed.md)? Only 3 runtime assembly instructions per _Trice_ are needed in the minimal case! It will require more processor cycles to add timestamps and addresses, disable and enable interrupts, and increment cycle counters, but a _Trice_ call is still incredibly fast.

### Robustness with COBS Encoding

When a _Trice_ data stream is interrupted, the [COBS](https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing) encoding allows an immediate re-sync with the next COBS package delimiter byte and a default _Trice_ cycle counter gives a high chance to detect lost _Trice_ messages.

Before COBS was ultimately chosen, [several encodings](https://github.com/rokath/trice/tree/master/docs/TriceObsoleteEncodings.md) were evaluated. A bonus of using COBS is the **trice** tool can include different decoders if necessary since COBS can handle multiple concurrent data streams.

### Just Like `printf` but Better

_Trice_ is usable inside interrupts and additional [format specifier support](https://github.com/rokath/trice/tree/master/docs/TriceVsPrintfSimilaritiesAndDifferences.md#Extended-format-specifier-possibilities) gives options like binary or boolean outputs. Transmitting runtime generated strings could be a need, so a `TRICE_S` macro exists supporting the `%s` format specifier for strings up to 1000 bytes long. It is possible to log float/double numbers using `%f` and the like, but the numbers need to be wrapped with the function `aFloat(x)` or `aDouble(y)`. UTF-8 encoded strings are implicitly supported if you use UTF-8 for the source code.



### Labels, Colors, and Logging Levels

You can label each _Trice_ with a channel specifier to [colorize](https://github.com/rokath/trice/tree/master/docs/TriceColor.md) the output. This is free of any runtime costs because the channel strings are part of the log format strings, which are not compiled into the target. The **trice** tool will strip full lowercase channel descriptors from the format string after setting the appropriate color, making it possible to give each letter its color.

Loggers use log levels and offer a setting like "log everything above **INFO**" for example. The _Trice_ channels implement this but can do better: Inside [emitter.ColorChannels](https://github.com/rokath/trice/tree/master/internal/emitter/lineTransformerANSI.go), all common log levels defined as _Trice_ channels can coexist with user-defined channels. The user can adjust this. The **trice** tool has the `-pick` and `-ban` switches to control the display in detail. Also a `-logLevel` switch can be used to set a display threshold as channel position inside ColorChannels.

If a target-side log level control is needed, a **trice** tool extension could each of these log level channels assign an ID range and a target-side log threshold can control which IDs are transmitted. No need to implement that right now, because the runtime and bandwidth costs are so small for each _Trice_ and a back control path is needed which is better designed by the user. Also, the [IDManagement](https://github.com/rokath/trice/tree/master/docs/TriceIDManagement.md) would get more complex.



### Compile-time Disabling of `TRICE` Macros on File Level

After debugging code in a file, there is [no need to remove or comment out `TRICE` macros](https://github.com/rokath/trice/blob/master/docs/TriceUserGuide.md#TargetsideTriceOn-Off). Write a `#define TRICE_OFF` just before the `#include "trice.h"` line and all `TRICE` macros in this file are ignored completely by the compiler, but not by the **trice** tool. In the case of re-constructing the [**T**rice **ID** **L**ist](https://github.com/rokath/trice/tree/master/til.json), these no code generating macros are regarded.

```c
//#define TRICE_OFF // uncomment this line to disable trice code generation in this file
#include "trice.h"
```

### Target and Host Timestamps

Enable target timestamps with a variable you want inside [triceConfig.h](https://github.com/rokath/trice/tree/master/test/MDK-ARM_STM32G071RB/Core/Inc/triceConfig.h). This adds a 32-bit value to each _Trice_ sequence, which can track the system clock, a millisecond timer, or another event counter. The **trice** tool will automatically recognize and display them in a default mode you can control. If several `TRICE` macros form a single line, the **trice** tool only displays the target timestamp of the first `TRICE` macro.

Embedded devices often lack a real-time clock and in some scenarios can have uptimes of weeks. Therefore the **trice** tool precedes each _Trice_ line with a PC timestamp, if not disabled. This is the _Trice_ received timestamp on the PC, which can be some milliseconds later than the target's event timestamp.

### Target Source Code Location

Some developers like to see the `filename.c` and `line` in front of each log line for quick source location. Enable this within [triceConfig.h](https://github.com/rokath/trice/tree/master/test/MDK-ARM_STM32G071RB/Core/Inc/triceConfig.h). This adds a 32-bit value to the _Trice_ sequence containing a 16-bit file ID and a 16-bit line number. The _Trice_ tool will automatically insert `#define TRICE_FILE Id(nnnnn)` with a generated file ID, and that's it!

### Multiple Target Devices in One Log Stream

Several **trice** tool instances can run in parallel or on different PCs. Each **trice** tool instance receives _Trices_ from an embedded device. Instead of displaying the log lines, the **trice** tool instances can transmit them over TCP/IP (`trice l -p COMx -ds`) to a **trice** tool instance acting as a display server (`trice ds`). The display server can interleave these log lines in one output. For each embedded device a separate _Trice_ line prefix and suffix is definable. This allows comparable time measurements in distributed systems. BTW: The _Trice_ message integration could also be done directly with the COBS packets.

### Any byte capable 1-wire connection usable

The usual _Trice_ output device is a UART but also [SEGGER-RTT](https://github.com/rokath/trice/tree/master/docs/TriceOverRTT.md) is supported over J-Link or ST-Link devices. Many microcontroller boards can act as a _Trice_ bridge to a serial port from any port ([example](https://github.com/rokath/trice/tree/master/docs/TriceOverOneWire.md)).

### Scalability

The various [_Trice_ ID management features](https://github.com/rokath/trice/tree/master/docs/TriceIDManagement.md) allow the organization also of bigger software systems. More than 65000 possible different IDs should match also large projects. Just in case: 16-bit for the ID is a not too hard changeable value.

### Portability and Modularity

The **trice** tool is written in the open source language [_Go_](https://go.dev/) and is therefore usable on many platforms. That means almost anyone can easily and automatically perform code patching and ID handling with `trice update`.

All C-compilers should be able to compile the target _Trice_ code and there is no hardware dependency despite the byte transmission. MCUs with 8-bit to 64-bit, little or big-endian are supported.

Any user program able to read a [JSON](https://github.com/rokath/trice/tree/master/til.json) file can receive the [documented](https://github.com/rokath/trice/tree/master/docs/TriceMessagesEncoding.md) _Trice_ message format, look up the ID, and perform a printf-like action to translate into log strings. The **trice** tool with its `log` switch is a working example.

Using [COBS](https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing) packets starting with a [package descriptor](https://github.com/rokath/trice/tree/master/docs/TriceMessagesEncoding.md#package-mode-prefix) allows user protocols to pass over the same transmission line. The other way around is also possible! A developer could embed `Trice` messages in their own protocol.

The **trice** tool is expandable with several decoders, which means it is possible to implement a minimal _Trice_ encoding, if bandwidth matters heavily and control that with switches.

When less RAM usage is more important the target double buffer is replaceable with a FIFO using a compile-time flag. Right now, an immediate mode is selectable inside [triceConfig.h](https://github.com/rokath/trice/tree/master/test/MDK-ARM_STM32G071RB/Core/Inc/triceConfig.h) avoiding any buffer by paying a time toll.

The **trice** tool supports [many command line switches](https://github.com/rokath/trice/tree/master/docs/TriceUserGuide.md#9-options-for-trice-tool).

### Optional _Trice_ Message Encryption

The encryption opportunity makes it possible to test thoroughly a binary with log output and release it without the need to change any bit but to make the log output unreadable for a not authorized person. Implemented is the lightweight [XTEA](https://de.wikipedia.org/wiki/Extended_Tiny_Encryption_Algorithm), which will work for many cases. It should also be easy to add a different algorithm.
