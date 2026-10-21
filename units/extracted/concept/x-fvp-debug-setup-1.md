---
id: "x-fvp-debug-setup-1"
type: "concept"
domain: "debug"
title: "FVP GDBServer plugin: -D starts the model halted, RSP detach does not resume"
status: "draft"
extracted_from: "proc-fvp-debug-setup"
source: "fvp-debug-setup/SKILL.md"
license: "Apache-2.0"
---

**`-D` / `--allow-debug-plugin` is what makes the model start halted at the reset vector.** With the plugin but without `-D` the model opens the port *and free-runs to completion* — a `tbreak main` would never fire. With `-D` it waits, and GDB attaches at `Reset_Handler`.
**RSP detach does not resume the target.** After `detach` the core stays halted at wherever it was, and `monitor help` lists only logging commands — there is no resume. So a "Run" action cannot resume a halted debug instance; it must start its own free-running model (no plugin, no `-D`).
