---
id: "intr-practical-zephyr-west-workspaces-p-manifest-imports"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Zephyr with West / Manifest imports"
summary: "The build fails since we're only adding the Zephyr repository as a dependency. This is not enough: The Zephyr repository has its own dependencies, which it lists as projects in its own west.yml file."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#manifest-imports"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Zephyr with West_

The build fails since we're only adding the _Zephyr_ repository as a dependency. This is not enough: The Zephyr repository has its own dependencies, which it lists as _projects_ in its own `west.yml` file. We can _recursively import_ the required projects from Zephyr using the `import` key as follows:

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
      # the path is no longer needed since we're now using `path-prefix`
      # path: deps/zephyr
      # explicitly adding the Zephyr-specific West extensions is also no longer needed since
      # they are added accordingly with the `import` key.
      # west-commands: scripts/west-commands.yml
      # recursively import Zephyr dependencies
      import:
        path-prefix: deps
        # the `file` key is not strictly needed since `west.yml` is the default value.
        file: west.yml
        name-allowlist:
          - cmsis
          - cmsis_6
          - hal_nordic
```

We got rid of the `path` key, since `import.path-prefix` allows us to define a common prefix for all projects. Using the `import.file` key, we're telling _West_ to look for a `west.yml` file in Zephyr's repository and also consider the projects and West commands listed there. Notice that by default West looks for a `west.yml` file when using `import` and therefore it is not necessary to provide the `import.file` entry.

Instead of adding _all_ of Zephyr's dependencies, we pick the ones we need _by their name_ using the `import.name-allowlist` key.

> **Notice:** Without `name-allowlist` we'd instruct _West_ to clone **all** dependencies, recursively. If you have a quick look at Zephyr's manifest file [`west.yml`](https://github.com/zephyrproject-rtos/zephyr/blob/main/west.yml), you'll see that it has _a lot_ of dependencies. Running `west update` without limiting the dependencies may take several minutes and lots of disk space!

With this, _West_ **recursively** imports all allowed dependencies from the `zephyr` project. The details are explained nicely in the [official documentation on "Manifest Imports"](https://docs.zephyrproject.org/latest/develop/west/manifest.html#west-manifest-import).

Running `west update`, the new dependencies are placed in the `deps/modules` folder: We specified the `deps` prefix, whereas the `module` folder comes from Zephyr's own `west.yml` file:

```bash
$ tree --dirsfirst -a -L 5
.
├── .west
│   └── config
├── app
│   ├── .git
│   ├── boards
│   │   └── nrf52840dk_nrf52840.overlay
│   ├── src
│   │   └── main.c
│   ├── CMakeLists.txt
│   ├── prj.conf
│   ├── setup-sdk-nrf.sh
│   └── west.yml
├── build  [13 entries exceeds filelimit, not opening dir]
└── deps
    ├── modules
    │   └── hal
    │       ├── cmsis
    │       └── nordic
    └── zephyr  [43 entries exceeds filelimit, not opening dir]
```

Now, our `west build` indeed succeeds:


```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 app
...

[163/163] Linking C executable zephyr/zephyr.elf
Memory region         Used Size  Region Size  %age Used
           FLASH:       24852 B         1 MB      2.37%
             RAM:        4416 B       256 KB      1.68%
        IDT_LIST:          0 GB         2 KB      0.00%
```

> **Notice:** In addition to the `name-allowlist` you can also instruct _West_ to use shallow clones instead of a complete `git clone` for all its projects. E.g., use `west update -o=--depth=1 -n` to create shallow clones. Have a look at the help output of `west update --help`!
