---
id: "pyocd-architecture-target-classes"
type: "concept"
domain: "debug"
title: "Architecture: Target classes"
summary: "These classes are all either direct or indirect subclasses of Target."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/api/architecture.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/api/architecture.md#target-classes"
license: "Apache-2.0"
mode: "V"
---

These classes are all either direct or indirect subclasses of `Target`.

### `SoCTarget`

- In `pyocd.core.soc_target`.
- Abstract class for the SoC.
- Runs init sequence created by subclass.
- Owns all cores, accessible through the `.cores` dict property.
- Has a notion of a _selected core_.
- Proxies Target methods to the selected core, which makes single-core MCUs transparent.

### `CoreTarget`

- In `pyocd.core.core_target`.
- Abstract class for a processor core.
- Used as a common, architecture-independent superclass for core target classes.
- Doesn't provide much additional functionality on its own.

### `CoreSightTarget`

- In `pyocd.coresight.coresight_target`.
- Concrete SoC class for Arm CoreSight based devices (subclass of `SoCTarget`).
- Used for generic Arm targets such as the `cortex_m` target type.
- Integrates CoreSight discovery into init sequence.
- Owns the DP and APs.

### `CortexM`

- In `pyocd.coresight.cortex_m`.
- Concrete CPU-level target for Arm M-profile cores, subclass of `CoreTarget`.
- Implements most of the `Target` methods.
- Determines CPU type and supported extensions (FPU, etc) by reading ID registers.
