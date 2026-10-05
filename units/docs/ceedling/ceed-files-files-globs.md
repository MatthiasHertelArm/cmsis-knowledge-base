---
id: "ceed-files-files-globs"
type: "concept"
domain: "test"
title: "`:files`: `:files` Globs"
summary: "Globs are effectively fancy wildcards. They are not as capable as full regular expressions but are easier to use. Various OSs and programming languages implement them differently."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/files.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/files/#files-globs"
license: "MIT"
mode: "V"
---

Globs are effectively fancy wildcards. They are not as capable as full regular
expressions but are easier to use. Various OSs and programming languages
implement them differently.

For a quick overview, see this [tutorial][globs-tutorial].

Ceedling supports globs so you can specify patterns of files as well as simple,
ordinary filepaths.

Ceedling `:files` globs operate identically to [Ruby globs][ruby-globs] except
that they ignore directory paths. Only filepaths are recognized.

Glob operators include the following: `*`, `**`, `?`, `[-]`, `{,}`.

* `*`
    * When used within a character string, `*` is simply a standard wildcard.
    * When used after a path separator, `/*` matches all subdirectories of depth
      1 below the parent path, not including the parent path.
* `**`: All subdirectories recursively discovered below the parent path, not
  including the parent path. This pattern only makes sense after a path
  separator `/**`.
* `?`: Single alphanumeric character wildcard.
* `[x-y]`: Single alphanumeric character as found in the specified range.
* `{x, y, ...}`: Matching any of the comma-separated patterns. Two or more
  patterns may be listed within the brackets. Patterns may be specific
  character sequences or other glob operators.
