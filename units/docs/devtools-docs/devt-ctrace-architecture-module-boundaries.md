---
id: "devt-ctrace-architecture-module-boundaries"
type: "concept"
domain: "trace"
title: "ctrace Architecture: Module boundaries"
summary: "control is the composition layer. The raw-file reader is a private implementation detail of FileDecodeJob, not a separate module or public abstraction."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/architecture.md#module-boundaries"
license: "Apache-2.0"
mode: "V"
---

### Entry point and orchestration

| Module | Responsibility |
| --- | --- |
| `src/CtraceMain.h` | Platform-independent entry point used by the executable trampoline |
| `src/cli` | Command-line parsing, value normalization, and validation |
| `src/control` | Solution-set orchestration, raw-file access, output setup, and per-file decode jobs |
| `src/diagnostics` | Structured diagnostics, severity tracking, and decoder issue reporting |

`control` is the composition layer. The raw-file reader is a private implementation detail of `FileDecodeJob`, not a
separate module or public abstraction. Control may depend on the other application modules, while lower-level modules
must not depend on control jobs or command-line details.

### Trace-run metadata

| Module | Responsibility |
| --- | --- |
| `src/tracerun` | File discovery, YAML parsing, schema subset validation, and normalized metadata |

The YAML reader's validation, provisional input-format, and metadata rules are recorded in the
[constraints](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/constraints.md).

`CtraceRunMeta` is the boundary between the YAML representation and runtime processing. `TraceRunInputDescriptor`
combines it with the selected open raw file and effective format. Decode and
output modules consume these normalized values instead of navigating YAML nodes or repeating discovery decisions.

### Decode and event model

| Module | Responsibility |
| --- | --- |
| `src/decode` | Raw-byte decoder interface, OpenCSD integration, packet recovery, timestamps, and Cortex-M semantics |
| `src/model` | Backend-independent event types, quality information, and event selection |

OpenCSD is isolated behind adapter classes in `src/decode`. OpenCSD-specific elements do not escape into the output
modules. The post-decoder maps them to `TraceEvent` variants such as software trace, DWT data, exceptions, timestamps,
overflow, and trace issues. `TraceSelection` owns the stable public type names and maps semantic events onto that
release-facing set.

Each event retains a normalized route identity and can retain its raw index, architectural Trace Bus ID, timestamp,
and quality state. The private route ID distinguishes even routes without an ATB ID; it is never exposed as a public
stream number. This allows diagnostics and backends to make independent decisions without reconstructing decoder
state.

`TraceByteSkip` is deliberately separate from `TraceEvent`: it carries a formatter-group offset, skipped payload-byte
count, reason, and optional observed ID. An observed ID may be NULL or reserved; it must not be turned into a decoded
route or assigned an invented clock for output convenience.

### Output

| Module | Responsibility |
| --- | --- |
| `src/output` | Backend requirements, output planning, and lifecycle management |
| `src/output/csv` | Stable CSV schema, row mapping, filtering, and file output |
| `src/output/ctf` | CTF metadata and stream encoding plus Trace Compass analysis XML |

Output requirements are evaluated per backend and selected route. For example, missing CTF-specific metadata on an
active route may disable CTF while an independent CSV output remains valid; metadata on a route excluded by the
stream filter is not required. `--all` therefore does not make the backends share failure state unnecessarily.

Each input writes separate `<set>.<channel>.csv` and `<set>.<channel>.ctf` artifacts. One optional
`<set>.traceanalysis.xml` describes the target's eligible completed bundles. CTF always uses the channel-qualified
path, including single-input runs; existing `<set>.ctf` bundles and old per-channel XML files are not migrated or
removed. The [CTF profile](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/ctf-format.md#files-and-common-structure)
records this intentional difference from the published bundle path.

CSV writes one combined file per input in sink callback order. `CtfBundleOutput` owns a bundle-local metadata model and
lazily creates a stream writer for each formatted route that emits selected events. Representation changes stay in
the backends: for example, CSV retains a DWT/PMU counter mask in one row while CTF expands it into individual records.

CTF finalization retains only emitted streams and exposes the completed metadata. `TraceDirectoryJob` gives these
results to a target-scoped `TraceCompassXmlOutput`; it does not discover contributions by scanning existing CTF files.
The collector prepares the target XML before the input jobs and writes it after all inputs have been attempted.
Only observed graphical topics in freshly completed bundles contribute views. Without graphical topics, it leaves no
XML; point events remain in the CTF event table.

Each contributing bundle must retain exactly one clock domain. Multi-clock bundles remain valid CTF but are excluded
with a warning because the supported reader cannot safely order their independent streams. Separate single-clock
bundles can contribute to one XML without clock correlation or timestamp rebasing. Every clock, including legacy
`swo_clock`, has a UUID; the XML scopes state by the reader's `hostId` (that UUID), public `cmsis_trace_bus_id`, and
topic. Channel/processor labels are display-only, and the private CTF `ctrace_route` context is no longer needed by
the XML. A deterministic namespace derived from the contributing clock identities prevents analysis/view collisions
between target XML files. The legacy binary event layout is unchanged.

The [CTF profile](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/ctf-format.md) defines event schemas, metadata, clock mappings, legacy layouts, and
[XML projection](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/ctf-format.md#generated-trace-compass-analysis). Cross-backend compatibility and failure rules belong
to the [output constraints](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/constraints.md#observable-behavior-and-output-safety).

Outputs use an explicit `start`, `writeEvent` / `writeByteSkip`, `stop`, and `abort` lifecycle. `TraceOutput`
owns the active state and common write-failure cleanup; concrete backends implement the protected lifecycle hooks.
The byte-skip hook defaults to no output, as required by CTF; CSV implements it independently of event filters.
A successful backend can finish even if another backend fails. When `FileDecodeJob` catches `OpenCsdFatalError`, it
passes a `TraceDecodeAbort` to output finalization. The default backend policy removes incomplete artifacts, as
required for CTF. CSV instead appends a global abort record and closes the already committed rows. Failed
CSV writes or finalization still remove the unreliable file; failures before output startup do not create one.
Target XML has an independent lifecycle: a failed input cannot remove another input's completed bundle or views,
and an XML preparation/write failure leaves completed CTF and CSV outputs intact. Preparing target XML never migrates
or removes historical per-channel XML files.
