---
id: "pyocd-command-reference-memory"
type: "concept"
domain: "debug"
title: "Command reference: Memory"
summary: "Command reference: Memory"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/command_reference.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/command_reference.md#memory"
license: "Apache-2.0"
mode: "V"
---

##### `compare`

**Aliases**: `cmp` \
**Usage**: compare ADDR [LEN] FILENAME \
Compare a memory range against a binary file. If the length is not provided, then the length of the file is used.


##### `disasm`

**Aliases**: `d` \
**Usage**: disasm [-c/--center] ADDR [LEN] \
Disassemble instructions at an address. The length argument is in bytes and is optional, with a default of 6. If the -c option is used, the disassembly is centered on the given address. Otherwise the disassembly begins at the given address.


##### `erase`

**Usage**: erase [ADDR] [COUNT] \
Erase all internal flash or a range of sectors.


##### `fill`

**Usage**: fill [SIZE] ADDR LEN PATTERN \
Fill a range of memory with a pattern. The optional SIZE parameter must be one of 8, 16, or 32. If not provided, the size is determined by the pattern value's most significant set bit. Only RAM regions may be filled.


##### `find`

**Usage**: find [-n] ADDR LEN BYTE+ \
Search for a value in memory within the given address range. A pattern of any number of bytes can be searched for. Each BYTE parameter must be an 8-bit value. If the -n argument is passed, the search is negated and looks for the first set of bytes that does not match the provided values.


##### `load`

**Usage**: load FILENAME [ADDR] \
Load a binary, hex, or elf file with optional base address.


##### `loadmem`

**Usage**: loadmem ADDR FILENAME \
Load a binary file to an address in memory (RAM or flash). This command is deprecated in favour of the more flexible 'load'.


##### `read16`

**Aliases**: `rh` \
**Usage**: read16 ADDR [LEN] \
Read 16-bit halfwords. Optional length parameter is the number of bytes (not half-words) to read. It must be divisible by 2. If the length is not provided, one halfword is read. The address may be unaligned.


##### `read32`

**Aliases**: `rw` \
**Usage**: read32 ADDR [LEN] \
Read 32-bit words. Optional length parameter is the number of bytes (not words) to read. It must be divisible by 4. If the length is not provided, one word is read. The address may be unaligned.


##### `read64`

**Aliases**: `rd` \
**Usage**: read64 ADDR [LEN] \
Read 64-bit words. Optional length parameter is the number of bytes (not double-words!) to read. It must be divisible by 8. If the length is not provided, one word is read. The address may be unaligned.


##### `read8`

**Aliases**: `rb` \
**Usage**: read8 ADDR [LEN] \
Read 8-bit bytes. Optional length parameter is the number of bytes to read. If the length is not provided, one byte is read.


##### `savemem`

**Usage**: savemem ADDR LEN FILENAME \
Save a range of memory to a binary file.


##### `write16`

**Aliases**: `wh` \
**Usage**: write16 ADDR DATA+ \
Write 16-bit halfwords to memory. The data arguments are 16-bit halfwords in big-endian format and are written as little-endian. The address may be unaligned. Can write to both RAM and flash. Flash writes are subject to minimum write size and alignment, and the flash page must have been previously erased.


##### `write32`

**Aliases**: `ww` \
**Usage**: write32 ADDR DATA+ \
Write 32-bit words to memory. The data arguments are 32-bit words in big-endian format and are written as little-endian. The address may be unaligned. Can write to both RAM and flash. Flash writes are subject to minimum write size and alignment, and the flash page must have been previously erased.


##### `write64`

**Aliases**: `wd` \
**Usage**: write64 ADDR DATA... \
Write 64-bit double-words to memory. The data arguments are 64-bit words in big-endian format and are written as little-endian. The address may be unaligned. Can write to both RAM and flash. Flash writes are subject to minimum write size and alignment, and the flash page must have been previously erased.


##### `write8`

**Aliases**: `wb` \
**Usage**: write8 ADDR DATA+ \
Write 8-bit bytes to memory. The data arguments are 8-bit bytes. Can write to both RAM and flash. Flash writes are subject to minimum write size and alignment, and the flash page must have been previously erased.
