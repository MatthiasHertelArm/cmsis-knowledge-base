---
id: "alp-silero-vad-ethos-u-3-run-on-fvp-run-silero-vad-on-the-fvp"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Build and run the Corstone-320 application: Run Silero VAD on the FVP"
summary: "Run the application and save its simulated UART output to fvp.log:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/3-run-on-fvp.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/3-run-on-fvp/#run-silero-vad-on-the-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the application and save its simulated UART output to `fvp.log`:

```bash
mkdir -p silero-vad-work/fvp
set -o pipefail
bash backends/arm/scripts/run_fvp.sh \
  --elf=silero-vad-work/app/silero_vad_ethos_u \
  --target=ethos-u85-256 \
  --timeout=300 2>&1 | tee silero-vad-work/fvp/fvp.log
```

The application prints one speech probability every 32 ms. Near the end, it reports a summary and stops the simulation:

The output is similar to:

```output
1 segments, 79 frames, 2.5s
Speech: 57/79 frames (72.2%)
Simulation complete, 0
No problems found!
```
