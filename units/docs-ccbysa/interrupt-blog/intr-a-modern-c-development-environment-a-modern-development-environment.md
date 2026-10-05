---
id: "intr-a-modern-c-development-environment-a-modern-development-environment"
type: "concept"
domain: "debug"
title: "A Modern C Development Environment: A \"modern\" development environment"
summary: "Throughout this article, we'll set up a complete, containerized development environment for a C project:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-09-a-modern-c-dev-env.md"
doc_source: "https://interrupt.memfault.com/blog/a-modern-c-dev-env#a-modern-development-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

Throughout this article, we'll set up a complete, containerized development environment for a `C` project:

- We'll create a *Docker* image that we can use as a development container with [vscode](https://code.visualstudio.com/)
- Based on a minimal *Dummy* library, we'll set up the tools to build the library within the container.
- We'll set up the static code analyzer [`clang-tidy`](https://clang.llvm.org/extra/clang-tidy/) to check our code for common mistakes.
- [`clang-format`](https://clang.llvm.org/docs/ClangFormat.html) will help us to keep our code base nicely formatted and tidy.
- We'll set up the [Unity](https://www.throwtheswitch.org/unity), executed on host via [Ceedling](https://www.throwtheswitch.org/ceedling) to test our dummy function.
- And finally, we'll set up a GitHub workflow to execute, build, and test our project using the same *Docker* image that we're using locally.

> **Disclaimer:** There are endless possibilities to set up environments and this is just one of them. Please be lenient in case some of my solutions are not ideal or could be solved differently.

Throughout this article, I'll make use of the [Docker](https://www.docker.com/) command line interface. It is, however, out of the scope to discuss the basic concepts or the *Docker* command line parameters. In case you don't understand why certain parameters are needed, I'd kindly ask you to refer to the online documentation.

The impatient reader can just skip ahead and open the [example project on GitHub](https://github.com/lmapii/cproject). If you're happy to be walked through the steps, however, I'd be happy to guide you through the entire setup.
