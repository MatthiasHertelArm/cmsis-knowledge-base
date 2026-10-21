---
id: "x-fvp-debug-setup-2"
type: "troubleshooting"
domain: "debug"
title: "GDB connects before the FVP model is listening"
status: "draft"
symptoms: ["gdb connection lost"]
extracted_from: "proc-fvp-debug-setup"
source: "fvp-debug-setup/SKILL.md"
license: "Apache-2.0"
---

The template sets both `port` and `serverParameters`, so GDB connects immediately while the model still needs a second or more to build the platform (plus a container start on macOS). The symptom is a session that tears itself down and only *then* prints the banner:

gdb connection lost
GDBServer: Listening address="0.0.0.0" port=3333    ← too late
Info: <model>: Stopping simulation...

Blank the port to select the event-driven branch — better than `serverStartupDelay`, which is a fixed cost paid on every single launch:

"port": "",
"serverPortRegExp": "GDBServer: Listening .*port=([0-9]+)",
"portDetectionTimeout": 300000

**(b) The banner is stuck in a pipe buffer.** The model block-buffers its own stdout whenever it is not a TTY — which it never is under VS Code — so the banner (and every semihosting `printf`) sits in a 4KB buffer until the model exits. Fix (a) reads that banner, so it depends on this. Run the model under `stdbuf -oL -eL`
