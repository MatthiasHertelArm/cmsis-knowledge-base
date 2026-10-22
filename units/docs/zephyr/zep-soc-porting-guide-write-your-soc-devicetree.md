---
id: "zep-soc-porting-guide-write-your-soc-devicetree"
type: "concept"
domain: "bring-up"
title: "SoC Porting Guide: Write your SoC devicetree"
summary: "SoC devicetree include files are located in the <zephyr-repo>/dts folder under a corresponding <ARCH>/<VENDOR>."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/soc_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/soc_porting.rst"
license: "Apache-2.0"
mode: "V"
---

SoC devicetree include files are located in the `<zephyr-repo>/dts` folder
under a corresponding `<ARCH>/<VENDOR>`.

The SoC `dts/<ARCH>/<VENDOR>/<soc>.dtsi` describes your SoC hardware in
the Devicetree Source (DTS) format and must be included by any boards which use
the SoC.

If a highlevel `<arch>.dtsi` file exists, then a good starting point is to
include this file in your `<soc>.dtsi`.

In general, `<soc>.dtsi` should look like this:

```devicetree

#include <arch>/<arch>.dtsi

/ {
        chosen {
                /* common chosen settings for your SoC */
        };

        cpus {
                #address-cells = <m>;
                #size-cells = <n>;

                cpu@0 {
                device_type = "cpu";
                compatible = "<compatibles>";
                /* ... your CPU definitions ... */
        };

        soc {
                /* Your SoC definitions and peripherals */
                /* such as ram, clock, buses, peripherals. */
        };
};
```

**Hint:** It is possible to structure multiple `<VENDOR>/<soc>.dtsi` files in sub-directories for a cleaner file system structure. For example organized pre SoC series, like this: `<VENDOR>/<SERIES>/<soc>.dtsi`.


### Multiple CPU clusters


Devicetree reflects the hardware. The memory space and peripherals available to
one CPU cluster can be very different from another CPU cluster, therefore each
CPU cluster will often have its own `.dtsi` file.

CPU cluster `.dtsi` files should follow the naming scheme
`<soc>_<cluster>.dtsi`. A `<soc>_<cluster>.dtsi` file will look
similar to a SoC `.dtsi` without CPU clusters.
