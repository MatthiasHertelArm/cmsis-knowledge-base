---
id: "intr-practical-zephyr-kconfig-part-2-persisting-menuconfig-and-guiconfig-chan"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Navigating Kconfig / Persisting `menuconfig` and `guiconfig` changes"
summary: "menuconfig and guiconfig can be used to test and explore configuration options. Typically, you'd use the Save operation to store the new configuration to the zephyr/.config file in your build directory."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#persisting-menuconfig-and-guiconfig-changes"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Navigating Kconfig_

`menuconfig` and `guiconfig` can be used to test and explore configuration options. Typically, you'd use the _Save_ operation to store the new configuration to the `zephyr/.config` file in your build directory. You can then also launch `menuconfig` multiple times and change the configuration to your needs, and the changes will always be reflected in the next build.

The downside of saving the configuration to `zephyr/.config` in the build directory is that **all changes will be lost** once you perform a clean build, e.g., using `west build --pristine`. To persist your changes, you need to place them into your [configuration files](https://docs.zephyrproject.org/latest/build/kconfig/setting.html#setting-kconfig-configuration-values).

**Using `diff`**

The people at [Golioth](https://golioth.io/) published a [short article](https://blog.golioth.io/zephyr-quick-tip-show-what-menuconfig-changed-and-make-changes-persistent/) that shows how to leverage the `diff` command to find out which configuration options have changed when using the normal _Save_ operation: Before writing the changes to the `zephyr/.config` file, Kconfig stores the old configuration in `build/zephyr/.config.old`. Thus, all changes that you make between a _Save_ operation are reflected by the differences between `zephyr/.config` and `build/zephyr/.config.old`:

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 -d ../build --pristine
$ west build -d ../build -t menuconfig
# Within menuconfig:
# - Disable BOOT_BANNER and PRINTK.
# - Save the changes to ../build/zephyr/.config using [S].

$ diff ../build/zephyr/.config ../build/zephyr/.config.old
1097c1097
< # CONFIG_BOOT_BANNER is not set
---
> CONFIG_BOOT_BANNER=y
1462c1462
< # CONFIG_PRINTK is not set
---
> CONFIG_PRINTK=y
```

> **Notice:** The `# CONFIG_<symbol> is not set` comment syntax is used by `zephyr/.config` instead of `CONFIG_<symbol>=n` for historical reasons, as also mentioned in the [official documentation](https://docs.zephyrproject.org/latest/build/kconfig/setting.html#setting-kconfig-configuration-values). This allows parsing configuration files directly as `makefiles`.

You can now simply take the changes from the `diff` and persist them, e.g., by writing them into your application configuration file. Keep in mind that this only works for changes performed between **one** _Save_ operation. If you _Save_ multiple times, `.config.old` is always replaced by the current `.config`. The `diff` operation must therefore be performed after each _Save_.

This approach, however, is not always feasible. E.g., try to enable the logging subsystem _Subsystems and OS Services > Logging_: You'll notice that the `diff` is huge even though you've only changed one option. This is due to the large number of dependencies of the `CONFIG_LOG=y` setting.

**Save minimal configuration**

Both `menuconfig` and `guiconfig` have the _Save minimal config_ option. As the name implies, this option exports a minimal `Kconfig` file containing _all_ symbols that differ from their default values. This does, however, also include symbols that differ from their default values due to _other_ `Kconfig` fragments than your application's configuration. E.g., the symbols in the `Kconfig` files of the chosen board are saved in this minimal configuration file.

Let's try this out with our settings for the `BOOT_BANNER` and `PRINTK` symbols.

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 -d ../build --pristine
$ west build -d ../build -t menuconfig
# Within menuconfig:
# - Disable BOOT_BANNER and PRINTK.
# - Use [D] "Save minimal config" and write the changes to tmp.conf.
$ cat tmp.conf
```

```conf
CONFIG_GPIO=y
CONFIG_PINCTRL=y
CONFIG_SERIAL=y
CONFIG_NRFX_GPIOTE_NUM_OF_EVT_HANDLERS=1
CONFIG_USE_SEGGER_RTT=y
CONFIG_SOC_SERIES_NRF52X=y
CONFIG_SOC_NRF52840_QIAA=y
CONFIG_ARM_MPU=y
CONFIG_HW_STACK_PROTECTION=y
# CONFIG_BOOT_BANNER is not set
CONFIG_CONSOLE=y
CONFIG_UART_CONSOLE=y
# CONFIG_PRINTK is not set
CONFIG_EARLY_CONSOLE=y
```

As you can see, this minimal configuration contains a lot more options than we changed within `menuconfig`. Some of these options come from the selected board, in my case `zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840_defconfig`, but are still listed since they do not use default values. However, the two changes to `PRINTK` and `BOOT_BANNER` are still visible. We can just take those options and write them to our application configuration file:

```bash
$ cat prj.conf
CONFIG_PRINTK=n
CONFIG_BOOT_BANNER=n
```

Now, after rebuilding, the output on our serial interface indeed remains empty. Also, if you look at the output of your build should notice that the _flash_ usage decreased by around 2 KB.
