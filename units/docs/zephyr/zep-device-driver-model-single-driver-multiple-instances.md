---
id: "zep-device-driver-model-single-driver-multiple-instances"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Single Driver, Multiple Instances"
summary: "Some drivers may be instantiated multiple times in a given system. For example there can be multiple GPIO banks, or multiple UARTS. Each instance of the driver will have a different config struct and data struct."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

Some drivers may be instantiated multiple times in a given system. For example
there can be multiple GPIO banks, or multiple UARTS. Each instance of the driver
will have a different `config` struct and `data` struct.

Configuring interrupts for multiple drivers instances is a special case. If each
instance needs to configure a different interrupt line, this can be accomplished
through the use of per-instance configuration functions, since the parameters
to `IRQ_CONNECT()` need to be resolvable at build time.

For example, let's say we need to configure two instances of `my_driver`, each
with a different interrupt line. In `drivers/subsystem/subsystem_my_driver.h`:

```C

typedef void (*my_driver_config_irq_t)(const struct device *dev);

struct my_driver_config {
      DEVICE_MMIO_ROM;
      my_driver_config_irq_t config_func;
};
```
In the implementation of the common init function:

```C

void my_driver_isr(const struct device *dev)
{
      /* Handle interrupt */
      ...
}

int my_driver_init(const struct device *dev)
{
      const struct my_driver_config *config = dev->config;

      DEVICE_MMIO_MAP(dev, K_MEM_CACHE_NONE);

      /* Do other initialization stuff */
      ...

      config->config_func(dev);

      return 0;
}
```
Then when the particular instance is declared:

```C

#if CONFIG_MY_DRIVER_0

DEVICE_DECLARE(my_driver_0);

static void my_driver_config_irq_0(const struct device *dev)
{
      IRQ_CONNECT(MY_DRIVER_0_IRQ, MY_DRIVER_0_PRI, my_driver_isr,
                  DEVICE_GET(my_driver_0), MY_DRIVER_0_FLAGS);
}

const static struct my_driver_config my_driver_config_0 = {
      DEVICE_MMIO_ROM_INIT(DT_DRV_INST(0)),
      .config_func = my_driver_config_irq_0
}

static struct my_data_0;

DEVICE_DEFINE(my_driver_0, MY_DRIVER_0_NAME, my_driver_init,
              NULL, &my_data_0, &my_driver_config_0,
              POST_KERNEL, MY_DRIVER_0_PRIORITY, &my_api_funcs);

#endif /* CONFIG_MY_DRIVER_0 */
```
Note the use of `DEVICE_DECLARE()` to avoid a circular dependency on providing
the IRQ handler argument and the definition of the device itself.
