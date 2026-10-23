---
id: "dbgx-arm-cmsis-debugger-known-limitations-and-workarounds"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Known Limitations and Workarounds"
summary: "There is an chip errata that single stepping on Cortex-M7 r0p1 processors enters the pending exception handler incorrectly which may result in error messages. Check the processor revision that is shown at debug start in the DEBUG CONSOLE."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/README.md#known-limitations-and-workarounds"
license: "Apache-2.0"
mode: "V"
---

### Internal Errors on stepping through code

There is an [chip errata](https://developer.arm.com/documentation/SDEN1068427/latest/) that single stepping on Cortex-M7 r0p1 processors enters the pending exception handler incorrectly which may result in error messages. Check the processor revision that is shown at debug start in the DEBUG CONSOLE.

**Workaround/Solution**:

Some devices allow to stop timer interrupts with control registers. For the example the STM32 devices have `DbgMCU_APB1_Fz` registers. Stop all timers that are active in your application. This can be typially configured in the [`*.dbgconf` file](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#device-configuration) of your project.

### pyOCD fails to load `*.cbuild-run.yml` in the default configuration

When I use the default debug configuration for pyOCD, I get errors that pyOCD cannot find the solutions
`*.cbuild-run.yml` file.

**Possible Reasons**:

1. The application's CMSIS solution was initially built with a CMSIS-Toolbox version prior to v2.8.0 which is
the first version to generate `*.cbuild-run.yml` files.
1. You are using an [Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) extension
prior to v1.52.0 which is the first version to fully support the `${command:cmsis-csolution.getCbuildRunFile}` command.

**Workarounds/Solutions**:

1. Update the CMSIS-Toolbox to the latest version. Additionally, you may have to run `cbuild setup --update-rte`
in a terminal for a first-time generation of `*.cbuild-run.yml` file in an existing workspace.
1. Update to Arm CMSIS Solution extension v1.52.0. Alternatively, replace
`${command:cmsis-csolution.getCbuildRunFile}` with the path to the `*.cbuild-run.yml` in your workspace
(`cmsis`>`cbuildRunFile` debug configuration setting).

### AXF files built with Arm Compiler 6 toolchain

When I download an AXF file built with Arm Compiler 6, I see the following warning and my application
does not execute correctly. This happens regardless of the selected GDB server.

```txt
warning: Loadable section "RW_RAM0" outside of ELF segments
  in /path/to/my/application.axf
```

**Possible Reason**: `arm-none-eabi-gdb` does not correctly load ELF program segments due to the way that
Arm Compiler 6 generates section and program header information when scatter loading is used.

**Workaround**: You can generate a HEX file for the program download, and the ELF file for debug purposes only.
The following steps are required if you build a [CSolution](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/)-based
application with the [CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/):

1. Edit the `*.cproject.yml` file(s) of your application.
1. Modify the [`output:type:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#output) node
to generate both an `elf` and a `hex` file:

```yml
  output:
    type:
      - elf
      - hex  
```

1. Build the solution.
1. Keep the default configuration's `program` setting as is.

```txt
"program": "${command:cmsis-csolution.getBinaryFile}",
```

1. Modify the default debug configuration's `initCommands` list, so that the `load` command gets the relative
path to the generated HEX file.

```json
"initCommands": [
    "load ./relative/path/to/my/application.hex",
    "break main"
],
```

This instructs the debugger to load the debug information from the ELF file and to use the HEX file
for program download.

### `arm-none-eabi-gdb` requires DWARF5 debug information

`arm-none-eabi-gdb` generates the following warnings when I debug ELF files with [DWARF](https://dwarfstd.org/) debug
information of standard version 4 and earlier. And the debug illusion seems to be broken in many places.  

```txt
warning: (Internal error: pc 0x8006a18 in read in CU, but not in symtab.)
```

**Possible Reason**: `arm-none-eabi-gdb` works best with DWARF debug information of standard version 5.

**Solution**: Make sure to build your application ELF file with DWARF version 5 debug information. Please refer to
your toolchain's user reference manual. This may require updates to all build tools like compiler and assembler.
For example use `-gdwarf-5` for `armclang`.

### Broken debug illusion

When debugging ELF files with [DWARF](https://dwarfstd.org/) debug information of standard version 4 and earlier,
`arm-none-eabi-gdb` generates the following warnings:

```txt
warning: (Internal error: pc 0x8006a18 in read in CU, but not in symtab.)
```

The debug illusion will be broken in many places.

**Possible Reason**: Missing DWARF5 debug information

`arm-none-eabi-gdb` works best with DWARF debug information of standard version 5.

**Solution**: Build the ELF file using DWARF5

Make sure to build your application ELF file with DWARF version 5 debug information.

### pyOCD port not available

When starting a debug session, you might see this error:

(figure: Remote communication error)

**Possible reason**: A running instance of pyOCD

This error might occur if a previous debug session has ended prematuerly and pyOCD has not exited. The orphaned instance
will still keep the port open (usually 3333) and thus you won't be able to open the port again in the new session.

**Solution**: Check open files and kill pyOCD

On Linux and macOS you can check the running open files using the [`lsof`](https://de.wikipedia.org/wiki/Lsof) command:

```sh
sudo lsof -i -n -P | grep 3333

Python    41836       user01    3u  IPv4 0xa6ef66ad5be49a4f      0t0    TCP *:3333 (LISTEN)
pyocd     41842       user01    8u  IPv4 0x9d09900145f3ca41
```

To kill the running pyOCD process, use:

```sh
sudo killall pyocd
```

On Windows systems, use the
[Windows Task Manager](https://learn.microsoft.com/en-us/troubleshoot/windows-server/support-tools/support-tools-task-manager)
or the [Process Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer) to find orphaned
processes.
