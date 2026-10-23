---
id: "zep-device-driver-model-memory-mapping"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Memory Mapping"
summary: "On some systems, the linear address of peripheral memory-mapped I/O (MMIO) regions cannot be known at build time:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

On some systems, the linear address of peripheral memory-mapped I/O (MMIO)
regions cannot be known at build time:

- The I/O ranges must be probed at runtime from the bus, such as with
  PCI express
- A memory management unit (MMU) is active, and the physical address of
  the MMIO range must be mapped into the page tables at some virtual
  memory location determined by the kernel.

These systems must maintain storage for the MMIO range within RAM and
establish the mapping within the driver's init function. Other systems
do not care about this and can use MMIO physical addresses directly from
DTS and do not need any RAM-based storage for it.

For drivers that may need to deal with this situation, a set of
APIs under the DEVICE_MMIO scope are defined, along with a mapping function
`device_map`.


### Device Model Drivers with one MMIO region


The simplest case is for drivers which need to maintain one MMIO region.
These drivers will need to use the `DEVICE_MMIO_ROM` and
`DEVICE_MMIO_RAM` macros in the definitions for their `config_info`
and `driver_data` structures, with initialization of the `config_info`
from DTS using `DEVICE_MMIO_ROM_INIT`. A call to `DEVICE_MMIO_MAP()`
is made within the init function:

```C

struct my_driver_config {
   DEVICE_MMIO_ROM; /* Must be first */
   ...
}

struct my_driver_dev_data {
   DEVICE_MMIO_RAM; /* Must be first */
   ...
}

const static struct my_driver_config my_driver_config_0 = {
   DEVICE_MMIO_ROM_INIT(DT_DRV_INST(...)),
   ...
}

int my_driver_init(const struct device *dev)
{
   ...
   DEVICE_MMIO_MAP(dev, K_MEM_CACHE_NONE);
   ...
}

int my_driver_some_function(const struct device *dev)
{
   ...
   /* Write some data to the MMIO region */
   sys_write32(0xDEADBEEF, DEVICE_MMIO_GET(dev));
   ...
}
```
The particular expansion of these macros depends on configuration. On
a device with no MMU or PCI-e, `DEVICE_MMIO_MAP` and
`DEVICE_MMIO_RAM` expand to nothing.


### Device Model Drivers with multiple MMIO regions


Some drivers may have multiple MMIO regions. In addition, some drivers
may already be implementing a form of inheritance which requires some other
data to be placed first in the  `config_info` and `driver_data`
structures.

This can be managed with the `DEVICE_MMIO_NAMED` variant macros. These
require that `DEV_CFG()` and `DEV_DATA()` macros be defined to obtain
a properly typed pointer to the driver's config_info or dev_data structs.
For example:

```C

struct my_driver_config {
   ...
     DEVICE_MMIO_NAMED_ROM(corge);
    DEVICE_MMIO_NAMED_ROM(grault);
   ...
}

struct my_driver_dev_data {
      ...
    DEVICE_MMIO_NAMED_RAM(corge);
    DEVICE_MMIO_NAMED_RAM(grault);
    ...
}

#define DEV_CFG(_dev) \
   ((const struct my_driver_config *)((_dev)->config))

#define DEV_DATA(_dev) \
   ((struct my_driver_dev_data *)((_dev)->data))

const static struct my_driver_config my_driver_config_0 = {
   ...
   DEVICE_MMIO_NAMED_ROM_INIT(corge, DT_DRV_INST(...)),
   DEVICE_MMIO_NAMED_ROM_INIT(grault, DT_DRV_INST(...)),
   ...
}

int my_driver_init(const struct device *dev)
{
   ...
   DEVICE_MMIO_NAMED_MAP(dev, corge, K_MEM_CACHE_NONE);
   DEVICE_MMIO_NAMED_MAP(dev, grault, K_MEM_CACHE_NONE);
   ...
}

int my_driver_some_function(const struct device *dev)
{
   ...
   /* Write some data to the MMIO regions */
   sys_write32(0xDEADBEEF, DEVICE_MMIO_GET(dev, grault));
   sys_write32(0xF0CCAC1A, DEVICE_MMIO_GET(dev, corge));
   ...
}
```

### Device Model Drivers with multiple MMIO regions in the same DT node


Some drivers may have multiple MMIO regions defined into the same DT device
node using the `reg-names` property to differentiate them, for example:

```devicetree

/dts-v1/;

/ {
        a-driver@40000000 {
                reg = <0x40000000 0x1000>,
                      <0x40001000 0x1000>;
                reg-names = "corge", "grault";
        };
};
```
This can be managed as seen in the previous section but this time using the
`DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME` macro instead. So the only difference
would be in the driver config struct:

```C

const static struct my_driver_config my_driver_config_0 = {
   ...
   DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME(corge, DT_DRV_INST(...)),
   DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME(grault, DT_DRV_INST(...)),
   ...
}
```

### Drivers that do not use Zephyr Device Model


Some drivers or driver-like code may not use Zephyr's device model,
and alternative storage must be arranged for the MMIO data. An
example of this are timer drivers, or interrupt controller code.

This can be managed with the `DEVICE_MMIO_TOPLEVEL` set of macros,
for example:

```C

DEVICE_MMIO_TOPLEVEL_STATIC(my_regs, DT_DRV_INST(..));

void some_init_code(...)
{
   ...
   DEVICE_MMIO_TOPLEVEL_MAP(my_regs, K_MEM_CACHE_NONE);
   ...
}

void some_function(...)
   ...
   sys_write32(DEVICE_MMIO_TOPLEVEL_GET(my_regs), 0xDEADBEEF);
   ...
}
```

### Drivers that do not use DTS


Some drivers may not obtain the MMIO physical address from DTS, such as
is the case with PCI-E. In this case the `device_map` function
may be used directly:

```C

void some_init_code(...)
{
   ...
   struct pcie_bar mbar;
   bool bar_found = pcie_get_mbar(bdf, index, &mbar);

   device_map(DEVICE_MMIO_RAM_PTR(dev), mbar.phys_addr, mbar.size, K_MEM_CACHE_NONE);
   ...
}
```
For these cases, DEVICE_MMIO_ROM directives may be omitted.
