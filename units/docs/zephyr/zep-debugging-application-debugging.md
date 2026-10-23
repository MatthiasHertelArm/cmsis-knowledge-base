---
id: "zep-debugging-application-debugging"
type: "concept"
domain: "debug"
title: "Debugging: Application Debugging"
summary: "This section is a quick hands-on reference to start debugging your application with QEMU. Most content in this section is already covered in QEMU and GNU_Debugger reference manuals."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/debug/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/debug/index.rst"
license: "Apache-2.0"
mode: "V"
---

This section is a quick hands-on reference to start debugging your
application with QEMU. Most content in this section is already covered in
QEMU and GNU_Debugger reference manuals.

In this quick reference, you'll find shortcuts, specific environmental
variables, and parameters that can help you to quickly set up your debugging
environment.

The simplest way to debug an application running in QEMU is using the GNU
Debugger and setting a local GDB server in your development system through QEMU.

You will need an `ELF (Executable and Linkable Format)` binary image for
debugging purposes.  The build system generates the image in the build
directory.  By default, the kernel binary name is `zephyr.elf`. The name
can be changed using `CONFIG_KERNEL_BIN_NAME`.


### GDB server


We will use the standard 1234 TCP port to open a `GDB (GNU Debugger)`
server instance. This port number can be changed for a port that best suits the
development environment. There are multiple ways to do this. Each way starts a
QEMU instance with the processor halted at startup and with a GDB server
instance listening for a connection.


#### Running QEMU directly


You can run QEMU to listen for a "gdb connection" before it starts executing any
code to debug it.

```bash

qemu -s -S <image>
```
will setup Qemu to listen on port 1234 and wait for a GDB connection to it.

The options used above have the following meaning:

* `-S` Do not start CPU at startup; rather, you must type 'c' in the
  monitor.
* `-s` Shorthand for `-gdb tcp::1234`: open a GDB server on
  TCP port 1234.



#### Running QEMU via `ninja`


Run the following inside the build directory of an application:

```console

ninja debugserver
```
QEMU will write the console output to the path specified in
`${QEMU_PIPE}` via CMake, typically `qemu-fifo` within the build
directory. You may monitor this file during the run with :command:`tail -f
qemu-fifo`.


#### Running QEMU via `west`


Run the following from your project root:

```console

west build -t debugserver_qemu
```
QEMU will write the console output to the terminal from which you invoked
`west`.


#### Configuring the `gdbserver` listening device


The Kconfig option `CONFIG_QEMU_GDBSERVER_LISTEN_DEV` controls
the listening device, which can be a TCP port number or a path to a character
device. GDB releases 9.0 and newer also support Unix domain sockets.

If the option is unset, then the QEMU invocation will lack a `-s` or a
`-gdb` parameter. You can then use the `QEMU_EXTRA_FLAGS` shell
environment variable to pass in your own listen device configuration.


### GDB client


Connect to the server by running `gdb` and giving these commands:

```bash

$ path/to/gdb path/to/zephyr.elf
(gdb) target remote localhost:1234
(gdb) dir ZEPHYR_BASE
```

**Note:** Substitute the correct ZEPHYR_BASE for your system.

You can use a local GDB configuration `.gdbinit` to initialize your GDB
instance on every run. Your home directory is a typical location for
`.gdbinit`, but you can configure GDB to load from other locations,
including the directory from which you invoked `gdb`. This example
file performs the same configuration as above:

```none

target remote localhost:1234
dir ZEPHYR_BASE
```

#### Alternate interfaces


GDB provides a curses-based interface that runs in the terminal. Pass the `--tui`
option when invoking `gdb` or give the `tui enable` command within
`gdb`.


**Note:** The GDB version on your development system might not support the `--tui` option. Please make sure you use the GDB binary from the SDK which corresponds to the toolchain that has been used to build the binary.

Finally, the command below connects to the GDB server using the :abbr:`DDD
(Data Display Debugger)`, a graphical frontend for GDB. The following command
loads the symbol table from the ELF binary file, in this instance,
`zephyr.elf`.

```bash

ddd --gdb --debugger "gdb zephyr.elf"
```
Both commands execute `gdb`. The command name might
change depending on the toolchain you are using and your cross-development
tools.

`ddd` may not be installed in your
development system by default. Follow your system instructions to install
it. For example, use `sudo apt-get install ddd` on an Ubuntu system.


### Debugging


As configured above, when you connect the GDB client, the application will be
stopped at system startup. You may set breakpoints, step through code, etc. as
when running the application directly within `gdb`.


**Note:** unlike when you run a native application in GDB directly. If you just but nothing will appear to happen. Check the console output as described above.
