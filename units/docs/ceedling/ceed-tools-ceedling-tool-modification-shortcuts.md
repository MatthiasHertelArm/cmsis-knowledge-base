---
id: "ceed-tools-ceedling-tool-modification-shortcuts"
type: "concept"
domain: "test"
title: "`:tools`: Ceedling tool modification shortcuts"
summary: "Sometimes Ceedling’s default tool definitions are this close to being just what you need. But, darn, you need one extra argument on the command line, or you just need to hack the tool executable."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/tools.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/tools/#ceedling-tool-modification-shortcuts"
license: "MIT"
mode: "V"
---

Sometimes Ceedling’s default tool definitions are _this close_ to being just
what you need. But, darn, you need one extra argument on the command line, or
you just need to hack the tool executable. You'd love to get away without
overriding an entire tool definition just in order to tweak it.

We got you.

### Ceedling tool executable replacement

Sometimes you need to do some sneaky stuff. We get it. This feature lets you
replace the executable of a tool definition — including an internal default —
with your own.

To use this shortcut, simply add a configuration section to your project file
at the top-level, `:tools_<tool_to_modify>` ↳ `:executable`. Of course, you
can combine this with the following modification option in a single block for
the tool. Executable replacement can make use of
[inline Ruby string expansion][inline-ruby-string-expansion].

See the list of tool names at the beginning of the `:tools` documentation to
identify the named options. Plugins can also include their own tool definitions
that can be modified with this same option.

This example YAML...

```yaml
:tools_test_compiler:
   :executable: foo
```

... will produce the following:

```shell
 > foo <Ceedling default command line>
```

### Ceedling tool arguments addition shortcut

Now, this little feature only allows you to add arguments to the end of a tool
command line. Not the beginning. And, you can't remove arguments with this
option.

Further, this little feature is a blanket application across all uses of a
tool. If you need fine-grained control of command line flags in build steps per
test executable, please see the [`:flags` configuration documentation][flags].

To use this shortcut, simply add a configuration section to your project file
at the top-level, `:tools_<tool_to_modify>` ↳ `:arguments`. Of course, you can
combine this with the preceding modification option in a single block for the
tool.

See the list of tool names at the beginning of the `:tools` documentation to
identify the named options. Plugins can also include their own tool definitions
that can be modified with this same hack.

This example YAML...

```yaml
:tools_test_compiler:
   :arguments:
      - --flag # Add `--flag` to the end of all test C file compilation
```

... will produce the following (for the default executable):

```shell
 > gcc <Ceedling default command line> --flag
```

[inline-ruby-string-expansion]: ../project-file.md#inline-ruby-string-expansion
