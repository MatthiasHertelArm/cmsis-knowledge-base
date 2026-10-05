---
id: "intr-practical-zephyr-devicetree-practi-rerouting-uart"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Rerouting UART"
summary: "With what we've learned about grouped pin control with the nRF52840, let's reroute our &uart0 instance to pins that are available on the development kit's pin rows instead of using the pins that lead to the USB interface."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#rerouting-uart"
license: "CC-BY-SA-4.0"
mode: "V"
---

With what we've learned about [grouped pin control with the nRF52840](#basics-and-grouped-pin-control-with-the-nrf52840), let's reroute our `&uart0` instance to pins that are available on the development kit's pin rows instead of using the pins that lead to the USB interface.

E.g., let's use the pins _P1.6_ and _P1.8_ instead. There are two ways to do this: Either we define our own nodes and assign them to the `pinctrl-<n>` properties of the `&uart0` node, or we overwrite the `psels` of the existing `&uart0_default` and `&uart0_default` nodes. For MCUs using the grouping approach, there's really no difference at all, and since it is easier, we'll just overwrite the existing nodes in our overlay as follows:

`04_practice/boards/nrf52840dk_nrf52840.overlay`

```dts
&uart0_default {
  group1 {
    psels = <NRF_PSEL(UART_TX, 1, 6)>, <NRF_PSEL_DISCONNECTED(UART_RTS)>;
  };
  group2 {
    psels = <NRF_PSEL(UART_RX, 1, 8)>, <NRF_PSEL_DISCONNECTED(UART_CTS)>;
    bias-pull-up;
  };
};
&uart0_sleep {
  group1 {
    psels =
      <NRF_PSEL(UART_TX, 1, 6)>,  <NRF_PSEL(UART_RX, 1, 8)>,
      <NRF_PSEL_DISCONNECTED(UART_RTS)>, <NRF_PSEL_DISCONNECTED(UART_CTS)>;
    low-power-enable;
  };
};
```

Notice that I've also disabled the RTS and CTS since we're not really using it. Since I don't have a working [FDTI](https://ftdichip.com/) cable, I'll be using my completely overqualified but trusted [Saleae](https://www.saleae.com) and connect it to the pins _P1.6_ and _P1.8_.



And it works!



Also, the output for the J-Link device remains empty, meaning that we really rerouted our UART node. A bit more intricate than reassigning GPIOs, but just as flexible.


### Switching to the STM32 Nucleo-64 development board

Since I have a spare [STM32 Nucleo-64 development board](https://www.st.com/en/evaluation-tools/nucleo-c031c6.html) at hand, it'd be nice to repeat the same steps and reroute the UART output for an MCU that uses the _pin approach_. Before we try to reroute anything, let's try to build the project for the matching board `nucleo_c031c6`:

```bash
$ rm -rf ../build
$ west build --no-sysbuild --board nucleo_c031c6 --build-dir ../build
```

```
In file included from <command-line>:
/opt/nordic/ncs/v3.2.1/zephyr/boards/st/nucleo_c031c6/nucleo_c031c6.dts:9:10: fatal error: st/c0/stm32c031c(4-6)tx-pinctrl.dtsi: No such file or directory
    9 | #include <st/c0/stm32c031c(4-6)tx-pinctrl.dtsi>
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
```

Well, that's embarrassing. Something's wrong with our setup, we don't seem to have all the files we need! At least this is what happens if you've followed my advice to use Nordic's toolchain installer in the very first article of this series. What's the reason for this error?

The reason is quite simple: Obviously, Nordic's toolchain installer assumes that you're only using their MCUs and the _nRF Connect SDK_, and not "vanilla Zephyr". It therefore doesn't include HALs and files from other vendors that are not required.

When using multiple MCUs it is therefore much better to stop using installed sources and use a _west workspace_ application instead. But that's a topic for the next and final article of this series. See? Embedded articles can have cliffhangers too!
