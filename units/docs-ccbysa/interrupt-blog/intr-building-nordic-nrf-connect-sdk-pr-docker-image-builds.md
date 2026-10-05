---
id: "intr-building-nordic-nrf-connect-sdk-pr-docker-image-builds"
type: "concept"
domain: "debug"
title: "Building Nordic nRF-Connect SDK Projects with GitHub Actions: Docker Image Builds 🐳"
summary: "So far we've been using the GitHub-hosted runners, which are virtual machines, to run our workflow."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-18-ncs-github-actions.md"
doc_source: "https://interrupt.memfault.com/blog/ncs-github-actions#docker-image-builds"
license: "CC-BY-SA-4.0"
mode: "V"
---

So far we've been using the GitHub-hosted runners, which are virtual machines,
to run our workflow. It's convenient, but we're at the mercy of the
configuration of those machines- the software installed might change at any
time, and we are not in full control.

We could work around that problem by installing custom copies of each piece of
software we rely on, but instead, let's use a Docker image to "freeze" our
dependencies.

> Note that we can specify a particular runner from the list
> [here](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources),
> for example `ubuntu-22.04`, which would likely give us more stable host
> software (and we could be explicit about which versions we select when we run
> `apt install`, but that relies on the Ubuntu package repositories keeping
> those versions available). But it's not guaranteed to exist forever- GitHub
> could at any time remove support for that runner.

### Zephyr Docker Image

Zephyr provides a Docker image that contains all the dependencies we need to
build our project, documented here:

<https://github.com/zephyrproject-rtos/docker-image/pkgs/container/ci>

We can make use of this image by specifying it as the runner in our GitHub
Actions workflow:


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
    container:
      # Zephyr toolchain from here:
      # https://github.com/zephyrproject-rtos/docker-image/pkgs/container/ci
      image: ghcr.io/zephyrproject-rtos/ci:v0.26.6
    env:
      # Tell cmake where to find the zephyr sdk
      CMAKE_PREFIX_PATH: /opt/toolchains
    steps:
      - uses: actions/checkout@v4
        with:
          # Clone the repo to a subdirectory, so we can initialize the Zephyr
          # workspace in the parent directory.
          path: zephyr-workspace/nrfconnect-ci-app

      - name: ♻️ Initialize Zephyr Workspace
        # Set up the Zephyr workspace and install the Python dependencies
        run: |
          cd zephyr-workspace
          rm -rf .west
          west init -l nrfconnect-ci-app
          west update --narrow -o=--depth=1

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
          ccache -z
          west build \
              --board nrf7002dk_nrf5340_cpuapp \
              --pristine=always nrfconnect-ci-app \
              -- \
              -DCONFIG_MEMFAULT_NCS_PROJECT_KEY=\"1234\"
          ccache -sv
```


Let's run that and see how it goes:



It ran in `4m53s`, much slower than the on-the-fly setup we had before, but we
didn't have to install anything- all the tools were pre-installed in the Docker
image, so they won't change (unless we update to a different image). This is a
really good property for CI!

This is the same image the Zephyr project uses for [their
CI](https://github.com/zephyrproject-rtos/zephyr/blob/f669e156d4a7d1f8cea6448896aa4b0226a891ce/.github/workflows/twister.yaml#L27),
which is a nice benefit- we can be sure that our project will build in the same
environment that the Zephyr project uses.

> From the [Practical Zephyr - Zephyr Basics (Part 1) article](https://interrupt.memfault.com/blog/practical_zephyr_basics),
> there's another example of using the Zephyr CI Docker image, which can be
> found here:
>
> <https://github.com/lmapii/practical-zephyr-manifest-repository/blob/main/.github/workflows/ci.yml>

The downside to this image is it's quite large (>13GB after uncompressing!) and
takes ~2m21s to load in our job (note that the Zephyr project relies on
self-hosted runners, which have the image pre-cached, so it's not as much of a
problem for them!).

One reason why the image is so large is because it contains toolchains for all
the many architectures Zephyr supports- at the time of writing, the image
contains toolchains for 22 different architectures 😮 (including
`sparc-zephyr-elf` 🤔)!

The image is open-source, built from the linked repo here:

<https://github.com/zephyrproject-rtos/docker-image>

So we can look at every piece of software added to that image.

Since our project only needs a single toolchain, let's go ahead and create our
own, custom Docker image!

### Custom Docker Image

Before we dive in, I'd like to mention a recent project that maintains several
very nice Docker images for embedded development:

<https://github.com/embeddedcontainers/ncs>

There's images there for building Zephyr projects and nRF-Connect SDK projects.
We can use those images as reference as we go to create our own custom image.

Fortunately, we already have all the pieces we need to construct our docker
image, from the section above where we installed all the [dependencies
on-the-fly](#runtime-environment-setup). We add all those pieces to a docker
image and upload it to the GitHub Container Registry, then use the image in our
build.

Here's the Dockerfile defining the image:

```dockerfile
FROM ubuntu:22.04

# set noninteractive installation
ENV DEBIAN_FRONTEND=noninteractive

# install host packages for Zephyr builds. package list is from here:
# https://docs.zephyrproject.org/3.5.0/develop/getting_started/index.html#install-dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
  ccache \
  cmake \
  file \
  g++-multilib \
  gcc \
  gcc-multilib \
  git \
  gperf \
  make \
  ninja-build \
  python3-venv \
  wget \
  xz-utils

# install the Zephyr toolchain only for arm-zephyr-eabi
ARG ZEPHYR_SDK_VERSION=0.16.4
RUN wget -q https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v${ZEPHYR_SDK_VERSION}/zephyr-sdk-${ZEPHYR_SDK_VERSION}_linux-x86_64_minimal.tar.xz \
  && mkdir -p /opt/toolchains \
  && tar xf zephyr-sdk-${ZEPHYR_SDK_VERSION}_linux-x86_64_minimal.tar.xz -C /opt/toolchains \
  && /opt/toolchains/zephyr-sdk-${ZEPHYR_SDK_VERSION}/setup.sh -c -t arm-zephyr-eabi \
  && rm zephyr-sdk-${ZEPHYR_SDK_VERSION}_linux-x86_64_minimal.tar.xz

# tell cmake where to find the Zephyr SDK cmake packages
ENV CMAKE_PREFIX_PATH /opt/toolchains

# create a Python virtual environment and install Python packages
RUN python3 -m venv /venv \
  && . /venv/bin/activate \
  && pip install --no-cache-dir \
    west==1.2.0

# fetch our target NCS version to make west update faster when we build
COPY west.yml /zephyr-workspace-cache/.manifest/west.yml

# retrieve a lighter version of the Zephyr workspace, which is enough to
# populate a cache for use when building. we'll need to re-generate this image
# if the manifest changes, to keep the benefit.
RUN . /venv/bin/activate \
  && cd /zephyr-workspace-cache \
  && west init -l .manifest \
  && west update --narrow --fetch-opt=--filter=tree:0

# install Python dependencies for the Zephyr workspace
RUN . /venv/bin/activate \
  && cd /zephyr-workspace-cache \
  && pip install --no-cache-dir -r zephyr/scripts/requirements.txt
```

We'll build the image using this command:

```bash
# note the image tag is set to use the GitHub container registry (ghcr.io), and
# we're setting the current ISO-8601 date as the tag
$ DOCKER_BUILDKIT=1 docker build -f .github/Dockerfile . -t ghcr.io/noahp/memfault-nrfconnect-ci-app:$(date --iso)
```

> Note: if your host machine is not amd64 (eg arm64), you'll need to pass the
> following option to the docker build command: `--platform linux/amd64`

Pushing the image to the GitHub container registry requires logging in
(instructions
[here](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-to-the-container-registry)),
then doing the normal docker push command:

```bash
$ docker push ghcr.io/noahp/memfault-nrfconnect-ci-app:2024-01-17
```

Once the image is uploaded to the GitHub container registry, we can use it in
our job:


```yaml
  custom-docker-image:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/noahp/memfault-nrfconnect-ci-app:2024-01-17
    steps:
      - uses: actions/checkout@v4
        with:
          # Clone the repo to a subdirectory, so we can initialize the Zephyr
          # workspace in the parent directory.
          path: zephyr-workspace/nrfconnect-ci-app

      - name: ♻️ Initialize Zephyr Workspace
        run: |
          cd zephyr-workspace
          west init -l nrfconnect-ci-app
          west update --narrow -o=--depth=1 --path-cache /zephyr-workspace-cache

      - name: 💾 Cache ~/.cache/ccache
        uses: actions/cache@v3
        with:
          path: ~/.cache/ccache
          key: ccache-v2-${{ runner.os }}-${{ hashFiles('zephyr-workspace/nrfconnect-ci-app/west.yml') }}
          restore-keys: |
            ccache-v2-${{ runner.os }}-

      - name: 🔨 Build Project
        run: |
          cd zephyr-workspace
          ccache -z
          west build \
              --board nrf7002dk_nrf5340_cpuapp \
              --pristine=always nrfconnect-ci-app \
              -- \
              -DCONFIG_MEMFAULT_NCS_PROJECT_KEY=\"1234\"
          ccache -sv
```




This runs in `1m31s` when cached, which is pretty good! The custom docker image
is about 3.4GB uncompressed, much smaller than the Zephyr general purpose image.

Overall advantages to our custom image:

- we can control exactly what software is installed
- smaller image size (more precisely fit to our needs)
- we can include a Zephyr workspace cache in the image, to speed up the
  `west update` step

The downside is that we're now on the hook for maintaining our Docker image. The
convenience of the GitHub container registry does make this a little less
painful, though.

### Fine Tuning Docker Images

I'll mention a few tools I use to tighten up Docker images:

- [dive](https://github.com/wagoodman/dive) - a sophisticated tool for analyzing
  each layer in a Docker image, and identifying opportunities to reduce unused
  items
- [dua](https://github.com/Byron/dua-cli) - this is actually not
  Docker-specific, but it's a great tool for quickly drilling through the Docker
  image file system, checking for large files that can be removed

Here's a way to use `dua` to inspect the file system of our image:

```bash
$ docker run --rm -i -t \
  ghcr.io/noahp/memfault-nrfconnect-ci-app:2024-01-17 \
    bash -c 'cd /tmp && wget -q -c https://github.com/Byron/dua-cli/releases/download/v2.17.5/dua-v2.17.5-x86_64-unknown-linux-musl.tar.gz -O - | tar -xz && ./dua*/dua i /'
```

Which yields an interactive view of the file system:


