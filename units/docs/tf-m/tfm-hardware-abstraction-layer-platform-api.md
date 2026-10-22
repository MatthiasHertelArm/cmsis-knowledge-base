---
id: "tfm-hardware-abstraction-layer-platform-api"
type: "concept"
domain: "security"
title: "Hardware Abstraction Layer: API Definition for TF-M SPM / Platform API"
summary: "The platform API is a higher-level abstraction layer of the platform, other than a dedicated API set for the special hardware devices."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/software/hardware_abstraction_layer.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/hardware_abstraction_layer.html#platform-api"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: API Definition for TF-M SPM_

The platform API is a higher-level abstraction layer of the platform, other than
a dedicated API set for the special hardware devices.


##### APIs


###### tfm_hal_platform_init()

**Prototype**

```c

enum tfm_hal_status_t tfm_hal_platform_init(void)
```
**Description**

This API performs the platform initializations **before** the `SPM`
initialization.

The initializations could include but not limited to:
- Fault handlers
- Reset configurations
- Debug init
- NVIC init

**Parameter**

- `void` - None.

**Return Values**

- `TFM_HAL_SUCCESS` - Init success.
- `TFM_HAL_ERROR_GENERIC` - Generic errors.


###### tfm_hal_system_reset()

**Prototype**

```c

void tfm_hal_system_reset(uint32_t sw_reset_syn_value)
```
**Description**

This API performs a system reset (cold reset).

The platform can uninitialize some resources before reset. The function gets passed
a parameter, usually a register value, that gets used to set the system reset syndrome
register before issueing the reset. This register survives resets and can be read
to understand the root cause of the reset. A platform that does not provide this
functionality still needs to pass `TFM_PLAT_SWSYN_DEFAULT` as a safe default value.
A platform can also to redefine the value of `TFM_PLAT_SWSYN_DEFAULT` in case the
default of `0x0UL` does not meet its requirements.

When `CONFIG_TFM_HALT_ON_CORE_PANIC` is disabled this function is called to reset
the system when a fatal error occurs.

**Parameter**

- `uint32_t sw_reset_syn_value` - The value of the register to be used to set
                                    the platform reset syndrome

**Return Values**

- `void` - None

**Note**

This API should not return.


###### tfm_hal_get_reset_syndrome()


**Prototype**

```c

void tfm_hal_get_reset_syndrome(void)
```
**Description**

This API performs reads the value of the reset syndrome register that has been
mirrored after the last reset.

**Parameter**

- `void` - None

**Return Values**

- `uint32_t` - The value of the reset syndrome register, usually a full 32 bits register

**Note**

None


###### tfm_hal_clear_reset_syndrome_bit()


**Prototype**

```c

void tfm_hal_clear_reset_syndrome_bit(uint8_t bit_pos)
```
**Description**

This API performs clears a specific bit of the reset syndrome register passed as input.

**Parameter**

- `uint8_t bit_pos` - Bit position to clear on the reset syndrome register

**Return Values**

- `void` - None

**Note**

None


###### tfm_hal_system_halt()

**Prototype**

```c

void tfm_hal_system_halt(void)
```
**Description**

This API enters the CPU into an infinite loop.

The platform can uninitialize some resources before looping forever.

When `CONFIG_TFM_HALT_ON_CORE_PANIC` is enabled this function is called to halt the
system when a fatal error occurs.

**Parameter**

- `void` - None

**Return Values**

- `void` - None

**Note**

This API should not return.
