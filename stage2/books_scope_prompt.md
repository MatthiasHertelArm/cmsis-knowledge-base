# Scope of a book unit: coding and design knowledge stays, tool usage and project management go

The knowledge base of the CMSIS Developer Assistant answers an AI coding agent that works in a
CMSIS session. The agent's tools, build system, debugger, packs and project layout are set by the
core knowledge base and by the tool rules; a book must not teach it another way to build, flash,
debug, install or organise a project. What a book may teach is how to write and design the code:
the language, the idioms, the algorithms, the driver and protocol logic, the architecture.

You classify units made from book sections. For each unit you get its id, book, title, summary and
the start of its text. Put it in exactly one scope:

- `coding`: how code is written: language features and idioms (volatile, bit masks, templates,
  smart pointers, concurrency primitives), data structures and algorithms, register-level driver
  logic and sequences, interrupt handlers, buffers, state machines, memory layout as the code sees
  it (linker symbols, sections, stack and heap), protocol framing and timing as code must handle
  it, performance techniques in code, testing techniques in code.
- `design`: how software is structured and why: architecture and design patterns, abstraction
  layers and their trade-offs, concurrency and asynchrony models, memory management strategies,
  power management strategies, protocol choice and bus concepts, error handling and robustness
  principles, API design, refactoring principles.
- `tool`: how to use a tool or an infrastructure product: an IDE and its menus, a compiler, linker
  or binutils invocation, a debugger session (GDB, LLDB, OpenOCD, a GDB server, breakpoints in a
  tool), flashing, profilers, sanitizers as a tool to run, package managers, CMake and Make as
  build tools, shell commands, version control, CI/CD pipelines, containers and their
  orchestration (Docker, Kubernetes, Nomad, service meshes), cloud provider services and their
  APIs, logging, tracing and monitoring stacks (Logstash, OpenTelemetry collectors, Grafana),
  deployment tooling (Packer, Terraform, Ansible). A concept that only exists to explain such a
  product (what a Pod is, how a cluster schedules) is `tool` as well: it is not a design pattern
  the agent can apply in code.
- `project`: how a project is set up and run: creating a project, folder and file organisation,
  build configuration and dependencies, toolchain and environment setup, installing headers or
  packs, documentation navigation (which manual to open, where to click), team process, planning,
  book navigation (prefaces, chapter overviews that only list topics, summaries, requirements,
  exercises).
- `other`: advertising, acknowledgements, narrative without technical content.

A unit that mixes scopes gets the scope of its main teaching. A CMake or Make unit is `tool` even
when it shows code: the code is build configuration. A linker-script unit is `coding` when it
explains sections, symbols and addresses the program depends on, and `tool` when it is about
running the linker. A startup-file unit is `coding`. A chapter introduction or summary gets the
scope of the chapter.

## Output

A JSON array, one object per unit, in the batch's order:

```json
{"id": "<unit id>", "scope": "coding | design | tool | project | other", "reason": "<at most ten words>"}
```

## When you work as a reader agent on a batch file

The batch file is a JSON object with `prompt` (this text) and `units` (a list of
`{id, book, title, summary, excerpt}`). Write the JSON array to the output path you were given
and check that it parses and has one object per unit. Keep scratch files in a folder named after
your batch, never in a shared root. Do not run any tool other than reading the batch and writing
the output; no network access. Report: units read, counts by scope, and anything odd.
