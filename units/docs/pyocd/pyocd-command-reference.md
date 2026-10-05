---
id: "pyocd-command-reference"
type: "concept"
domain: "debug"
title: "Command reference"
summary: "PyOCD has a simple command processor that is accessible from the console via the commander subcommand, or from gdb as remote monitor commands."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/command_reference.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/command_reference.md"
license: "Apache-2.0"
mode: "V"
---

PyOCD has a simple command processor that is accessible from the console via the commander subcommand,
or from gdb as remote monitor commands.

The syntax for the commands is straightforward. The command line is first split into individual
commands separated by `;` (semicolon). Each command is then split into words separated by
whitespace. The whitespace characters are space, tab, CR, and LF. Words can be quoted with either a
single or double quote to include whitespace (or quotes) in the word.

Any prefix of a command name is accepted as long as it is unique. If a command prefix is entered
that ambiguous because it matches multiple commands, an error will be reported showing the matched
command names. In addition, commonly used commands often have a short alias. The alias takes
precedence even when it is a prefix of multiple other commands.

<!--
Maintainer note: the following is auto-generated. Edit the command class INFO dict source material,
then run ./scripts/generate_command_help.py.
-->

All commands
------------



| Command | Arguments | Description |
|---|---|---|
| **Breakpoints** |  |  |
| [`break`](#break) | ADDR | Set a breakpoint address. |
| [`lsbreak`](#lsbreak) |  | List breakpoints. |
| [`lswatch`](#lswatch) |  | List watchpoints. |
| [`rmbreak`](#rmbreak) | ADDR | Remove a breakpoint. |
| [`rmwatch`](#rmwatch) | ADDR [r\|w\|rw] [1\|2\|4] | Remove watchpoint(s). |
| [`watch`](#watch) | ADDR [r\|w\|rw] [1\|2\|4] | Set a watchpoint address, and optional access type (default rw) and size (4). |
| **Bringup** |  |  |
| [`initdp`](#initdp) |  | Init DP and power up debug. |
| [`makeap`](#makeap) | APSEL | Creates a new AP object for the given APSEL. |
| [`reinit`](#reinit) |  | Reinitialize the target object. |
| **Commander** |  |  |
| [`exit`](#exit), [`quit`](#exit) |  | Quit pyocd commander. |
| [`list`](#list) |  | Show available targets. |
| **Core** |  |  |
| [`continue`](#continue), [`c`](#continue), [`go`](#continue), [`g`](#continue) |  | Resume execution of the target. |
| [`core`](#core) | [NUMBER \| NAME] | Select CPU core by number or name, or print selected core. |
| [`halt`](#halt), [`h`](#halt) |  | Halt the target. |
| [`step`](#step), [`s`](#step) | [COUNT] | Step one or more instructions. |
| **Dap** |  |  |
| [`readap`](#readap), [`rap`](#readap) | [APSEL] ADDR | Read AP register. |
| [`readdp`](#readdp), [`rdp`](#readdp) | ADDR | Read DP register. |
| [`writeap`](#writeap), [`wap`](#writeap) | [APSEL] ADDR DATA | Write AP register. |
| [`writedp`](#writedp), [`wdp`](#writedp) | ADDR DATA | Write DP register. |
| **Device** |  |  |
| [`reset`](#reset) | [halt\|-halt\|-h] [TYPE] | Reset the target, optionally with halt and/or specifying the reset type. |
| [`unlock`](#unlock) |  | Unlock security on the target. |
| **Gdbserver** |  |  |
| [`exit`](#exit) |  | Terminate running gdbservers in this session. |
| **General** |  |  |
| [`help`](#help), [`?`](#help) | [CMD] | Show help for commands. |
| **Memory** |  |  |
| [`compare`](#compare), [`cmp`](#compare) | ADDR [LEN] FILENAME | Compare a memory range against a binary file. |
| [`disasm`](#disasm), [`d`](#disasm) | [-c/--center] ADDR [LEN] | Disassemble instructions at an address. |
| [`erase`](#erase) | [ADDR] [COUNT] | Erase all internal flash or a range of sectors. |
| [`fill`](#fill) | [SIZE] ADDR LEN PATTERN | Fill a range of memory with a pattern. |
| [`find`](#find) | [-n] ADDR LEN BYTE+ | Search for a value in memory within the given address range. |
| [`load`](#load) | FILENAME [ADDR] | Load a binary, hex, or elf file with optional base address. |
| [`loadmem`](#loadmem) | ADDR FILENAME | Load a binary file to an address in memory (RAM or flash). |
| [`read16`](#read16), [`rh`](#read16) | ADDR [LEN] | Read 16-bit halfwords. |
| [`read32`](#read32), [`rw`](#read32) | ADDR [LEN] | Read 32-bit words. |
| [`read64`](#read64), [`rd`](#read64) | ADDR [LEN] | Read 64-bit words. |
| [`read8`](#read8), [`rb`](#read8) | ADDR [LEN] | Read 8-bit bytes. |
| [`savemem`](#savemem) | ADDR LEN FILENAME | Save a range of memory to a binary file. |
| [`write16`](#write16), [`wh`](#write16) | ADDR DATA+ | Write 16-bit halfwords to memory. |
| [`write32`](#write32), [`ww`](#write32) | ADDR DATA+ | Write 32-bit words to memory. |
| [`write64`](#write64), [`wd`](#write64) | ADDR DATA... | Write 64-bit double-words to memory. |
| [`write8`](#write8), [`wb`](#write8) | ADDR DATA+ | Write 8-bit bytes to memory. |
| **Nrf91** |  |  |
| [`nrf91-update-modem-fw`](#nrf91-update-modem-fw) | [-f] mfw_nrf91xx_x.x.x.zip | Update modem firmware for an nRF91 target. |
| **Openocd_compatibility** |  |  |
| [`init`](#init) |  | Ignored; for OpenOCD compatibility. |
| **Probe** |  |  |
| [`flushprobe`](#flushprobe) |  | Ensure all debug probe requests have been completed. |
| **Registers** |  |  |
| [`reg`](#reg), [`rr`](#reg) | [-p] [-f] [REG...] | Print core or peripheral register(s). |
| [`wreg`](#wreg), [`wr`](#wreg) | [-r] [-p] [-f] REG VALUE | Set the value of a core or peripheral register. |
| **Rtt** |  |  |
| [`rtt`](#rtt) | rtt {setup,start,stop,channels,server} | Control SEGGER RTT compatible interface. |
| **Semihosting** |  |  |
| [`arm`](#arm) | semihosting {enable,disable} | Enable or disable semihosting. |
| **Servers** |  |  |
| [`gdbserver`](#gdbserver) | {start,stop,status} | Control the gdbserver for the selected core. |
| [`probeserver`](#probeserver) | {start,stop,status} | Control the debug probe server. |
| **Symbols** |  |  |
| [`symbol`](#symbol) | NAME | Show a symbol's value. |
| [`where`](#where) | [ADDR] | Show symbol, file, and line for address. |
| **Target** |  |  |
| [`status`](#status), [`st`](#status) |  | Show the target's current state. |
| **Threads** |  |  |
| [`threads`](#threads) | {flush,enable,disable,status} | Control thread awareness. |
| **Utility** |  |  |
| [`sleep`](#sleep) | MILLISECONDS | Sleep for a number of milliseconds before continuing. |
| **Values** |  |  |
| [`set`](#set) | NAME VALUE | Set a value. |
| [`show`](#show) | NAME | Display a value. |




All values
----------

Values represent a setting or piece of information that can be read and/or changed. They are accessed with
the [`show`](#show) and [`set`](#set) commands. The "Access" column of the table below shows whether the
command can be read, written, or both.



| Value | Access | Description |
|---|---|---|
| [`accessible-pins`](#accessible-pins) | read-write | Display which debug probe pins can be read and written with the 'pins' value. |
| [`aps`](#aps) | read-only | List discovered Access Ports. |
| [`cores`](#cores) | read-only | Information about CPU cores in the target. |
| [`debug-sequences`](#debug-sequences) | read-only | Show the available debug sequences from the target's DFP. |
| [`fault`](#fault) | read-only | Fault status information. |
| [`frequency`](#frequency) | write-only | Set SWD or JTAG clock frequency in Hertz. |
| [`graph`](#graph) | read-only | Print the target object graph. |
| [`hnonsec`](#hnonsec) | read-write | The current HNONSEC attribute value used by the selected MEM-AP. |
| [`hprot`](#hprot), [`memap_attr`](#hprot) | read-write | The current memory transfer attributes value used by the selected MEM-AP. |
| [`locked`](#locked) | read-only | Report whether the target is locked. |
| [`log`](#log) | write-only | Set log level to one of 'debug', 'info', 'warning', 'error', 'critical'. |
| [`map`](#map) | read-only | Target memory map. |
| [`mem-ap`](#mem-ap) | read-write | The currently selected MEM-AP used for memory read/write commands. |
| [`nreset`](#nreset) | read-write | Current nRESET signal state. |
| [`option`](#option) | read-write | The current value of one or more session options. |
| [`peripherals`](#peripherals) | read-only | List of target peripheral instances. |
| [`pins`](#pins) | read-write | Current debug probe protocol I/O pin states. |
| [`probe-uid`](#probe-uid), [`uid`](#probe-uid) | read-only | Target's unique ID. |
| [`register-groups`](#register-groups) | read-only | Display available register groups for the selected core. |
| [`reset-type`](#reset-type) | read-write | Show reset configuration and all available reset types for each core. Set current reset type. |
| [`step-into-interrupts`](#step-into-interrupts), [`si`](#step-into-interrupts) | read-write | Display whether interrupts are enabled when single stepping. |
| [`target`](#target) | read-only | General target information. |
| [`vector-catch`](#vector-catch), [`vc`](#vector-catch) | read-write | Show current vector catch settings. |




Command details
---------------
