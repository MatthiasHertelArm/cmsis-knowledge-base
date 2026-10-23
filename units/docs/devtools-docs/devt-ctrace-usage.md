---
id: "devt-ctrace-usage"
type: "concept"
domain: "trace"
title: "ctrace: Usage"
summary: "Values for --type and --stream are space-separated, so place the trace directory before these multi-value options. If the directory follows them, terminate option parsing explicitly, for example ctrace --type itm dwt -- .trace."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/README.md#usage"
license: "Apache-2.0"
mode: "V"
---

```text
ctrace <trace-dir> [options]

  -t, --target <name>       Process one solution set; otherwise process all
      --csv                 Generate CSV output
      --ctf                 Generate CTF and Trace Compass XML output
  -a, --all                 Generate all output formats
      --type <type ...>     Select event types
      --stream <id ...>     Select streams (0 for unformatted; ATB IDs 1 to 111)
  -v, --verbose             Show detailed CLI diagnostics and run information
  -h, --help                Print command-line help
  -V, --version             Print the version
```

Values for `--type` and `--stream` are space-separated, so place the trace directory before these multi-value options.
If the directory follows them, terminate option parsing explicitly, for example
`ctrace --type itm dwt -- .trace`. With no output option, `ctrace` validates and decodes the capture without writing
output files. Run `ctrace --help` for the current option details.

Normal CLI diagnostics use the same compact trace messages as CSV. Add `--verbose` (or `-v`) to include detailed
reasons, raw positions with bounded inspection windows, native decoder codes, packet previews and technical run
information on stderr. This option does not change CSV or CTF output, event selection or the exit status.
