---
id: "intr-building-nordic-nrf-connect-sdk-pr-runtime-environment-setup"
type: "concept"
domain: "debug"
title: "Building Nordic nRF-Connect SDK Projects with GitHub Actions: Runtime Environment Setup"
summary: "Now that we've got a basic skeleton in place, it's time to set up the workflow to also be able to build our project."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-18-ncs-github-actions.md"
doc_source: "https://interrupt.memfault.com/blog/ncs-github-actions#runtime-environment-setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we've got a basic skeleton in place, it's time to set up the workflow
to also be able to build our project. The first approach we'll take is to
install all the dependencies we need on-the-fly during the workflow run. The
tools we need are:

- host build dependencies (e.g. `cmake`, `ninja`, etc.)
- Zephyr SDK toolchain (this is the C compiler, linker, libc, etc.)
- the `west` Python tool

I followed the details in the [Zephyr Getting Started
Guide](https://docs.zephyrproject.org/3.5.0/develop/getting_started/index.html)
for installing these dependencies.

> Note: Nordic provides a ["toolchain manager"
> GUI](https://docs.nordicsemi.com/bundle/ncs-2.5.1/page/nrf/installation/installing.html)
> for installing nRF-Connect SDK dependencies. This isn't suitable for CI, where
> we need to install dependencies non-interactively. Nordic also conveniently
> provides a command-line version of the toolchain manager, called `nrfutil`;
> see the [nrfutil
> documentation](https://docs.nordicsemi.com/bundle/nrfutil/page/guides/getting_started.html)
> for details.
>
> **However**, we're going to install the normal Zephyr build dependencies
> ourselves, instead of using those convenience tools. This gives us a better
> understanding of the components in our build environment, and also makes it
> easier to manage each dependency separately (for example, if we need to update
> our `cmake` version). `nrfutil` at this time also is no longer open-source,
> and it's nice to be able to peek under the hood of our build environment, if
> we ever need to.
>
> Note that Martin's article
> ["Practical Zephyr - Zephyr Basics (Part 1)"](https://interrupt.memfault.com/blog/practical_zephyr_basics#setup-using-nordics-toolchain-manager)
> has a great rundown of these options, check it out!

Below find the updated workflow file, with the Zephyr build dependencies
installed on-the-fly (the emojis are optional but recommended 😅):

```yaml
on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          # Clone the repo to a subdirectory, so we can initialize the Zephyr
          # workspace in the parent directory.
          path: zephyr-workspace/nrfconnect-ci-app

      - name: 🧰 Install Dependencies + West
        # Install the Zephyr host build dependencies, and the `west` Python tool.
        # This list is from Zephyr's getting started guide:
        # https://docs.zephyrproject.org/latest/develop/getting_started/index.html
        run: |
          sudo apt update
          sudo apt install --no-install-recommends git cmake ninja-build gperf \
            ccache dfu-util device-tree-compiler wget \
            python3-dev python3-pip python3-setuptools python3-tk python3-wheel xz-utils file \
            make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1

          pip3 install west

      - name: 🪁 Install Zephyr SDK
        # Fetch the Zephyr SDK from the GitHub Release artifact, unpack it and
        # run the setup script, selecting the '-c' option to install cmake
        # packages and the '-t arm-zephyr-eabi' option to install the toolchain
        # only for the arm-zephyr-eabi (Cortex-M) architecture, since we don't
        # need the other toolchains (xtensa, riscv, etc.)
        run: |
          wget -q https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.4/zephyr-sdk-0.16.4_linux-x86_64_minimal.tar.xz
          tar xf zephyr-sdk-0.16.4_linux-x86_64_minimal.tar.xz -C ~/
          ~/zephyr-sdk-0.16.4/setup.sh -c -t arm-zephyr-eabi

      - name: ♻️ Initialize Zephyr Workspace
        # Set up the Zephyr workspace and install the Python dependencies
        run: |
          cd zephyr-workspace
          west init -l nrfconnect-ci-app
          west update --narrow -o=--depth=1
          pip3 install -r zephyr/scripts/requirements.txt

      - name: 🔨 Build Project
        run: |
          cd zephyr-workspace
          west build \
            --board nrf7002dk_nrf5340_cpuapp \
            --pristine=always nrfconnect-ci-app \
            -- \
            -DCONFIG_MEMFAULT_NCS_PROJECT_KEY=\"1234\"
```

Pushing this to our `main` branch will re-run the workflow, and we can check
that it succeeded:



An interesting note here: even though we're setting up the build environment
during the workflow run, it completes pretty quickly, reported as `2m36s` by
GitHub Actions. The breakdown is as follows:

- `🧰 Install Dependencies + West` : 19s (12%)
- `🪁 Install Zephyr SDK` : 8s (5%) 😮
- `♻️ Initialize Zephyr Workspace` : 1m13s (47%)
- `🔨 Build Project` : 54s (35%)

The biggest chunk of time is spent initializing the Zephyr workspace, which
makes sense- it's pulling down multiple Git repositories (45 total, in fact!).

Let's add one more step to our job- saving the output artifacts. In practice, we
might want to upload these to a cloud storage service (like AWS S3), or even
execute OTA deployments directly from the GitHub action, but that's a topic for
another day. For now, we'll just save the build artifacts as a GitHub Action
artifact:

```yaml
      - name: 📦 Save Build Artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build-artifacts
          path: zephyr-workspace/build
```

In practice we might only be interested in certain files in the build folder,
like `build/zephyr/zephyr.elf` and `build/zephyr/app_update.bin` for devices
with OTA capability.

Running the above change, we can see some artifacts are saved during the build,
and we can download and inspect them:


