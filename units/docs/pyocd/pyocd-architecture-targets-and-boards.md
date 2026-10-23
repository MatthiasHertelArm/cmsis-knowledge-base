---
id: "pyocd-architecture-targets-and-boards"
type: "concept"
domain: "debug"
title: "Architecture: Targets and boards"
summary: "Target and board support are two separate but related pieces of functionality."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/architecture.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/architecture.md#targets-and-boards"
license: "Apache-2.0"
mode: "V"
---

Target and board support are two separate but related pieces of functionality.

#### Target support

Each supported target enables debugging and flash programming a given MCU. A single target can be
used for potentially multiple boards, or there may not be board with the target. Users can
override the target type on the command line or when creating the `Session`.

Each supported target is defined as a `CoreSightTarget` subclass. Builtin targets are held in a
Python file in the `pyocd/target/builtin` directory. If the target has internal or connected flash,
then a flash algo dict and possibly a `Flash` subclass will be paired with it in the same source
file. The `Flash` subclass is only required if special flash programming semantics are needed,
otherwise the base `Flash` class is automatically used. The flash algo dict and/or `Flash` subclass
are set on flash memory regions when they are created in the memory map. Some device families have
family subclasses under `pyocd/target/family`.
