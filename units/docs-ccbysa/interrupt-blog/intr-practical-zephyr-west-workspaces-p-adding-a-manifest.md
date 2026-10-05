---
id: "intr-practical-zephyr-west-workspaces-p-adding-a-manifest"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Creating a workspace from scratch / Adding a manifest"
summary: "Part of: Creating a workspace from scratch"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#adding-a-manifest"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Creating a workspace from scratch_

We now want to use _West_ to handle our dependencies: We really want to move on from using a global installation that may or will change at any time, and instead have all of our dependencies managed in our _workspace_. Zephyr evolves fast and it is therefore very important to have fixed versions of all modules and Zephyr's source code.

_West_ solves this by using a so-called [_manifest_ file](https://docs.zephyrproject.org/latest/develop/west/manifest.html), which is nothing else than a list of external dependencies - and then some. _West_ uses this manifest file to basically act like a package manager for your _C_ project, similar to what [`cargo`](https://doc.rust-lang.org/stable/cargo/) does with its `cargo.toml` files for [_Rust_](https://www.rust-lang.org/).

> **Note:** Please don't pin me down for comparing _West_ with _cargo_. I'm just trying to find some other description than "Swiss Army Knife".

> **Note:** The complete complete manifest repository used in this section is available on GitHub: [practical-zephyr-t2-empty-ws](https://github.com/lmapii/practical-zephyr-t2-empty-ws).

_West_ can also be used if you're _not_ planning to create a Zephyr project. In fact, let's start with a manifest file that doesn't include Zephyr at all. For that, we create the file `app/west.yml` in our `workspace` folder.

```bash
workspace $ mkdir app
workspace $ tree
.
├── app
│   └── west.yml
├── Pipfile
└── Pipfile.lock
```

The minimal content of our _manifest_ file is the following:

`app/west.yml`

```yaml
manifest:
  # lowest version of the manifest file schema that can parse this file’s data
  version: 1.2
```

Zephyr's [official documentation on West basics](https://docs.zephyrproject.org/latest/develop/west/basics.html) calls the `workspace` folder the "_topdir_" and our `app` folder the _manifest **repository**_: In an idiomatic workspace, the folder containing the manifest file is a direct sibling of the "topdir" or workspace root directory, and it is a `git` repository. The folder name `app` is just a personal preference.

> **Note:** I'm using the term "idiomatic" since there are multiple ways of setting up _West workspaces_. Placing your manifest file into a folder that is a direct sibling of the workspace is a _convention_. Nothing stops you from placing your manifest file in a different folder, e.g., deeper within your folder tree. This does, however, have some drawbacks since some of the _West_ commands, e.g., `west init`, are currently not very customizable, e.g., initializing a workspace using a repository and the `-m` argument won't work out-of-the-box.
>
> Feel free to experiment with your version of _West_. I'm sure there will be some changes in the future, but for now, we focus on the intended or "_idiomatic_" way of using _West_.

Let's initialize the repository for our `app` folder containing the manifest files:

```bash
workspace/app $ git init
Initialized empty Git repository in /path/to/workspace/app/.git/

workspace/app $ tree --dirsfirst -a -L 2 ../
../      # topdir
├── app  # manifest _repository_
│   ├── .git
│   └── west.yml  # manifest _file_
├── Pipfile
└── Pipfile.lock

workspace/app $ git remote add origin git@github.com:lmapii/practical-zephyr-t2-empty-ws.git
workspace/app $ git add --all
workspace/app $ git commit -m "initial commit"
workspace/app $ git push -u origin main
```
