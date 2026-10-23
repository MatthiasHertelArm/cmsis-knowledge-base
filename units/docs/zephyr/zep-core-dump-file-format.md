---
id: "zep-core-dump-file-format"
type: "concept"
domain: "debug"
title: "Core Dump: File Format"
summary: "The core dump binary file consists of one file header, one architecture-specific block, zero or one threads metadata block(s), and multiple memory blocks. All numbers in the headers below are little endian."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/coredump.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/coredump.rst"
license: "Apache-2.0"
mode: "V"
---

The core dump binary file consists of one file header, one
architecture-specific block, zero or one threads metadata block(s),
and multiple memory blocks. All numbers in
the headers below are little endian.


### File Header


The file header consists of the following fields:


* - Field
  - Data Type
  - Description
* - ID
  - `char[2]`
  - `Z`, `E` as identifier of file.
* - Header version
  - `uint16_t`
  - Identify the version of the header. This needs to be incremented
    whenever the header struct is modified. This allows parser to
    reject older header versions so it will not incorrectly parse
    the header.
* - Target code
  - `uint16_t`
  - Indicate which target (e.g. architecture or SoC) so the parser
    can instantiate the correct register block parser.
* - Pointer size
  - 'uint8_t'
  - Size of `uintptr_t` in power of 2. (e.g. 5 for 32-bit,
    6 for 64-bit). This is needed to accommodate 32-bit and 64-bit
    target in parsing the memory block addresses.
* - Flags
  - `uint8_t`
  -
* - Fatal error reason
  - `unsigned int`
  - Reason for the fatal error, as the same in
    `enum k_fatal_error_reason` defined in

### Architecture-specific Block


The architecture-specific block contains the byte stream of data specific
to the target architecture (e.g. CPU registers)


* - Field
  - Data Type
  - Description
* - ID
  - `char`
  - `A` to indicate this is a architecture-specific block.
* - Header version
  - `uint16_t`
  - Identify the version of this block. To be interpreted by the target
    architecture specific block parser.
* - Number of bytes
  - `uint16_t`
  - Number of bytes following the header which contains the byte stream
    for target data. The format of the byte stream is specific to
    the target and is only being parsed by the target parser.
* - Register byte stream
  - `uint8_t[]`
  - Contains target architecture specific data.

### Threads Metadata Block


The threads metadata block contains the byte stream of data necessary
for debugging threads.


* - Field
  - Data Type
  - Description
* - ID
  - `char`
  - `T` to indicate this is a threads metadata block.
* - Header version
  - `uint16_t`
  - Identify the version of the header. This needs to be incremented
    whenever the header struct is modified. This allows parser to
    reject older header versions so it will not incorrectly parse
    the header.
* - Number of bytes
  - `uint16_t`
  - Number of bytes following the header which contains the byte stream
    for target data.
* - Byte stream
  - `uint8_t[]`
  - Contains data necessary for debugging threads.

### Memory Block


The memory block contains the start and end addresses and the data within
the memory region.


* - Field
  - Data Type
  - Description
* - ID
  - `char`
  - `M` to indicate this is a memory block.
* - Header version
  - `uint16_t`
  - Identify the version of the header. This needs to be incremented
    whenever the header struct is modified. This allows parser to
    reject older header versions so it will not incorrectly parse
    the header.
* - Start address
  - `uintptr_t`
  - The start address of the memory region.
* - End address
  - `uintptr_t`
  - The end address of the memory region.
* - Memory byte stream
  - `uint8_t[]`
  - Contains the memory content between the start and end addresses.
