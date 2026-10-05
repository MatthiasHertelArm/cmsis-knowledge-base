---
id: "ceed-dependencies-fetching-dependencies"
type: "concept"
domain: "test"
title: "Dependencies: Fetching Dependencies"
summary: "The :dependencies plugin supports the ability to automatically fetch your dependencies for you... using some common methods of fetching source. This section contains only a couple of fields:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#fetching-dependencies"
license: "MIT"
mode: "V"
---

The `:dependencies` plugin supports the ability to automatically fetch your dependencies
for you... using some common methods of fetching source. This section contains only a
couple of fields:

- `:method` -- This is the method that this dependency is fetched.
    - `:none` -- This tells Ceedling that the code is already included in the project.
    - `:zip` -- This tells Ceedling that we want to unpack a zip file to our source path.
    - `:gzip` -- This tells Ceedling that we want to unpack a gzip file to our source path.
    - `:git` -- This tells Ceedling that we want to clone a git repo to our source path.
    - `:svn` -- This tells Ceedling that we want to checkout a subversion repo to our source path.
    - `:custom` -- This tells Ceedling that we want to use a custom command or commands to fetch the code.
- `:source` -- This is the path or url to fetch code when using the `:zip`, `:gzip` or `:git` method.
- `:tag`/`:branch` -- This is the specific tag or branch that you wish to retrieve (`:git` only, optional).
- `:hash` -- This is the specific SHA1 hash you want to fetch (`:git` only, optional and triggers a deep clone).
- `:revision` -- This is the specific revision you want to fetch (`:svn` only, optional).
- `:executable` -- This is a YAML list of commands to execute when using the `:custom` method

Some notes:

* The `:source` location for fetching a `:zip` or `:gzip` file is relative to the `:paths` ↳ `:source`
folder.
