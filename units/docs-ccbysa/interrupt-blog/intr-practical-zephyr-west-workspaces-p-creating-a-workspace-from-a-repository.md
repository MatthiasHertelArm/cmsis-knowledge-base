---
id: "intr-practical-zephyr-west-workspaces-p-creating-a-workspace-from-a-repository"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Creating a workspace from a repository"
summary: "In Zephyr's official documentation for West, the first example call to west init uses the -m argument to specify the manifest repository's URL."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#creating-a-workspace-from-a-repository"
license: "CC-BY-SA-4.0"
mode: "V"
---

In Zephyr's official documentation for _West_, the first example call to `west init` uses the `-m` argument to specify the manifest repository's URL. In the previous section, we've seen how we can _create_ such a manifest repository and how to use `west init --local` to initialize the workspace _locally_.

Instead of initializing a workspace _locally_, let's use the manifest file and repository that we've created in the previous section and initialize the workspace from scratch using its remote URL. Let's fire up a new terminal (I'll be installing _West_ again in a virtual environment) and get started right away:

```bash
$ mkdir workspace-m
$ cd workspace-m

workspace-m $ west init -m git@github.com:lmapii/practical-zephyr-t2-empty-ws.git
=== Initializing in /path/to/workspace-m
--- Cloning manifest repository from git@github.com:lmapii/practical-zephyr-t2-empty-ws.git
Cloning into '/path/to/workspace-m/.west/manifest-tmp'...
...
--- setting manifest.path to practical-zephyr-t2-empty-ws.git
=== Initialized. Now run "west update" inside /path/to/workspace-m.

workspace-m $ tree --charset=utf-8 --dirsfirst -a -L 2
.
├── .west
│   └── config
├── practical-zephyr-t2-empty-ws.git
│   ├── .git
│   └── west.yml
├── Pipfile
└── Pipfile.lock
```

Notice that we no longer specify the current directory in the call to `west init` using "`.`". In fact, the directory - optionally passed as the last argument to `west init` - is interpreted **differently** by _West_ when using the `--local` flag or the `-m` arguments:

- With `--local`, the _directory_ specifies the path to the local manifest repository.
- Without the `--local` flag, the _directory_ refers to the _topdir_ and thus the folder in which to create the workspace (defaulting to the current working directory in this case).

Awkward, but this approach is probably used due to legacy reasons. If no `--local` flag is used and no repository is specified using `-m`, _West_ defaults to using the Zephyr repository.

The file tree, however, isn't exactly what we wanted ... `west init` created a folder `practical-zephyr-t2-empty-ws.git` instead of the folder called `app` that we've had before. Well, there's no way for _West_ to know that we want the manifest repository to use the folder name `app`, so it uses the repository's name instead. How can we change that?


### Updating the manifest repository path

The manifest file uses the key `manifest.self` for configuring the manifest repository itself, meaning that all settings in the `manifest.self` key are only applied to the manifest repository. The key `manifest.self.path` can be used to specify the path that _West_ uses when cloning the manifest repository, relative to the _West_ workspace _topdir_.

Let's update the `west.yml` file in the folder that `west init` cloned for us as follows:

`practical-zephyr-t2-empty-ws.git/west.yml`

```yaml
manifest:
  version: 1.2

  # Entries in the `self` key are only applied to the _manifest repository_
  self:
    path: app

  projects:
    - name: doxygen-awesome
      url: https://github.com/jothepro/doxygen-awesome-css
      revision: main
      path: deps/utilities/doxygen-awesome-css
```

Don't forget to commit and push the change: We're passing a URL to `west init` so _West_ obviously won't pick up local changes during the workspace initialization.

To reinitialize the workspace, we **must** remove the `.west` folder, otherwise `west init` throws an error telling us that the workspace is already initialized:

```bash
workspace-m $ west init -m git@github.com:lmapii/practical-zephyr-t2-empty-ws.git
FATAL ERROR: already initialized in /path/to/workspace-m, aborting.
  Hint: if you do not want a workspace there,
  remove this directory and re-run this command:

  /path/to/workspace-m/.west
```

Let's follow the instructions and also remove `practical-zephyr-t2-empty-ws.git` before reinitializing the workspace:

```bash
workspace-m $ rm -rf .west practical-zephyr-t2-empty-ws.git
workspace-m $ west init -m git@github.com:lmapii/practical-zephyr-t2-empty-ws.git
=== Initializing in /path/to/workspace-m
...
--- setting manifest.path to app
=== Initialized. Now run "west update" inside /path/to/workspace-m.

workspace-m $ tree --charset=utf-8 --dirsfirst -a -L 2
.
├── .west
│   └── config
├── app
│   ├── .git
│   └── west.yml
├── Pipfile
└── Pipfile.lock
```

Now we can run `west update` and we end up with the same workspace as we got when initializing it locally:

```bash
workspace-m $ west update
=== updating doxygen-awesome (deps/utilities/doxygen-awesome-css):
--- doxygen-awesome: initializing
Initialized empty Git repository in /path/to/workspace-m/deps/utilities/doxygen-awesome-css/.git/
--- doxygen-awesome: fetching, need revision v2.2.1
...
HEAD is now at df83fbf fix rendering error in example class

workspace-m $ tree --dirsfirst -a -L 3 --filelimit 8
.
├── .west
│   └── config
├── app
│   ├── .git  [10 entries exceeds filelimit, not opening dir]
│   └── west.yml
├── deps
│   └── utilities
│       └── doxygen-awesome-css
├── Pipfile
└── Pipfile.lock
```


### Locally vs. remotely initialized workspaces

What is the difference between a _West workspace_ that has been initialized locally using the `--local` flag, or remotely by passing the URL of the manifest repository? As mentioned already, thankfully, the short answer is _none_.

The only difference is that for remotely initialized workspaces _West_ clones the repository for you and thus you essentially don't need to use `git clone` to obtain the manifest repo used to setup the workspace.

We can also see this in the configuration file `.west/config`:

```bash
workspace-m $ cat .west/config
```

```ini
[manifest]
path = app
file = west.yml
```

Just like for the locally initialized repository, the `[manifest]` section points to the manifest file in the `app` folder. Running `west update` therefore only checks the contents of the local manifest file. It won't try to pull new changes in the manifest repository and it also won't attempt to read the file from the remote.

If there were any changes to the manifest file in the repository, you'll have to `git pull` them in your manifest repository - which is a good thing. In fact, `west update` will never attempt to modify the manifest repository and also states this in the `--help` information for the `update` command:

> "This command does not alter the manifest repository's contents."
