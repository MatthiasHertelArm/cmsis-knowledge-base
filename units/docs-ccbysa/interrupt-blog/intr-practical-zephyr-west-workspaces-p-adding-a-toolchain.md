---
id: "intr-practical-zephyr-west-workspaces-p-adding-a-toolchain"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Zephyr with West / Adding a toolchain"
summary: "Toolchain management is always a highly opinionated topic, so I'll try to keep that discussion out of this article. The point is this: West workspaces do not include the required toolchain needed for building your application."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#adding-a-toolchain"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Zephyr with West_

Toolchain management is always a highly opinionated topic, so I'll try to keep that discussion out of this article. The point is this: West workspaces do **not** include the required _toolchain_ needed for building your application. This is something that you need to manage yourself, using whatever approach you feel comfortable with:

- Whether you're installing the toolchain globally,
- or decide to use [NixOS](https://nixos.org/explore),
- or maybe use [Docker](https://www.docker.com/),
- or something like [Nordic's toolchain manager](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/installation/assistant.html#install-toolchain-manager),

... or any other approach, is entirely up to you. What you need for building Zephyr applications are:

- Host dependencies such as `python`, `cmake`, `ninja`, etc., as explained in Zephyr's [Getting Started guide](https://docs.zephyrproject.org/latest/develop/getting_started/index.html#install-dependencies)
- An installation of the _Zephyr SDK_, containing the architecture specific toolchain. Zephyr's official documentation includes a dedicated section on the [Zephyr SDK](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html) and its installation instructions. The _Zephyr SDK_ does **not** contain Zephyr's _sources_!

Thankfully, Zephyr now made it easy to install the "Zephyr SDK" using a dedicated _West_ extension command, which is also explained in Zephyr's [Getting Started guide](https://docs.zephyrproject.org/latest/develop/getting_started/index.html#install-dependencies). E.g., to install the Zephyr SDK for `arm-zephyr-eabi` I could run the following command _in my West workspace_:

```bash
$ west sdk install --toolchains arm-zephyr-eabi
```

> **Note:** Running this command outside of a _West workspace_ fails ... unless you have an environment variable `ZEPHYR_BASE` pointing to [Zephyr's main repository](https://github.com/zephyrproject-rtos/zephyr/) on your filesystem.

The host tools are typically in your `$PATH` - at least for the executing terminal. For pointing Zephyr's build process to your installed SDK you can use the two environment variables [`ZEPHYR_TOOLCHAIN_VARIANT`](https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-ZEPHYR_TOOLCHAIN_VARIANT) and [`ZEPHYR_SDK_INSTALL_DIR`](https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-ZEPHYR_SDK_INSTALL_DIR).

In the first article of this series, we installed the correct SDK for the [nRF52840 Development Kit](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk) using Nordic's [`nrfutil`](https://docs.nordicsemi.com/bundle/nrfutil/page/README.html) command line tool. This installation contains not only the Zephyr SDK but also the host dependencies that I need for building Zephyr applications for nRF devices.

Since both, the STM32 and the nRF52840, are ARM MCUs, the installed Zephyr SDK already also contains the toolchain for building for the [STM32 Nucleo-64 development board](https://www.st.com/en/evaluation-tools/nucleo-f411re.html). All I need to do is provide the required environment variables.

For that, I could, e.g., use a _shell_ script similar to what we've seen in the first article of this series:

`app/setup-sdk-nrf.sh`

```sh
#!/bin/sh

ncs_install_dir="${ncs_install_dir:-/opt/nordic/ncs}"
ncs_bin_version="${ncs_bin_version:-322ac893fe}"

paths=(
    $ncs_install_dir/toolchains/$ncs_bin_version/bin
    $ncs_install_dir/toolchains/$ncs_bin_version/opt/nanopb/generator-bin
)

# required if dependencies are not installed, see also
# https://docs.zephyrproject.org/latest/develop/getting_started/index.html#install-dependencies
# e.g., "Ninja"
for entry in ${paths[@]}; do
    export PATH=$PATH:$entry
done

# use the nrfutil installation from the toolchain installation
export NRFUTIL_HOME=$ncs_install_dir/toolchains/$ncs_bin_version/nrfutil/home

# only export the paths to the SDK, no longer export the path to the zephyr installation.
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
export ZEPHYR_SDK_INSTALL_DIR=$ncs_install_dir/toolchains/$ncs_bin_version/opt/zephyr-sdk
```

> **Notice:** Zephyr provides [environment scripts](https://docs.zephyrproject.org/latest/develop/env_vars.html#zephyr-environment-scripts) including a `zephyr-env.sh`, which you can source in case you're using [Zephyr's official SDK](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html).

In this script, I'm extending my `$PATH` for the binaries that come with Nordic's toolchain installation. This includes `cmake`, `ninja`, and all other host tools used by Zephyr. In fact, this installation even contains `git` and `python`, but by appending to `$PATH`, my local installations have precedence over Nordic's binaries.

Then, I'm setting the `ZEPHYR_TOOLCHAIN_VARIANT` to `zephyr` and point `ZEPHYR_SDK_INSTALL_DIR` to the full path of the toolchain installation. Since I'm still using my own virtual environment, I need to install all Python packages required by Zephyr. Instead of cloning Zephyr as documented in the [getting started guide](https://docs.zephyrproject.org/latest/develop/getting_started/index.html#install-dependencies), I can use the locally populated Zephyr installation:

```bash
$ pip install -r deps/zephyr/scripts/requirements.txt
```

> **Note:** Using the above shell script I could actually scrap my virtual python environment, since all dependencies and packages are installed in Nordic's installation.

Having all tools installed, the build should now pass, or shouldn't it? Worth a try!

```bash
$ source app/setup-sdk-nrf.sh
$ west build --no-sysbuild --board nrf52840dk/nrf52840 app
-- west build: generating a build system
Loading Zephyr default modules (Zephyr base (cached)).
-- Application: /path/to/workspace/app
...
-- Found host-tools: zephyr 0.17.0 (/opt/nordic/ncs/toolchains/322ac893fe/opt/zephyr-sdk)
-- Found toolchain: zephyr 0.17.0 (/opt/nordic/ncs/toolchains/322ac893fe/opt/zephyr-sdk)
...
-- Including generated dts.cmake file: /path/to/workspace/build/zephyr/dts.cmake

warning: USE_SEGGER_RTT (defined at modules/segger/Kconfig:12) was assigned the value 'y' but got
the value 'n'. Check these unsatisfied dependencies: HAS_SEGGER_RTT (=n), 0 (=n). See
http://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_SEGGER_RTT and/or look up
USE_SEGGER_RTT in the menuconfig/guiconfig interface. The Application Development Primer, Setting
Configuration Values, and Kconfig - Tips and Best Practices sections of the manual might be helpful
too.
...
error: Aborting due to Kconfig warnings

CMake Error at /path/to/workspace/deps/zephyr/cmake/modules/kconfig.cmake:343 (message):
  command failed with return code: 1
Call Stack (most recent call first):
  /path/to/workspace/deps/zephyr/cmake/modules/zephyr_default.cmake:115 (include)
  /path/to/workspace/deps/zephyr/share/zephyr-package/cmake/ZephyrConfig.cmake:66 (include)
  /path/to/workspace/deps/zephyr/share/zephyr-package/cmake/ZephyrConfig.cmake:97 (include_boilerplate)
  CMakeLists.txt:2 (find_package)


-- Configuring incomplete, errors occurred!
FATAL ERROR: command exited with status 1: /opt/homebrew/bin/cmake -DWEST_PYTHON=/path/to/workspace/.venv/bin/python -B/path/to/workspace/build -GNinja -S/path/to/workspace/app
```

The build process was now able to correctly determine the `host-tools` and `toolchains`, but the build still failed with an error message that is quite hard to comprehend. Something seems to be missing!
