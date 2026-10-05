---
id: "intr-cortex-m-mcu-emulation-with-renode-running-our-firmware-in-renode"
type: "concept"
domain: "debug"
title: "Cortex-M MCU Emulation with Renode: Running our firmware in Renode"
summary: "Let's write a hello world firmware to run via Renode. We will target the STM23F4 Discovery board, as the emulator supports it out of the box."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-23-intro-to-renode.md"
doc_source: "https://interrupt.memfault.com/blog/intro-to-renode#running-our-firmware-in-renode"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's write a hello world firmware to run via Renode. We will target the STM23F4
Discovery board, as the emulator supports it out of the box.

### A simple firmware

I chose to use libopencm3[^1], an open-source library for ARM cortex-M
microcontrollers. I enjoy how easy it is to get started with it and appreciate
the consistent API across microcontrollers. Note however that the library is
still in its early stages and likely not fit for production use. I used the
libopencm3 template [^2] as a starting point.

To get to a "hello, world!", we must:

1. Setup the peripheral clocks
2. Enable the UART GPIOs
3. Configure the UART peripheral
4. Implement the `_write` syscall

I've reproduced the source code below, you can find the full project (Makefile
included) in the interrupt Github repo.

```c
#include <errno.h>
#include <stdio.h>
#include <unistd.h>
#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>
#include <libopencm3/stm32/usart.h>

static void clock_setup(void)
{
    /* Enable GPIOD clock for LED & USARTs. */
    rcc_periph_clock_enable(RCC_GPIOD);
    rcc_periph_clock_enable(RCC_GPIOA);

    /* Enable clocks for USART2. */
    rcc_periph_clock_enable(RCC_USART2);
}

static void usart_setup(void)
{
    /* Setup USART2 parameters. */
    usart_set_baudrate(USART2, 115200);
    usart_set_databits(USART2, 8);
    usart_set_stopbits(USART2, USART_STOPBITS_1);
    usart_set_mode(USART2, USART_MODE_TX);
    usart_set_parity(USART2, USART_PARITY_NONE);
    usart_set_flow_control(USART2, USART_FLOWCONTROL_NONE);

    /* Finally enable the USART. */
    usart_enable(USART2);
}

static void gpio_setup(void)
{
    /* Setup GPIO pin GPIO12 on GPIO port D for LED. */
    gpio_mode_setup(GPIOD, GPIO_MODE_OUTPUT, GPIO_PUPD_NONE, GPIO12);

    /* Setup GPIO pins for USART2 transmit. */
    gpio_mode_setup(GPIOA, GPIO_MODE_AF, GPIO_PUPD_NONE, GPIO2);

    /* Setup USART2 TX pin as alternate function. */
    gpio_set_af(GPIOA, GPIO_AF7, GPIO2);
}

int _write(int file, char *ptr, int len)
{
    int i;

    if (file == STDOUT_FILENO || file == STDERR_FILENO) {
        for (i = 0; i < len; i++) {
            if (ptr[i] == '\n') {
                usart_send_blocking(USART2, '\r');
            }
            usart_send_blocking(USART2, ptr[i]);
        }
        return i;
    }
    errno = EIO;
    return -1;
}

int main(void) {
    clock_setup();
    gpio_setup();
    usart_setup();

    printf("hello world!\n");

    while (1) {}

    return 0;
}
```

If all goes well, we now have a `renode-example.elf` file we can load in the
emulator.

### Running our firmware in Renode

Next up, we must spin up a machine in Renode and run our firmware in it.

Like we did earlier, we first start Renode:

```
$ git clone https://github.com/memfault/interrupt.git
$ cd example/renode/
$ make
# Note: on Linux this just is the "renode" command
$ sh /Applications/Renode.app/Contents/MacOS/macos_run.command
```

The window that pops up is called the Renode _monitor_. In it, you can run
Renode commands.

We now need to create a _machine_. A machine represents a device, which can have
a number of cores. Renode can run multiple machines in a single run.

We can create, add, and remove machines with the `mach` command:

```
(monitor) mach create
(machine-0)
```

The prompt now includes our machine name. Since we did not name our machine, it
just says "machine-0".

Next, we configure our machine. We could specify each bus and peripheral by
hand, but instead we will load a prebuilt configuration.

```
(machine-0) machine LoadPlatformDescription @platforms/boards/stm32f4_discovery-kit.repl
(machine-0)
```

You will notice that the path is prepended with the `@` sign. This is a C#-ism.
Renode will load absolute paths, as well as paths relative to your working
directory, and paths relative to the renode installation. In our case, we used
the latter as `platforms` is bundled with the Renode installation.

Next, we load our firmware:

```
(machine-0) sysbus LoadELF @renode-example.elf
(machine-0)
```

> Note: You can also load `.bin` files with `sysbus LoadBinary`

Before we start the machine, we want to do one last thing: open a terminal to
display UART data. Some peripherals come with what Renode calls "Analyzers",
which are ways to display their state and data. We enabled UART2 in our
firmware, so we will show the analyzer for UART2.

```
(machine-0) showAnalyzer sysbus.uart2
(machine-0)
```

You should now have two Renode windows open, the monitor window and the UART2
window.

We are now ready to run our simulation with the `start` command:

```
(machine-0) start
```

#### Adding CCM memory

... Well, this is embarrassing. Nothing happened.

In the terminal window we used to start the Renode app, we see line after line
of warnings:

```
[...]
20:46:07.5783 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AA3, value 0x0.
20:46:07.5783 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AA4, value 0x0.
20:46:07.5783 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AA5, value 0x0.
20:46:07.5795 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AA6, value 0x0.
20:46:07.5799 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AA7, value 0x0.
20:46:07.5800 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AA8, value 0x0.
20:46:07.5800 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AA9, value 0x0.
20:46:07.5800 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AAA, value 0x0.
20:46:07.5801 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AAB, value 0x0.
20:46:07.5801 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AAC, value 0x0.
20:46:07.5801 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AAD, value 0x0.
20:46:07.5802 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AAE, value 0x0.
20:46:07.5802 [WARNING] sysbus: [cpu: 0x8000926] WriteByte to non existing peripheral at 0x10152AAF, value 0x0.
[...]
```

Let's quit the emulator for now and restart it once things are fixed

```
(monitor) quit
```

Looking at our chip's memory map, we notice that `0x10XXXXXX` is in the CCM
region. Turns out the renode model does not implement it. Fear not! This is
easily fixed.

The easiest way to modify our Machine to add the CCM RAM is to write a Renode
Platform (or "repl") file. Repl files use YAML-like syntax to define
peripherals, including their type, address, and size.

You can read more about the Platform Description file format in the [Renode
Documentation](https://renode.readthedocs.io/en/latest/advanced/platform_description_format.html)
Adding our CCM region requires the following:

```
// In "add-ccm.repl"
ccm: Memory.MappedMemory @ sysbus 0x10000000
    size: 0x10000
```

Since platform descriptions are composable, We can now load that file using the
same `LoadPlatformDescription` command we used earlier:

```
(machine-0) machine LoadPlatformDescription @add-ccm.repl
(machine-0)
```

Putting it all together we have:

```
(monitor) mach create
(machine-0) machine LoadPlatformDescription @platforms/boards/stm32f4_discovery-kit.repl
(machine-0) sysbus LoadELF @renode-example.elf
(machine-0) machine LoadPlatformDescription @add-ccm.repl
(machine-0) showAnalyzer sysbus.uart2
(machine-0) start
```

And voila, we now have `hello world!` string in the analyzer!



### Automating setup with a `.resc` script

Typing all this out is a bit of a hassle, this is where Renode Scripts ".resc"
files come in.

Not much documentation can be found on `.resc` files, but here are a few things
I was able to figure out:

1. variables can be created with `$` and assigned with `=`. For example: `$hello = "world"`.
2. renode are executed in the order written
3. macros can be defined with the keyword `macro`, and start and end with `"""`

Putting this all together, we can write the following script to setup our hello
world example:

```
# Filename: renode-config.resc
$bin?=@renode-example.elf

# Create Machine & Load config
mach create
machine LoadPlatformDescription @platforms/boards/stm32f4_discovery-kit.repl
machine LoadPlatformDescription @add-ccm.repl

# Create a terminal window showing the output of UART2
showAnalyzer sysbus.uart2

macro reset
"""
    sysbus LoadELF $bin
"""

runMacro $reset
```

We can start renode with this script by passing it as an argument to our renode
command. I wrapped it all in a `start.sh` shell script:

```
#!/bin/sh

sh /Applications/Renode.app/Contents/MacOS/macos_run.command renode-config.resc
```

> **Reset macro**: Renode looks for a macro named "reset", and uses it to reset
> the machine when the `machine Reset` or `machine RequestReset` are issued. In our script,
> we use that macro to reload our elf file every time, so we do not have to do
> it manually between resets. This also guarantees that the latest elf file is
> picked up and allows us to iterate on code quickly.

### Managing machine lifecycle

Starting renode every time you want to restart your machine is cumbersome.
Instead, we can use lifecycle commands to start, pause, and reset our machine:

```
# start a machine
(machine-0) start
# pause a machine
(machine-0) pause
# reset a machine
(machine-0) machine RequestReset
```

These are all pretty self-explanatory. Note that the `RequestReset` command will
invoke your `reset` macro if you have one specified.

Last but not least, you can drop the whole emulation by using the `Clear`
command.
