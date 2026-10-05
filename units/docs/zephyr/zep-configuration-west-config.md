---
id: "zep-configuration-west-config"
type: "concept"
domain: "project"
title: "Configuration: west config"
summary: "The built-in config command can be used to get and set configuration values. You can pass west config the options --system, --global, or --local to specify which configuration file to use."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/config.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/config.rst"
license: "Apache-2.0"
mode: "V"
---

The built-in `config` command can be used to get and set configuration
values. You can pass `west config` the options `--system`, `--global`, or
`--local` to specify which configuration file to use. Only one of these can
be used at a time. If none is given, then writes default to `--local`, and
reads show the final value after applying overrides.

Some examples for common uses follow; run `west config -h` for detailed help,
and see west-config-index for more details on built-in options.

To set `manifest.path` to `some-other-manifest`:

```console

west config manifest.path some-other-manifest
```
Doing the above means that commands like `west update` will look for the
`west manifest` inside the `some-other-manifest` directory
(relative to the workspace root directory) instead of the directory given to
`west init`, so be careful!

To read `zephyr.base`, the value which will be used as `ZEPHYR_BASE` if it
is unset in the calling environment (also relative to the workspace root):

```console

west config zephyr.base
```
You can switch to another zephyr repository without changing `manifest.path`
-- and thus the behavior of commands like `west update` -- using:

```console

west config zephyr.base some-other-zephyr
```
This can be useful if you use commands like `git worktree` to create your own
zephyr directories, and want commands like `west build` to use them instead
of the zephyr repository specified in the manifest. (You can go back to using
the directory in the upstream manifest by running ``west config zephyr.base
zephyr``.)

To set `color.ui` to `false` in the global (user-wide) configuration file,
so that west will no longer print colored output for that user when run in any
workspace:

```console

west config --global color.ui false
```
To undo the above change:

```console

west config --global color.ui true
```
