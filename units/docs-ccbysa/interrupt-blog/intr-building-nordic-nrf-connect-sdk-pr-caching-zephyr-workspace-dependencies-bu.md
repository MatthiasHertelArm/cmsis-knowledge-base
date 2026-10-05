---
id: "intr-building-nordic-nrf-connect-sdk-pr-caching-zephyr-workspace-dependencies-bu"
type: "concept"
domain: "debug"
title: "Building Nordic nRF-Connect SDK Projects with GitHub Actions: Caching Zephyr Workspace Dependencies + Build Artifacts"
summary: "Now that we've got a working workflow, let's see if we can speed it up a bit. There are 2 steps that are consuming the majority of the time, and both can benefit from caching:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-18-ncs-github-actions.md"
doc_source: "https://interrupt.memfault.com/blog/ncs-github-actions#caching-zephyr-workspace-dependencies-build-artifacts"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we've got a working workflow, let's see if we can speed it up a bit.
There are 2 steps that are consuming the majority of the time, and both can
benefit from caching:

- Initializing the Zephyr workspace
- Building the project

### Caching Zephyr Workspace Dependencies

There are (at least) two different ways to cache Zephyr workspace dependencies:

- Cache the entire Zephyr workspace
- Make use of the `west update` `--path-cache`/`--name-cache` options, to have
  `west update` check a local cache directory for Git repositories before
  fetching them

The first option is the simplest, but it can be a little more fragile (since
we'll restore the entire Zephyr workspace, we'll need to ensure we properly
install the updated project repo). The second option works well, but it seems to
require a fully populated (non-shallow) Zephyr workspace cache, which can be
several gigabytes in size.

### Caching Build Artifacts

We can use `ccache` to cache the compiler output (see Tyler's article about
[Improving Compilation Times](https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects) for details).

Zephyr's build system will automatically detect and use `ccache`, so all we have
to do here is save and restore the `ccache` cache directory, and we'll get
dramatically faster build times.

Note that the cache should be periodically freshened (this can be done on a
nightly or weekly build, for example) to ensure that the compilation cache
doesn't become stale and lose its benefit.

### Putting it all together

It's a bit detailed, but here's the approach I used to implement the caching as
described above. I also made 2 other performance tweaks:

- cache the Python dependencies, by installing them into a Python virtualenv,
  and caching the virtualenv
- reduce the number of host packages installed (`apt install`), since some are
  already present in the GitHub-hosted runner environment (the list of installed
  software in these virtual machines can be found by following the information
  [here](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners/about-github-hosted-runners#preinstalled-software))

Here's the updated workflow file:


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
      - name: 💾 Cache Zephyr Workspace
        uses: actions/cache@v3
        with:
          path: zephyr-workspace
          key: zephyr-workspace-v1-${{ runner.os }}-${{ hashFiles('zephyr-workspace/nrfconnect-ci-app/west.yml') }}
          restore-keys: |
            zephyr-workspace-v1-${{ runner.os }}-

      - name: 🧹 Clean Landing Site
        run: |
          rm -rf zephyr-workspace/nrfconnect-ci-app

      - uses: actions/checkout@v4
        with:
          # Clone the repo to a subdirectory, so we can initialize the Zephyr
          # workspace in the parent directory.
          path: zephyr-workspace/nrfconnect-ci-app

      - name: 💾 Cache ~/.venv
        uses: actions/cache@v3
        with:
          path: ~/.venv
          key: venv-${{ runner.os }}-${{ hashFiles('zephyr-workspace/zephyr/scripts/requirements.txt') }}
          restore-keys: |
            venv-${{ runner.os }}-

      - name: 🧰 Install Dependencies + West
        # Install the Zephyr host build dependencies, and the `west` Python tool. This list is from
        # https://docs.zephyrproject.org/3.5.0/develop/getting_started/index.html#install-dependencies
        run: |
          sudo apt update
          sudo apt install --no-install-recommends \
            ccache \
            ninja-build \

          python3 -m venv ~/.venv
          source ~/.venv/bin/activate
          # insert the PATH changes the venv activate made to be present for
          # future steps
          echo "PATH=$PATH" >> $GITHUB_ENV
          pip3 install west ninja

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
          rm -rf .west
          west init -l nrfconnect-ci-app
          west update --narrow -o=--depth=1

      - name: 🐍 Install Python Dependencies
        run: |
          cd zephyr-workspace
          pip3 install -r zephyr/scripts/requirements.txt

      - name: 💾 Cache ~/.cache/ccache
        uses: actions/cache@v3
        with:
          path: ~/.cache/ccache
          key: ccache-v1-${{ runner.os }}-${{ hashFiles('zephyr-workspace/nrfconnect-ci-app/west.yml') }}
          restore-keys: |
            ccache-v1-${{ runner.os }}-

      - name: 🔨 Build Project
        run: |
          cd zephyr-workspace
          # zero ccache statistics
          ccache -z
          west build \
              --board nrf7002dk_nrf5340_cpuapp \
              --pristine=always nrfconnect-ci-app \
              -- \
              -DCONFIG_MEMFAULT_NCS_PROJECT_KEY=\"1234\"
          # print detailed ccache statistics
          ccache -sv
```


After all that, our total build time as reported by GitHub Actions goes down to
`1m43s`, or `34%` faster. Honestly not that much faster, but it's a start!


