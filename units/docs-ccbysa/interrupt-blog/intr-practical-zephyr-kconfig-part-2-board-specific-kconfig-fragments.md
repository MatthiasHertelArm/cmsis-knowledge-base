---
id: "intr-practical-zephyr-kconfig-part-2-board-specific-kconfig-fragments"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Using different configuration files / Board-specific Kconfig fragments"
summary: "Part of: Using different configuration files"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#board-specific-kconfig-fragments"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Using different configuration files_

Aside from the application configuration file [prj.conf](https://github.com/lmapii/practical-zephyr/blob/main/01_kconfig/prj.conf), Zephyr also automatically picks up board-specific Kconfig _fragments_. Board fragments are placed in the `boards` directory in the project root (next to the `CMakeLists.txt` file) and use the `<board>.conf` name format.

E.g., throughout this guide, we're using the nRF52840 development kit, which has the board name `nrf52840dk_nrf52840`. Thus, the file `boards/nrf52840dk_nrf52840.conf` is automatically merged into the `Kconfig` configuration during the build, if present.

Let's try this by disabling UART as console output using a new fragment `boards/nrf52840dk_nrf52840.conf`. For the nRF52840 development kit, this symbol is enabled by default. You can go ahead and verify this by checking the default configuration `zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840_defconfig` - or take my word for it:

```bash
tree --charset=utf-8 --dirsfirst
.
├── boards
│   └── nrf52840dk_nrf52840.conf
├── src
│   └── main.c
├── CMakeLists.txt
├── prj.conf
└── prj_release.conf

$ cat boards/nrf52840dk_nrf52840.conf
```

```conf
CONFIG_UART_CONSOLE=n
```

Then, we perform a _pristine_ build of the project. Notice that a `--pristine` build is required at this point because otherwise, the build system does not pick up our newly added `.conf` file. This is one of the very few occasions where a pristine build is actually required.

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 -d ../build --pristine
```

In the output of `west build` shown below you can see that the new file `boards/nrf52840dk_nrf52840.conf` is indeed merged into the `Kconfig` configuration. You can also see a warning that the Zephyr library `drivers__console` is excluded from the build since it now has no `SOURCES`:

```
Parsing /opt/nordic/ncs/v3.2.1/zephyr/Kconfig
Loaded configuration '/opt/nordic/ncs/v3.2.1/zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840_defconfig'
Merged configuration '/path/to/01_kconfig/prj.conf'
Merged configuration '/path/to/01_kconfig/boards/nrf52840dk_nrf52840.conf'
Configuration saved to '/path/to/build/zephyr/.config'
...
CMake Warning at /opt/nordic/ncs/v3.2.1/zephyr/CMakeLists.txt:838 (message):
  No SOURCES given to Zephyr library: drivers__console
  Excluding target from build.
```

You can of course verify that the symbol is indeed disabled by checking the `zephyr/.config` file in the `build` directory.

> **Notice:** Previous versions of Zephyr used a `prj_<board>.conf` fragment in the project root directory instead of board fragments in the `boards` directory. At the time of writing, the build system still merges any such file into the configuration. However, this `prj_<board>.conf` fragment is deprecated, and `boards/<board>.conf` should be used instead.

How are board fragments used by our previously created `release` build type? Let's try it out and have a look at the build output:

```bash
$ rm -rf ../build
$ west build --no-sysbuild --board nrf52840dk/nrf52840 -d ../build -- -DCONF_FILE=prj_release.conf
```

```
Parsing /opt/nordic/ncs/v3.2.1/zephyr/Kconfig
Loaded configuration '/opt/nordic/ncs/v3.2.1/zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840_defconfig'
Merged configuration '/path/to/01_kconfig/prj_release.conf'
Configuration saved to '/path/to/build/zephyr/.config'
```

Well, this is awkward: Even though we provided a board-specific `Kconfig` fragment, it is ignored as soon as we switch to our alternative `prj_release.conf` configuration. This is, however, [working as intended](https://docs.zephyrproject.org/latest/build/kconfig/setting.html#the-initial-configuration): When using alternative `Kconfig` files in the format `prj_<build>.conf`, Zephyr looks for a board fragment matching the file name `boards/<board>_<build>.conf`.

In my case, I need to create the file `boards/nrf52840dk_nrf52840_release.conf`. Let's get rid of the warning for the Zephyr library `drivers__console` by disabling the `CONSOLE` entirely in our board's release configuration:

```bash
tree --charset=utf-8 --dirsfirst
.
├── boards
│   ├── nrf52840dk_nrf52840.conf
│   └── nrf52840dk_nrf52840_release.conf
├── src
│   └── main.c
├── CMakeLists.txt
├── prj.conf
└── prj_release.conf

$ cat boards/nrf52840dk_nrf52840_release.conf
```

```conf
CONFIG_CONSOLE=n
CONFIG_UART_CONSOLE=n
```

Now, when we rebuild the project, we see that our board fragment is merged into the `Kconfig` configuration, and no warning is issued by `west build`:

```bash
$ rm -rf ../build
$ west build --no-sysbuild --board nrf52840dk/nrf52840 -d ../build -- -DCONF_FILE=prj_release.conf
```

```
Parsing /opt/nordic/ncs/v3.2.1/zephyr/Kconfig
Loaded configuration '/opt/nordic/ncs/v3.2.1/zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840_defconfig'
Merged configuration '/path/to/01_kconfig/prj_release.conf'
Merged configuration '/path/to/01_kconfig/boards/nrf52840dk_nrf52840_release.conf'
Configuration saved to '/path/to/build/zephyr/.config'
```
