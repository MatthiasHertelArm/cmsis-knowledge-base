---
id: "intr-practical-zephyr-west-workspaces-p-initializing-the-workspace"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Creating a workspace from scratch / Initializing the workspace"
summary: "Part of: Creating a workspace from scratch"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#initializing-the-workspace"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Creating a workspace from scratch_

Having everything under version control we can relax and start exploring. First, we finally _initialize_ the _West_ workspace using [`west init`](https://docs.zephyrproject.org/latest/develop/west/basics.html#west-init-and-west-update). There are two ways to initialize a _West_ workspace:

- **Locally**, using the `-l` or `--local` flag: This assumes that your manifest repository already exists in your filesystem, e.g., you already used `git clone` to populate it in the _topdir_.
- **Remotely**, by specifying the URL to the manifest repository using the argument `-m`. With this argument, _West_ clones the manifest repository into the _topdir_ for you before initializing the workspace. We'll see how this works in a [later section](#creating-a-workspace-from-a-repository).

There is no difference between the two methods except that _West_ also clones the repository when using the `-m` argument to pass the manifest repository URL. Since our manifest repository is initialized already in the `app` folder, we can initialize the workspace using this local manifest repository:

```bash
workspace/app $ west init --local .
=== Initializing from existing manifest repository app
--- Creating /path/to/workspace/.west and local configuration file
=== Initialized. Now run "west update" inside /path/to/workspace.

workspace/app $ tree --dirsfirst -a -L 2 ../
../
├── .west
│   └── config
├── app
│   ├── .git
│   └── west.yml
├── Pipfile
└── Pipfile.lock
```

When initializing a workspace, _West_ creates a `.west` directory in the _topdir_, which in turn contains a configuration file.

```bash
workspace/app $ cat ../.west/config
```

```ini
[manifest]
path = app
file = west.yml
```

The location of the `.west` folder "marks" the _topdir_ and thus the _West_ workspace root directory. Within this file, we can see that _West_ stores the location and name of the manifest file. Modifying this file - or any file within the `.west` folder -  is not recommended, since some of _West's_ commands might no longer work as expected.

_"west/config"_ sounds familiar, doesn't it? If you've been following this article series, you might remember that we already encountered the `west config` command in the very [first article](https://interrupt.memfault.com/blog/practical_zephyr_basics): We used the command "`west config build.board nrf52840dk/nrf52840`" to configure the _board_ for our build so that we didn't have to pass it as an argument to `west build` anymore. This does sound suspiciously similar to _"west/config"_!

Let's try and see how `west config` affects our workspace and `.west/config`:

```bash
workspace/app $ west config build.board nrf52840dk/nrf52840
workspace/app $ cat ../.west/config
```

```ini
[manifest]
path = app
file = west.yml

[build]
board = nrf52840dk/nrf52840
```

Having initialized a _West workspace_, we can now see that `west config` by default uses this _local_ configuration file to store its configuration options. _West_ also supports storing configuration options globally or even system-wide. Have a look at the  [official documentation](https://docs.zephyrproject.org/latest/develop/west/config.html) in case you need to know more.

Let's get rid of the configuration option and finally run [`west update`](https://docs.zephyrproject.org/latest/develop/west/basics.html#west-init-and-west-update) as suggested by the output we got in our call to `west init`:

```bash
workspace/app $ west config -d build.board
workspace/app $ cd ../
workspace $ west update
workspace $ # nothing happens
```

Huh, that was disappointing. `west update` didn't do anything - feel free to check your files, nothing changed! The reason for that is quite simple: With `west init` we already took care of initializing the workspace. Since we don't have any external dependencies to manage, we have no work for `west update`.
