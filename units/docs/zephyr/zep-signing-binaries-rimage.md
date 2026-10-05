---
id: "zep-signing-binaries-rimage"
type: "concept"
domain: "project"
title: "Signing Binaries: rimage"
summary: "rimage configuration uses an approach that does not rely on Kconfig or CMake but on west config, similar to west-building-cmake-config."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/sign.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/sign.rst"
license: "Apache-2.0"
mode: "V"
---

rimage configuration uses an approach that does not rely on Kconfig or CMake
but on west config, similar to
west-building-cmake-config.

Signing involves a number of "wrapper" scripts stacked on top of each other: ``west
flash` invokes `west build` which invokes `cmake` and `ninja`` which invokes
`west sign` which invokes `imgtool` or rimage. As long as the signing
parameters desired are the default ones and fairly static, these indirections are
not a problem. On the other hand, passing `imgtool` or `rimage` options through
all these layers can causes issues typical when the layers don't abstract
anything. First, this usually requires boilerplate code in each layer. Quoting
whitespace or other special characters through all the wrappers can be
difficult. Reproducing a lower `west sign` command to debug some build-time issue
can be very time-consuming: it requires at least enabling and searching verbose
build logs to find which exact options were used. Copying these options from the
build logs can be unreliable: it may produce different results because of subtle
environment differences. Last and worst: new signing feature and options are
impossible to use until more boilerplate code has been added in each layer.

To avoid these issues, `rimage` parameters can bet set in `west config`.
Here's a `workspace/.west/config` example:

```ini

[sign]
# Not needed when invoked from CMake
tool = rimage

[rimage]
# Quoting is optional and works like in Unix shells
# Not needed when rimage can be found in the default PATH
path = "/home/me/zworkspace/build-rimage/rimage"

# Not needed when using the default development key
extra-args = -i 4 -k 'keys/key argument with space.pem'
```
In order to support quoting, values are parsed by Python's `shlex.split()` like in
west-building-cmake-args.

The `extra-args` are passed directly to the `rimage` command. The example
above has the same effect as appending them on command line after `--` like this:
`west sign --tool rimage -- -i 4 -k 'keys/key argument with space.pem'`. In case
both are used, the command-line arguments go last.
