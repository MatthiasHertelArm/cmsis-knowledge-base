---
id: "mbedtls-tips-for-debugging-mbed-tls-reverse-debugging"
type: "concept"
domain: "security"
title: "Tips for debugging Mbed TLS: Reverse debugging"
summary: "Also known as back-in-time debugging or time travel debugging."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/debugging_tips.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/debugging_tips.md#reverse-debugging"
license: "Apache-2.0"
mode: "V"
---

### What is reverse debugging?

Also known as back-in-time debugging or time travel debugging.

Reverse debugging allows you to go backward in time when stepping through a program. For example, a reverse single step after returning from a function goes back to the function's `return` statement.

### Tools for reverse debugging

* Gdb supports reverse debugging, but not out of the box, it requires some complex setup.
* LLDB does not support reverse debugging as of 2025.
* Visual Studio (under Windows) supports reverse debugging since 2017.

Reverse debugging works by taking snapshots of a program and recording its inputs and outputs. It may or may not work when the program interacts with its environment in complex ways, since the environment does not roll back when the program does.

### Replay debuggers

A replay debugger records one execution of the program. It then replays this same execution, simulating all inputs and outputs.

#### Replay debugging on Linux with rr

Install the Mozilla Record and Replay framework (rr) from https://rr-project.org/ or e.g. `apt install rr`.​

If needed, give yourself debugging permission:

```
# The Ubuntu default is 4 which is too paranoid.
sudo sysctl kernel.perf_event_paranoid=1.​
# Make this persistent across reboots.
echo 'kernel.perf_event_paranoid = 1' >>/etc/sysctl.d/zz-local.conf​
```

To debug a program​, build it with debugging symbols as usual (`-O0 –g3` or `–Og -g3`).​ Then run it once to save a full trace of the execution:

```
rr record tests/test_suite_ssl
```

Then `rr replay` gives you a gdb interface where reverse execution actually works.​ You can use [`reverse-xxx` commands​](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Reverse-Execution.html) such as:

* `rs` (`reverse-step`) steps into functions​.
* `rn` (`reverse-next`) steps over function calls​.
* `reverse-finish` goes back to where the current function was called​.
* `set exec-direction reverse` changes `step`, `next`, etc. to go backwards. Switch this off with `set exec-direction forward`.

If you use a frontend, configure it to run `rr replay` instead of `gdb myprogram`.​ If the frontend uses gdb's machine interface, use `rr replay -i=mi …` instead of `gdb -i=mi …`.

#### Replay debugging on macOS with warpspeed

Try [warpspeed](https://github.com/kallsyms/warpspeed).
