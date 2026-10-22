---
id: "ceed-dependencies-fetching-dependencies"
type: "concept"
domain: "test"
title: "Dependencies: Fetching dependencies"
summary: "The plugin fetches a dependency with one of several common methods, configured under its :fetch:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#fetching-dependencies"
license: "MIT"
mode: "V"
---

The plugin fetches a dependency with one of several common methods, configured under its
`:fetch`:

- `:method`, the way this dependency is fetched:
    - `:none`: the code is already part of the project, so nothing is fetched.
    - `:zip`: unpack a zip archive into the fetch path.
    - `:tar_gzip`: unpack a gzipped tar archive into the fetch path.
    - `:git`: clone a git repository into the fetch path.
    - `:svn`: check out a Subversion repository into the fetch path.
    - `:custom`: run commands of your own in the fetch path.
- `:source`: the archive or repository to fetch from (`:zip`, `:tar_gzip`, `:git`, and
  `:svn`, all of which require it).
- `:tag` or `:branch`: the tag or branch to clone (`:git` only, optional). A tag wins
  when both are given.
- `:hash`: the commit to check out (`:git` only, optional). It makes a full clone rather
  than a shallow one, so the commit is available.
- `:revision`: the revision to check out (`:svn` only, optional).
- `:executable`: the list of commands to run (`:custom` only, required).

Fetching runs from inside the fetch path, so an archive `:source` given as a relative
path is relative to the fetch path.

A dependency is fetched once. Once its fetch path holds files, fetching it again, or
building it after a fetch, leaves those files alone. To fetch a fresh copy, clean the
dependency first with `dependencies:clean`.

The `:zip`, `:tar_gzip`, `:git`, and `:svn` methods use the plugin’s
[tools](#custom-tools) (`unzip`, `tar`, `git`, and `svn`). Each is checked just before a
dependency fetches with it, so a missing tool stops only that fetch, and a machine that
never fetches, such as a CI agent working from fetched dependencies, needs none of them.
