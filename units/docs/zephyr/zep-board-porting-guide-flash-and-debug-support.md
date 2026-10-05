---
id: "zep-board-porting-guide-flash-and-debug-support"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Flash and debug support"
summary: "Zephyr supports west-build-flash-debug via west extension commands."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr supports west-build-flash-debug via west extension commands.

To add `west flash` and `west debug` support for your board, you need to
create a `board.cmake` file in your board directory. This file's job is
to configure a "runner" for your board. (There's nothing special you need to
do to get `west build` support for your board.)

"Runners" are Zephyr-specific Python classes that wrap :ref:`flash and debug
host tools <flash-debug-host-tools>` and integrate with west and the zephyr build
system to support `west flash` and related commands. Each runner supports
flashing, debugging, or both. You need to configure the arguments to these
Python scripts in your `board.cmake` to support those commands like this
example `board.cmake`:

```cmake

board_runner_args(jlink "--device=nrf52" "--speed=4000")
board_runner_args(pyocd "--target=nrf52" "--frequency=4000000")

include(${ZEPHYR_BASE}/boards/common/nrfutil.board.cmake)
include(${ZEPHYR_BASE}/boards/common/nrfjprog.board.cmake)
include(${ZEPHYR_BASE}/boards/common/jlink.board.cmake)
include(${ZEPHYR_BASE}/boards/common/pyocd.board.cmake)
```
This example configures the `nrfutil`, `nrfjprog`, `jlink`, and `pyocd`
runners.


**Warning:** Runners usually have names which match the tools they wrap, so the `jlink` runner wraps Segger's J-Link tools, and so on. But the runner command line options like `--speed` etc. are specific to the Python scripts.


**Note:** Runners and board configuration should be created without being targeted to a single operating system if the tool supports multiple operating systems, nor should it rely upon special system setup/configuration. For example; do not assume that a user will have prior knowledge/configuration or (if using Linux) special udev rules installed, do not assume one specific `/dev/X` device for all platforms as this will not be compatible with Windows or macOS, and allow for overriding of the selected device so that multiple boards can be connected to a single system and flashed/debugged at the choice of the user.

For more details:

- Run `west flash --context` to see a list of available runners which support
  flashing, and `west flash --context -r <RUNNER>` to view the specific options
  available for an individual runner.
- Run `west debug --context` and `west debug --context <RUNNER>` to get
  the same output for runners which support debugging.
- Run `west flash --help` and `west debug --help` for top-level options
  for flashing and debugging.
- See west-runner for Python APIs.
- Look for `board.cmake` files for other boards similar to your own for
  more examples.

To see what a `west flash` or `west debug` command is doing exactly, run it
in verbose mode:

```sh

west --verbose flash
west --verbose debug
```
Verbose mode prints any host tool commands the runner uses.

The order of the `include()` calls in your `board.cmake` matters. The
first `include` sets the default runner if it's not already set. For example,
including `nrfjprog.board.cmake` first means that `nrfjprog` is the default
flash runner for this board. Since `nrfjprog` does not support debugging,
`jlink` is the default debug runner.
