---
id: "pyocd-architecture-top-level-objects"
type: "concept"
domain: "debug"
title: "Architecture: Top level objects"
summary: "Architecture: Top level objects"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/api/architecture.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/api/architecture.md#top-level-objects"
license: "Apache-2.0"
mode: "V"
---

### `Session`

- In `pyocd.core.session`.
- Represents a target connection through a debug probe.
- Root of object graph.
- Owns the `Board` instance, and through that the `SoCTarget` instance.
- Manages session options, user script, and project file access.

### `DebugProbe`

- In `pyocd.probe.DebugProbe`.
- Manages connection to probe.
- Abstracts target control actions.
- Concrete subclasses implement a debug probe’s protocol.
- Returns available instances of a debug probe type. For instance, for listing available probes.
- Can be used alone (without `Target`) for some use cases.
- Each subclass is a plug-in.
- Concrete classes include
    - `CMSISDAPProbe`
    - `STLinkProbe`
    - and more

### `Target`

- In `pyocd.core.target`.
- Defines the abstract API primarily used by scripts.
- Superclass for both SoC and core classes.
- Functionality includes
    - Memory transfers
    - Core register access
    - Reset
    - Run control (halt/step/resume)
    - Breakpoints/watchpoints
    - Misc status
- Defines some enumerations used in many places, such as `Target.ResetType` and `Target.State`.
- Concrete classes include
    - `CoreSightTarget`
    - `CortexM`
