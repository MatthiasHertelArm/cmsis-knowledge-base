---
id: "intr-using-swig-to-generate-bindings-be-setting-up"
type: "concept"
domain: "debug"
title: "Using SWIG to generate bindings between C and Lua: Setting up"
summary: "We’ll start by writing a Dockerfile that will host our desktop environment including Lua, SWIG, CMake, and GCC. Let’s build on top of alpine:3.16 image for a smaller size."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-11-29-swig-for-c-and-lua.md"
doc_source: "https://interrupt.memfault.com/blog/swig-for-c-and-lua#setting-up"
license: "CC-BY-SA-4.0"
mode: "V"
---

> To follow along, I've provided all example code on [GitHub in the Interrupt repo under `example/swig-for-c-and-lua`](https://github.com/memfault/interrupt/tree/master/example/swig-for-c-and-lua).

We’ll start by writing a Dockerfile that will host our desktop environment including Lua, SWIG, CMake, and GCC. Let’s build on top of `alpine:3.16` image for a smaller size.

First, let’s get Lua 5.4.4 in:

```dockerfile
FROM alpine:3.16

WORKDIR /app

RUN apk add git make curl gcc tar
RUN apk add libc-dev

RUN curl -R -O http://www.lua.org/ftp/lua-5.4.4.tar.gz
RUN tar zxf lua-5.4.4.tar.gz
RUN rm lua-5.4.4.tar.gz
RUN cd lua-5.4.4 && make all test && make install
```

Then add SWIG 4.1.0, GCC, CMake:

```dockerfile
RUN apk add git make automake autoconf libtool
RUN git clone https://github.com/swig/swig --branch v4.1.0

RUN apk add pcre2-dev
RUN apk add bison flex
RUN apk add gcc g++

RUN cd swig && ./autogen.sh && ./configure && make
RUN cd swig && make install

RUN apk add cmake
```

And finally, check if both Lua and SWIG programs are available (if any of these commands fails the Docker image build will fail too):

```dockerfile
RUN luac -v
RUN swig -version
```

Here is the whole resulting Dockerfile for reference ([link](https://github.com/memfault/interrupt/tree/master/example/swig-for-c-and-lua/Dockerfile)):

```dockerfile
FROM alpine:3.16

WORKDIR /app

RUN apk add git make curl gcc tar
RUN apk add libc-dev

RUN curl -R -O http://www.lua.org/ftp/lua-5.4.4.tar.gz
RUN tar zxf lua-5.4.4.tar.gz
RUN rm lua-5.4.4.tar.gz
RUN cd lua-5.4.4 && make all test && make install

RUN apk add git make automake autoconf libtool
RUN git clone https://github.com/swig/swig --branch v4.1.0

RUN apk add pcre2-dev
RUN apk add bison flex
RUN apk add gcc g++

RUN cd swig && ./autogen.sh && ./configure && make
RUN cd swig && make install

RUN apk add cmake

# Check installed programs
RUN luac -v
RUN swig -version

ENTRYPOINT ["/bin/sh"]
```

To build and run this container, we can run the following command in our shell:

```shell
# Host machine
$ docker build -t swig . && docker run -v $PWD:/app -it swig

... # Build output

# Docker container shell starts!
/app # ls
Dockerfile   example1     ...
```

Now, using this Docker image we can parse Lua scripts, compile Lua to bytecode, generate bindings with SWIG, and compile C/C++ programs using CMake!

To make things as easy for you to replicate what I'm doing in this post, I've created shell scripts for each example, such as `example1.sh`, that can be run from your host machine with Docker installed.
