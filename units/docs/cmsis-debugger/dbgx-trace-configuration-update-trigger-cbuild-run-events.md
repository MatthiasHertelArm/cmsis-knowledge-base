---
id: "dbgx-trace-configuration-update-trigger-cbuild-run-events"
type: "concept"
domain: "debug"
title: "Trace Configuration Update Triggers: cbuild-run events"
summary: "At startup, after an active-solution or cbuild-index change, and when the watched cbuild-run is created or changed, TraceConfigurationFileWatcher forwards the active cbuild-run event. TraceConfigurationGeneratedCTraceFileManager writes the matching ctrace file only when it is new or needs processor setup entries."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:docs/trace-configuration/update-triggers.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/docs/trace-configuration/update-triggers.md#cbuild-run-events"
license: "Apache-2.0"
mode: "V"
---

At startup, after an active-solution or cbuild-index change, and when the
watched cbuild-run is created or changed, `TraceConfigurationFileWatcher`
forwards the active cbuild-run event. `TraceConfigurationGeneratedCTraceFileManager`
writes the matching ctrace file only when it is new or needs processor setup
entries.

```mermaid
flowchart TD
    Event["Existing or changed active cbuild-run"] --> Mode{"Trace mode on?"}
    Mode -->|no| Off["No ctrace update"]
    Mode -->|yes| Update["Create or update ctrace if needed"]
    Update --> Written{"Was ctrace written?"}
    Written -->|yes| File["pyTS via ctrace file watch<br/><code>(PyTsController)</code>"]
    Written -->|no| Direct["Queue pyTS through controller<br/><code>(PyTsController.convertCTrace())</code>"]
    File --> Load["Load ctrace in view"]
    Direct --> Load
```

For an unchanged existing ctrace file, every forwarded cbuild-run event queues
an explicit conversion, even when the production ctrace-run file already
exists. The cbuild-run input may have changed while the ctrace input stayed the
same, making the existing output stale. Equivalent requests that overlap are
coalesced by `PyTsController`; sequential events after a conversion completes
remain distinct. A ctrace write can still start pyTS through the separate
`PyTsController` watcher below.
