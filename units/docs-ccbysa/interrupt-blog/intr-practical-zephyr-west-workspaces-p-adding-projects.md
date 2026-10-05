---
id: "intr-practical-zephyr-west-workspaces-p-adding-projects"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Creating a workspace from scratch / Adding projects"
summary: "Part of: Creating a workspace from scratch"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#adding-projects"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Creating a workspace from scratch_

In your manifest file, you can use the `manifest.projects` key to define all Git repositories that you want to have in your workspace. Let's say that we're planning to use a more modern [doxygen](https://doxygen.nl/) documentation for our project and therefore want to add [Doxygen Awesome](https://github.com/jothepro/doxygen-awesome-css) to our workspace. We can add this external dependency as an entry in the `manifest.projects` key of our manifest file:

`app/west.yml`

```yaml
manifest:
  version: 1.2

  projects:
    - name: doxygen-awesome
      url: https://github.com/jothepro/doxygen-awesome-css
      # you can also use SSH instead of HTTPS:
      # url: git@github.com:jothepro/doxygen-awesome-css.git
      revision: main
      path: deps/utilities/doxygen-awesome-css
```

Every _project_ at least has a **unique** name. Typically, you'll also specify the `url` of the repository, but there are several options, e.g., you could use the [`remotes` key](https://docs.zephyrproject.org/latest/develop/west/manifest.html#remotes) to specify a list of URLs and add specify the `remote` that is used for your project. You can find examples and a detailed explanation of all available options in the [official documentation for the `projects` key](https://docs.zephyrproject.org/latest/develop/west/manifest.html#projects).

With the `revision` key you can tell _West_ to check out either a specific _branch_, _tag_, or commit hash. Without specifying the `revision`, at the time of writing _West_ defaults to the `master` branch. Since [Doxygen Awesome](https://github.com/jothepro/doxygen-awesome-css) uses `main` as a development branch, we have to specify it explicitly.

The `path` key is also an optional key that tells _West_ the _relative_ path to the _topdir_ that it should use when cloning the project. Without specifying the `path`, _West_ uses the project's `name` as the path. Notice that you're **not** allowed to specify a path that is outside of the _topdir_ and thus _West_ workspace.

With that project added, we finally have some work for `west update`:

```bash
workspace $ west update
=== updating doxygen-awesome (deps/utilities/doxygen-awesome-css):
--- doxygen-awesome: initializing
Initialized empty Git repository in /path/to/workspace/deps/utilities/doxygen-awesome-css/.git/
--- doxygen-awesome: fetching, need revision main
...
HEAD is now at 8cea9a0 security: fix link vulnerable to reverse tabnabbing (#127)
```

Great! Now _West_ populated our dependencies and we have [Doxygen Awesome](https://github.com/jothepro/doxygen-awesome-css) available in the specified `path`:

```bash
workspace $ tree --dirsfirst -a -L 3 --filelimit 8
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

The folder name `deps` is again just a personal choice. I have borrowed this convention from Mike Szczys' talk ["Manifests: Project Sanity in the Ever-Changing Zephyr World"](https://www.youtube.com/watch?v=PVhu5rg_SGY) from the 2022 Zephyr Developer Summit, and we'll see why it makes sense to collect your dependencies in just a bit.

In our manifest file, we specified that we want to use the `main` branch for the `doxygen-awesome` project. This kind of defeats the purpose of using a manifest to create a stable workspace since we'll always be checking out the latest version of the repository when using `west update`. Instead, you'll typically either specify a _tag_ or even a specific commit in the revision.

At the time of writing, the tag `v2.2.1` was the latest release available for `doxygen-awesome`, pointing at the commit with the shortened hash `df83fbf`. Let's update the manifest to use the latest tag:

`app/west.yml`

```yaml
manifest:
  version: 1.2

  projects:
    - name: doxygen-awesome
      url: https://github.com/jothepro/doxygen-awesome-css
      revision: v2.2.1
      path: deps/utilities/doxygen-awesome-css
```

Running `west update` changes our dependency to the specified revision:

```bash
workspace $  west update
=== updating doxygen-awesome (deps/utilities/doxygen-awesome-css):
Warning: you are leaving 2 commits behind, not connected to
any of your branches:

  8cea9a0 security: fix link vulnerable to reverse tabnabbing (#127)
  00a52f6 Makefile: install -tabs.js as well (#122)

If you want to keep them by creating a new branch, this may be a good time
to do so with:

 git branch <new-branch-name> 8cea9a0

HEAD is now at df83fbf fix rendering error in example class
```

Looks like the `main` branch was already two commits ahead of the specified revision!

_West_ thus takes care of all the projects that we're using. We can, in fact, delete the entire `deps` repository and run `west update` again, and it'll simply put it back into its specified state. This is also the reason why it makes sense to group external dependencies, e.g., into this `deps` folder (full credits to Mike Szczys and [Golioth](https://golioth.io/)): Whenever you're not working on this project anymore, you can simply delete the `deps` and `.west` folders to save disk space (as soon as we'll add Zephyr this becomes a significant amount of disk space). Once you pick it up again, simply run `west init` and `west update` and you're ready to go.

> **Note:** More complex applications include lots of _projects_ in their manifest hierarchy. Having a single dependency folder `deps` can also help in your CI builds: E.g., with GitHub actions you can _cache_ your dependency folder and thereby significantly reduce the time required to run `west update`. The GitHub action used by the [practical-zephyr-manifest-repository](https://github.com/lmapii/practical-zephyr-manifest-repository/blob/main/.github/workflows/ci.yml) that we'll create later in this article uses such a cache for demonstration purposes. Noah Pendleton wrote an [excellent article](https://interrupt.memfault.com/blog/ncs-github-actions) about GitHub actions for NCS applications.

Whatever project structure you're using, however, is entirely up to you and always subject to personal preference.
