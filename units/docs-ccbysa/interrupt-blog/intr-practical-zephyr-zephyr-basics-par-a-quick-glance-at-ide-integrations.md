---
id: "intr-practical-zephyr-zephyr-basics-par-a-quick-glance-at-ide-integrations"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1): A quick glance at IDE integrations"
summary: "In the prerequisites, we've promised that we won't have a detailed look at IDEs - and we won't. In this section, we'll just have a look at VS Code and some information that is relevant for any type of editor."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics#a-quick-glance-at-ide-integrations"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the [prerequisites](#prerequisites), we've promised that we won't have a detailed look at IDEs - and we won't. In this section, we'll just have a look at `VS Code` and some information that is relevant for any type of editor. Let's start with the editor-independent information:

Zephyr configures CMake to export a _compilation database_ and thus produces a `compile_commands.json` file in the build directory:

`zephyr/cmake/modules/kernel.cmake`
```cmake
set(CMAKE_EXPORT_COMPILE_COMMANDS TRUE CACHE BOOL
    "Export CMake compile commands. Used by gen_app_partitions.py script"
    FORCE
)
```

This compilation database essentially contains the commands that are used for each and every file that is compiled in the project. The database is not only used by tools such as [`clang-tidy`](https://clang.llvm.org/extra/clang-tidy) but also by IDEs and their extensions, e.g., to resolve include paths.

E.g., `VS Code` has a [C/C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools), which can be configured to pick up the provided compilation database as follows in `VS Code`'s [`settings.json`](https://github.com/lmapii/practical-zephyr/blob/main/.vscode/settings.json):

`.vscode/settings.json`
```json
{
  "C_Cpp.default.compileCommands": "build/compile_commands.json",
}
```

If you like `VS Code` and use [Nordic](https://www.nordicsemi.com/)'s MCUs, you can also have a look at their [extension pack](https://nrfconnect.github.io/vscode-nrf-connect/), which comes with a graphical *devicetree* and *KConfig* extension, debugging support, and much more:



> **Note:** Personally, I do not use the full extension pack since one key reason for using Zephyr is being able to use MCUs from _any_ supported vendor. I also tend to stick to the command line since I want to understand the process and do not rely on buttons in an IDE. Also, the extension pack somewhat conflicts with the very popular CMake extension [`ms-vscode.cmake-tools`](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools). But in general, [Nordic](https://www.nordicsemi.com/) did a great job of providing an easy way to develop applications with their extension pack. My only hope would be, that they'll make the *Kconfig* and *devicetree* extensions usable without the full extension pack.

And that's it about IDE integrations! Ok, almost, we'll still see them every now and then in the article series.
