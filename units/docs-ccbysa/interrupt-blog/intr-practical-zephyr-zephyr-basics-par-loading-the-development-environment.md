---
id: "intr-practical-zephyr-zephyr-basics-par-loading-the-development-environment"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1): Installation / Loading the development environment"
summary: "After installing nrfutil and its sdk-manager extension command (see below), you can install different versions of the nRF Connect SDK. E.g., to install the version 3.2.1 of the nRF Connect SDK, use the following commands."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics#loading-the-development-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Installation_

After installing `nrfutil` and its `sdk-manager` extension command (see below), you can install different versions of the nRF Connect SDK. E.g., to install the version 3.2.1 of the _nRF Connect SDK_, use the following commands.

```bash
$ nrfutil install sdk-manager
$ nrfutil sdk-manager install v3.2.1

$ nrfutil sdk-manager list
SDK Type  SDK Version  SDK Status  Toolchain Status
nrf       v3.2.1       Installed   Installed
```

However, when using Zephyr's tools in your normal command line, you should notice that the commands cannot be located yet. E.g., this is the output of my `zsh` terminal when trying to execute [Zephyr's meta-tool _West_](https://docs.zephyrproject.org/latest/develop/west/index.html) (we'll see the tool later):

```zsh
$ west --version
zsh: command not found: west
```

Nordic gives you several options to launch your development environment with all paths set up correctly using `nrfutil`:

```bash
# the following prints all environment variables used by the
# toolchain installation for the nRF Connect SDK version 3.2.1
$ nrfutil sdk-manager toolchain env --ncs-version v3.2.1

# the same command with the --as-script generates an output
# that can be used as a shell script
$ nrfutil sdk-manager toolchain env --ncs-version v3.2.1 --as-script

# the following opens a new terminal with the environment set up correctly
$ nrfutil sdk-manager toolchain launch --ncs-version v3.2.1 --terminal

# ... or you can launch within your existing shell
$ nrfutil sdk-manager toolchain launch --ncs-version v3.2.1 --shell
```

Since we want a better idea of what's happening underneath it all, we'll use *none* of the above options. Instead, we create our own `setup.sh` script based on what `nrfutil` generates when using `env --as-script`.
