---
id: "zepb-nrf52840dk-changing-uart1-pins"
type: "concept"
domain: "bring-up"
title: "nrf52840dk: Changing UART1 pins"
summary: "The following approach can be used when an application needs to use another set of pins for UART1:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/nordic/nrf52840dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#changing-uart1-pins"
license: "Apache-2.0"
mode: "V"
---

The following approach can be used when an application needs to use another set
of pins for UART1:

1. Add devicetree overlay file to the main directory of your application:

```devicetree

&pinctrl {
   uart1_default_alt: uart1_default_alt {
      group1 {
         psels = <NRF_PSEL(UART_TX, 0, 14)>,
                 <NRF_PSEL(UART_RX, 0, 16)>;
      };
   };
   /* required if CONFIG_PM_DEVICE=y */
   uart1_sleep_alt: uart1_sleep_alt {
      group1 {
         psels = <NRF_PSEL(UART_TX, 0, 14)>,
                 <NRF_PSEL(UART_RX, 0, 16)>;
         low-power-enable;
      };
   };
};

&uart1 {
  pinctrl-0 = <&uart1_default_alt>;
  /* if sleep state is not used, use /delete-property/ pinctrl-1; and
   * skip the "sleep" entry.
   */
  pinctrl-1 = <&uart1_sleep_alt>;
  pinctrl-names = "default", "sleep";
};
```
   In the overlay file above, pin P0.16 is used for RX and P0.14 is used for TX

See set-devicetree-overlays for further details.


### Selecting the pins


Pins can be configured in the board pinctrl file. To see the available mappings,
open the nRF52840 Product Specification, chapter 7 'Hardware and Layout'.
In the table 7.1.1 'aQFN73 ball assignments' select the pins marked
'General purpose I/O'.  Note that pins marked as 'low frequency I/O only' can only be used
in under-10KHz applications. They are not suitable for 115200 speed of UART.
