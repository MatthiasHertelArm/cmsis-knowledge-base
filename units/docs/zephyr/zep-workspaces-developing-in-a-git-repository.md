---
id: "zep-workspaces-developing-in-a-git-repository"
type: "concept"
domain: "project"
title: "Workspaces: Developing in a git repository"
summary: "west \"projects\" in a workspace are ordinary git repositories."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/workspaces.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/workspaces.rst"
license: "Apache-2.0"
mode: "V"
---

`west` "projects" in a workspace are ordinary git repositories. Left to
itself, west only creates and updates the `manifest-rev` branch and the refs
under `refs/west/`; the branches you create are yours, and west only rebases
them when you ask it to with `west update --rebase`.

That is also why a plain west update leaves you on a
detached `HEAD`: it checks out the new `manifest-rev` and leaves your
branches exactly where they are. See west-update-detached-heads for the
rationale.


**Note:** Zephyr *modules* and west projects are not the same thing, even though west projects are often also modules; see modules-vs-projects. The git workflow below applies to all west projects whether they are Zephyr modules or not.

A workflow which works well when you have local changes is:

#. Create a branch in the repository and commit to it as usual:

```console

git -C <repository-path> switch --create <your-branch>
```
#. Update your workspace with `west update --rebase`, then look at what
   changed:

```console

west update --rebase
west compare
```
   Your branch stays checked out and is rebased onto the new `manifest-rev`.
   This is the only time west touches your own branch. If it conflicts, the
   command fails and you resolve it with git as usual.

#. If you would rather not have west rebase your branch, a plain
   `west update` will switch away from it instead (unless this causes git
   conflicts). `west update --keep-descendants` is a third option which
   never fails. See the `checked out branch behavior` option group in
   `west update --help`, and west-update for all the details.


### Committing on a detached `HEAD`


Do not commit on a detached `HEAD` left behind by `west update`: git warns
you that those commits are not reachable from any branch and they may be
garbage-collected later. Create a branch for your work instead; or use an
alternative git client purposely designed for "branchless" work, like for
instance JJ.
