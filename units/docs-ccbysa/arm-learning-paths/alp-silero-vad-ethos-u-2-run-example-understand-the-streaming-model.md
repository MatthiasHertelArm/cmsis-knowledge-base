---
id: "alp-silero-vad-ethos-u-2-run-example-understand-the-streaming-model"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Export Silero VAD for Ethos-U85: Understand the streaming model"
summary: "The application supplies one 512-sample audio frame at a time. The exported program keeps the LSTM hidden and cell state between calls. The program produces one speech probability every 32 ms."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/2-run-example.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/2-run-example/#understand-the-streaming-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

The application supplies one 512-sample audio frame at a time. The exported program keeps the LSTM hidden and cell state between calls. The program produces one speech probability every 32 ms.

(figure: Runtime diagram showing 64 context samples and a 512-sample frame entering the ExecuTorch program, model operations delegated to Ethos-U85, an internal int8 hidden and cell state reused between calls, and one speech probability emitted every 32 ms.#center)

The Vela output contains two subgraphs with no CPU operators: the main VAD network and a smaller state-quantization subgraph. Only small boundary conversions and the state update remain as portable ExecuTorch operations.
