---
id: "tfm-hardware-abstraction-layer-interrupt-apis"
type: "concept"
domain: "security"
title: "Hardware Abstraction Layer: API Definition for TF-M SPM / Interrupt APIs"
summary: "The SPM HAL interrupt APIs are intended for operations on Interrupt Controllers of platforms."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/software/hardware_abstraction_layer.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/hardware_abstraction_layer.html#interrupt-apis"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: API Definition for TF-M SPM_

The SPM HAL interrupt APIs are intended for operations on Interrupt Controllers
of platforms.

APIs for control registers of interrupt sources are not in the scope of this set
of APIs.
Secure Partitions should define the APIs for managing interrupts with those MMIO
registers.


##### APIs



###### tfm_hal_irq_enable()


**Prototype**

```c

enum tfm_hal_status_t tfm_hal_irq_enable(uint32_t irq_num)
```
**Description**

This API enables an interrupt from the Interrupt Controller of the platform.

**Parameter**

- `irq_num` - the interrupt to be enabled with a number

**Return Values**

- `TFM_HAL_ERROR_INVALID_INPUT` - the `irq_num` exceeds The maximum
  supported number of external interrupts.
- `TFM_HAL_ERROR_GENERIC` - failed to enable the interrupt.
- `TFM_HAL_SUCCESS` - the interrupt is successfully enabled.


###### tfm_hal_irq_disable()


**Prototype**

```c

enum tfm_hal_status_t tfm_hal_irq_disable(uint32_t irq_num)
```
**Description**

This API disables an interrupt from the Interrupt Controller of the platform.

**Parameter**

- `irq_num` - the interrupt to be disabled with a number

**Return Values**

- `TFM_HAL_ERROR_INVALID_INPUT` - the `irq_num` exceeds The maximum
  supported number of external interrupts.
- `TFM_HAL_ERROR_GENERIC` - failed to disable the interrupt.
- `TFM_HAL_SUCCESS` - the interrupt is successfully disabled.


###### tfm_hal_irq_clear_pending()


**Prototype**

```c

enum tfm_hal_status_t tfm_hal_irq_clear_pending(uint32_t irq_num)
```
**Description**

This API clears an active and pending interrupt.

**Parameter**

- `irq_num` - the interrupt to be disabled with a number

**Return Values**

- `TFM_HAL_ERROR_INVALID_INPUT` - the `irq_num` exceeds The maximum
  supported number of external interrupts.
- `TFM_HAL_ERROR_GENERIC` - failed to clear the pending interrupt.
- `TFM_HAL_SUCCESS` - the pending interrupt has been cleared.


###### Initializations


**Prototype**

```c

enum tfm_hal_status_t {source_symbol}_init(void *p_pt,
                                           const struct irq_load_info_t *p_ildi)
```
The `{source_symbol}` is:

- `irq_{source}`, if the `source` attribute of the IRQ in Partition manifest
  is a number
- Lowercase of `source` attribute, if `source` is a symbolic name

**Description**

Each interrupt has an initialization function individually.
The `SPM` calls the functions while loading the Partitions.

The following initializations are required for each interrupt:

- Setting the priority. The value must between 0 to 0x80 exclusively.
- Ensuring that the interrupt targets the Secure State.
- Saving the input parameters for future use.

Platforms can have extra initializations as well.

**Parameter**

- `p_pt` - pointer to Partition runtime struct of the owner Partition
- `p_ildi` - pointer to `irq_load_info_t` struct of the interrupt

**Note**

Please refer to the
:doc: `IRQ integration guide<tfm_secure_irq_integration_guide>`
for more information.
