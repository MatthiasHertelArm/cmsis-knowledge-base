---
id: "alp-silero-vad-ethos-u-3-run-on-fvp-build-the-silero-vad-applicati"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Build and run the Corstone-320 application: Build the Silero VAD application"
summary: "Configure the application with the exported model, validation audio, and a speech threshold of 0.55."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/3-run-on-fvp.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/3-run-on-fvp/#build-the-silero-vad-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

Configure the application with the exported model, validation audio, and a speech threshold of `0.55`. 

Select your host operating system:


  **Linux:**
cmake \
  -S examples/arm/silero_vad_example_ethos_u/runtime \
  -B silero-vad-work/app \
  -DCMAKE_TOOLCHAIN_FILE="$PWD/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake" \
  -DET_BUILD_DIR_PATH="$PWD/cmake-out-arm" \
  -DTARGET_CPU=cortex-m85 \
  -DET_PTE_FILE_PATH="$PWD/silero-vad-work/export/silero_vad_ethos_u.pte" \
  -DAUDIO_PATH="$PWD/silero-vad-work/assets/validation.wav" \
  -DVAD_THRESHOLD=0.55 \
  -DPYTHON_EXECUTABLE="$(command -v python)"
  
  **macOS:**
cmake \
  -S examples/arm/silero_vad_example_ethos_u/runtime \
  -B silero-vad-work/app \
  -DCMAKE_TOOLCHAIN_FILE="$PWD/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake" \
  -DET_BUILD_DIR_PATH="$PWD/cmake-out-arm" \
  -DTARGET_CPU=cortex-m85 \
  -DET_PTE_FILE_PATH="$PWD/silero-vad-work/export/silero_vad_ethos_u.pte" \
  -DAUDIO_PATH="$PWD/silero-vad-work/assets/validation.wav" \
  -DVAD_THRESHOLD=0.55 \
  -DUART0_BASE=0x49303000 \
  -DPYTHON_EXECUTABLE="$(command -v python)"
  


Build the configured application:

```bash
cmake --build silero-vad-work/app \
  --target silero_vad_ethos_u --parallel
```

The build creates `silero-vad-work/app/silero_vad_ethos_u`. This ELF image contains both the `.pte` model and the 2.5-second validation clip.
