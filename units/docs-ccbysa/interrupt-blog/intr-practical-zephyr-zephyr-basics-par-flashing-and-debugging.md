---
id: "intr-practical-zephyr-zephyr-basics-par-flashing-and-debugging"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1): Flashing and debugging"
summary: "Having built our first freestanding application, let's have a brief look at how we can flash and debug it on our target. We can do both using the flash and debug extension commands provided by Zephyr for West."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics#flashing-and-debugging"
license: "CC-BY-SA-4.0"
mode: "V"
---

Having built our first freestanding application, let's have a brief look at how we can flash and debug it on our target. We can do both using the `flash` and `debug` [extension commands](https://docs.zephyrproject.org/latest/develop/west/build-flash-debug.html) provided by Zephyr for _West_. With the development kit plugged in, all we need to do is run `west flash` to program the MCU (the parameter `-d` is necessary to select the correct build directory in case it isn't located in the executing folder):

```bash
west flash -d ../build
-- west flash: rebuilding
ninja: no work to do.
-- west flash: using runner nrfjprog
Using board 123456789
-- runners.nrfjprog: Flashing file: ../build/zephyr/zephyr.hex
Parsing image file.
Verifying programming.
Verified OK.
Enabling pin reset.
Applying pin reset.
-- runners.nrfjprog: Board with serial number 123456789 flashed successfully.
```

> **Note:** In case you haven't followed the [installation](#installation) in this article but instead used your own setup, this step might not succeed: As you can see, _West_ uses Nordic's [nRF Command Line Tool](https://www.nordicsemi.com/Products/Development-tools/nrf-command-line-tools) `nrfjprog` to program the development kit. In case this tool isn't available, the execution will fail. In general, flashing and debugging is always very target specific and you'll need to ensure that the correct tools are installed.

Wait, so how does Zephyr know which USB device to flash and _how_ to do this? _West_ uses so-called [flash and debug **runners**](https://docs.zephyrproject.org/latest/develop/west/build-flash-debug.html#flash-and-debug-runners). In the above output, you can see that it selects Nordic's `nrfjprog` [command line tool](https://www.nordicsemi.com/Products/Development-tools/nrf-command-line-tools) as _runner_, which is, in turn, able to identify whether or not a board is connected to your computer. In case only a single matching board is present, it automatically programs that board.

The _West_ extension command `debug` works similarly:

```bash
$ west debug -d ../build
-- west debug: rebuilding
ninja: no work to do.
-- west debug: using runner jlink
-- runners.jlink: JLink version: 7.66a
-- runners.jlink: J-Link GDB server running on port 2331; no thread info available
SEGGER J-Link GDB Server V7.66a Command Line Version

...

--Type <RET> for more, q to quit, c to continue without paging--
(gdb)
```

Here, _West_ selected the J-Link runner since the development kit comes with a J-Link debugger. We end up with a `gdb` console which we can use to debug our application:

```bash
(gdb) break main
Breakpoint 1 at 0x4730: file /path/to/src/main.c, line 11.
(gdb) continue
Continuing.

Breakpoint 1, main () at /path/to/src/main.c:11
11              k_msleep(SLEEP_TIME_MS);
(gdb) next

Breakpoint 1, main () at /path/to/src/main.c:11
11              k_msleep(SLEEP_TIME_MS);
(gdb) next

Breakpoint 1, main () at /path/to/src/main.c:11
11              k_msleep(SLEEP_TIME_MS);
```

Debugging with `gdb` may be all you need, especially if you pair this with Python scripts.


### Debugging ARM Cortex-M targets in `VS Code`

Aside from plain `gdb`, step debugging in your editor of choice is another very popular approach.

`VS Code` is becoming more and more prominent, which is why it is worth mentioning that debugging solutions exist that allow step debugging within the editor, e.g., via the [`cortex-debug`](https://marketplace.visualstudio.com/items?itemName=marus25.cortex-debug) extension for ARM Cortex-M microcontrollers.

Setting up debugging in `VS Code` is explained in the [official documentation](https://code.visualstudio.com/docs/editor/debugging), and comes down to providing launch configurations in the JSON file `.vscode/launch.json`. The following is an example file that can be used to debug Zephyr applications on boards using the nRF52840 microcontroller:

`.vscode/launch.json`
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "nRF52840_xxAA - attach",
      "device": "nRF52840_xxAA",
      "cwd": "${workspaceFolder}",
      "executable": "build/zephyr/zephyr.elf",
      "request": "launch",
      "type": "cortex-debug",
      "runToEntryPoint": "main",
      "servertype": "jlink",
      "gdbPath": "/opt/nordic/ncs/toolchains/322ac893fe/opt/zephyr-sdk/arm-zephyr-eabi/bin/arm-zephyr-eabi-gdb"
    }
  ]
}
```

> **Note:** Support for GDB comes out of the box with `VS Code` and could also be used instead of relying on `cortex-debug`. Also, in case you're sourcing `setup.sh` before launching `VS Code`, you can use the environment variable for the `gdbPath` setting, e.g., `"gdbPath": "${env:ZEPHYR_SDK_INSTALL_DIR}/arm-zephyr-eabi/bin/arm-zephyr-eabi-gdb"`



Your mileage, however, will always vary according to the MCU that you're using, and there is no generic solution. Zephyr's official documentation also comes with a dedicated [section about debugging](https://docs.zephyrproject.org/latest/develop/debug/index.html), and a separate section about [flash & debug host tools](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html). Pick your poison!

Another great resource about `VS Code` with Zephyr is [Jonathan Beri's presentation "Zephyr & Visual Studio Code: How to Develop Zephyr Apps with a Modern, Visual IDE"](https://www.youtube.com/watch?v=IKNHPmG-Qxo) from the 2023 Zephyr Development Summit.
