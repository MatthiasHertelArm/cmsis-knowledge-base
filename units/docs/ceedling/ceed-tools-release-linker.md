---
id: "ceed-tools-release-linker"
type: "concept"
domain: "test"
title: "`:tools`: `:release_linker`"
summary: "To accomplish useful work on multiple files, a configured tool will most often require that some number of its arguments or even the executable itself change for each run."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/tools.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/tools/#release-linker"
license: "MIT"
mode: "V"
---

Linker for release source code

- `${1}`: input objects
- `${2}`: output binary
- `${3}`: optional output map
- `${4}`: optional library list
- `${5}`: optional library path list

**Default**: `gcc`

### Tool definition configurable elements

1. `:executable` - Command line executable (required).

    !!! tip "Spaces in an executable name"
        If an executable contains a space (e.g. `Code Cruncher`), and the
        shell executing the command line generated from the tool definition needs
        the name quoted, add escaped quotes in the YAML:

        ```yaml
        :tools:
          :test_compiler:
            # YAML explicitly requires the outer quotation marks.
            # The command line requires the inner escaped quotation marks.
            :executable: "\"Code Cruncher\""
        ```

1. `:arguments` - List (array of strings) of command line arguments and
    substitutions (required).

1. `:name` - Simple name (i.e. "nickname") of tool beyond its executable name.
   This is optional. If not explicitly set then Ceedling will form a name from
   the tool’s YAML entry key.

1. `:stderr_redirect` - Control of capturing `$stderr` messages
    {`:none`, `:auto`, `:win`, `:unix`, `:tcsh`}.
    Defaults to `:none` if unspecified. You may create a custom entry by
    specifying a simple string instead of any of the recognized symbols. As an
    example, the `:unix` symbol maps to the string `2>&1` that is automatically
    inserted at the end of a command line.

    !!! warning "`$stderr` is rarely necessary"
        Originally, `$stderr` redirection was often needed in early versions of 
        Ceedling. Shell output stream handling is now automatically handled. 
        This option is preserved for possible edge cases.

1. `:optional` - By default a tool you define is required for operation. This
   means a build will be aborted if Ceedling cannot find your tool’s executable
   in your environment. However, setting `:optional` to `true` causes this
   check to be skipped. This is most often needed in plugin scenarios where a
   tool is only needed if an accompanying configuration option requires it. In
   such cases, a programmatic option available in plugin Ruby code using the
   Ceedling class `ToolValidator` exists to process tool definitions as needed.

### Tool element runtime substitution

To accomplish useful work on multiple files, a configured tool will most often
require that some number of its arguments or even the executable itself change
for each run. Consequently, every tool’s argument list and executable field
possess two means for substitution at runtime.

Ceedling provides inline Ruby string expansion and a notation for populating
tool elements with dynamically gathered values within the build environment.

#### Tool element runtime substitution: Inline Ruby string expansion

`"#{...}"`: This notation is that of the beloved
[inline Ruby string expansion][inline-ruby-string-expansion] available in a
variety of configuration file sections. This string expansion occurs each time
a tool configuration is executed during a build.

#### Tool element runtime substitution: Notational substitution

A Ceedling tool’s other form of dynamic substitution relies on a `$` notation.
These `$` operators can exist anywhere in a string and can be decorated in any
way needed. To use a literal `$`, escape it as `\\$`.

* `$`: Simple substitution for value(s) globally available within the runtime
  (most often a string or an array).

* `${#}`: When a Ceedling tool’s command line is expanded from its configured
  representation, runs of that tool will be made with a parameter list of
  substitution values. Each numbered substitution corresponds to a position in
  a parameter list.

    * In the case of a compiler `${1}` will be a C code file path, and `${2}`
     will be the file path of the resulting object file.

    * For a linker `${1}` will be an array of object files to link, and `${2}`
     will be the resulting binary executable.

    * For an executable test fixture `${1}` is either the binary executable
     itself (when using a local toolchain such as GCC) or a binary input file
     given to a simulator in its arguments.
