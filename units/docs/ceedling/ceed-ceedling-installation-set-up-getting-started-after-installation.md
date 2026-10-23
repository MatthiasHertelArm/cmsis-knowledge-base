---
id: "ceed-ceedling-installation-set-up-getting-started-after-installation"
type: "concept"
domain: "test"
title: "Ceedling Installation & Set Up: Getting Started after installation"
summary: "Ceedling Installation & Set Up: Getting Started after installation"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/getting-started/installation.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/installation/#getting-started-after-installation"
license: "MIT"
mode: "V"
---

1. Certain advanced features of Ceedling rely on `gcc` as a preprocessing tool.
   In most Linux systems, the GNU Compiler Collection is already available.
   For Windows environments, we recommend [MinGW-w64](https://www.mingw-w64.org).
   MinGW-w64 is GCC and its tools built to produce native Windows executables.
   The easiest way to install it is through [MSYS2](https://www.msys2.org), a
   software distribution and package manager for Windows that provides current
   MinGW-w64 toolchains. This represents an optional, additional setup /
   installation step to complement the list above. Upon installing MinGW-w64
   ensure your system path is updated or set `:environment` ↳ `:path` in your
   project configuration (see `:environment` section).

1. Once Ceedling is installed, you'll want to start to integrate it with new
   and old projects alike. If you wanted to start to work on a new project
   named `foo`, Ceedling can create the skeleton of the project using `ceedling
   new foo `<destination>``. Likewise if you already have a project named `bar` 
   and you want to "inject" Ceedling into it, you would run `ceedling new bar 
   <destination>`, and Ceedling will create any files and directories it needs.

1. Now that you have Ceedling integrated with a project, you can start using it.
   A good starting point is to enable the [plugin](https://throwtheswitch.github.io/Ceedling/getting-started/installation/../plugins/index.md) 
   `module_generator` in your project configuration file and create a source +
   test code module to get accustomed to Ceedling by issuing the command 
   `ceedling 'module:create[name]'`.
