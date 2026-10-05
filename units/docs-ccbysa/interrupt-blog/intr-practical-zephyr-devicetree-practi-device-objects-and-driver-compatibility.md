---
id: "intr-practical-zephyr-devicetree-practi-device-objects-and-driver-compatibility"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Dissecting the GPIO pin information type / Device objects and driver compatibility"
summary: "Part of: Dissecting the GPIO pin information type"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#device-objects-and-driver-compatibility"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Dissecting the GPIO pin information type_

We now know how the `.pin` and `.dt_flags` fields of the structure are populated, but what about the `.port`? Let's try to find out what the macro expands to.

```c
#define GPIO_DT_SPEC_GET(node_id, prop)                                  \
  {                                                                      \
    .port = DEVICE_DT_GET(DT_GPIO_CTLR_BY_IDX(node_id, prop, /*idx*/0)), \
    .pin = DT_PHA_BY_IDX(node_id, prop, /*idx*/0, pin),                  \
    .dt_flags = DT_PHA_BY_IDX_OR(node_id, prop, /*idx*/0, flags, 0),     \
  }
```

The macro parameters are given in our application and expand as described in the following snippet:

```c
static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(DT_CHOSEN(app_led), gpios);
// Knowing that `DT_CHOSEN(app_led)` expands to `DT_CHOSEN_app_led`,
// we can look up `DT_CHOSEN_app_led` in `devicetree_generated.h`,
// which is defined as `DT_N_S_leds_S_led_0`.

// Thus:
// - node_id = DT_N_S_leds_S_led_0
// - prop    = gpios
//
// .port = DEVICE_DT_GET(DT_GPIO_CTLR_BY_IDX(DT_N_S_leds_S_led_0, gpios, /*idx*/0)),
```

#### Macrobatics: Resolving device objects with `DEVICE_DT_GET`

Before resolving macros manually, it is always worth looking into the documentation. We have two nested macros, so it makes sense to check the inner `DT_GPIO_CTLR_BY_IDX` first. The API documentation claims that it can be used to "_get the node identifier for the controller phandle from a gpio phandle-array property_". For the assignment `gpios = <&gpio0 13 GPIO_ACTIVE_LOW>;` in our LED node, we'd thus expect to get the node identifier for the phandle `&gpio0`.

Let's have a look at the macro and its expansion:

```c
// We want to know the expansion of the following macro:
#define DT_GPIO_CTLR_BY_IDX(node_id, gpio_pha, idx) \
  DT_PHANDLE_BY_IDX(node_id, gpio_pha, idx)

// Knowing that DT_PHANDLE_BY_IDX is defined as follows:
#define DT_PHANDLE_BY_IDX(node_id, prop, idx) \
  DT_CAT6(node_id, _P_, prop, _IDX_, idx, _PH)

// Given:
// node_id = DT_N_S_leds_S_led_0
// prop    = gpios
// idx     = 0

// DT_GPIO_CTLR_BY_IDX
//    = DT_N_S_leds_S_led_0 ## _P_ ## gpios ## _IDX_ ## 0 ## _PH
//    = DT_N_S_leds_S_led_0_P_gpios_IDX_0_PH
```

Thus, `DT_GPIO_CTLR_BY_IDX` resolves to `DT_N_S_leds_S_led_0_P_gpios_IDX_0_PH`. We can find a macro for that token in `devicetree_generated.h`, which indeed resolves to the GPIO node's identifier `DT_N_S_soc_S_gpio_50000000`:

```bash
$ grep DT_N_S_leds_S_led_0_P_gpios_IDX_0_PH ../build/zephyr/include/generated/devicetree_generated.h
#define DT_N_S_leds_S_led_0_P_gpios_IDX_0_PH DT_N_S_soc_S_gpio_50000000
```

On we go! `DEVICE_DT_GET` takes this node identifier as its parameter `node_id`.

```c
// Original macro from zephyr/include/zephyr/device.h
#define DEVICE_DT_GET(node_id) (&DEVICE_DT_NAME_GET(node_id))
```

What can the documentation tell us about this macro?

> Returns a pointer to a device object created from a Devicetree node, if any device was allocated by a driver. If no such device was allocated, this will fail at linker time [with an error like `undefined reference to __device_dts_ord_<N>`]

Since we don't know yet what "_device objects_" are, this is a bit cryptic. There is, however, one good hint in the linker error message: It seems like this macro is trying to provide a reference to a symbol called `__device_dts_ord_<N>`, where `N` is a number.

Without the need for _macrobatics_ on your side, your editor of choice should be able to resolve this macro. The following is a screenshot from `vscode`, where the last line indeed shows that - for my application - `.port` is assigned a reference to the symbol `__device_dts_ord_11`:



We could be satisfied with this resolution, but we're not, are we? Aren't you curious how we somehow get from a node identifier to this weird symbol with the ordinal _11_? Well, I am so it's time for some more macrobatics!

In the following snippet we replace referenced macros step by step _without_ showing their definition, and thus - to some extent - perform the same expansion as the preprocessor. Since the steps are not _exactly_ the same, however, we're calling them "_replacements_" and not _"expansions"_:

```c
// Original macro from zephyr/include/zephyr/device.h
#define DEVICE_DT_GET(node_id) (&DEVICE_DT_NAME_GET(node_id))

// 1st replacement: Given DEVICE_DT_NAME_GET = DEVICE_NAME_GET(Z_DEVICE_DT_DEV_ID(node_id))
#define DEVICE_DT_GET_1st(node_id) (&DEVICE_NAME_GET(Z_DEVICE_DT_DEV_ID(node_id)))

// 2nd replacement: Given DEVICE_NAME_GET = _CONCAT(__device_, dev_id)
#define DEVICE_DT_GET_2nd(node_id) (&_CONCAT(__device_, ,Z_DEVICE_DT_DEV_ID(node_id)))

// 3rd replacement: Z_DEVICE_DT_DEV_ID = _CONCAT(dts_ord_, DT_DEP_ORD(node_id))
#define DEVICE_DT_GET_3rd(node_id) (&_CONCAT(__device_, _CONCAT(dts_ord_, DT_DEP_ORD(node_id))))

// 4th replacement: DT_DEP_ORD = DT_CAT(node_id, _ORD)
#define DEVICE_DT_GET_4th(node_id) (&_CONCAT(__device_, _CONCAT(dts_ord_, DT_CAT(node_id, _ORD))))
```

> **Note:** In case you're wondering what the difference between `_CONCAT` and `DT_CAT` is, experiment with token pasting. Hint: One of the macros simply pastes tokens, whereas the other one also expands the pasted token.

It's easy enough to see how we end up with the prefix `__device_dts_ord_`, but it is not entirely clear yet how we get to the ordinal _11_. For this, we still need to resolve `DT_CAT(node_id, _ORD)`. Remembering that we already resolved our input parameter `node_id` to `DT_N_S_soc_S_gpio_50000000`, `DT_CAT` simply pastes the two tokens, and we end up with `DT_N_S_soc_S_gpio_50000000_ORD`. But what's that? This is a macro that is again provided by Zephyr's Devicetree generator:

```bash
$ grep DT_N_S_soc_S_gpio_50000000_ORD ../build/zephyr/include/generated/devicetree_generated.h
#define DT_N_S_soc_S_gpio_50000000_ORD 11
```

In simple words, Zephyr's Devicetree generator assigns _ordinals_ to device instances. This is a fundamental concept of Zephyr's _device_ API `zephyr/include/zephyr/device.h`, which is used to represent devices and their instances. Since this is a rather elaborate concept that goes beyond the scope of this article series, I'll leave you with a link to Zephyr's official documentation about the [device driver model](https://docs.zephyrproject.org/latest/kernel/drivers/index.html) and [instance-based APIs](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-inst-apis).

> **Note:** You might ask yourself why we even need _ordinals_ if Devicetree nodes are unique. One simple reason is that nodes can support multiple _drivers_, e.g., an IC might support SPI as well as I2C, and therefore two instances exist for a single node.

For now, it is enough to know that Zephyr creates symbols for each device instance in the Devicetree. In fact, in `devicetree_generated.h` we can find a list of the node ordering and thus ordinals of each instance at the very beginning of the file. Here, we find the ordinal _11_ for the device of the GPIO node `/soc/gpio@50000000`, and also the ordinal _104_ of the device for our second GPIO node `/soc/gpio@50000300`:

`build/zephyr/include/generated/devicetree_generated.h`

```c
/*
 * Generated by gen_defines.py
 *
 * DTS input file:
 *   /path/to/build/zephyr/zephyr.dts.pre
 *
 * Directories with bindings:
 *   /opt/nordic/ncs/v3.2.1/nrf/dts/bindings, /path/to/dts/bindings, $ZEPHYR_BASE/dts/bindings
 *
 * Node dependency ordering (ordinal and path):
 *   0   /
 *   1   /aliases
 *   2   /analog-connector
 * --snip--
 *   11  /soc/gpio@50000000
 * --snip--
 *   104 /soc/gpio@50000300
 * --snip--
 */

// --snip--
#define DT_N_S_soc_S_gpio_50000300_ORD 104
// --snip--
#define DT_N_S_soc_S_gpio_50000000_ORD 11
```

Now we can finalize the macro expansion of `DEVICE_DT_GET`:

```c
// given `DT_N_S_soc_S_gpio_50000000` for `node_id`:
// DT_CAT(node_id, _ORD)) resolves to `DT_N_S_soc_S_gpio_50000000_ORD`

#define DEVICE_DT_GET_4th(node_id) (&_CONCAT(__device_, _CONCAT(dts_ord_, DT_CAT(node_id, _ORD))))
#define DEVICE_DT_GET_x_1st()      (&_CONCAT(__device_, _CONCAT(dts_ord_, DT_N_S_soc_S_gpio_50000000_ORD)))
#define DEVICE_DT_GET_x_2nd()      (&_CONCAT(__device_, dts_ord_11))
#define DEVICE_DT_GET_x_3rd()      (&__device_dts_ord_11)
```

With this, we finally pieced together the complete assignment for our LED's GPIO specification:

```c
static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(LED_NODE, gpios);
// =  {
//    .port = (&__device_dts_ord_11),
//    .pin = 13 /* DT_N_S_leds_S_led_0_P_gpios_IDX_0_VAL_pin */,
//    .dt_flags = 1 /* DT_N_S_leds_S_led_0_P_gpios_IDX_0_VAL_flags */,
//  }
```

That's all good and well, but where is this symbol `__device_dts_ord_11` coming from? With all this macro magic, we can imagine that it is very unlikely that a search for `__device` within Zephyr's codebase provides any valuable hint about the symbol's location. Instead, we can use a much more reliable method: Let's look for the symbol in the `.map` file:

```bash
$ grep -sw __device_dts_ord_11 ../build/zephyr/zephyr.map -A 1 -B 3
 .z_device_PRE_KERNEL_140_
    0x0000000000006550  0x30 zephyr/drivers/gpio/libdrivers__gpio.a(gpio_nrfx.c.obj)
    0x0000000000006550           __device_dts_ord_104
    0x0000000000006568           __device_dts_ord_11
 .z_device_PRE_KERNEL_155_
```

> **Note:** Your `grep` mileage may vary, I've just added `-A 1` and `-B 3` since I know that, in my application, the corresponding object and all the remaining instances are visible if I include one line _after_ (`-A 1`) and three lines _before_ (`-B 3`) the occurrence.

We found it! It seems to be declared in Nordic's GPIO driver `zephyr/drivers/gpio/gpio_nrfx.c`.


#### Macrobatics: Declaring compatilble drivers and device object

I promised that we wouldn't go into detail about [Zephyr's device driver model](https://docs.zephyrproject.org/latest/kernel/drivers/index.html) - and we won't. In this section, we'll only look at how the device instances are defined and how the connection with the nodes in the Devicetree is established.

The two responsible parts within `gpio_nrfx.c` for defining the instances are the following:

```c
#define DT_DRV_COMPAT nordic_nrf_gpio
/* --snip-- the entire driver implementation */

#define GPIO_NRF_DEVICE(id)                 \
  /* --snip-- */                            \
  DEVICE_DT_INST_DEFINE(id, gpio_nrfx_init, \
      /* --snip-- */                        \
      &gpio_nrfx_drv_api_funcs);

DT_INST_FOREACH_STATUS_OKAY(GPIO_NRF_DEVICE)
```

The macro definition `DT_DRV_COMPAT` is placed at the beginning of the file. It is the device driver's equivalent to the `compatible` property of Devicetree nodes and the same-named key in the Devicetree binding: It is defined to the "lowercase-and-underscore" form `nordic_nrf_gpio` of `nordic,nrf-gpio`.

At the end of the file, the device driver creates instances for all GPIO devices with the `status` property set to "okay" using the macro `DT_INST_FOREACH_STATUS_OKAY`. And that's where somehow the "_device objects_" `__device_dts_ord_104` and `__device_dts_ord_11` of the corresponding GPIO nodes are created, pretty likely through `DEVICE_DT_INST_DEFINE`.

Let's dissect these macros one by one, starting with `DT_INST_FOREACH_STATUS_OKAY`, which is more concise but also more complex:

```c
#define DT_INST_FOREACH_STATUS_OKAY(fn)                       \
  COND_CODE_1(DT_HAS_COMPAT_STATUS_OKAY(DT_DRV_COMPAT),       \
    (UTIL_CAT(DT_FOREACH_OKAY_INST_, DT_DRV_COMPAT)(fn)),     \
    ()                                                        \
  )
```

For the expansion of `COND_CODE_1` we rely on the docs, which state that this macro _"insert[s] code depending on whether _flag expands to 1 or not."_. The first parameter is the *_flag*, the second parameter is the code in case *_flag* expands to 1, and finally, the third parameter is the code that is used in case the *_flag* is **not** 1 or undefined.

To get to the flag, we need to check `DT_HAS_COMPAT_STATUS_OKAY(DT_DRV_COMPAT)`:

```c
#define DT_HAS_COMPAT_STATUS_OKAY(compat) \
  IS_ENABLED(DT_CAT(DT_COMPAT_HAS_OKAY_, compat))
```

We've seen the `IS_ENABLED` macro already: It is a more intricate macro that allows evaluating tokens even if they are not even defined. Since we know that in our case `compat` is `nordic_nrf_gpio`, we're looking for a macro `DT_COMPAT_HAS_OKAY_nordic_nrf_gpio`, which, as usual, we can find in `devicetree_generated.h`:

```bash
grep -w DT_COMPAT_HAS_OKAY_nordic_nrf_gpio ../build/zephyr/include/generated/devicetree_generated.h
#define DT_COMPAT_HAS_OKAY_nordic_nrf_gpio 1
```

Zephyr's Devicetree generator creates a lot more information than just macros for the property values of our Devicetree nodes! Here, we see that the generator also provides macros indicating whether it encountered some nodes that claim compatibility with "`nordic,nrf-gpio`". If it doesn't encounter any such node, it won't create the corresponding macros and we'd know that the content of any driver compatible with "`nordic,nrf-gpio`" is unused and can thus be discarded. Pretty neat!

The Devicetree generator does this for each and every driver and node. This allows heavy optimizations in the codebase as we've seen above.

Now we found out that our driver is used, and thus the second parameter of `COND_CODE_1` is expanded. We've already seen that `UTIL_CAT` concatenates and expands the provided macros, which are `DT_FOREACH_OKAY_INST_` and our `DT_DRV_COMPAT` macro, which expands to `nordic_nrf_gpio`. Thus, we're now looking for a macro `DT_FOREACH_OKAY_INST_nordic_nrf_gpio`:

```bash
grep -w DT_FOREACH_OKAY_INST_nordic_nrf_gpio ../build/zephyr/include/generated/devicetree_generated.h
#define DT_FOREACH_OKAY_INST_nordic_nrf_gpio(fn) fn(0) fn(1)
```

Also here Zephyr's Devicetree generator creates another useful macro based on the number of devices in the Devicetree claiming compatibility with the `nordic,nrf-gpio` device driver. For each device it encounters it adds a `fn(n)` to the macro, where `n` is the _instance_ number of the device, one for each of our GPIO nodes. Given this macro, we now know the complete expansion of the `DT_INST_FOREACH_STATUS_OKAY` macro:

```c
// `DT_INST_FOREACH_STATUS_OKAY(GPIO_NRF_DEVICE)`
// given DT_DRV_COMPAT = nordic_nrf_gpio
// expands to:
GPIO_NRF_DEVICE(0) GPIO_NRF_DEVICE(1)
```

The above macros are expanded for the corresponding device _instance_ number, but we still don't know how to associate the instance number with the _ordinals_, which are _11_ and _104_ for our GPIO devices. So far, we can only establish a connection to the nodes `/soc/gpio@50000000` and `/soc/gpio@50000300` via the _ordinals_.

This leads us to the expansion of `DEVICE_DT_INST_DEFINE` used by `GPIO_NRF_DEVICE`:

```c
#define GPIO_NRF_DEVICE(id)                 \
  /* --snip-- */                            \
  DEVICE_DT_INST_DEFINE(id, gpio_nrfx_init, \
      /* --snip-- */                        \
      &gpio_nrfx_drv_api_funcs);

// 1st replacement:
// DEVICE_DT_INST_DEFINE(inst, ...) =
//   DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
#define GPIO_NRF_DEVICE_1st(id)                     \
  /* --snip-- */                                    \
  DEVICE_DT_DEFINE(DT_DRV_INST(id), gpio_nrfx_init, \
      /* --snip-- */                                \
      &gpio_nrfx_drv_api_funcs);
```

The documentation of `DT_DRV_INST` states that it is used to get the "_node identifier for an instance of a `DT_DRV_COMPAT` compatible_". That's exactly what we'd expect, but we want to know _how_ this is done: How do we match a node (identifier) to a device _instance_ number? Looks like we'll have to do a quick macro expansion for `DT_DRV_INST` as well:

```c
// Expansion of DT_DRV_INST, given
// DT_INST(inst, compat) = UTIL_CAT(DT_N_INST, DT_DASH(inst, compat))
// and DT_DASH pastes underscores before and between the arguments.
#define DT_DRV_INST_1st(inst)  DT_INST(inst, DT_DRV_COMPAT)
#define DT_DRV_INST_2nd(inst)  UTIL_CAT(DT_N_INST, DT_DASH(inst, DT_DRV_COMPAT))
#define DT_DRV_INST_3rd(inst)  UTIL_CAT(DT_N_INST, _ ## inst ## DT_DRV_COMPAT)

// Given:
// - DT_DRV_COMPAT = nordic_nrf_gpio
// - inst = 0 (and analog for 1, from the expansion of DT_INST_FOREACH_STATUS_OKAY)
#define DT_DRV_INST_0_1st  UTIL_CAT(DT_N_INST, DT_DASH(0, nordic_nrf_gpio))
#define DT_DRV_INST_0_2nd  UTIL_CAT(DT_N_INST, _0_nordic_nrf_gpio)
#define DT_DRV_INST_0_3rd  DT_N_INST_0_nordic_nrf_gpio
// and  DT_DRV_INST_1_3rd  DT_N_INST_1_nordic_nrf_gpio  ... for inst = 1
```

```bash
$ grep -w DT_N_INST_0_nordic_nrf_gpio ../build/zephyr/include/generated/devicetree_generated.h
#define DT_N_INST_0_nordic_nrf_gpio DT_N_S_soc_S_gpio_50000000
$ grep -w DT_N_INST_1_nordic_nrf_gpio ../build/zephyr/include/generated/devicetree_generated.h
#define DT_N_INST_1_nordic_nrf_gpio DT_N_S_soc_S_gpio_50000300
```

Yet again Zephyr's Devicetree generator provides the necessary macros to map the instance number `inst` to the matching node that claims compatibility with a given device driver:

- `/soc/gpio@50000000` is instance _0_, and
- `/soc/gpio@50000300` is instance _1_ of the driver `nordic,nrf-gpio`.

This is it! We now have the connection from our _instance_ number to _node identifier_ and thus the Devicetree node. We've already seen how we can get from the _node identifier_ to the _"device object's"_ name, and can therefore apply that knowledge to declare the symbol.

Through several expansions, the device macro `DEVICE_DT_DEFINE` effectively does exactly that: It declares a global constant using the name `__device_dts_ord_<N>`, where `N` is the ordinal it obtains using the _node identifier_ of the corresponding instance. The following is an oversimplified definition for the macro `DEVICE_DT_DEFINE`:

```c
// Simplified definition of DEVICE_DT_DEFINE for the device object:
#define DEVICE_DT_DEFINE_simplified(node_id, ...)                     \
  const struct device DEVICE_NAME_GET(Z_DEVICE_DT_DEV_ID(node_id)) =  \
    Z_DEVICE_INIT(/* --snip-- */)

// Remember the expansion of DEVICE_NAME_GET(Z_DEVICE_DT_DEV_ID(node_id)
// in the expansion for DEVICE_DT_GET that we've seen before.

// For node_id = DT_N_S_soc_S_gpio_50000000 ->
// const struct device __device_dts_ord_11 = ...
// For node_id = DT_N_S_soc_S_gpio_50000300 ->
// const struct device __device_dts_ord_104 = ...
```

In practice, Zephyr also creates other symbols that are used to populate the device object. This device object contains, e.g., a function table for the entire GPIO API, such that a call to a `gpio` function leads to the correct call of the vendor's function. E.g., a call to `gpio_pin_toggle_dt` for a GPIO that is compatible with `nordic,nrf-gpio` eventually leads to a call to `gpio_nrfx_port_toggle_bits`.

For details, however, you'll need to refer to Zephyr's official documentation about the [device driver model](https://docs.zephyrproject.org/latest/kernel/drivers/index.html) and [instance-based APIs](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-inst-apis), or watch the tutorial ["Mastering Zephyr Driver Development"](https://www.youtube.com/watch?v=o-f2qCd2AXo) by Gerard Marull Paretas from the Zephyr Development Summit 2022.

There's also a blog post on this Interrupt blog about [building drivers on Zephyr](https://interrupt.memfault.com/blog/building-drivers-on-zephyr).
