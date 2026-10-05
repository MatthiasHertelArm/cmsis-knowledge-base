---
id: "zep-configuration-built-in-configuration-options"
type: "concept"
domain: "project"
title: "Configuration: Built-in Configuration Options"
summary: "The following table documents configuration options supported by west's built-in commands. Configuration options supported by Zephyr's extension commands are documented in the pages for those commands."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/config.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/config.rst"
license: "Apache-2.0"
mode: "V"
---

The following table documents configuration options supported by west's
built-in commands. Configuration options supported by Zephyr's extension
commands are documented in the pages for those commands.

.. NOTE: docs authors: keep this table sorted by section, then option.


* - Option
  - Description
* - `alias.{ALIAS}`
  - String. If non-empty the `<ALIAS>` can be used as a west command.
    See west-aliases.
* - `color.ui`
  - Boolean. If `true` (the default), then west output is colorized when
    stdout is a terminal.
* - `commands.allow_extensions`
  - Boolean, default `true`, disables west-extensions if `false`
* - `grep.color`
  - String, default empty. Set this to `never` to disable `west grep`
    color output. If set, `west grep` passes the value to the grep tool's
    `--color` option.
* - `grep.tool`
  - String, one of `"git-grep"` (default), `"ripgrep"`, or `"grep"`.
    The grep tool that `west grep` should use.
* - `grep.<TOOL>-args`
  - String, default empty. The `<TOOL>` part is a pattern that can be any
    `grep.tool` value, so `grep.ripgrep-args` is an example
    configuration option. If set, arguments that `west grep` should pass
    to the corresponding grep tool. Run `west help grep` for details.
* - `grep.<TOOL>-path`
  - String, default empty. The `<TOOL>` part is a pattern that can be any
    `grep.tool` value, so `grep.ripgrep-path` is an example
    configuration option. The path to the corresponding tool that ``west
    grep` should use instead of searching for the command. Run `west help
    grep`` for details.
* - `manifest.file`
  - String, default `west.yml`. Relative path from the manifest repository
    root directory to the manifest file used by `west init` and other
    commands which parse the manifest.
* - `manifest.group-filter`
  - String, default empty. A comma-separated list of project groups to
    enable and disable within the workspace. Prefix enabled groups with
    `+` and disabled groups with `-`. For example, the value
    `"+foo,-bar"` enables group `foo` and disables `bar`. See
* - `manifest.path`
  - String, relative path from the `west workspace` root directory
    to the manifest repository used by `west update` and other commands
    which parse the manifest. Set locally by `west init`.
* - `manifest.project-filter`
  - Comma-separated list of strings.

    The option's value is a comma-separated list of regular expressions,
    each prefixed with `+` or `-`, like this:

    .. code-block:: none

       +re1,-re2,-re3

    Project names are matched against each regular expression (`re1`,
    `re2`, `re3`, ...) in the list, in order. If the entire project name
    matches the regular expression, that element of the list either
    deactivates or activates the project. The project is deactivated if the
    element begins with `-`. The project is activated if the element
    begins with `+`. (Project names cannot contain `,` if this option is
    used, so the regular expressions do not need to contain a literal `,`
    character.)

    If a project's name matches multiple regular expressions in the list,
    the result from the last regular expression is used. For example,
    if `manifest.project-filter` is:

    .. code-block:: none

       -hal_.*,+hal_foo

    Then a project named `hal_bar` is inactive, but a project named
    `hal_foo` is active.

    If a project is made inactive or active by a list element, the project
    is active or not regardless of whether any or all of its groups are
    disabled. (This is currently the only way to make a project that has no
    groups inactive.)

    Otherwise, i.e. if a project does not match any regular expressions in
    the list, it is active or inactive according to the usual rules related
    to its groups (see west-project-group-examples for examples in
    that case).

    Within an element of a `manifest.project-filter` list, leading and
    trailing whitespace are ignored. That means these example values
    are equivalent:

    .. code-block:: none

       +foo,-bar
       +foo , -bar

    Any empty elements are ignored. That means these example values are
    equivalent:

    .. code-block:: none

        +foo,,-bar
        +foo,-bar

* - `update.auto-cache`
  - String. If non-empty, `west update` will use its value as the
    `--auto-cache` option's value if not given on the command line.
* - `update.fetch`
  - String, one of `"smart"` (the default behavior starting in v0.6.1) or
    `"always"` (the previous behavior). If set to `"smart"`, the
    from project remotes when those projects' revisions in the manifest file
    are SHAs or tags which are already available locally. The `"always"`
    behavior is to unconditionally fetch from the remote.
* - `update.name-cache`
  - String. If non-empty, `west update` will use its value as the
    `--name-cache` option's value if not given on the command line.
* - `update.narrow`
  - Boolean. If `true`, `west update` behaves as if `--narrow` was
    given on the command line. The default is `false`.
* - `update.path-cache`
  - String. If non-empty, `west update` will use its value as the
    `--path-cache` option's value if not given on the command line.
* - `update.sync-submodules`
  - Boolean. If `true` (the default), west-update will synchronize
    Git submodules before updating them.
* - `zephyr.base`
  - String, default value to set for the `ZEPHYR_BASE` environment
    variable while the west command is running. By default, this is set to
    the path to the manifest project with path `zephyr` (if there is
    one) during `west init`. If the variable is already set, then this
    setting is ignored unless `zephyr.base-prefer` is `"configfile"`.
* - `zephyr.base-prefer`
  - String, one the values `"env"` and `"configfile"`. If set to
    `"env"` (the default), setting `ZEPHYR_BASE` in the calling
    environment overrides the value of the `zephyr.base` configuration
    option. If set to `"configfile"`, the configuration option wins
    instead.
