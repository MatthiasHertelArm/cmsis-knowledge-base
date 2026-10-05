---
id: "ceed-mixins-designing-for-mixins-merge-rules"
type: "concept"
domain: "test"
title: "Mixins: Designing for Mixins merge rules"
summary: "Merging of any sort tends to be hard to do well. It’s tricky at a code-level, yes, but, just as importantly, merging can be hard to grasp in your head."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/mixins.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/mixins/#designing-for-mixins-merge-rules"
license: "MIT"
mode: "V"
---

Merging of any sort tends to be hard to do well. It’s tricky at a 
code-level, yes, but, just as importantly, merging can be hard to grasp in
your head.

The brief sections that follow provide an overview of our recommended
design approach and the merge rules at play.

!!! tip "Use `dumpconfig` to debug mixins"
    `ceedling dumpconfig` can be invaluable in developing and troubleshooting
    your mixins. The `dumpconfig` application command will load your mixins
    just as a build would but produce the resulting merged configuration for
    inspection in a YAML file you specify.

### Additive Mixin merges

Generally speaking, the simplest way to conceive of managing your project
configuration with mixins is to design for an additive merge. This means
each mixin is successively adding something to your base configuration. 
In certain scenarios it is possible to overwrite configuration values with 
mixin values (see the rules that follow), but an additive merge is 
probably easier to understand and create.

At a high level, additive merges can be constructed like this:

1. Plan to add to lists with mixins. Path collections, plugins, and 
   tool flags & compilation symbols are all examples of lists that
   can be added to. Other lists exist in a project configuration too —
   many within containing configuration entries. Add paths, plugins, and 
   flags & symbols to your base configuration that are in common to all 
   your buid variations and then customize the lists by adding to them 
   with mixins.
1. Leave entire sections in your base configuration blank and fill them 
   out by merging mixins. With this strategy, you might configure all
   the basics in a base project configuration but merge into it the 
   path collections, tool configurations, and compilation symbols you need
   for a specific project.

### Mixins deep merge rules

Mixins are merged in a specific order. See the documentation sections 
following the examples for details.

Smooshing of mixin configurations into the base project configuration
follows a few basic rules.

#### New key/value pair

If a configuration key/value pair does not already exist at the time
of merging, the mixin key/value pair is added to the configuration.

#### Existing container (list or hash)

If a container — e.g. list or hash — already exists at the time of a
merge, the contents are _combined_.

##### Hash merge

A hash (key/value pairs) merge is straightforward. The key/value pairs
are intermingled at the same level.

##### List merge

A list merge is a bit more complex:

* When two lists are merged, the mixin’s entries are placed _before_ the
  existing list entries. This means higher-priority mixin content appears
  first in the combined list. For example, if a command line mixin and
  the base project configuration both add header search paths, the
  command line mixin paths come first in the resulting merged list. As
  such, ultimately, the mixin’s paths are searched first.
* If the existing configuration contains a list but the mixin value is a 
  different type, the mixin is treated as a one-element list and placed 
  before the existing list. The typical case is a list of strings growing 
  with an additional single string.

!!! note "An exception to the preceding — tool argument lists"
    In the case of tool argument lists (`:tools` ↳ `<tool name>` ↳ `:arguments`),
    mixin entries are placed _after_ the existing argument list entries 
    rather than before. Command line tools tend to process arguments 
    left-to-right such that a later occurrence of a flag takes precedence 
    (e.g. `-O0` after `-O2` overrides `-02`). Appending ensures that a 
    higher-priority mixin’s tool arguments override lower-priority 
    arguments by conforming to the typical CLI convention.

#### Existing simple value (boolean, string, numeric)

If a simple value already exists in the configuration at the time of
merging, that value is replaced by the mixin value being merged. Because
higher-priority mixins are merged last, the last write wins.

!!! info "Mixin merge order and list content order"
    Because mixin entries are placed _before_ existing list entries,
    higher-priority mixin content appears first in combined lists. For
    example, include search paths added by a command line mixin will be
    searched before those in an environment variable mixin, which will be
    searched before those in the project configuration file. See the
    section [Test build search paths](https://throwtheswitch.github.io/Ceedling/configuration/mixins/../testing-guide/conventions.md#test-build-search-paths)
    for more.
