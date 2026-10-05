---
id: "intr-from-zero-to-main-bootstrapping-li-setup"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bootstrapping libc with Newlib: Setup"
summary: "As we did in our previous posts, we are using Adafruit’s Metro M0 development board to run our examples. We use a cheap CMSIS-DAP adapter and openOCD to program it."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-12-bootstrapping-libc-with-newlib.md"
doc_source: "https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib#setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

As we did in our previous posts, we are using Adafruit’s Metro M0 development
board to run our examples. We use a cheap CMSIS-DAP adapter and openOCD to
program it.

You can find a step by step guide [in our previous
post](https://interrupt.memfault.com/blog/getting-started-with-ibdap-and-atsamd21g18).

As with previous examples, we start with our “minimal” example which you can
find [on GitHub](https://github.com/memfault/zero-to-main/tree/master/minimal).
I’ve reproduced the source code for `main.c` below:

```c
#include <samd21g18a.h>

#include <port.h>
#include <string.h>

#define LED_0_PIN PIN_PA17

static void set_output(const uint8_t pin) {
  struct port_config config_port_pin;
  port_get_config_defaults(&config_port_pin);
  config_port_pin.direction = PORT_PIN_DIR_OUTPUT;
  port_pin_set_config(pin, &config_port_pin);
  port_pin_set_output_level(pin, false);
}

int main() {
  memcpy(NULL, NULL, 0);
  set_output(LED_0_PIN);
  while (true) {
    port_pin_toggle_output_level(LED_0_PIN);
    for (int i = 0; i < 100000; ++i) {}
  }
}
```
