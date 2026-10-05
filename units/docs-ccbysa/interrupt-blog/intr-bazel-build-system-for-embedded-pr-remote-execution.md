---
id: "intr-bazel-build-system-for-embedded-pr-remote-execution"
type: "concept"
domain: "debug"
title: "Bazel Build System for Embedded Projects: Toolchains / Remote execution"
summary: "Another interesting use case that Bazel can solve is remote execution. This can be useful in the domain of embedded development for the following scenarios for example:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-30-bazel-build-system-for-embedded-projects.md"
doc_source: "https://interrupt.memfault.com/blog/bazel-build-system-for-embedded-projects#remote-execution"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Toolchains_

Another interesting use case that Bazel can solve is remote execution. This can be useful in the domain of embedded development for the following scenarios for example:

- The toolchain only runs on Windows but the developers have Linux machines
- There is a limited number of licenses for a tool
- A hardware key is required for a specific tool
- ...

For all these use cases, it is hard to integrate such tools in the developer workflow as it requires building on a specific machine or has other accessibility constraints.

By setting up a remote execution server (here is a list of available options: [](https://bazel.build/community/remote-execution-services)), Bazel can execute some of these actions on a remote machine. This is done by changing the default strategy (as we did in the previous section) to remote and pointing to the address of this server, like in this example:

```bash
build --remote_executor=grpc://my/server:8980
build --spawn_strategy=remote,sandboxed
```

The selection of the remote runners is done by matching the set of `exec_properties` from the selected execution platform, similar to how the Docker image was selected in the previous section.

The rest of the configuration is specific to the remote execution server you selected, so please refer to their documentation if you want to explore this option.
