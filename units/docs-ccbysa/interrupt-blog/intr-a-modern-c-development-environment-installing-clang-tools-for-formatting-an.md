---
id: "intr-a-modern-c-development-environment-installing-clang-tools-for-formatting-an"
type: "concept"
domain: "debug"
title: "A Modern C Development Environment: Installing `clang` tools for formatting and static code analysis"
summary: "The flexibility of C and C++ comes with plenty of massive footguns so, I try to add at least a minimal static code analysis to my project."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-09-a-modern-c-dev-env.md"
doc_source: "https://interrupt.memfault.com/blog/a-modern-c-dev-env#installing-clang-tools-for-formatting-and-static-code-analysis"
license: "CC-BY-SA-4.0"
mode: "V"
---

The flexibility of C and C++ comes with plenty of massive footguns so, I try to add at least a minimal static code analysis to my project. This helps to catch the most obvious mistakes and gives some extra confidence in the codebase. There are plenty of tools out there, but my personal preference so far is [`clang-tidy`](https://clang.llvm.org/extra/clang-tidy/).

Also, when collaborating on a codebase, a formatter is always a nice thing to have, and since we're installing `clang-tidy` anyhow, we might as well go ahead and install [`clang-format`](https://clang.llvm.org/docs/ClangFormat.html).

The two configuration files [`.clang-format`](https://github.com/lmapii/cproject/blob/main/.clang-format) and [`.clang-tidy`](https://github.com/lmapii/cproject/blob/main/.clang-tidy) are placed into the root directory of the project such that any IDE picks them up automatically. I won't go into detail about the options of the two tools and will just assume that the reader follows the previous links for more details or copies the files from the [example project on GitHub](https://github.com/lmapii/cproject). So this is what we have now:

```bash
$ tree --charset=utf-8 --dirsfirst -a -I build -I .git -L 1
.
├── .devcontainer
├── include
├── src
├── .clang-format
├── .clang-tidy
├── CMakeLists.txt
├── builder.Dockerfile
└── makefile
```

### Installing specific in the builder image

Here's a catch with `clang-tidy` and `clang-format`: The configuration files must match the tool version, they are not necessarily backward compatible. It is therefore important to install compatible versions for your configuration files. Since we have a container we'll always be using the correct version! The installation, however, can be tricky. Why? Running `apt-get` to install the tools does not always work since the package registries typically contain ancient tool versions. One way around this is to install them manually in our *Dockerfile*:

```dockerfile
ARG base_tag=bullseye
ARG llvm_version=16
RUN apt-get update --fix-missing && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends \
    gnupg2 \
    gnupg-agent \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl --fail --silent --show-error --location https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
RUN echo "deb http://apt.llvm.org/$base_tag/ llvm-toolchain-$base_tag-$llvm_version main" >> /etc/apt/sources.list.d/llvm.list

RUN apt-get update --fix-missing && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends \
    clang-format-${llvm_version} \
    clang-tidy-${llvm_version} \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/clang-format-${llvm_version} /usr/local/bin/clang-format
RUN ln -s /usr/bin/clang-tidy-${llvm_version} /usr/local/bin/clang-tidy
```

This is one of the steps in a *Dockerfile* that I've previously mentioned which can break quite easily when you're trying to rebuild an image in a couple of years. In case you're happy with the packages provided for your base images, you can also simply install the packages that are provided with the `apt` registry. Now both `clang-format` and `clang-tidy` are available in the image:

```bash
$ make builder-build
$ make builder-run

$ clang-format --version
Debian clang-format version 16.0.6 (++20230704084212+7cbf1a259152-1~exp1~20230704204302.101)

$ clang-tidy --version
Debian LLVM version 16.0.6
  Optimized build.
```

### Using `clang-format` in the Development Container

`vscode` typically needs to be instructed to rebuild the development container from the *Dockerfile*. You can do so explicitly using the command prompt:



Now you have `clang-tidy` and `clang-format` available within your development container. You can now also instruct `vscode` to automatically format your files on save. For this, we create a workspace configuration [`.vscode/settings.json`](https://github.com/lmapii/cproject/blob/main/.vscode/settings.json) file:

```json
{
  "[c]": {
    "editor.formatOnSave": true
  },
  "[cpp]": {
    "editor.formatOnSave": true
  },
  "C_Cpp.default.compileCommands": "${workspaceFolder}/src/build/compile_commands.json",
  "cmake.configureOnOpen": true
}
```

I've hidden a little detail here: `clang-tidy` operates on the `compile_commands.json` file that can be created when using `cmake` as a build system. I've enabled this option within the [`CMakeLists.txt`](https://github.com/lmapii/cproject/blob/main/CMakeLists.txt) file. At the same time, we're allowing the `cmake` extension for `vscode` to configure the project when opening and therefore have all the fancy buttons and actions available to build the project in case you don't like the command line. Personally, I still fall back to the command line. But then, I'm a dinosaur.

Now, if you open the `dummy.c` file in your editor it will automatically format it according to the rules in your `.clang-format` file whenever you save the file. But what if someone in your team doesn't use `vscode` or forgot to enable the format-on-save feature?

### Wrapping `clang-format` and `clang-tidy` calls

This section is a little self-promotion of two wrapper scripts for `clang-format` and `clang-tidy` that I am maintaining: [run-clang-tidy](https://github.com/lmapii/run-clang-tidy) and [run-clang-format](https://github.com/lmapii/run-clang-format). Both tools are command line tools written in [Rust](https://www.rust-lang.org/) that simplify and parallelize the execution of `clang-format` and `clang-tidy` from the command line.

In our `builder.dockerfile` we'll now install the released, architecture-specific versions from the *GitHub* repositories of [run-clang-tidy](https://github.com/lmapii/run-clang-tidy) and [run-clang-format](https://github.com/lmapii/run-clang-format).

```dockerfile
RUN mkdir -p /usr/local/run-clang-format
RUN wget -O clang-utils.tgz "https://github.com/lmapii/run-clang-format/releases/download/v1.4.10/run-clang-format-v1.4.10-i686-unknown-linux-gnu.tar.gz" && \
    tar -C /usr/local/run-clang-format -xzf clang-utils.tgz --strip-components 1 && \
    rm clang-utils.tgz

ENV PATH /usr/local/run-clang-format:$PATH
RUN run-clang-format --version

RUN mkdir -p /usr/local/run-clang-tidy
RUN wget -O clang-utils.tgz "https://github.com/lmapii/run-clang-tidy/releases/download/v0.2.1/run-clang-tidy-v0.2.1-i686-unknown-linux-gnu.tar.gz" && \
    tar -C /usr/local/run-clang-tidy -xzf clang-utils.tgz --strip-components 1 && \
    rm clang-utils.tgz

ENV PATH /usr/local/run-clang-tidy:$PATH
RUN run-clang-format --version
```

Instead of just downloading the pre-built binaries, it is also possible to use the below steps to install *Rust* and its [package manager `cargo`](https://github.com/rust-lang/cargo) using the [Rust toolchain installer `rustup`](https://rustup.rs/), and then install the two tools by running `cargo install`:

```dockerfile
RUN curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain stable -y
ENV PATH=/root/.cargo/bin:$PATH

RUN cargo install run-clang-format
RUN cargo install run-clang-tidy
```

While this approach is less verbose, it significantly increases the image size and image build time: First of all, this installs the full Rust toolchain, which in my tests increased the image size by almost *1 GB*, and second the `cargo install` commands compile both tools and all of its dependencies from scratch, which - on my machine - took almost 4 minutes for each. When creating such builder images, it is therefore always important to find the right fit for your need: If you won't be developing using *Rust* you might be better off *not* installing it in your builder. This way, you keep build times and the image size as low as possible - no matter how awesome [Rust](https://www.rust-lang.org/) is.

But let's keep on working on our development environment. Why do we need [run-clang-tidy](https://github.com/lmapii/run-clang-tidy) and [run-clang-format](https://github.com/lmapii/run-clang-format)? These wrapper scripts allow to define the execution of `clang-format` and `clang-tidy` based on `.json` input files. Within these files, it is possible to efficiently filter all files, e.g., third-party software for which the format-on-save would be more cumbersome than helpful. Since we'll be adding unit tests later, we can prepare the configurations already:

For formatting, we simply need to provide the paths to the source files and filters for files that we want to exclude from formatting or from the glob expansion:

```json
{
  "paths": ["./src/**/*.[ch]", "./include/**/*.[h]", "./tests/unittest/test/*.[ch]"],
  "filterPre": [".*"],
  "filterPost": ["./src/build/**", "./tests/unittest/build/**", "./tests/unittest/generated"]
}
```

For the static analysis, we also need to tell the tool where to find the `compile_commands.json`:

```json
{
  "paths": ["./src/**/*.[ch]", "./include/**/*.[h]"],
  "filterPre": [".*"],
  "filterPost": ["./build/**"],
  "buildRoot": "./build"
}
```

Now we just need to update our image and run the commands. Whether you do this by spinning up your container or by rebuilding the `vscode` development container is up to you, it should run in both environments:

```bash
$ make builder-build
$ make builder-run

$ run-clang-format clang-format.json
 [ 1/5 ] No style file specified, assuming .clang-format exists in the project tree
 [ 2/5 ] Found 2 files for the provided path patterns
 [ 3/5 ] Found clang-format version 16.0.6 using command clang-format
 [ 4/5 ] Executing clang-format ...

  Formatting /builder/mnt/src/dummy.c
  Formatting /builder/mnt/include/dummy/dummy.h
     Running [==========================] 2/2
     Finished in 0 seconds

$ run-clang-tidy clang-tidy.json
 [ 1/6 ] No tidy file specified, assuming .clang-tidy exists in the project tree
 [ 2/6 ] Using build root /workspaces/cproject/build
 [ 3/6 ] Found 1 files for the provided path patterns
 [ 4/6 ] Found clang-tidy version 16.0.6 using command clang-tidy
 [ 5/6 ] Executing clang-tidy ...

          Ok /workspaces/cproject/src/dummy.c
     Running [==========================] 1/1
     Finished in 1 second
```

> **Note:** Instead of running `cmake --build build` every time you modify your files, you can now also simply execute the static code analysis instead. It also compiles your files, but at the same time points out some of the mistakes that you have enabled.
