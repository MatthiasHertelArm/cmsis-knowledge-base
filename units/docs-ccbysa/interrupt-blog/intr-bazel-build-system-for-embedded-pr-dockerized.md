---
id: "intr-bazel-build-system-for-embedded-pr-dockerized"
type: "concept"
domain: "debug"
title: "Bazel Build System for Embedded Projects: Toolchains / Dockerized"
summary: "Often when dealing with cross-compilation, you don’t get a self-contained binary or package that you can just unzip and use directly, but you need to install the toolchain on your machine, which makes it very difficult to use …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-30-bazel-build-system-for-embedded-projects.md"
doc_source: "https://interrupt.memfault.com/blog/bazel-build-system-for-embedded-projects#dockerized"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Toolchains_

Often when dealing with cross-compilation, you don’t get a self-contained binary or package that you can just unzip and use directly, but you need to install the toolchain on your machine, which makes it very difficult to use or integrate into CI for example or might conflict with an existing installation you already have. Or just by simplicity you might have your environment already set up in a Docker image and would like to be able to integrate it seamlessly into the build process.

For such a situation, Bazel can use a toolchain (or any tool in general) hosted on a docker image. This is done by defining an execution platform that makes use of the docker image.

#### Create an execution platform

First, we need to create the platform that will be used as the execution platform.
The constraint value associated with this platform will be used to select the toolchain, so we can create an arbitrary constraint value.

Here is an example:

```python
constraint_setting(
    name = "docker_image"
)

constraint_value(
    name = "docker_image_linux_arm64",
    constraint_setting = ":docker_image",
)

platform(
    name = "execution_platform",
    constraint_values = [
        ":docker_image_linux_arm64",
    ],
    exec_properties = {
        "container-image": "docker://docker.io/dockcross/linux-arm64:20230421-a0eaff4",
    },
)
```

The important piece is to point to the docker image URL with the `container-image` key of the `exec_properties` attribute.

#### Register the execution platform

Then we need to register the execution platform in the `WORKSPACE` file:

```python
register_execution_platforms(
    "//toolchain_arm64_gcc_docker:execution_platform",
)
```

This step makes the execution platform known by Bazel available for selection during the automatic toolchain resolution process. In Bazel point of view, all the execution platforms registered as such, are available from this host machine to execute an action.

#### Create the toolchain

In the same way as a toolchain was defined in the previous section, the `toolchain`, `cc_toolchain`, and `cc_toolchain_config` rules need to be created and point to the binaries within the Docker container.

The only difference is that now the toolchain rule takes as `exec_compatible_with` constraint, the one we used to create the execution platform.

#### Update the sandbox strategy

The last step is to tell Bazel to prioritize Docker sandboxing over the default strategy. That way, Bazel will check if the execution platform selected is compatible with the Docker strategy and use it, if not, the default sandboxing will be used.

This is done by adding these 2 lines in the `.bazelrc` file:

```bash
build --experimental_enable_docker_sandbox
build --spawn_strategy=docker,sandboxed
```

That’s it, you can now run a toolchain or any tool from within a docker image!

The code described in this section can be found here: [](https://github.com/blaizard/bazel-examples/tree/main/toolchain-arm64-gcc-docker)
