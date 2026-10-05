---
id: "dbgx-trace-configuration-update-trigger-ctrace-file-events"
type: "concept"
domain: "debug"
title: "Trace Configuration Update Triggers: ctrace file events"
summary: "The \"Generate default ctrace\" command (TraceConfigurationCommands), an external edit, and a webview Save (TraceConfigurationModel) can all write the production ctrace file. They do not call pyTS directly."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:docs/trace-configuration/update-triggers.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/docs/trace-configuration/update-triggers.md#ctrace-file-events"
license: "Apache-2.0"
mode: "V"
---

The "Generate default ctrace" command (`TraceConfigurationCommands`), an
external edit, and a webview Save (`TraceConfigurationModel`) can all write
the production ctrace file. They do not call pyTS directly.

`TraceConfigurationGeneratedCTraceFileManager` may also write that file when
it processes a created or changed cbuild-run, including an existing one selected
after the active solution changes.

The ctrace create/change event starts pyTS only if `PyTsController` is already
watching and receives it.

```mermaid
flowchart TD
    Change["ctrace file created or changed"] --> Active{"PyTsController watcher<br/>active and event received?"}
    Active -->|yes| Reject{"Is backup or different project<br/>from debug cbuild-run?"}
    Reject -->|no| Contents{"Contents changed since<br/>last observed?"}
    Contents -->|yes| Queue["Queue conversion"]
    Queue --> Call["Call pyTS"]
    Call --> Run["ctrace-run output"]
    Ignored["No watcher pyTS call"]
    Active -->|no| Ignored
    Reject -->|yes| Ignored
    Contents -->|no| Ignored
    Manual["Launch pyTS command<br/><code>(TraceCommands)</code>"] --> Call
```

The watcher observes `.cmsis/[!~]*.ctrace.{yml,yaml}` while the
trace-generation view setting is enabled. It matches ctrace names to the
debug session's cbuild-run filename and locates `.cmsis` under the active
solution folder when available. Without a `.cbuild-run.yml` session path, it
skips the project check.

`TraceConfigurationFileWatcher.watchCurrentFile()` reloads YAML only;
it is installed after a generated file is loaded and pauses during unsaved
webview edits.
