---
id: "ceed-tools-ceedling-tool-definitions"
type: "concept"
domain: "test"
title: "`:tools`: Ceedling tool definitions"
summary: "Contained in this section are details on Ceedling’s default tool definitions. For sake of space, the entirety of a given definition is not shown."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/tools.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/tools/#ceedling-tool-definitions"
license: "MIT"
mode: "V"
---

Contained in this section are details on Ceedling’s default tool definitions.
For sake of space, the entirety of a given definition is not shown. If you need
to get in the weeds or want a full example, see the file `defaults.rb` in
Ceedling’s lib/ directory.

### Tool definition overview

Listed below are the built-in tool names, corresponding to build steps along
with the numbered parameters that Ceedling uses to fill out a full command line
for the named tool. The full list of fundamental elements for a tool definition
are documented in the sections that follow along with examples.

Not every numbered parameter listed immediately below must be referenced in a
Ceedling tool definition. If `${4}` isn't referenced by your custom tool,
Ceedling simply skips it while expanding a tool definition into a command line.

The numbered parameters below are references that expand / are replaced with
actual values when the corresponding command line is constructed. If the values
behind these parameters are lists, Ceedling expands the containing reference
multiple times with the contents of the value. A conceptual example is
instructive…

### Simplified tool definition / expansion example

A partial tool definition:

```yaml
:tools:
   :power_drill:
      :executable: dewalt.exe
      :arguments:
         - "--X${3}"
```

Let’s say that `${3}` is a list inside Ceedling, `[2, 3, 7]`. The expanded tool
command line for `:tools` ↳ `:power_drill` would look like this:

```shell
 > dewalt.exe --X2 --X3 --X7
```
