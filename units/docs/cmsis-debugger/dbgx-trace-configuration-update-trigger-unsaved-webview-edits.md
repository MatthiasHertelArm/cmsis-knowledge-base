---
id: "dbgx-trace-configuration-update-trigger-unsaved-webview-edits"
type: "concept"
domain: "debug"
title: "Trace Configuration Update Triggers: Unsaved webview edits"
summary: "An edit remains in memory while DebouncedTraceConfigurationBackup writes a backup beside the production ctrace file. Restoring an existing backup follows the same validation path. PyTsTraceConfigurationPrevalidator checks that the file is the active pyTS input before calling pyTS."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:docs/trace-configuration/update-triggers.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/docs/trace-configuration/update-triggers.md#unsaved-webview-edits"
license: "Apache-2.0"
mode: "V"
---

An edit remains in memory while `DebouncedTraceConfigurationBackup` writes a
backup beside the production ctrace file. Restoring an existing backup follows
the same validation path. `PyTsTraceConfigurationPrevalidator` checks that the
file is the active pyTS input before calling pyTS.

```mermaid
flowchart TD
    Edit["Unsaved webview edit"] --> Backup["Write .cmsis/~*.ctrace.yml backup"]
    Restore["Restore existing backup"] --> Check{"Active cbuild-run resolves<br/>to this ctrace file?"}
    Backup --> Check
    Check -->|no| Unavailable["Validation unavailable"]
    Check -->|yes| Call["Call pyTS for validation"]
    Call --> Run["May update .trace/~*.ctrace-run.yml"]
    Run --> Messages["Show validation result and<br/>available backup messages"]
```

### ctrace-run observation

`TraceConfigurationFileWatcher.watchCurrentRunFiles()` watches both ctrace-run
filenames for the current ctrace file. `TraceConfigurationModel` reads
validation messages on create/change and clears them on delete. It uses
production messages when clean and backup messages while an unsaved edit is
active. Loading a clean ctrace file also reads an existing production
ctrace-run file without waiting for a watcher event.
