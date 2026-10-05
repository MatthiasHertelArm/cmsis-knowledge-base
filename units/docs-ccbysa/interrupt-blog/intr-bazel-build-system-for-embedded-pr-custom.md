---
id: "intr-bazel-build-system-for-embedded-pr-custom"
type: "concept"
domain: "debug"
title: "Bazel Build System for Embedded Projects: Toolchains / Custom"
summary: "For this example, we will integrate a pre-compiled ARM C++ toolchain into Bazel (taken from the official ARM website)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-30-bazel-build-system-for-embedded-projects.md"
doc_source: "https://interrupt.memfault.com/blog/bazel-build-system-for-embedded-projects#custom"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Toolchains_

For this example, we will integrate a pre-compiled ARM C++ toolchain into Bazel (taken from the official [ARM website](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads)). This will create a semi-hermetic toolchain ("semi" because it will still rely on some of the libraries of the host such as libc, etc. There are ways to make it fully hermetic but this is not the topic of this article.)

For this process, we will follow specific steps that can be re-used to integrate any toolchain.

#### Fetch the binaries

The first step is to integrate the pre-compiled binaries into Bazel, so that it can be accessed by a toolchain rule. The binaries can be downloaded with the Bazel repository rule http_archive. This will simply download a binary from a URL, unpack it and make it accessible as an external resource from Bazel. Note that you must provide a `BUILD` file in addition to exposing the interface from this newly created repository.

As this is a repository rule, it must be called from the `WORKSPACE` file.
For example:

```python
http_archive(
    name = "arm64_gcc_linux_x86_64",
    urls = ["https://developer.arm.com/-/media/Files/downloads/gnu/12.2.rel1/binrel/arm-gnu-toolchain-12.2.rel1-x86_64-aarch64-none-linux-gnu.tar.xz"],
    strip_prefix = "arm-gnu-toolchain-12.2.rel1-x86_64-aarch64-none-linux-gnu",
    sha256 = "6e8112dce0d4334d93bd3193815f16abe6a2dd5e7872697987a0b12308f876a4",
    build_file = "//toolchain_arm64_gcc:arm64_gcc_linux_x86_64.BUILD",
)
```

and the toolchain_arm64_gcc/arm64_gcc_linux_x86_64.BUILD file looks like:

```python
filegroup(
    name = "all",
    srcs = glob(["**/*",]),
)
```

After this step, the binaries will be accessible from the Bazel target `@arm64_gcc_linux_x86_64//:all`.

#### Create a CC toolchain

Now we need to create a `cc_toolchain`, this will instruct Bazel how to use the C++ toolchain just fetched previously.
The `cc_toolchain` rule, takes as parameters the set of files that need to be added to the sandbox for the different toolchain actions (compiling, linking, etc). Since we already exposed all the files from the package before with a `filegroup` named `all`, we can re-use it for all these arguments.

> Note that it is recommended to use the smallest set of files possible to avoid pulling all files every time, which could slow down the process on some execution platforms.

The `cc_toolchain` also requires a `toolchain_config` argument, which we will create in the next step. This is how the `cc_toolchain` invocation could look like in `toolchain_arm64_gcc/arm64_gcc_linux_x86_64.BUILD`:

```python
cc_toolchain(
    name = "cc_toolchain",
    all_files = ":all",
    ar_files = ":all",
    as_files = ":all",
    compiler_files = ":all",
    dwp_files = ":all",
    linker_files = ":all",
    objcopy_files = ":all",
    strip_files = ":all",
    static_runtime_lib = ":all",
    toolchain_config = ":my_cc_toolchain_config",
)
```

To create the `toolchain_config` that we named `my_cc_toolchain_config` in this example, we can use the `cc_toolchain_config` rule provided by the `@bazel_tools//` repository.

With this rule, we can tell Bazel how to use the toolchain binaries (which one to call and with which arguments).

We need to provide the path of all the binaries needed for the different toolchain actions, and the set of flags that need to be provided to the tools when compiling and linking. There are more options, but these are the most important to get started.

Without going too much into detail here is how this could look like in `toolchain_arm64_gcc/arm64_gcc_linux_x86_64.BUILD`:

```python
load("@bazel_tools//tools/cpp:unix_cc_toolchain_config.bzl", "cc_toolchain_config")

cc_toolchain_config(
    name = "my_cc_toolchain_config",
    cpu = "arm64",
    compiler = "gcc",
    toolchain_identifier = "arm64_gcc",
    host_system_name = "local",
    target_system_name = "local",
    target_libc = "unknown",
    abi_version = "unknown",
    abi_libc_version = "unknown",
    tool_paths = {
        "gcc": "bin/aarch64-none-linux-gnu-g++",
        "cpp": "bin/aarch64-none-linux-gnu-cpp",
        "ar": "bin/aarch64-none-linux-gnu-ar",
        "nm": "bin/aarch64-none-linux-gnu-nm",
        "ld": "bin/aarch64-none-linux-gnu-ld",
        "as": "bin/aarch64-none-linux-gnu-as",
        "objcopy": "bin/aarch64-none-linux-gnu-objcopy",
        "objdump": "bin/aarch64-none-linux-gnu-objdump",
        "gcov": "bin/aarch64-none-linux-gnu-gcov",
        "strip": "bin/aarch64-none-linux-gnu-strip",
        "llvm-cov": "/bin/false",
    },
    compile_flags = [
        "-isystem", "external/arm64_gcc_linux_x86_64/aarch64-none-linux-gnu/include/c++/12.2.1/aarch64-none-linux-gnu",
        "-isystem", "external/arm64_gcc_linux_x86_64/aarch64-none-linux-gnu/include/c++/12.2.1",
        "-isystem", "external/arm64_gcc_linux_x86_64/aarch64-none-linux-gnu/include",
        "-isystem", "external/arm64_gcc_linux_x86_64/aarch64-none-linux-gnu/libc/usr/include",
        "-isystem", "external/arm64_gcc_linux_x86_64/lib/gcc/aarch64-none-linux-gnu/12.2.1/include",
    ],
    link_flags = [],
)
```

At this point, we instructed Bazel on how to use the toolchain, now we need to tell Bazel when to use it and for which language.

#### Create a toolchain

A toolchain is created with the toolchain rule and associates a language-specific toolchain (like the `cc_toolchain` we previously created) with a toolchain type (that describes the C++ language in our case) and a set of constraints that need to be matched to be selected by the automatic toolchain resolution process we mentioned before.

In our case, the constraints for the execution platform will describe the host on which the toolchain we downloaded is built to run. While the constraints for the target platform will describe the ARM CPU.

Here is what the toolchain rule can look like in `toolchain_arm64_gcc/BUILD`:

```python
toolchain(
    name = "arm64_gcc_linux_x86_64",
    exec_compatible_with = [
        "@platforms//os:linux",
        "@platforms//cpu:x86_64",
    ],
    target_compatible_with = [
        "@platforms//cpu:arm64",
    ],
    toolchain_type = "@rules_cc//cc:toolchain_type",
    toolchain = "@arm64_gcc_linux_x86_64//:cc_toolchain",
)
```

#### Register the toolchain

Now we need to register the toolchain so that Bazel knows about its existence. This is done in the `WORKSPACE` file as follows:

```python
register_toolchains(
    "//toolchain_arm64_gcc:arm64_gcc_linux_x86_64",
)
```

#### Create a platform

At this point, the toolchain is fully integrated into Bazel and ready to be used. We only need a way to select it, this is done by creating a platform that will set the constraints we defined previously in the toolchain rule.

We need to create a platform that will be used as the target platform. Note the execution platform is the same as the host platform and is auto-generated by Bazel and it matches your current host environment.

This target platform only needs to set constraints to define the ARM CPU, it can be done as following in `toolchain_arm64_gcc/BUILD`:

```python
platform(
    name = "toolchain_arm64_gcc",
    constraint_values = [
        "@platforms//cpu:arm64",
    ],
)
```

#### Use the toolchain

We now have all the pieces to build a target with our new toolchain. To invoke this toolchain, we need to tell Bazel that we want to build for the previously create target platform. This is done as follow:

```bash
bazel build … --platforms=//toolchain_arm64_gcc --incompatible_enable_cc_toolchain_resolution
```

This is it! You have integrated a semi-hermetic toolchain into Bazel!

Note, `--incompatible_enable_cc_toolchain_resolution` is required to enable toolchain resolution with platforms for C++ toolchains. This flag should be enabled by default starting from Bazel 7.0.0, so in future releases, it will not be needed anymore.

The code described in this section can be found here: [](https://github.com/blaizard/bazel-examples/tree/main/toolchain-arm64-gcc)
