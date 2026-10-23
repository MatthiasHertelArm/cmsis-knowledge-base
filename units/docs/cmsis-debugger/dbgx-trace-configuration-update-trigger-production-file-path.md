---
id: "dbgx-trace-configuration-update-trigger-production-file-path"
type: "concept"
domain: "debug"
title: "Trace Configuration Update Triggers: Production file path"
summary: "The two ctrace watchers have different jobs."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:docs/trace-configuration/update-triggers.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/docs/trace-configuration/update-triggers.md#production-file-path"
license: "Apache-2.0"
mode: "V"
---

The two ***ctrace*** watchers have different jobs.

- `PyTsController` starts pyTS conversion.
- `TraceConfigurationFileWatcher.watchCurrentFile()` reloads the displayed YAML.

The same `TraceConfigurationFileWatcher` class also watches the current
**ctrace-run** files. Each class named on a file-event edge registers its watch
through `FileWatchManager.addWatch()`.

```mermaid
flowchart TB
    Build["Active cbuild-run"] --> Manager["Generated-file manager<br/><code>(TraceConfigurationGeneratedCTraceFileManager)</code>"]
    Manager -->|creates file or adds missing processor setups| Source[".cmsis/*.ctrace.yml"]
    Source -->|PyTsController watch: accepted create/change| Converter["pyTS ctrace watcher<br/><code>(PyTsController)</code>"]
    Converter --> PyTS["pyTS conversion<br/><code>(PyTsProcessManager)</code>"]
    PyTS --> Run["<b>.trace/*.ctrace-run.yml</b>"]
    Source -->|TraceConfigurationFileWatcher watch: loaded file event| SourceWatch["Current ctrace watcher<br/>reloads displayed YAML<br/><code>(TraceConfigurationFileWatcher.watchCurrentFile())</code>"]
    SourceWatch --> View["Trace Configuration view<br/><code>(TraceConfigurationModel)</code>"]
    Run -->|TraceConfigurationFileWatcher watch: run file event| RunWatch["Current ctrace-run watcher<br/>reads validation messages<br/><code>(TraceConfigurationFileWatcher.watchCurrentRunFiles())</code>"]
    RunWatch --> View
```

The **loaded file** is the exact ctrace file currently open in the Trace
Configuration view. Its watcher receives create, change, and delete events for
that path; it reloads the displayed YAML only when the file's timestamp or
size differs from the last loaded version. The watcher is paused during
unsaved webview edits.

An **accepted create/change event** means the separate `PyTsController`
watcher is active, receives an event for a non-backup ctrace file matching
`.cmsis/[!~]*.ctrace.{yml,yaml}`, accepts it for the current debug context,
and finds that its contents differ from the last observed contents. That
watcher then queues pyTS conversion. It does not process delete events.
