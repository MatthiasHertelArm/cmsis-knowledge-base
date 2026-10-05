---
id: "intr-get-the-most-out-of-the-linker-map-blinky"
type: "concept"
domain: "debug"
title: "Get the most out of the linker map file: Blinky"
summary: "👨‍🦳 What's better than our good old friend to explain the basics of the map file?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-09-get-the-most-out-of-the-linker-map-file.md"
doc_source: "https://interrupt.memfault.com/blog/get-the-most-out-of-the-linker-map-file#blinky"
license: "CC-BY-SA-4.0"
mode: "V"
---

👨‍🦳 What's better than our good old friend to explain the basics of the map file?

In order to learn about map files, let's compile a simple LED-blink program, and modify it to add a call to `atoi`. We will then use the map file to dissect the differences between both programs. The main file, available [here](https://github.com/memfault/interrupt/blob/master/example/linker-map-post/main.c) for you to play with, can be used as a replacement for the Blinky example from the nRF5 SDK. Looking at the `main.c` file, 3 configurations are possible: `NO_ATOI`, `STD_ATOI`, `CUSTOM_ATOI`.

Let's build the simplest version of that project (`NO_ATOI`), equivalent to this piece of code:
```c

#include <stdbool.h>
#include <stdint.h>
#include "nrf_delay.h"
#include "boards.h"

/**
 * @brief Function for application main entry.
 */
int main(void)
{
    /* Configure board. */
    bsp_board_init(BSP_INIT_LEDS);

    /* Toggle LEDs. */
    while (true)
    {
        for (int i = 0; i < LEDS_NUMBER; i++)
        {
            bsp_board_led_invert(i);
            nrf_delay_ms(300);
        }
    }
}
```

Compiling:
```
    $ make
    Assembling file: gcc_startup_nrf52840.S
    Compiling file: boards.c
    Compiling file: main.c
    Compiling file: system_nrf52840.c
    Linking target: _build/nrf52840_xxaa.out
       text	   data	    bss	    dec	    hex	filename
       1704	    108	     28	   1840	    730	_build/nrf52840_xxaa.out
    Preparing: _build/nrf52840_xxaa.hex
    Preparing: _build/nrf52840_xxaa.bin
    DONE nrf52840_xxaa
```

The generated map file is 563-line long 😮, even though it does nothing more than blink LEDs. That many lines cannot be left unseen, there must be some serious information in there...

Now let's modify our program to add a call to `atoi`. Instead of using an integer directly for the delay, we'll encode it as a string and decode it with `atoi`.
Here is the code using the configuration `STD_ATOI`:

```c

#include <stdbool.h>
#include <stdint.h>
#include "nrf_delay.h"
#include "boards.h"
#include "stdlib.h"

static const char* _delay_ms_str = "300";

/**
 * @brief Function for application main entry.
 */
int main(void)
{
    /* Configure board. */
    bsp_board_init(BSP_INIT_LEDS);
    int delay = atoi(_delay_ms_str);

    /* Toggle LEDs. */
    while (true)
    {
        for (int i = 0; i < LEDS_NUMBER; i++)
        {
            bsp_board_led_invert(i);
            nrf_delay_ms(delay);
        }
    }
}
```

After compilation, the whole program goes from 1840 bytes to 2396 bytes.

```
       text	   data	    bss	    dec	    hex	filename
       2256	    112	     28	   2396	    95c	_build/nrf52840_xxaa.out
```

We expected more code to come with calling `atoi`, but a 30% increase in our program size is huge! 🤔

Now that I have two map files, I want to know the differences between the two.
