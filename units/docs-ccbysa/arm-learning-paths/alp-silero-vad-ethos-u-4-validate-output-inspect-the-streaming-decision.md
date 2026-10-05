---
id: "alp-silero-vad-ethos-u-4-validate-output-inspect-the-streaming-decision"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Validate the FVP speech probabilities: Inspect the streaming decisions"
summary: "The application sends one PROB line over the simulated UART for every 512-sample frame. It also merges consecutive speech frames into SEGMENT lines."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/4-validate-output.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/4-validate-output/#inspect-the-streaming-decisions"
license: "CC-BY-SA-4.0"
mode: "V"
---

The application sends one `PROB` line over the simulated UART for every 512-sample frame. It also merges consecutive speech frames into `SEGMENT` lines.

Inspect the first probability records and the detected speech segments:

```bash
grep -Eo 'PROB .*$' \
  silero-vad-work/fvp/fvp.log | head -n 10
grep -Eo 'SEGMENT .*$' \
  silero-vad-work/fvp/fvp.log
```

The output is similar to:

```output
PROB 0.000 0.211681 silence
PROB 0.032 0.211681 silence
...
PROB 0.224 0.995684 speech
...
SEGMENT 0.224 2.048 speech
```

Each `PROB` line contains the frame timestamp in seconds, the probability of speech, and the decision produced with a threshold of `0.55`. Your probability values and speech segments depend on the validation audio.

The validation question is: Did the host and FVP label every frame the same way? In this run, both the host and the FVP found one speech segment from `0.224` to `2.048` seconds, with no decision mismatches.

(figure: Two matching timelines for the same 2.5-second audio clip. The host reference and FVP output both show silence, speech from 0.224 to 2.048 seconds, then silence. All 79 frame decisions match.#center)
