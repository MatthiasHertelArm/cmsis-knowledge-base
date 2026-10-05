---
id: "intr-practical-zephyr-kconfig-part-2-kconfig"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Kconfig"
summary: "We've seen that Zephyr uses CMake as one of its build and configuration systems. On top of CMake - just like the Linux kernel - Zephyr uses the kernel configuration system \"Kconfig\"."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#kconfig"
license: "CC-BY-SA-4.0"
mode: "V"
---

We've seen that Zephyr uses [CMake](https://docs.zephyrproject.org/latest/build/cmake/index.html) as one of its [build and configuration systems](https://docs.zephyrproject.org/latest/build/index.html). On top of CMake - just like the Linux kernel - Zephyr uses the [kernel configuration system "Kconfig"](https://docs.zephyrproject.org/latest/build/kconfig/index.html#configuration-system-kconfig). We've already encountered Kconfig in the previous section, where we had to provide an empty _application configuration file_ [prj.conf](https://github.com/lmapii/practical-zephyr/blob/main/00_basics/prj.conf).

In this article, we'll explore the _practical_ aspects of Kconfig. As always, much more detailed information about Kconfig in Zephyr can be found in the [official documentation](https://docs.zephyrproject.org/latest/build/kconfig/index.html#configuration-system-kconfig). So, what is Kconfig?

In simple words, Kconfig is a configuration system that uses a hierarchy of configuration _files_ (with their own syntax), which in turn define a hierarchy of configuration _options_, also called _symbols_. The _build system uses these symbols_ to include or exclude files from the build process and as configuration options in the _source code_ itself. All in all, this allows you to modify your application without modifying the source code.

### Configuring symbols

For the time being, let's ignore _how_ the entire _Kconfig_ hierarchy is built or merged, and let's just have a look at how the configuration system works in general.

The debugging subsystem of Zephyr defines the _Kconfig_ symbol `PRINTK` that allows you to enable or disable the `printk` output. This `PRINTK` _symbol_ is defined in the `Kconfig` file `zephyr/subsys/debug/Kconfig`. We won't go into detail about the syntax here. It is quite self-explanatory for this example.

> For details about _Kconfig_'s syntax, you can have a look at the _Kconfig_ language specification in the [Linux kernel documentation](https://www.kernel.org/doc/html/latest/kbuild/kconfig-language.html) or Zephyr's [Kconfig tips and best practices](https://docs.zephyrproject.org/latest/build/kconfig/tips.html#kconfig-tips-and-best-practices).

`zephyr/subsys/debug/Kconfig`

```conf
config PRINTK
	bool "Send printk() to console"
	default y
```

As you can see from the above `Kconfig` file, unless configured otherwise, `PRINTK` is *enabled* by default. We can configure symbols to our needs in the _application configuration file_ [prj.conf](https://github.com/lmapii/practical-zephyr/blob/main/01_kconfig/prj.conf) that we've encountered in the previous article. Symbols are assigned their values using the following syntax:

```conf
CONFIG_<symbol name>=<value>
```

> **Note:**  At the time of writing, no spaces are allowed before or after the `=` operator.

Our `PRINTK` is a symbol of type `bool` and can be assigned the values `y` and `n` (have a look at the [official documentation](https://docs.zephyrproject.org/latest/build/kconfig/setting.html#setting-kconfig-configuration-values) for details). To disable `PRINTK`, we can therefore add the following to our application configuration file [prj.conf](https://github.com/lmapii/practical-zephyr/blob/main/01_kconfig/prj.conf):

```conf
CONFIG_PRINTK=n
```

What's the effect of changing a symbol? As mentioned before, this _can_ affect the build options and _can_ also be used by some subsystem's implementation. Whatever a symbol does, however, is specific for each symbol, meaning there is no convention for symbol names that always have the same effect. Thus, in the end, it is up to you to dig into the sources and documentation to see which options are available and what effect they have (there's a [Kconfig search](#kconfig-search) that we'll see later).

Let's have a short look at our `PRINTK` symbol. A quick search for `CONFIG_PRINTK` in our local Zephyr code reveals how the symbol is used in the implementation of the `printk` debugging subsystem. Notice that the below snippets are simplified versions of the real code:

`zephyr/lib/os/printk.h`

```c
#ifdef CONFIG_PRINTK
extern void printk(const char *fmt, ...);
#else
static inline void printk(const char *fmt, ...)
{
    ARG_UNUSED(fmt);
}
```

`zephyr/lib/os/printk.c`

```c
#ifdef CONFIG_PRINTK
void printk(const char *fmt, ...)
{
    // ...
}
#endif /* defined(CONFIG_PRINTK) */
```

> **Notice:** In our `prj.conf` file, we **set** `CONFIG_PRINTK=n`, but in the implementation, this translates to a missing definition, not a definition with a value of `n`. This is simply what a `bool` symbol translates to in the implementation. For details, I'll once again have to direct you to the [official documentation](https://docs.zephyrproject.org/latest/build/kconfig/setting.html#setting-kconfig-configuration-values).

In the header file `zephyr/lib/os/printk.h` we can see that `printk` is replaced by a dummy function in case `PRINTK` is disabled. Thus, all the calls to `printk` will effectively be removed by the compiler. In the `zephyr/lib/os/printk.c` source file, we can see that the `#if` directive is used to conditionally compile the relevant source code only in case `PRINTK` is enabled. Later in this section, we'll also see an example of how files can be excluded entirely by the build system if an option is not enabled.

With `printk` disabled in our application configuration file, let's try to rerun our application to verify that the output is indeed disabled:

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build --pristine
$ west flash --build-dir ../build
```

> **Notice:** In most cases when changing your _Kconfig_ symbols, you can simply run `west build` and the build system will rebuild the appropriate source. But in some cases, it is required to use the `--pristine` option to enforce a complete rebuild of your application. Typically, this is needed when adding new build or configuration files. If you encounter a build error or are missing a configuration change, try rebuilding with `--pristine`. This in turn also requires specifying the correct `--board` in case you didn't configure it using `west config`.

```
$ screen /dev/tty.usbmodem<some-serial-number> 115200
*** Booting Zephyr OS build v3.3.99-ncs1 ***
Message in a bottle.
```

Huh. Even though we've disabled `PRINTK` using `CONFIG_PRINTK=n` in our `prj.conf` file, the output is still not disabled. The build passed, and there were no warnings - did we miss something?
