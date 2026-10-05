---
id: "intr-seamless-firmware-development-with-getting-started-with-the-platformio-cli"
type: "concept"
domain: "debug"
title: "Seamless firmware development with PlatformIO: Getting Started with the PlatformIO CLI"
summary: "My favorite way to use PlatformIO is with the CLI, also known as \"PlatformIO Core\". Although some people swear by the VSCode plugin, I prefer my PlatformIO separate from my IDE so I can use trusty old Vim."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-08-seamless-firmware-with-platformio.md"
doc_source: "https://interrupt.memfault.com/blog/seamless-firmware-with-platformio#getting-started-with-the-platformio-cli"
license: "CC-BY-SA-4.0"
mode: "V"
---

My favorite way to use PlatformIO is with the CLI, also known as "PlatformIO Core".
Although some people swear by the VSCode plugin, I prefer my PlatformIO separate
from my IDE so I can use trusty old Vim.

In this next section, I will walk you through installing the CLI, starting a
project, adding some libraries, and compiling your work. All code is available
in the [Interrupt Github repository](https://github.com/memfault/interrupt),
under `example/platformio`.

### Installing the CLI

Installing the PlatformIO CLI is easy. On some platform, you can use your
package manager. For example, on mac:
```
$ brew install platformio
```

For all other platforms, you can use the `get-platformio.py` script, available
on their website[^get-platformio]. Download it and run it with `python
get-platformio.py`.

At this point, you should have `platformio` available as a CLI utility, as well
as a `pio` alias for faster use.

### Creating a project

The `pio` tool comes with project management commands. Let's say we want to
start a new project for our STM32F429zi discovery board.

First, we'll create a folder:
```
$ mkdir my-project
$ cd my-project
```

Then, we'll initialize the project with `pio project init`, and pass it a board
and a framework

```
$ pio project init --board disco_f429zi --project-options "framework=STM32Cube"
...
Project has been successfully initialized! Useful commands:
`pio run` - process/build project from the current directory
`pio run --target upload` or `pio run -t upload` - upload firmware to a target
`pio run --target clean` - clean project (remove compiled files)
`pio run --help` - additional information
```

### Toolchains and linker scripts

On many of my projects, I use a specific version of the GCC toolchain, and to
write my own linker script. You'll have to update your `platformio.ini` to
enable both of those things:

```
[env]
platform = ststm32
board = disco_f429zi
framework = stm32cube
platform_packages =
  ; GCC 4.8.4
  toolchain-gccarmnoneeabi@1.40804.0
board_build.ldscript = STM32F429ZIYX_FLASH.ld
```

The `board_build.ldscript` bit is straightforward: simply point it at the path
to your linker script within the project folder.

The `platform_packages` variable is more complicated. This option lets you
override the version of built-in packages, such as the support for different
Frameworks, specific toolchains, or built-in tools like OpenOCD.

Tool Packages can be downloaded from Github, or from Bintray where the PlatformIO
project hosts many of its binaries. For example, you can the list of available
builds of GCC at
https://bintray.com/platformio/tool-packages/toolchain-gccarmnoneeabi-darwin_x86_64#files.[^gcc-versions]

In my case, I specified "toolchain-gccarmnoneeabi@1.40804.0" which is GCC 4.8.4
(see the "40804" part of the package version?).

Using a custom built toolchain is a whole other can of worm, which requires
creating your own platform package.

### Writing some code

Your code should go under the `src` folder. In my case, I added a `main.c` file
and wrote a simple blinky firmware:

```c
#include "stm32f4xx_hal.h"

#define LED_PIN                                GPIO_PIN_5
#define LED_GPIO_PORT                          GPIOA
#define LED_GPIO_CLK_ENABLE()                  __HAL_RCC_GPIOA_CLK_ENABLE()
void LED_Init() {
  LED_GPIO_CLK_ENABLE();
  GPIO_InitTypeDef GPIO_InitStruct;
  GPIO_InitStruct.Pin = LED_PIN;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  GPIO_InitStruct.Speed = GPIO_SPEED_HIGH;
  HAL_GPIO_Init(LED_GPIO_PORT, &GPIO_InitStruct);
}

void SysTick_Handler(void) {
  HAL_IncTick();
}

int main(void) {
  HAL_Init();
  LED_Init();

  while (1)
  {
    HAL_GPIO_TogglePin(LED_GPIO_PORT, LED_PIN);
    HAL_Delay(1000);
  }
}
```

That's it! Note that your SDK configuration files (e.g. the `hal_conf.h` from
STM32Cube) should go in your `src` folder as well.

### Building the project

Next, we need to build our project. Here again we use the `platformio` cli tool.

```
$ pio run
Processing release (platform: ststm32; board: disco_f429zi; framework: stm32cube)
------------------------------------------------------------------------------------------------------------
Verbose mode can be enabled via `-v, --verbose` option
CONFIGURATION: https://docs.platformio.org/page/boards/ststm32/disco_f429zi.html
PLATFORM: ST STM32 (10.0.1) > ST 32F429IDISCOVERY
HARDWARE: STM32F429ZIT6 180MHz, 256KB RAM, 2MB Flash
DEBUG: Current (stlink) On-board (stlink) External (blackmagic, cmsis-dap, jlink)
PACKAGES:
 - framework-stm32cubef4 1.25.2
 - tool-ldscripts-ststm32 0.1.0
 - toolchain-gccarmnoneeabi 1.40804.0 (4.8.4)
LDF: Library Dependency Finder -> http://bit.ly/configure-pio-ldf
LDF Modes: Finder ~ chain, Compatibility ~ soft
Found 48 compatible libraries
Scanning dependencies...
No dependencies
Building in release mode
Compiling .pio/build/release/src/main.o
...
Linking .pio/build/release/firmware.elf
Checking size .pio/build/release/firmware.elf
Building .pio/build/release/firmware.bin
Advanced Memory Usage is available via "PlatformIO Home > Project Inspect"
RAM:   [          ]   0.0% (used 44 bytes from 262144 bytes)
Flash: [          ]   0.1% (used 1296 bytes from 2097152 bytes)
======================================= [SUCCESS] Took 10.92 seconds =====================================
```

Here's everything PlatformIO does for us here:

1. Download the library and framework files (e.g. chip SDK, RTOS, ...) for our project
2. Build all C, C++, and assembly files in our `src` folder
3. Build all the private libraries in `lib` and create static libraries for them
4. Link everything into an ELF
5. Copy it into a BIN
6. Print out RAM and Flash usage

All with minimal configuration!

### Unit Tests

Regular readers of Interrupt will know that we are [big fans of unit
testing](https://interrupt.memfault.com/blog/unit-testing-basics). PlatformIO has built in supports for running tests on your
host or on target.

For a simple example, consider this trivial library:

Header:
```c
// lib/add/src/add .h
#pragma once

int add(int a, int b);
```

C:
```c
// lib/add/src/add.c
#include "add.h"

int add(int a, int b) {
    return a + b;
}
```

We put those two files in our project under `lib/add/src`, and add a local test
target to our platformio.ini

```
[env:native]
platform = native
```

It's also a good idea to add a `default_envs` property at the top of our
`platformio.ini` file to avoid building the `native` environment for regular
builds. Otherwise PlatformIO will try building our firmware for our native
machine when running `pio run` which will fail:

```
[platformio]
default_envs = release
```

We then write a test file in the `test` folder:

```c
// test/test_add.c
#include "add.h"


void test_add(void) {
    TEST_ASSERT_EQUAL(32, add(25, 7));
}

int main(int argc, char **argv) {
    UNITY_BEGIN();
    RUN_TEST(test_add);
    UNITY_END();

    return 0;
}
```

We can then run our test with `pio test -e native`:

```
$ pio test -e native
Verbose mode can be enabled via `-v, --verbose` option
Collected 1 items

Processing test_add in native environment
------------------------------------------------------------------------------------------------------------
Building...
Testing...
test/test_add/test_add.c:13:test_add    [PASSED]

-----------------------
1 Tests 0 Failures 0 Ignored
OK
======================================== [PASSED] Took 1.27 seconds ========================================

Test      Environment    Status    Duration
--------  -------------  --------  ------------
test_add  native         PASSED    00:00:01.265
======================================= 1 succeeded in 00:00:01.265 =======================================
```
