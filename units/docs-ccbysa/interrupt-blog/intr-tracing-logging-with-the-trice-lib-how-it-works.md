---
id: "intr-tracing-logging-with-the-trice-lib-how-it-works"
type: "concept"
domain: "debug"
title: "Tracing & Logging with the `TRICE` Library (Interrupts too!): How It Works"
summary: "Trice performs zero costly printf-like functions on the target at all. The TRICE macro, instead, just copies an ID together with the optional values to a buffer."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-01-12-trice.md"
doc_source: "https://interrupt.memfault.com/blog/trice#how-it-works"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Trice_ performs **zero** [costly](https://github.com/rokath/trice/tree/master/docs/TriceVsPrintfSimilaritiesAndDifferences.md#printf-like-functions) printf-like functions on the target at all. The `TRICE` macro, instead, just copies an ID together with the optional values to a buffer. In the minimum case, this can happen in [6-8](https://github.com/rokath/trice/tree/master/docs/TriceSpeed.md) processor clocks even with target timestamps included. When running on a 64 MHz clock, **light can travel about 30 meters in that time**.

To achieve this, an automatic pre-compile step is triggered by executing a `trice update` command on the PC. The **trice** tool then parses the source tree for macros like `TRICE( "msg: %d Kelvin\n", k );` and patches them to `TRICE( Id(12345), "msg: %d Kelvin\n", k );`, where `12345` is a generated 16-bit identifier copied into a [**T**rice **I**D **L**ist](https://github.com/rokath/trice/tree/master/til.json). During compilation than, the `TRICE` macro is translated to the `12345` ID and the optional parameter values. The format string is ignored by the compiler.

The target code is [project-specific](https://github.com/rokath/trice/tree/master/test/MDK-ARM_STM32G071RB/Core/Inc/triceConfig.h) and can be configured by modifying this header file. In **immediate mode**, the stack is used as the _Trice_ buffer and the TRICE macro execution includes the quick [COBS](https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing) encoding and the data transfer. This more straightforward, but slower architecture, can be interesting for many cases because it is anyway much faster than printf-like functions calls. In **deferred mode**, a service swaps the _Trice_ double buffer periodically, encodes it according to COBS, and the background transfer is triggered.

During runtime, the PC **trice** tool receives everything that happened in the last ~100ms as a COBS packet from the UART port. The `0x30 0x39` is the ID 12345 and a map lookup delivers the format string _`msg: %d Kelvin\n`_ and also the bit width information. Now the **trice** tool can write the target timestamp, set the message color, and execute `printf("%d Kelvin\n", 0x0000000e);`

---



The **trice** tool runs in the background allowing the developer to focus on programming tasks. Once an ID is generated from a string, it keeps the same ID unless the _Trice_ is changed. If for example the format string gets changed into `"msg: %d Celsius\n"`, a new ID is inserted automatically and the reference list gets extended. Obsolete IDs are kept inside the [**T**rice **I**D **L**ist](https://github.com/rokath/trice/tree/master/til.json) (`til.json`) for compatibility with older firmware versions. It could be possible when merging code, an **ID** is used twice for different format strings. In that case, the **ID** inside the reference list wins and the additional source gets patched with a new **ID**. This may be unwanted, but patching is avoidable with proper [ID management](https://github.com/rokath/trice/tree/master/docs/TriceIDManagement.md). The reference list should be kept under source code control.
