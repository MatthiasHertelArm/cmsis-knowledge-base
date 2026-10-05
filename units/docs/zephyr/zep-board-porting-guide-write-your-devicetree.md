---
id: "zep-board-porting-guide-write-your-devicetree"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Write your devicetree"
summary: "The devicetree file boards/<vendor>/plank/plank<qualifiers>.dts describes your board hardware in the Devicetree Source (DTS) format (as usual, change plank to your board's name). If you're new to devicetree, see devicetree-intro."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

The devicetree file `boards/<vendor>/plank/plank_<qualifiers>.dts` describes your board
hardware in the Devicetree Source (DTS) format (as usual, change `plank` to
your board's name). If you're new to devicetree, see devicetree-intro.

In general, `plank_<qualifiers>.dts` should look like this:

```devicetree

/dts-v1/;
#include <your_soc_vendor/your_soc.dtsi>

/ {
        model = "A human readable name";
        compatible = "yourcompany,plank";

        chosen {
                zephyr,console = &your_uart_console;
                zephyr,sram = &your_memory_node;
                /* other chosen settings  for your hardware */
        };

        /*
         * Your board-specific hardware: buttons, LEDs, sensors, etc.
         */

        leds {
                compatible = "gpio-leds";
                led0: led_0 {
                        gpios = </* GPIO your LED is hooked up to */>;
                        label = "LED 0";
                };
                /* ... other LEDs ... */
        };

        buttons {
                compatible = "gpio-keys";
                /* ... your button definitions ... */
        };

        /* These aliases are provided for compatibility with samples */
        aliases {
                led0 = &led0; /* now you support the blinky sample! */
                /* other aliases go here */
        };
};

&some_peripheral_you_want_to_enable { /* like a GPIO or SPI controller */
        status = "okay";
};

&another_peripheral_you_want {
        status = "okay";
};
```
In the case a board has only a single SoC, without any board variants then the dts file can be
named `<plank>.dts` instead, however this is not recommended due to the file silently be
unused if a variant or other SoC is added to the board.

If you're in a hurry, simple hardware can usually be supported by copy/paste
followed by trial and error. If you want to understand details, you will need
to read the rest of the devicetree documentation and the devicetree
specification.


### Example: FRDM-K64F and Hexiwear K64


.. Give the filenames instead of the full paths below, as it's easier to read.
   The cramped 'foo.dts<path>' style avoids extra spaces before commas.

This section contains concrete examples related to writing your board's
devicetree.

The FRDM-K64F and Hexiwear K64 board devicetrees are defined in
`frdm_k64fs.dts <boards/nxp/frdm_k64f/frdm_k64f.dts>` and
`hexiwear_k64.dts <boards/mikroe/hexiwear/hexiwear_mk64f12.dts>`
respectively. Both boards have NXP SoCs from the same Kinetis SoC family, the
K6X.

Common devicetree definitions for K6X are stored in :zephyr_file:`nxp_k6x.dtsi
<dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi>`, which is included by both board
`.dts` files. `nxp_k6x.dtsi<dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi>`
in turn includes
`armv7-m.dtsi<dts/arm/armv7-m.dtsi>`, which has common definitions
for Arm v7-M cores.

Since `nxp_k6x.dtsi<dts/arm/nxp/kinetis/k6x/nxp_k6x.dtsi>` is meant to be
generic across K6X-based boards, it leaves many devices disabled by default
using `status` properties.  For example, there is a CAN controller defined as
follows (with unimportant parts skipped):

```devicetree

can0: can@40024000 {
     ...
     status = "disabled";
     ...
};
```
It is up to the board `.dts` or application overlay files to enable these
devices as desired, by setting `status = "okay"`. The board `.dts`
files are also responsible for any board-specific configuration of the device,
such as adding nodes for on-board sensors, LEDs, buttons, etc.

For example, FRDM-K64 (but not Hexiwear K64) `.dts` enables the CAN
controller and sets the bus speed:

```devicetree

&can0 {
     status = "okay";
};
```
The `&can0 { ... };` syntax adds/overrides properties on the node with label
`can0`, i.e. the `can@4002400` node defined in the `.dtsi` file.

Other examples of board-specific customization is pointing properties in
`aliases` and `chosen` to the right nodes (see dt-alias-chosen), and
making GPIO/pinmux assignments.
