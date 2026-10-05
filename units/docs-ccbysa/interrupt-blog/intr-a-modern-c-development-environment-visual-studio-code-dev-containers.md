---
id: "intr-a-modern-c-development-environment-visual-studio-code-dev-containers"
type: "concept"
domain: "debug"
title: "A Modern C Development Environment: Visual Studio Code Dev Containers"
summary: "The downside of not having all tools installed locally is that those tools can not be leveraged by your IDE of choice."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-09-a-modern-c-dev-env.md"
doc_source: "https://interrupt.memfault.com/blog/a-modern-c-dev-env#visual-studio-code-dev-containers"
license: "CC-BY-SA-4.0"
mode: "V"
---

The downside of **not** having all tools installed locally is that those tools can not be leveraged by your IDE of choice. E.g., when using `vscode` you won't be able to properly set up intellisense or any other helpers if you don't have any compiler installed.

`vscode` allows you to run an instance of the editor within a so-called *development container*. This is also the reason why we chose the `mcr.microsoft.com/vscode/devcontainers/base` image as the base image: We can connect `vscode` within our builder container and therefore have all the tools installed in our *Docker* image available! Notice, however, that this `vscode` instance does **not** match your local `vscode` installation. This `vscode` instance is created from scratch and works very similar to remote instances: E.g., you need to explicitly install all the extensions and provide all the settings that you have already set up in your local instance. Have a look at the [tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial) for the exact steps or in case anything fails whilst following along this article. For now, I assume that you have `vscode` and the [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) extension installed.

By creating the [`.devcontainer/devcontainer.json`](https://github.com/lmapii/cproject/blob/main/.devcontainer/devcontainer.json) file, we can tell `vscode` to use our newly built image for its development container. We're also installing three extensions within this `vscode` instance by using the `customizations.extensions` field in the `devcontainer.json` configuration file:

```json
{
  "name": "C",
  "build": {
    "dockerfile": "../builder.Dockerfile"
  },
  "runArgs": ["--platform=linux/amd64"],
  "customizations": {
    "vscode": {
      "settings": {
        "terminal.integrated.defaultProfile.linux": "bash",
        "extensions.verifySignature": false
      },
      "extensions": ["ms-vscode.cpptools", "ms-vscode.cmake-tools", "cschlosser.doxdocgen"]
    }
  }
}
```

If you now reload your window or reopen `vscode` (using the `cproject` folder as the root folder!) `vscode` should now ask you if it should use the detected development container.



It'll take a while for `vscode` to set up your container and install the extensions, but in the end you should have `vscode` connected to your Linux container, with all previous tools installed.


