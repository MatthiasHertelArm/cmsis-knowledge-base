---
id: "intr-profiling-firmware-on-cortex-m-setup"
type: "concept"
domain: "debug"
title: "Profiling Firmware on Cortex-M: Setup"
summary: "All of the code in this post was written for the STM32F429i Discovery Kit[^disco] by ST Micro."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-02-profiling-firmware-on-cortex-m.md"
doc_source: "https://interrupt.memfault.com/blog/profiling-firmware-on-cortex-m#setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

All of the code in this post was written for the STM32F429i Discovery
Kit[^disco] by ST Micro. This board is well supported by open source tooling and
comes with a built-in STLink debugger with the SWO pin routed through it (more
on that later).

As in previous blog posts, we use the excellent openocd tool[^openocd] to
interface with the board on our laptop. Openocd allows us to flash, debug, and
profile the board over USB using the STLink protocol. Since it has built it
support for our Discovery board, we simply need to connect our board to our
laptop over USB via the "USB-STLINK" port, and run the following command on
a recent version of the tool:

```bash
$ openocd -f board/stm32f429disc1.cfg
```

### Enabling SWO

Note that the SWO pin is not connected by default on the Discovery board.
Instead, a solder bridge is used to enable the functionality per the User
Manual, Section 6.13[^disco-um].

Simply grab a soldering iron and bridge the two pads labeled "SB9" with a bit
of solder or a 0-ohm resistor. Here is my handywork:



### Code Under Test

In order to have something interesting to profile, we used the Mandelbrot
program bundled as an example with libopenCM3[^libopencm3]. This simple program
draws the Mandelbrot fractal on the Discovery board's LCD screen in a loop. This
is CPU intensive and gives us good profiling data.

The example is available on
[Github](https://github.com/libopencm3/libopencm3-examples/tree/master/examples/stm32/f4/stm32f429i-discovery/mandelbrot-lcd).

To clone, build, and flash this example follow these simple steps:

```shell
# Clone libopencm3-examples with submodules
$ git clone https://github.com/libopencm3/libopencm3-examples.git --recurse-submodules
...
# Navigate to the Mandelbrot example
$ cd libopencm3-examples/examples/stm32/f4/stm32f429i-discovery/mandelbrot-lcd

# Build the example
$ make
Using ../../../../../libopencm3/ path to library
arm-none-eabi-gcc -Os -std=c99 -ggdb3 -mthumb -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 -Wextra -Wshadow -Wimplicit-function-declaration -Wredundant-decls -Wmissing-prototypes -Wstrict-prototypes -fno-common -ffunction-sections -fdata-sections  -MD -Wall -Wundef -DSTM32F4 -I../../../../../libopencm3//include  -o sdram.o -c sdram.c
arm-none-eabi-gcc -Os -std=c99 -ggdb3 -mthumb -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 -Wextra -Wshadow -Wimplicit-function-declaration -Wredundant-decls -Wmissing-prototypes -Wstrict-prototypes -fno-common -ffunction-sections -fdata-sections  -MD -Wall -Wundef -DSTM32F4 -I../../../../../libopencm3//include  -o lcd.o -c lcd.c
arm-none-eabi-gcc -Os -std=c99 -ggdb3 -mthumb -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 -Wextra -Wshadow -Wimplicit-function-declaration -Wredundant-decls -Wmissing-prototypes -Wstrict-prototypes -fno-common -ffunction-sections -fdata-sections  -MD -Wall -Wundef -DSTM32F4 -I../../../../../libopencm3//include  -o clock.o -c clock.c
arm-none-eabi-gcc -Os -std=c99 -ggdb3 -mthumb -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 -Wextra -Wshadow -Wimplicit-function-declaration -Wredundant-decls -Wmissing-prototypes -Wstrict-prototypes -fno-common -ffunction-sections -fdata-sections  -MD -Wall -Wundef -DSTM32F4 -I../../../../../libopencm3//include  -o mandel.o -c mandel.c
arm-none-eabi-gcc --static -nostartfiles -T../stm32f429i-discovery.ld -mthumb -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 -ggdb3 -Wl,-Map=mandel.map -Wl,--cref -Wl,--gc-sections -L../../../../../libopencm3//lib sdram.o lcd.o clock.o mandel.o -lopencm3_stm32f4 -Wl,--start-group -lc -lgcc -lnosys -Wl,--end-group -o mandel.elf

# start GDB
$ arm-none-eabi-gdb mandel.elf

# Connect to OpenOCD (it must already be running in another terminal)
(gdb) target remote :3333

# Reset & Halt the target
(gdb) monitor reset halt

# Flash the firmware
(gdb) load

# Start the firmware
(gdb) continue
```

You should now be seeing the Mandelbrot fractal on the LCD of the Discovery
board. Here it is!


