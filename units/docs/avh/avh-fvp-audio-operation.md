---
id: "avh-fvp-audio-operation"
type: "concept"
domain: "test"
title: "FVP Audio: Operation"
summary: "The application initializes both audio input and output streams and then continuously captures audio samples from the input stream and copies them directly to the output stream."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:example/FVP_Audio/README.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/example/FVP_Audio/README.md#operation"
license: "Apache-2.0"
mode: "V"
---

The application initializes both audio input and output streams and then continuously
captures audio samples from the input stream and copies them directly to the output
stream.

Streaming stops after receiving the `END_OF_STREAM` event or can be configured to
stop after `AUDIO_STREAM_DURATION` seconds.

The example uses CMSIS-RTOS2 for thread management and event-driven processing.

### Configuration

Default configuration ([app_config.h](https://github.com/ARM-software/AVH/blob/bb8431b/example/FVP_Audio/project/app_config.h)) expects the following input
and output stream format:

- 16kHz, 16-bit, 2-channels (stereo)

To change the default configuration use the following defines:

- `AUDIO_CHANNELS`    - sets the number of channels in a stream
- `AUDIO_SAMPLE_BITS` - sets the number of bits per sample
- `AUDIO_SAMPLE_RATE` - sets the number of samples per second

The default streaming duration is indefinite. To change this, use:

- `AUDIO_STREAM_DURATION` - sets the streaming duration in seconds (0: stream indefinitely)
