---
id: "devt-ctrace-constraints-input-format-framing-and-discovery"
type: "concept"
domain: "trace"
title: "ctrace Constraints: Input format, framing, and discovery"
summary: "ctrace Constraints: Input format, framing, and discovery"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/constraints.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/constraints.md#input-format-framing-and-discovery"
license: "Apache-2.0"
mode: "V"
---

- Optional `ctrace-run.trace-format` accepts only `unformatted` or `formatted`. An explicit value overrides the
  channel-based default. Missing or null selects `unformatted` for SWO and `formatted` for TB or named-TB without an
  Error. Discovery resolves this effective format separately for each input before route normalization. An explicit
  override applies to every supported input associated with that trace-run configuration.
- Every existing `<set>.SWO.raw`, `<set>.TB.raw`, and `<set>.TB_<name>.raw` is processed independently and sequentially.
  `--target` selects a solution set, including all its supported inputs. A set without an eligible input reports an error.
  Each input must be a regular, readable file and is opened during its own preflight, before that input's decoder and
  output backends are constructed. Target XML preparation precedes these per-input jobs. Event Recorder input remains
  diagnosed and excluded from processing.
- Input preflight, route normalization, decoding, and output failures do not prevent processing the remaining inputs
  or solution sets. Each input has independent decoder and output state; any failing input contributes to a non-zero
  command exit status. A configuration read failure prevents processing that set but does not stop later sets.
- The standardized `trace-buffer` selection belongs to solution/build-run producer configuration, not to the
  `*.ctrace-run.yml` file consumed by ctrace. The caller-facing selection and format/framing contract remains
  follow-up work; this does not imply adding fields to `*.ctrace-run.yml`. Current discovery processes all supported
  matching files and applies the channel-based defaults above.
- Formatted input globally uses 16-byte memory-aligned CoreSight frames. Its length must be a multiple of 16, and it
  contains neither FSYNC nor HSYNC framing. Ctrace does not parse or emit a `trace-framing` YAML field; supporting
  another framing mode requires a public trace contract first.
- Format describes the effective bytes in the selected capture, not target capability. The channel-based default is
  a heuristic, not byte-content detection: ctrace does not infer format from synchronization patterns, configured
  route count, or target setup. An explicit declaration is required when the bytes differ from the channel default.
