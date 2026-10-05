---
id: "intr-practical-zephyr-zephyr-basics-par-creating-a-setup-script"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1): Installation / Creating a setup script"
summary: "Instead of using the provided launch options, we'll use our own minimalistic shell script to explore the ecosystem and get to know the most important environment variables."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics#creating-a-setup-script"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Installation_

Instead of using the provided launch options, we'll use our own minimalistic shell script to explore the ecosystem and get to know the most important environment variables. You can find the complete [setup script](https://github.com/lmapii/practical-zephyr/blob/main/setup.sh) in the root folder of the [accompanying GitHub repository](https://github.com/lmapii/practical-zephyr).

After installing a toolchain with `nrfutil` you should see a tree similar to the following in your installation directory, in my case `/opt/nordic/ncs`:

```bash
tree /opt/nordic/ncs --dirsfirst -L 2 -I downloads -I tmp
/opt/nordic/ncs
├── toolchains
│   ├── 322ac893fe
│   └── toolchains.json
└── v3.2.1
    ├── bootloader
    ├── modules
    ├── nrf
    ├── nrfxlib
    ├── test
    ├── tools
    └── zephyr
```

The toolchain - and therefore **all** required host tools - are installed in a separate folder _toolchains_, whereas the actual SDK is placed in a folder with its version name. We'll make use of this to first set up our `$PATH` variable with a minimal set of `bin` directories from the installation:

```sh
ncs_install_dir=/opt/nordic/ncs
ncs_sdk_version=v3.2.1
ncs_bin_version=322ac893fe
shell_name=$(basename "$SHELL")

paths=(
    $ncs_install_dir/toolchains/$ncs_bin_version/bin
    $ncs_install_dir/toolchains/$ncs_bin_version/opt/nanopb/generator-bin
)

for entry in ${paths[@]}; do
    export PATH=$PATH:$entry
done
```

> **Note:** Depending on whether or not you want to replace _all_ binaries - including `git` - with Nordic's installation, _append_ or _prepend_ to `PATH`. In the above example, we _append_ and thus use local installations over the installation provided by the toolchain installer, if available.

After sourcing this script, you should now have, e.g., [Zephyr's meta-tool _West_](https://docs.zephyrproject.org/latest/develop/west/index.html) and [CMake](https://cmake.org/) in your path:

```bash
$ source setup.sh
$ which cmake
/opt/nordic/ncs/toolchains/322ac893fe/bin/cmake
$ which west
/opt/nordic/ncs/toolchains/322ac893fe/bin/west
```

Only [two environment variables are significant](https://docs.zephyrproject.org/latest/develop/env_vars.html#important-environment-variables) when configuring the toolchain:
- [`ZEPHYR_SDK_INSTALL_DIR`](https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-ZEPHYR_SDK_INSTALL_DIR) must be set to the installation directory of the SDK,
- [`ZEPHYR_TOOLCHAIN_VARIANT`](https://docs.zephyrproject.org/latest/develop/beyond-GSG.html#install-a-toolchain) selects the toolchain to use, e.g., `llvm` or in our case `zephyr`.

> **Note:** Yes, the inconsistent use of the term "SDK" is quite annoying. Nordic uses the term "SDK" to refer to its sources, whereas Zephyr uses _SDK_ to refer to the toolchain. I'm used to Nordic's terminology where an SDK also includes source code.

Once those environment variables are set, we can source the `zephyr-env.sh` that is provided by Zephyr itself, as shown below. This [Zephyr environment script](https://docs.zephyrproject.org/latest/develop/env_vars.html#zephyr-environment-scripts) is the recommended way to load an environment in case Zephyr is not installed globally.

```sh
# continuing setup.sh from the previous snippet

# for the sake of completeness, also show that we use the version of `nrfutil`
# that comes with Nordic's toolchain installation.
export NRFUTIL_HOME=$ncs_install_dir/toolchains/$ncs_bin_version/nrfutil/home

export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
export ZEPHYR_SDK_INSTALL_DIR=$ncs_install_dir/toolchains/$ncs_bin_version/opt/zephyr-sdk
source $ncs_install_dir/$ncs_sdk_version/zephyr/zephyr-env.sh
west zephyr-export
```

Instead of setting `ZEPHYR_BASE` manually as, e.g., done `nrfutil`, `ZEPHYR_BASE` is now set by the `zephyr-env.sh` script (we'll see how `ZEPHYR_BASE` is used when building our application). In addition, this also allows [using `.zephyrrc` files](https://docs.zephyrproject.org/latest/develop/env_vars.html#option-3-using-zephyrrc-files) in your application root directory - a feature we won't cover in this series.

The final command, `west zephyr-export`, is a ["Zephyr extension command"](https://docs.zephyrproject.org/latest/develop/west/zephyr-cmds.html#installing-cmake-packages-west-zephyr-export) that installs the required _CMake_ packages that we'll need in the next steps when using `find_package` to locate Zephyr's sources in a `CMakeLists.txt` file.

That's it for the environment; we can now create applications. One last time, this was just a warm-up to start with Zephyr. It is not required or recommended to use such a `setup.sh` script; it's just one of many possibilities you have when bringing up your development environment.
