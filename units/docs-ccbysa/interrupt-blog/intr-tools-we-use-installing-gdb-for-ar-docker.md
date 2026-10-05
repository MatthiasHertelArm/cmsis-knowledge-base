---
id: "intr-tools-we-use-installing-gdb-for-ar-docker"
type: "concept"
domain: "debug"
title: "Tools we use: installing GDB for ARM: Details on each strategy / Docker"
summary: "Docker is a well-known technology for freezing dependencies, by using virtualization."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-03-installing-gdb.md"
doc_source: "https://interrupt.memfault.com/blog/installing-gdb#docker"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Details on each strategy_

[Docker](https://www.docker.com/) is a well-known technology for freezing
dependencies, by using virtualization.

For development tooling, you can set up a Docker image that contains all the
tooling you need to build + debug an embedded project:

```dockerfile
# select a specific SHA, to strictly pin the base image
FROM ubuntu:22.04@sha256:bace9fb0d5923a675c894d5c815da75ffe35e24970166a48a4460a48ae6e0d19

ARG DEBIAN_FRONTEND=noninteractive

# install GDB + GCC for ARM
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc-arm-none-eabi \
    gdb-multiarch
```

This approach has a few advantages:

- anyone using the same Docker image should be using _exactly_ the same version
  of the tools
- the same Docker image can be used in your test / CI infrastructure, which
  simplifies things greatly
- Docker images can be used on Linux/Mac/Windows without too much host setup

And a few downsides:

- running Docker images on Mac or Windows is likely going to be lower
  performance than on Linux, especially for file IO, since on those platforms
  Docker containers are running in a virtualization environment
- accessing host data (files) from within the Docker container can be tricky
- accessing host hardware (USB or Serial ports) can be easy or impossible,
  depending on host platform
- maintaining the Docker image itself requires some knowledge of Docker (though
  there are a lot of good tutorials online)

Plug- Memfault also provides a Docker image for running gdb-multiarch:

- <https://docs.memfault.com/docs/mcu/coredump-elf-with-gdb/#multi-architecture-gdb-using-docker>
