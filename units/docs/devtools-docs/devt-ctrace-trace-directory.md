---
id: "devt-ctrace-trace-directory"
type: "concept"
domain: "trace"
title: "ctrace: Trace directory"
summary: "Input and output files share a solution-set base name:"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/README.md#trace-directory"
license: "Apache-2.0"
mode: "V"
---

Input and output files share a solution-set base name:

```text
.trace/
  Board.ctrace-run.yml
  Board.SWO.raw
```

For `ctrace .trace --target Board --all`, the supported input produces:

```text
.trace/
  Board.SWO.csv
  Board.SWO.ctf/
    metadata
    stream_0
  Board.traceanalysis.xml     # graphical views from eligible completed CTF bundles
```

Discovery processes every existing `Board.SWO.raw`, `Board.TB.raw`, and `Board.TB_<name>.raw` input independently,
one after another. `--target Board` selects the solution set and all its supported inputs. Each input gets its own
CSV and CTF bundle, using `<solution-set>.<channel>` as their common base name. CTF uses
this channel-qualified name even for a single input; older `Board.ctf` bundles are neither reused nor removed.
The [CTF profile](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/ctf-format.md#files-and-common-structure) records the required specification alignment.

Trace references use `index:` for ITM channel and DWT comparator numbers, as a scalar or array. The YAML reader
ignores fields it does not consume. The fourth CSV column is also named `index`; its values are unchanged.

One optional `Board.traceanalysis.xml` collects graphical views from all eligible CTF bundles completed for that
target in the current invocation. Each contributing bundle must retain exactly one clock domain. A multi-clock bundle
remains valid CTF but is omitted from the XML with a warning. Independent single-clock bundles can contribute together;
their clock UUIDs keep sources separate without synchronizing or rebasing their timestamps. No old per-channel XML
files are migrated or deleted. An XML failure leaves completed CSV and CTF outputs intact.

Without a format declaration, each SWO input defaults to unformatted ITM and each TB or named-TB input defaults to
formatted CoreSight. Missing or null `trace-format` uses these channel-based defaults; an explicit value overrides
the format for every supported input in that trace-run:

```yaml
ctrace-run:
  trace-format: formatted  # formatted or unformatted
  # ctrace-setup and ctrace-refs follow here
```

This optional, ctrace-private provisional field does not select a file. The channel-based default is a heuristic, not
byte-content detection. Formatted input currently requires complete 16-byte
memory-aligned CoreSight frames; there is no public `trace-framing` field yet. See the
[constraints](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/constraints.md) for the full discovery, routing, and
compatibility contract.

Event Recorder (`Board.ER.raw`) remains unsupported and is skipped with a warning. A solution set without a supported
input reports an error. A failure in one input leaves the remaining inputs and solution sets available for processing;
the command returns non-zero if any input fails. This also applies when validating without output options.
