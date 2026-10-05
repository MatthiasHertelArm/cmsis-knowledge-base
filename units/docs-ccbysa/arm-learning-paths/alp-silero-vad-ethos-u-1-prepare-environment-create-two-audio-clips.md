---
id: "alp-silero-vad-ethos-u-1-prepare-environment-create-two-audio-clips"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Prepare the environment and model inputs: Create two audio clips"
summary: "The target processes 2.5 seconds of audio. Copy the following snippet once to create a calibration clip and a separate validation clip:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/1-prepare-environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/1-prepare-environment/#create-two-audio-clips"
license: "CC-BY-SA-4.0"
mode: "V"
---

The target processes 2.5 seconds of audio. Copy the following snippet once to create a calibration clip and a separate validation clip:

```bash
python3 - <<'PY'
import wave
from pathlib import Path

source_path = Path("silero-vad-work/assets/test.wav")
clips = (("calibration.wav", 0.0), ("validation.wav", 2.5))

with wave.open(str(source_path), "rb") as source:
    parameters = source.getparams()
    if (
        parameters.nchannels,
        parameters.sampwidth,
        parameters.framerate,
        parameters.comptype,
    ) != (1, 2, 16000, "NONE"):
        raise SystemExit("test.wav must be mono, 16 kHz, 16-bit PCM")
    if source.getnframes() < 5 * parameters.framerate:
        raise SystemExit("test.wav does not contain five seconds of audio")
    for name, start_seconds in clips:
        source.setpos(int(start_seconds * parameters.framerate))
        frames = source.readframes(int(2.5 * parameters.framerate))
        if len(frames) != 40000 * parameters.sampwidth:
            raise SystemExit(f"Could not create a 2.5-second {name} clip")
        with wave.open(str(source_path.with_name(name)), "wb") as target:
            target.setparams(parameters)
            target.writeframes(frames)
PY
```

Use `calibration.wav` to calibrate quantization. The FVP will process the separate `validation.wav` clip.
