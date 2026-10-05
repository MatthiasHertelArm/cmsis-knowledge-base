---
id: "ethu-zephyr-describe-the-npu-in-devicetree"
type: "concept"
domain: "edge-ai"
title: "Zephyr: Describe the NPU in devicetree"
summary: "The Zephyr arm,ethos-u binding belongs in the device-specific devicetree because the NPU address and interrupt are properties of the SoC integration."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/zephyr/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/zephyr/src/main.md#describe-the-npu-in-devicetree"
license: "Apache-2.0"
mode: "V"
---

The Zephyr [`arm,ethos-u` binding](https://docs.zephyrproject.org/latest/build/dts/api/bindings/arm/arm%2Cethos-u.html)
belongs in the device-specific devicetree because the NPU address and interrupt
are properties of the SoC integration. Use an application overlay only to
adjust a board definition for the application; do not copy addresses or
interrupt encodings from a different device.

The binding uses these properties:

| Property | Requirement | Purpose |
|---|---|---|
| `compatible = "arm,ethos-u"` | Required | Selects the Zephyr Ethos-U driver. |
| `reg` | Required | Defines the NPU register address and size. |
| `interrupts` or `interrupts-extended` | Required | Defines the NPU interrupt using the parent controller's encoding. |
| `status = "okay"` | Required to use the device | Enables the NPU instance. |
| `secure-enable` | Optional boolean | Configures secure operation when present. |
| `privilege-enable` | Optional boolean | Configures privileged operation when present. |
| `fast-memory-region` | Optional phandle | Selects a `zephyr,memory-region` used as spill cache for a Vela Dedicated-SRAM model on Ethos-U65 or Ethos-U85. |

The following is a structural example. Replace every `SOC_*` value with values
from the device integration and use the interrupt-cell format required by the
interrupt controller:

```devicetree
/ {
    ethosu_fast_memory: memory@SOC_ETHOSU_FAST_BASE {
        compatible = "zephyr,memory-region";
        reg = <SOC_ETHOSU_FAST_BASE SOC_ETHOSU_FAST_SIZE>;
    };

    ethosu: npu@SOC_ETHOSU_BASE {
        compatible = "arm,ethos-u";
        reg = <SOC_ETHOSU_BASE SOC_ETHOSU_SIZE>;
        interrupts = <SOC_ETHOSU_IRQ SOC_ETHOSU_IRQ_FLAGS>;
        status = "okay";

        /* Add only when required by the system configuration. */
        secure-enable;
        privilege-enable;

        /* Ethos-U65/U85 Dedicated-SRAM mode only. */
        fast-memory-region = <&ethosu_fast_memory>;
    };
};
```

If the board already declares the NPU, an application overlay typically only
needs to enable or override that node, for example:

```devicetree
&ethosu {
    status = "okay";
};
```

Omit `fast-memory-region` when the Vela model does not use Dedicated-SRAM mode.
When it is present, its address and size must match the fast staging/cache area
used by the linker and Vela configuration.
