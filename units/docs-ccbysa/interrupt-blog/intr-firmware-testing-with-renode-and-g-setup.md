---
id: "intr-firmware-testing-with-renode-and-g-setup"
type: "concept"
domain: "debug"
title: "Firmware Testing with Renode and GitHub Actions: Setup"
summary: "All the code in this post was written for the STM32F429 MCU by ST Micro. While the examples run fine on the STM32F429i discovery board, they were developed in Renode, a popular MCU emulation platform."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-07-test-automation-renode.md"
doc_source: "https://interrupt.memfault.com/blog/test-automation-renode#setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Example Repo

All the code in this post was written for the STM32F429 MCU by ST Micro. While
the examples run fine on the STM32F429i discovery board, they were developed in
Renode, a popular MCU emulation platform.

You can find the complete code example for this blog post in a separate
[GitHub repository](https://github.com/memfault/interrupt-renode-test-automation).

```
$ git clone --recurse-submodules https://github.com/memfault/interrupt-renode-test-automation.git
```

### Toolchain

I used the following tools to build my firmware:

- GCC 8.3.1 / GNU Arm Embedded Toolchain as our compiler[^gnu_toolchain]
- GNU Make 4.2.1 as the build system

Running automated tests with Renode, unfortunately, requires Python 2.7. To keep
things simple for me, I decided to use a Conda environment to keep this entire
environment isolated.

```
$ conda create -n renode
$ conda activate renode
$ conda install -c conda-forge -c memfault \
      python=2.7 gcc-arm-none-eabi make=4.2.1

$ which arm-none-eabi-gcc
/Users/tyler/miniconda3/envs/renode/bin/arm-none-eabi-gcc
```

Perfect, I now have `arm-none-eabi-gcc` and `python2.7` in my path.

> Want to learn more about Conda? Check out my previous post on using [Conda environments for embedded development](https://interrupt.memfault.com/blog/conda-developer-environments).

It turns out the Renode team packages the application in a
[Renode Conda package](https://anaconda.org/antmicro/renode), but at the time of
writing this post, not all platforms had the latest version released (v1.9,
released in March). For that reason, I chose to install it locally for this
post.

### Renode & Robot Framework

To install Renode, I've found the best instructions to be on the
[Renode GitHub Page](https://github.com/renode/renode#installation). In the
example repo, I've created a `start.sh` script which points to my local Renode
installation on my Mac. If you are using another platform, you'll have to update
this script to point to your own Renode start script.

```bash
#!/bin/sh

sh /Applications/Renode.app/Contents/MacOS/macos_run.command renode-config.resc
```

To run Robot Framework alongside Renode, we'll also need to clone the Renode
repository and all of its submodules, as well as install all of the required
Python dependencies.

```
$ git clone --recurse-submodules git@github.com:renode/renode.git
$ cd renode

# Install Robot Framework and other dependencies
$ pip install -r tools/requirements.txt
```

### Docker

To use Renode with Robot Framework in CI, it's best to use the official
[Renode Docker image](https://hub.docker.com/r/antmicro/renode) for running the
tests. If you haven't already, you'll want to install
[Docker](https://www.docker.com/products/docker-desktop).
