---
id: "intr-tools-for-firmware-code-size-optim-puncover"
type: "concept"
domain: "debug"
title: "Tools for Firmware Code Size Optimization: Puncover"
summary: "Although you can get quite far with the ARM GNU tools, my favorite tool for code size analysis by far is Puncover. It was built by Heiko Behrens, my former coworker at Pebble."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-06-06-best-firmware-size-tools.md"
doc_source: "https://interrupt.memfault.com/blog/best-firmware-size-tools#puncover"
license: "CC-BY-SA-4.0"
mode: "V"
---

Although you can get quite far with the ARM GNU tools, my favorite tool for code
size analysis by far is [Puncover](https://github.com/memfault/puncover).
It was built by [Heiko Behrens](https://heikobehrens.net/), my former
coworker at Pebble.

Puncover will give you a full hierarchical view of both code size and static
memory per module, file, and function. See the screenshot below:



It also shows you details for each function, including callers, callees, and
disassembly.



Truly, it is a firmware analysis swiss army knife!

Using puncover is relatively straightforward. You'll need to lightly prepare
your codebase, setup the tool itself, and run it.

### Preparing our codebase

In order to for puncover to work, our elf file needs to contain the requisite
information. As such, you'll need to make sure you've got the following CFLAGS
set:

- `-g`: this generates debug information which puncover requires for analysis
- `-fdebug-prefix-map=/=`: this flag forces gcc to collect full paths for
  filenames. This allows puncover to create the hierarchical view of the code.
  Even better would be to use your repository's root (usually found by running
  `git rev-parse --show-toplevel`).

I typically add those two to my CFLAGS for every project directly in my
Makefile.

### Setting up puncover

Puncover is relatively straightforward to setup: you simply need to clone it,
setup a virtualenv, and install the dependencies.

```terminal
# Clone
$ git clone git@github.com:memfault/puncover.git
Cloning into 'puncover'...
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 609 (delta 0), reused 0 (delta 0), pack-reused 608
Receiving objects: 100% (609/609), 1.22 MiB | 1.39 MiB/s, done.
Resolving deltas: 100% (325/325), done.
$ cd puncover

# Setup venv
$ python2.7 -m virtualenv venv
New python executable in /Users/francois/code/puncover/venv/bin/python2.7
Also creating executable in /Users/francois/code/puncover/venv/bin/python
Installing setuptools, pip, wheel...
done.

# Install dependencies
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
[...]
Successfully installed Flask-0.10.1 Jinja2-2.10.1 MarkupSafe-1.1.1
Werkzeug-0.15.2 argparse-1.4.0 certifi-2019.3.9 chardet-3.0.4 codecov-2.0.5
cov-core-1.15.0 coverage-4.5.3 funcsigs-1.0.2 idna-2.8 itsdangerous-1.1.0
mock-1.3.0 nose-1.3.7 nose-cov-1.6 pbr-5.2.0 requests-2.21.0 six-1.12.0
urllib3-1.24.3
```

### Running puncover

While you can install puncover as an executable, I typically just run the
`runner.py` script directly. All it requires is the path to your GNU ARM
toolchain:

```terminal
python runner.py --arm_tools_dir=<path-to-arm-tools-folder> --elf_file <path-to-elf-file>
```

Note that puncover needs the top level folder for your arm tools, not the `bin`
file. For me that's `/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/`.

If all goes well, you should see that puncover has spun up a webserver:

```terminal
(venv) $ python runner.py
--arm_tools_dir=/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/ --e_file
~/code/zero-to-main/with-libc/build/with-libc.elf
DEPRECATED: argument --arm_tools_dir will be removed, use --gcc_tools_base
instead.
parsing ELF at /Users/francois/code/zero-to-main/with-libc/build/with-libc.elf
enhancing function sizes
deriving folders
enhancing file elements
enhancing assembly
enhancing call tree
enhancing siblings
unmangling c++ symbols
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit
```

Now open your favorite web browser at localhost:5000, and enjoy!

Note: You may notice that some code size will be attributed to symbols under
`<Unknown>`. If you dig into those, you will see that they are all symbols
provided by the compiler or libc, such as `__aeabi_idiv0` or `_printf_i`. These
symbols do not come with file information as newlib is not compiled with `-g` in
most distributions. If you built your own newlib from source, you could fix
that!

### Puncover in Zephyr

The Zephyr RTOS project has the ability to [run puncover directly within West](https://docs.zephyrproject.org/latest/develop/optimizations/tools.html#build-target-puncover). It's slick!

You can do so by running the following:

```
# Build as normal
west build ...

# After installing puncover with 'pip install puncover'
west build -t puncover
```
