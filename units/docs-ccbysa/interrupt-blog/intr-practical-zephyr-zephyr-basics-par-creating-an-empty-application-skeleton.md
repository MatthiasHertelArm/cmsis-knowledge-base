---
id: "intr-practical-zephyr-zephyr-basics-par-creating-an-empty-application-skeleton"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1): Creating an empty application skeleton"
summary: "Now that we have a working installation, we can start with the important parts of this article series. Before creating our first files, let's review Zephyr's supported application types."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics#creating-an-empty-application-skeleton"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we have a working installation, we can start with the important parts of this article series. Before creating our first files, let's review Zephyr's supported application _types_.

### Zephyr application types

Zephyr supports different [application types](https://docs.zephyrproject.org/latest/develop/application/index.html#application-types), differentiated by the location of your application in relation to Zephyr's sources

- [Freestanding applications](https://docs.zephyrproject.org/latest/develop/application/index.html#zephyr-freestanding-app) exist independent of Zephyr's location, meaning Zephyr is not part of the application's repository or file tree. The relation with Zephyr is only established in the build process when using `find_package` to locate Zephyr, typically based on the `ZEPHYR_BASE` environment variable.
- [Workspace applications](https://docs.zephyrproject.org/latest/develop/application/index.html#zephyr-workspace-app) use a [_West_ workspace](https://docs.zephyrproject.org/latest/develop/west/workspaces.html#west-workspaces): For such applications, _West_ is used to initialize your workspace, e.g., based on a `west.yml` manifest file. _West_ uses the manifest file to create complex workspaces: The location and revision are specified in the manifest file for each external dependency used in your project. West then uses this manifest to populate your workspace—like a very, very powerful version of [Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
- [Zephyr repository applications](https://docs.zephyrproject.org/latest/develop/application/index.html#zephyr-repo-app) live within the Zephyr repository itself, e.g., demo applications that are maintained with Zephyr. You could add applications in a fork of the Zephyr repository, but this is not very common.

The most common and easiest approach is to **start** with a freestanding application: You'll only need a couple of files to get started. As with the nRF Connect SDK, Zephyr is configured via the environment in a known installation directory.

In more advanced projects, you typically want all dependencies in your workspace. You will, therefore, switch to a workspace application type: External dependencies will be cloned directly into your project by _West_ to avoid depending on separate local installations. We'll get to that at the end of this article series.

We'll rely entirely on the [freestanding application type](https://docs.zephyrproject.org/latest/develop/application/index.html#zephyr-freestanding-app).

### A skeleton freestanding application

The steps to create an application from scratch are also documented in [Zephyr's documentation](https://docs.zephyrproject.org/latest/develop/application/index.html#creating-an-application-by-hand). We'll simply repeat them here and add some explanations, where necessary. Start by creating the following skeleton:

```bash
$ tree --charset=utf-8 --dirsfirst
.
├── src
│   └── main.c
├── CMakeLists.txt
└── prj.conf
```

You should immediately notice that we're using a `CMakeLists.txt`. Zephyr's build system is based on [CMake](https://cmake.org/). You've read that right: Zephyr provides its own meta-tool _West_, which uses yet another meta build system _CMake_, which will, in turn, e.g., use `make` or `ninja`.

> **Note:** You can find the complete application skeleton, including some additional comments, in the [`00_basics` folder of the accompanying GitHub repository](https://github.com/lmapii/practical-zephyr/tree/main/00_basics).

#### West vs. CMake

[West](https://docs.zephyrproject.org/latest/develop/west/index.html) is Zephyr's "Swiss army knife tool": It is mainly used for managing multiple repositories but also provides [Zephyr extension commands](https://docs.zephyrproject.org/latest/develop/west/zephyr-cmds.html) for building, flashing, and debugging applications. [CMake](https://cmake.org/), on the other hand, is used exclusively for building your application.

Since we want to learn how things work underneath, for the following steps, we'll be using _CMake_ first and circle back to _West_ after exploring the build process.

#### Kconfig

Our application skeleton also has a very suspicious `prj.conf` file. This file must exist for any application, even if empty, and is used by the [Kconfig configuration system](https://docs.zephyrproject.org/latest/build/kconfig/index.html). We'll go into detail about [Kconfig](https://docs.zephyrproject.org/latest/build/kconfig/index.html) (and *devicetree*) later in this series.

For now, simply keep in mind that we'll be using this configuration file to tell the build system which modules and which features we want to use in our application. Anything we don't plan on using will be deactivated, decreasing the size of our application and reducing compilation times.

#### Sources

Aside from our build and configuration file, we've created a still empty [`src/main.c`](https://github.com/lmapii/practical-zephyr/blob/main/00_basics/src/main.c) file. The convention is to place all sources in this `src` folder, but you might need a more complex setup as your application grows. For now, that'll do.
