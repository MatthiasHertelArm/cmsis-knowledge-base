---
id: "intr-a-modern-c-development-environment-containers-for-development"
type: "concept"
domain: "debug"
title: "A Modern C Development Environment: Containers for development"
summary: "Working with embedded systems or C/C++ sometimes requires installing lots of specialized tools or compilers. If you are working on different projects at the same time, you'll easily end up with conflicting versions."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-09-a-modern-c-dev-env.md"
doc_source: "https://interrupt.memfault.com/blog/a-modern-c-dev-env#containers-for-development"
license: "CC-BY-SA-4.0"
mode: "V"
---

Working with embedded systems or C/C++ sometimes requires installing lots of specialized tools or compilers. If you are working on different projects at the same time, you'll easily end up with conflicting versions. Therefore, whenever feasible, I tend to run everything within a [Docker](https://www.docker.com/) *container*.

Another benefit is that you can also use your *Dockerfiles* as recipes in case you need to install tools locally. The real benefit, however, is that it makes it easy for anyone to join a project by using either a prebuilt image or by attempting to build the image locally. Also, your CI can use the same environment as you do!

### Why Docker? Where's the catch?

Don't get me wrong, *Docker* is far from being perfect and I experienced plenty of issues personally, but it is a decent solution if you keep some limitations in mind. If you're new to *Docker*, maybe consider the following:

- *Dockerfiles* are not stable. A *Dockerfile* that built just fine yesterday might fail to build today. There are simply too many external dependencies.
- *Docker* is not platform-independent. Especially if you're running a container on other CPU architectures, e.g., Apple ARM, you'll notice that some things don't run. We'll see this later.
- Some *Docker* features are only supported in Linux or dedicated Windows containers. E.g., mounting a USB device into a Docker container is not supported on all platforms; a limitation known [since 2016](https://github.com/docker/for-mac/issues/900).
- *Docker* - just like all the big companies out there - can suddenly deprecate even major features of their tools. I experienced this with [docker-machine](https://github.com/docker/roadmap/issues/245). It is always best not to bet 100% on one technology and you always need to be prepared to switch.
- *Docker* is no longer entirely free to use. At the time of writing, *Docker* was still free to use for personal use and small businesses, but please make sure to check their latest [license agreement](https://docs.docker.com/subscription/desktop-license/).

With all this in mind, *Docker* images are an elegant solution for development environments, especially if you have the chance to spin up your own registry. This sounds harder than it is since solutions already exist, e.g., [Google Cloud](https://cloud.google.com), [JFrog Artifactory](https://jfrog.com/artifactory/), and other providers.

I have personally experienced the huge upside of this with my first dockerized environment. By pulling the images from a registry of a project that was parked for over four years, I had the development environment back up and running in under 10 minutes.

### Let's do this

Let's start from zero with an empty repository:

```bash
mkdir cproject
cd cproject
git init
```

Make sure you have [Docker](https://www.docker.com/) installed and running. Create the following [`builder.Dockerfile`](https://github.com/lmapii/cproject/blob/main/builder.Dockerfile) in the root directory of the project:

```dockerfile
ARG base_tag=bullseye
ARG base_img=mcr.microsoft.com/vscode/devcontainers/base:dev-${base_tag}

FROM --platform=linux/amd64 ${base_img} AS builder-install

RUN apt-get update --fix-missing && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends \
    apt-utils \
    curl \
    cmake \
    build-essential \
    gcc \
    g++-multilib \
    locales \
    make \
    ruby \
    gcovr \
    wget \
    && rm -rf /var/lib/apt/lists/*
```

> **Note:** Throughout this article, I'll only show relevant parts of the *Dockerfile* and may omit some sections that you'll find in the [*Dockerfile* in the demo repository](https://github.com/lmapii/cproject/blob/main/builder.Dockerfile).

This *Dockerifle* specifies a base image and installs some packages that we'll use in future steps. I won't go into detail about each package: When creating your image you'll soon notice if something is missing and you can just extend this list of packages. What is important is the following:

- For the base image, I highly recommend using a specific *tag*. The `apt` packages vary wildly between base images, so choosing a tag buys you a bit more time until your *Dockerfiles* fail, e.g., when the `apt` registry changes.
- For development images, I tend to use a specific **platform**. This is important in later steps, where specific tools might not exist for the CPU architecture of your machine, e.g., if you're using an Apple ARM-based computer.

If you're not using [vscode](https://code.visualstudio.com/) you could also specify a different base image, e.g., `base_img=debian:${base_tag}`. In this article we're spinning up a development environment with `vscode` and we'll therefore stick to an image that is supported by its [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers).

The image is built with the following command, which might take a little time to execute:

```bash
docker build -f builder.Dockerfile -t cproject-builder:latest .
```

> **Note:** Running this command again will execute much faster since all steps within a *Dockerfile* are cached! Only if, e.g., you add new packages to the list, the whole step will be re-executed.

### A shortcut for verbose command line invocations

Docker commands are quite verbose, and they only tend to become even longer, which is why I typically park my most used commands in a [`makefile`](https://github.com/lmapii/cproject/blob/main/makefile) in the project root. Assuming you have `make` installed, you could do the following to make your life a little easier. Your future self will thank you for not having to remember all commands:

```makefile
project_name=cproject
builder-build :
  docker build -f builder.Dockerfile -t $(project_name)-builder:latest .
```

Now, all you need to do is the following to rebuild your image:

```bash
make builder-build
```

> **Note:** A more elegant solution than `makefiles` is [Invoke](http://www.pyinvoke.org/), presented in a [previous article](https://interrupt.memfault.com/blog/building-a-cli-for-firmware-projects). Since I'm a dinosaur, however, and for the sake of simplicity, I'll stick to `makefiles` in this article.

Let's spin up a container from our image and take it for a test drive:

```bash
$ docker run --rm -it --platform linux/amd64 cproject-builder:latest /bin/bash

$ gcc --version
gcc (Debian 10.2.1-6) 10.2.1 20210110
Copyright (C) 2020 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

$ cmake --version
cmake version 3.18.4
CMake suite maintained and supported by Kitware (kitware.com/cmake).

$ exit
```

When using `apt`, the version of the tools that have been installed depends on the base image and therefore on the package registry. If you want to install specific versions, you can do this by executing custom `RUN` commands as we'll see later.
