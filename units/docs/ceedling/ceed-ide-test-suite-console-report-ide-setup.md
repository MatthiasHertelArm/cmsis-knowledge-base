---
id: "ceed-ide-test-suite-console-report-ide-setup"
type: "concept"
domain: "test"
title: "IDE Test Suite Console Report: IDE Setup"
summary: "An IDE reads only output it captures. Run Ceedling from within the IDE, as a build, task, or tool, as each section below describes."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/report-tests-ide-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-ide-stdout/#ide-setup"
license: "MIT"
mode: "V"
---

An IDE reads only output it captures. Run Ceedling from within the IDE, as a build,
task, or tool, as each section below describes.

### Eclipse CDT

Eclipse CDT finds problems by matching build output against regular expressions.
Its GCC error parser reads this plugin’s default lines.

1. Use a Makefile project that runs Ceedling as its build. In _Project Properties_ ↳
   _C/C++ Build_ ↳ _Builder Settings_, clear _Use default build command_ and set the
   build command to `ceedling`. On the _Behavior_ tab, set the build target to
   `test:all`.
1. In _C/C++ Build_ ↳ _Settings_ ↳ _Error Parsers_, enable _GNU gcc/g++ Error Parser_.
1. Build the project. Failed tests appear in the _Problems_ view as errors, and
   ignored tests as warnings.

Eclipse reads output only from builds. Ceedling run in a terminal or as an
external tool creates no Eclipse problems to be matched and linked.

Eclipse checks a few special-purpose patterns before its error pattern. A failure
message containing the words _required from_ or _instantiated from_ appears as
information rather than an error.

### VS Code

VS Code reads problems from a task’s output through a problem matcher. The C/C++
extension supplies a `$gcc` matcher that reads this plugin’s default lines.

Add a task to `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Ceedling: test all",
      "type": "shell",
      "command": "ceedling test:all",
      "problemMatcher": "$gcc",
      "group": "test"
    }
  ]
}
```

Without the C/C++ extension, give the task its own matcher:

```json
"problemMatcher": {
  "owner": "ceedling",
  "fileLocation": ["autoDetect", "${workspaceFolder}"],
  "pattern": {
    "regexp": "^(.*?):(\\d+):(\\d+):\\s+(warning|error):\\s+(.*)$",
    "file": 1,
    "line": 2,
    "column": 3,
    "severity": 4,
    "message": 5
  }
}
```

This matcher reads relative paths against the workspace folder. If your project
sits in a folder below the workspace’s root, use `:absolute_paths: TRUE` with
either matcher.

VS Code’s terminal also links `file:line:column` text. Lines printed by Ceedling
in the integrated terminal can be clicked without any task.

#### Ceedling for VS Code

The [Ceedling for VS Code][vscode-ceedling] extension runs your test suite in VS
Code’s _Testing_ view. It reads test results from the
[Test Suite Report Log Factory](https://throwtheswitch.github.io/Ceedling/plugins/report-tests-ide-stdout/report-tests-log-factory.md) plugin’s `cppunit`
report, so enable that plugin and report too (note that more recent versions of
the extension enable this for you).

The extension can also add this plugin’s lines to the _Problems_ view. Its `gcc`
preset scans only `$stderr`, and this report prints to `$stdout`. Give it patterns
of its own that scan `$stdout`:

```json
"ceedlingExplorer.problemMatching": {
  "mode": "patterns",
  "patterns": [
    {
      "scanStdout": true,
      "severity": "error",
      "filePrefix": "${projectPath}",
      "regexp": "^(.*):(\\d+):(\\d+):\\s+error:\\s+(.*)$",
      "file": 1,
      "line": 2,
      "column": 3,
      "message": 4
    },
    {
      "scanStdout": true,
      "severity": "warning",
      "filePrefix": "${projectPath}",
      "regexp": "^(.*):(\\d+):(\\d+):\\s+warning:\\s+(.*)$",
      "file": 1,
      "line": 2,
      "column": 3,
      "message": 4
    }
  ]
}
```

These patterns also scan `$stderr`, as the extension’s patterns do by default, so
compiler errors and warnings appear too.

[vscode-ceedling]: https://marketplace.visualstudio.com/items?itemName=throw-the-switch.vscode-ceedling

### CLion

CLion links tool output to files through an External Tool’s output filters. Its
filters find only absolute paths.

1. Set `:format: :clion` in your project file.
1. In _Settings_ ↳ _Tools_ ↳ _External Tools_, add a tool. Set _Program_ to `ceedling`,
   _Arguments_ to `test:all`, and _Working directory_ to `$ProjectFileDir$`.
1. Under the tool’s _Advanced Options_ ↳ _Output Filters_, add
   `$FILE_PATH$:$LINE$:$COLUMN$.*`.
1. Run the tool from _Tools_ ↳ _External Tools_. Each failed and ignored test’s location
   becomes a link in the Run window.

CLion’s built-in test runner does not support Unity. For code insight, the
[Compile Commands JSON DB](https://throwtheswitch.github.io/Ceedling/plugins/report-tests-ide-stdout/compile-commands-json-db.md) plugin writes a compilation
database that CLion can open as a project.
