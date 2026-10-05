---
id: "ceed-dependencies-environment-variables"
type: "concept"
domain: "test"
title: "Dependencies: Environment Variables"
summary: "Many build systems support customization through environment variables. By specifying an array of environment variables, the Dependencies plugin will customize the shell environment before calling the build process."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#environment-variables"
license: "MIT"
mode: "V"
---

Many build systems support customization through environment variables. By specifying
an array of environment variables, the Dependencies plugin will customize the shell environment 
before calling the build process.

Note that Ceedling’s project configuration includes a top-level `:environment` sections itself.
The top-level `:environment` section is for all of Ceedling. The `:environment` section nested 
within a specific dependency’s configuration is only for the shell environment used to process
that dependency. The format and abilities of the two `:environment` configuration sections are
also different.

Environment variables may be specified in three ways. Let’s look at one of each:

```yaml
:dependencies:
  <a dependency configuration>:
    :environment:
      - ARCHITECTURE=ARM9
      - CFLAGS+=-DADD_AWESOMENESS
      - CFLAGS-=-DWASTE
```

In the first example, you see the most straightforward method. The environment variable
`ARCHITECTURE` is set to the value `ARM9`. That’s it. Simple.

The next two options modify an existing symbol. In the first one, we use `+=`, which tells
Ceedling to add the define `ADD_AWESOMENESS` to the environment variable `CFLAGS`. The second
tells Ceedling to remove the define `WASTE` from the same environment variable.

There are a couple of things to note here.

First, when adding to a variable, Ceedling has no way of knowing
what delimiter you are expecting. In this example you can see we manually added some whitespace.
If we had been modifying `PATH` instead, we might have had to use a `:` on a unux or `;` on
Windows.

Second, removing an argument will have no effect on the argument if that argument isn't found
precisely. It’s case sensitive and the entire string must match. If symbol doesn't already exist,
it WILL after executing this command... however it will be assigned to nothing.
