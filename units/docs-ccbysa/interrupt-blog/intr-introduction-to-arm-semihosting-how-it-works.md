---
id: "intr-introduction-to-arm-semihosting-how-it-works"
type: "concept"
domain: "debug"
title: "Introduction to ARM Semihosting: How It Works"
summary: "This is done by halting the CPU target by the debugger agent, either by running into a breakpoint instruction (BKPT 0xAB for ARMv6-M or ARMv7-M) or by sending a supervisor call instruction (SVC 0xAB or SVC 0x123456) depending …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-02-16-arm-semihosting.md"
doc_source: "https://interrupt.memfault.com/blog/arm-semihosting#how-it-works"
license: "CC-BY-SA-4.0"
mode: "V"
---

This is done by halting the CPU target by the debugger agent, either by running
into a breakpoint instruction (`BKPT 0xAB`  for ARMv6-M or ARMv7-M) or by
sending a supervisor call instruction (`SVC 0xAB` or `SVC 0x123456`) depending
on the target architecture or processor.

This indicates to the host that the target is requesting a semihosting
operation.

The debugger agent then figures out the operation requested by the target by
reading the content of `r0`, and, if necessary, accesses all other function
parameters pointed by `r1`.

While the CPU is still halted, the host will execute the requested operation and
return the result in `r0` before allowing the processor to continue running its
program.

The following is a list of the semihosting operations defined by ARM[^2]:

```c
/* File operations */
SYS_OPEN        EQU 0x01 //Open a file or stream on the host system.
SYS_ISTTY       EQU 0x09 //Check whether a file handle is associated with a file or a stream/terminal such as stdout.
SYS_WRITE       EQU 0x05 //Write to a file or stream.
SYS_READ        EQU 0x06 //Read from a file at the current cursor position.
SYS_CLOSE       EQU 0x02 //Closes a file on the host which has been opened by SYS_OPEN.
SYS_FLEN        EQU 0x0C //Get the length of a file.
SYS_SEEK        EQU 0x0A //Set the file cursor to a given position in a file.
SYS_TMPNAM      EQU 0x0D //Get a temporary absolute file path to create a temporary file.
SYS_REMOVE      EQU 0x0E //Remove a file on the host system. Possibly insecure!
SYS_RENAME      EQU 0x0F //Rename a file on the host system. Possibly insecure!

/* Terminal I/O operations */
SYS_WRITEC      EQU 0x03 //Write one character to the debug terminal.
SYS_WRITE0      EQU 0x04 //Write a 0-terminated string to the debug terminal.
SYS_READC       EQU 0x07 //Read one character from the debug terminal.

/* Time operations */
SYS_CLOCK       EQU 0x10
SYS_ELAPSED     EQU 0x30
SYS_TICKFREQ    EQU 0x31
SYS_TIME        EQU 0x11

/* System/Misc. operations */
SYS_ERRNO       EQU 0x13 //Returns the value of the C library errno variable that is associated with the semihosting implementation.
SYS_GET_CMDLINE EQU 0x15 //Get commandline parameters for the application to run with (argc and argv for main())
SYS_HEAPINFO    EQU 0x16
SYS_ISERROR     EQU 0x08
SYS_SYSTEM      EQU 0x12
```
