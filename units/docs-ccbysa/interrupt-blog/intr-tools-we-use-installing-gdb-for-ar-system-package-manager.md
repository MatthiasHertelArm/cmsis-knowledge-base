---
id: "intr-tools-we-use-installing-gdb-for-ar-system-package-manager"
type: "concept"
domain: "debug"
title: "Tools we use: installing GDB for ARM: Details on each strategy / System package manager"
summary: "Depending on your host platform (Linux, Mac, Windows, \\BSD, etc), you may or may not have a built-in or defacto package manager. For example, on Linux, you may have one of:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-03-installing-gdb.md"
doc_source: "https://interrupt.memfault.com/blog/installing-gdb#system-package-manager"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Details on each strategy_

Depending on your host platform (Linux, Mac, Windows, \*BSD, etc), you may or
may not have a built-in or defacto package manager. For example, on Linux, you
may have one of:

- `apt-get` / `apt` (Debian, Ubuntu)
- `pacman` (Arch)
- `yum` (Red Hat)

Mac users will often install [homebrew](https://brew.sh/), since there is no
built-in package manager.

Windows users may use something like [chocolately](https://chocolatey.org/) or
the recent
[winget](https://docs.microsoft.com/en-us/windows/package-manager/winget/) tool.

It's certainly convenient to be able to do something as simple as this to
acquire a version of `gdb` compatible with arm targets:

```bash
❯ sudo apt install gdb-multiarch
```

On Linux, those `gdb-multiarch` packages usually have a _lot_ of supported
targets. On my Ubuntu 22.04 machine, it's **214** supported targets!

(the `sed` one-liner is from [below](#build-from-source))

```bash
# using the one liner from below to list supported targets
❯ gdb-multiarch --batch -nx --ex 'set architecture' 2>&1 | tail -n 1 | sed 's/auto./\n/g' | sed 's/,/\n/g' | sed 's/Requires an argument. Valid arguments are/\n/g' | sed '/^[ ]*$/d' | sort | uniq | wc -l

214
```

Of course, it's only important that the targets we're interested in are
supported.

There are a few downsides to using a package manager to install the tools:

- you are at the mercy of the available packages (or you need to create and
  maintain a package, which is probably more difficult than a normal from-source
  build!)
- available versions could be pulled from registries for no reason, leaving your
  environment stranded
- bugs in package versions might be difficult to deal with, since packages may
  not be updated frequently
- package managers are usually host-specific (homebrew does support some Linux
  packages though!), which means if your development team is using different
  host machines, it may be difficult to standardize on one set of tools
