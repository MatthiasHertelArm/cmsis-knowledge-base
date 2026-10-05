---
id: "avh-use-with-keil-vision-program-build-and-debug"
type: "concept"
domain: "test"
title: "Use with Keil µVision: Program Build and Debug"
summary: "Project build and debug on an Arm FVP target can be done in the similar way as any other Keil µVision project:"
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/infrastructure/src/avh_mdk_uv4.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/avh_mdk_uv4.md#program-build-and-debug"
license: "Apache-2.0"
mode: "V"
---

Project build and debug on an Arm FVP target can be done in the similar way as any other Keil µVision project:

- Press _Rebuild_ button in µVision toolbar (or use `F7` hotkey).
- Start the debug session from µVision toolbar (or with `Ctrl-F5`). The model executable window should pop up (with
  `C:\WINDOWS\system32\cmd.exe`) but it will stay empty during the session.
- If enabled in mdk_uv4_fvp_debug, a Telnet client will start. Program output should be expected there.
- Debug the project as usual with available µVision functionality. Refer to
  [Application Debug on Arm FVPs](https://developer.arm.com/documentation/101407/0540/Simulation/AVH-FVP-Targets/Application-Debug)
  for additional details and references.
