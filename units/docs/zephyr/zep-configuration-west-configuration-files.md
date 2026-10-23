---
id: "zep-configuration-west-configuration-files"
type: "concept"
domain: "project"
title: "Configuration: West Configuration Files"
summary: "West's configuration file syntax is INI-like; here is an example file:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/config.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/config.rst"
license: "Apache-2.0"
mode: "V"
---

West's configuration file syntax is INI-like; here is an example file:

```ini

[manifest]
path = zephyr

[zephyr]
base = zephyr
```
Above, the `manifest` section has option `path` set to `zephyr`. Another
way to say the same thing is that `manifest.path` is `zephyr` in this file.

There are three types of configuration file:

1. **System**: Settings in this file affect west's behavior for every user
   logged in to the computer. Its location depends on the platform:

   - Linux: `/etc/westconfig`
   - macOS: `/usr/local/etc/westconfig`
   - Windows: `%PROGRAMDATA%\\west\\config`

2. **Global** (per user): Settings in this file affect how west behaves when
   run by a particular user on the computer.

   - All platforms: the default is `.westconfig` in the user's home
     directory.
   - Linux note: if the environment variable `XDG_CONFIG_HOME` is set,
     then `$XDG_CONFIG_HOME/west/config` is used.
   - Windows note: the following environment variables are tested to find the
     home directory: `%HOME%`, then `%USERPROFILE%`, then a
     combination of `%HOMEDRIVE%` and `%HOMEPATH%`.

3. **Local**: Settings in this file affect west's behavior for the
   current `west workspace`. The file is `.west/config`, relative
   to the workspace's root directory.

A setting in a file which appears lower down on this list overrides an earlier
setting. For example, if `color.ui` is `true` in the system's configuration
file, but `false` in the workspace's, then the final value is
`false`. Similarly, settings in the user configuration file override system
settings, and so on.
