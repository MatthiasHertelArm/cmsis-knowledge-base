---
id: "intr-from-zero-to-main-bare-metal-c-setting-the-stage"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bare metal C: Setting the stage"
summary: "While most of the concepts and code presented in this series should work for all Cortex-M series MCUs, our examples target the SAMD21G18 processor by Atmel. This is a Cortex-M0+ chip found on several affordable development boards."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-14-zero-to-main-1.md"
doc_source: "https://interrupt.memfault.com/blog/zero-to-main-1#setting-the-stage"
license: "CC-BY-SA-4.0"
mode: "V"
---

While most of the concepts and code presented in this series should work for all
Cortex-M series MCUs, our examples target the SAMD21G18 processor by Atmel. This
is a Cortex-M0+ chip found on several affordable development boards.

Specifically, we are using:

- Adafruit's [Metro M0 Express](https://www.adafruit.com/product/3505) as our
  development board,
- a simple [CMSIS-DAP Adapter](https://www.adafruit.com/product/2764)
- OpenOCD (the [Arduino fork](https://github.com/arduino/OpenOCD)) for programming

In each case, we'll implement a simple blinking LED application. It is not
particularly interesting in itself, but for the sake of completeness you can
find the code reproduced below.

```c
#include <samd21g18a.h>

#include <port.h>
#include <stdbool.h>
#include <stdint.h>

#define LED_0_PIN PIN_PA17

static void set_output(const uint8_t pin) {
  struct port_config config_port_pin;
  port_get_config_defaults(&config_port_pin);
  config_port_pin.direction = PORT_PIN_DIR_OUTPUT;
  port_pin_set_config(pin, &config_port_pin);
  port_pin_set_output_level(pin, false);
}

int main() {
  set_output(LED_0_PIN);
  while (true) {
    port_pin_toggle_output_level(LED_0_PIN);
    for (volatile int i = 0; i < 100000; ++i) {}
  }
}
```
