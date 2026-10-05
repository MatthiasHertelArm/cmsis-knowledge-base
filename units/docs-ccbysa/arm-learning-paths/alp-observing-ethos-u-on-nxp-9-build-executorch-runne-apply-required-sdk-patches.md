---
id: "alp-observing-ethos-u-on-nxp-9-build-executorch-runne-apply-required-sdk-patches"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Build Cortex-M33 firmware for ExecuTorch: Apply required SDK patches"
summary: "The MCUXpresso SDK ships with a linker script and an Ethos-U driver log header that need two fixes before the firmware can run correctly."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33/#apply-required-sdk-patches"
license: "CC-BY-SA-4.0"
mode: "V"
---

The MCUXpresso SDK ships with a linker script and an Ethos-U driver log header that need two fixes before the firmware can run correctly. The patch script in the repository reads `SdkRootDirPath` to locate your SDK and applies both fixes automatically.

Using a `bash` shell, navigate to the `Executorch_runner_cm33` directory and run:

```bash
./patches/apply_patches.sh
```

You should see output confirming each patch:

```output
=== ExecuTorch Runner SDK Patches ===

[1/2] Linker script GOT fix: .../MIMX9352xxxxM_ram.ld
  APPLIED: Added *(.got) and *(.got.plt) inside .data section.

[2/2] Ethos-U driver log redirect: .../ethosu_log.h
  APPLIED: LOG_ERR/LOG_WARN/LOG_INFO/LOG_DEBUG now write to remoteproc trace buffer.

=== All patches applied successfully ===
```

The two patches and what they fix:

| Patch | What it changes | What happens without it |
|-------|----------------|------------------------|
| **GOT initialization** | Adds `*(.got)` and `*(.got.plt)` inside the `.data` section of the SDK linker script so the startup code copies the Global Offset Table from flash to RAM | The GOT stays zeroed out after boot. Every C++ virtual call resolves to address zero, causing a **BUS FAULT** the first time the firmware calls `load_method` |
| **NPU log redirect** | Replaces the Ethos-U driver's `LOG_ERR`/`LOG_INFO` macros so they write to the remoteproc trace buffer instead of the UART | NPU error messages go to UART only. When you read `trace0` from Linux, driver errors are invisible, making NPU failures difficult to diagnose |

**Note:**
Run the patch script once after installing the SDK. If you run it again, the script detects that the patches are already in place and skips them. If you reinstall or update the SDK, run the script again.
