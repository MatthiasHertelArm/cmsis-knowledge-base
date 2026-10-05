---
id: "intr-practical-zephyr-west-workspaces-p-setting-up-the-manifest-repository-and-f"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Zephyr with West / Setting up the manifest repository and file"
summary: "For our workspace structure, we're using what's known as a \"T2 star topology\": In such a topology, the manifest repository does not only contain the manifest file(s) but also contains all application files."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#setting-up-the-manifest-repository-and-file"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Zephyr with West_

For our workspace structure, we're using what's known as a ["T2 star topology"](https://docs.zephyrproject.org/latest/develop/west/workspaces.html#topologies-supported): In such a topology, the _manifest repository_ does not only contain the _manifest file(s)_ but also contains all application files.

We have all of our application code ready in the `app` folder, so let's go ahead, create an empty `app/west.yml` and make the `app` folder our manifest repository:

```bash
$ cd app
$ git init
$ touch west.yml
$ git add --all
$ cd ../

$ tree --dirsfirst -a -L 3
.
└── app  # manifest repository
    ├── .git
    ├── boards
    │   └── nrf52840dk_nrf52840.overlay
    ├── src
    │   └── main.c
    ├── CMakeLists.txt
    ├── prj.conf
    └── west.yml  # manifest file
```

With this, we can initialize our workspace as follows:

```bash
$ west init --local app
=== Initializing from existing manifest repository app
--- Creating /path/to/workspace/.west and local configuration file
=== Initialized. Now run "west update" inside /path/to/workspace.
```

Before running `west update`, let's add Zephyr as a project in `manifest.projects` just like what we've done for the [Doxygen-Awesome](https://github.com/jothepro/doxygen-awesome-css) dependency before:

`app/west.yml`

```yaml
manifest:
  version: 1.2

  self:
    path: app

  projects:
    - name: zephyr
      revision: v4.3.0
      url: https://github.com/zephyrproject-rtos/zephyr
      path: deps/zephyr
```

Running `west update` clones the Zephyr repository into `deps/zephyr` and checks out the commit with the tag `v4.3.0`:

```bash
$ west update
=== updating zephyr (deps/zephyr):
--- zephyr: initializing
Initialized empty Git repository in /path/to/workspace/deps/zephyr/.git/
--- zephyr: fetching, need revision v4.3.0
...
HEAD is now at 3568e1b6 release: Zephyr 4.3.0 release
```

Now, we have a complete "T2 star topology" workspace, where the Zephyr dependency is placed in a separate `deps` folder in the _topdir_ (again following the convention presented by Mike Szczys in his talk ["Manifests: Project Sanity in the Ever-Changing Zephyr World"](https://www.youtube.com/watch?v=PVhu5rg_SGY)):


```bash
tree --dirsfirst -a -L 3
.  # topdir
├── .west
│   └── config
├── app  # manifest repository
│   ├── .git
│   ├── boards
│   │   └── nrf52840dk_nrf52840.overlay
│   ├── src
│   │   └── main.c
│   ├── CMakeLists.txt
│   ├── prj.conf
│   └── west.yml  # manifest file
└── deps
    └── zephyr
```

Since we've used this application already in the previous article, we're pretty sure that it should build. However, building still fails since we didn't tell _West_ about Zephyr's extension commands yet:

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 app
usage: west [-h] [-z ZEPHYR_BASE] [-v] [-V] <command> ...
west: unknown command "build"; workspace /path/to/workspace does not define this extension command -- try "west help"
```

We can fix this by adding the `west-commands` key to the `zephyr` project: Zephyr's _West_ extensions are provided by the file `scripts/west-commands.yml` in Zephyr's repository. Using the key `west-commands`, we can provide a relative path to _West_ extension commands within the project:

`app/west.yml`

```yaml
manifest:
  version: 1.2

  self:
    path: app

  projects:
    - name: zephyr
      revision: v4.3.0
      url: https://github.com/zephyrproject-rtos/zephyr
      path: deps/zephyr
      # explicitly add Zephyr-specific West extensions
      west-commands: scripts/west-commands.yml
```

With the `west-commands` in place we can re-run `west update` to try and build our application. Several things can go wrong at this point. Best case, you'll see the error message below. Otherwise, the build might fail, e.g., because you don't have [_CMake_](https://cmake.org/) installed or because the _Zephyr SDK_ doesn't match the target:

```bash
west build --no-sysbuild --board nrf52840dk/nrf52840 app
-- west build: generating a build system
Loading Zephyr default modules (Zephyr base).
...
-- ZEPHYR_TOOLCHAIN_VARIANT not set, trying to locate Zephyr SDK
CMake Error at /path/to/workspace/deps/zephyr/cmake/modules/FindZephyr-sdk.cmake:108 (find_package):
  Could not find a package configuration file provided by "Zephyr-sdk"
  (requested version 0.15) with any of the following names:

    Zephyr-sdkConfig.cmake
    zephyr-sdk-config.cmake

  Add the installation prefix of "Zephyr-sdk" to CMAKE_PREFIX_PATH or set
  "Zephyr-sdk_DIR" to a directory containing one of the above files.  If
  "Zephyr-sdk" provides a separate development package or SDK, be sure it has
  been installed.
```

The error message is quite clear: Zephyr builds require that a toolchain is either installed globally or specified using the `ZEPHYR_TOOLCHAIN_VARIANT` environment variable. I didn't do either.

> **Note:** The `west-commands` is only needed since we've not seen the `import` key yet. I've added it explicitly so that you know about this key and how the West extension commands are handled in a manifest file, but you typically don't need to specify this in your `west.yml`.

The term ["Zephyr SDK"](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html) refers to the `zephyr` toolchain variant that must be provided for each of Zephyr’s supported architectures. With our manifest, we only add Zephyr's _sources_ to our workspace. The required tools, however, e.g., the GCC compiler for ARM Cortex-M, are **not** included.

> **Note:** Yes, the inconsistent use of the term "SDK" is quite annoying. While Zephyr uses _SDK_ exclusively for referring to the toolchain, I'd claim that an SDK typically also includes source code.
