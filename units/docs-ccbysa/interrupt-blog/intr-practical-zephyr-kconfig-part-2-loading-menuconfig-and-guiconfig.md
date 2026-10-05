---
id: "intr-practical-zephyr-kconfig-part-2-loading-menuconfig-and-guiconfig"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Navigating Kconfig / Loading `menuconfig` and `guiconfig`"
summary: "For the build command, West has some builtin targets, two of which are used for Kconfig:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#loading-menuconfig-and-guiconfig"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Navigating Kconfig_

For the `build` command, _West_ has some builtin _targets_, two of which are used for _Kconfig_:

```bash
$ west build --no-sysbuild --build-dir ../build -t usage
-- west build: running target usage
...
Kconfig targets:
  menuconfig - Update .config using a console-based interface
  guiconfig  - Update .config using a graphical interface
...
```

The targets `menuconfig` and `guiconfig` can be used to start graphical _Kconfig_ tools which allow modifying the `.config` file in your build directory. Both tools are essentially identical. The only difference is that `menuconfig` is a text-based graphical interface that opens directly in your terminal, whereas `guiconfig` is a "clickable" user interface running in its own window. The screenshots below show the tools launched by the following commands:

```bash
$ west build --build-dir ../build -t menuconfig
$ west build --build-dir ../build -t guiconfig
```

> **Notice:** If you did not build your project or the build system cannot build the required targets due to CMake/Kconfig processing issues, the tool will not load since the `zephyr/.config` file is missing.




For the sake of simplicity, we'll use `menuconfig` in the remainder of this article. In both tools, you can search for configuration symbols. In `menuconfig` - similar to `vim` - you can use the forward slash `/` to start searching, e.g., for our `PRINTK` symbol. Several results match, but only one of them is the plain symbol `PRINTK` which also shows the same description that we've seen in the `Kconfig` file:

```
PRINTK(=y) "Send printk() to console"
```

Navigate to the symbol using the search or the path _Subsystems and OS Services > Debugging Options_. You should see the following screen:



Typically, you can toggle `bool` symbols using `Space` or `Enter`, but this does not seem to be possible for `PRINTK`. You can see that a symbol cannot be changed - which is indicated by the marker `*` being enclosed by dashes `-*-` instead of square brackets `[*]`. Using `?`, we can display the symbol's information:

```
Name: PRINTK
Prompt: Send printk() to console
Type: bool
Value: y

Help:

  This option directs printk() debugging output to the supported
  console device, rather than suppressing the generation
  of printk() output entirely. Output is sent immediately, without
  any mutual exclusion or buffering.

Default:
  - y

Symbols currently y-selecting this symbol:
  - BOOT_BANNER
...
```

We found the reason why we can't disable the symbol at the very bottom of the `PRINTK`'s symbol information! The symbol `BOOT_BANNER` is `y-selecting` the `PRINTK` symbol, so we can't disable it, and the application's configuration has no effect. This simple example should also make you realize that it is hard, if not impossible, to figure out dependencies by navigating `Kconfig` fragments file by file.

> **Notice:** If you can't find a Kconfig symbol in `menuconfig`, you can toggle the _Show all_ mode using `Shift+A`. This shows hidden Kconfig symbols - your symbol might be one of those!

Let's fix our configuration:

* Navigate to the `BOOT_BANNER` symbol and disable it.
* Going back to `PRINTK` it should now be possible to disable it.
