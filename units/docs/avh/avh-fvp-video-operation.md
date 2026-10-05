---
id: "avh-fvp-video-operation"
type: "concept"
domain: "test"
title: "FVP Video: Operation"
summary: "The application initializes both video input and output streams and then continuously captures video frames from the input stream and copies them to the output stream. Application assumes that the video frame pixel format is RGB888."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:example/FVP_Video/README.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/example/FVP_Video/README.md#operation"
license: "Apache-2.0"
mode: "V"
---

The application initializes both video input and output streams and then continuously
captures video frames from the input stream and copies them to the output stream.
Application assumes that the video frame pixel format is RGB888.

If input and output stream resolutions differ the input frame is centered within the
output frame and/or cropped when required.

Streaming stops after receiving the `END_OF_STREAM` event or can be configured to
stop after `AUDIO_STREAM_DURATION` seconds.

The example uses CMSIS-RTOS2 for thread management and event-driven processing.

### Configuration

Default configuration ([app_config.h](https://github.com/ARM-software/AVH/blob/bb8431b/example/FVP_Video/project/app_config.h)) expects the following input
and output stream format:

- 640 x 480 pixels, 30FPS

To change the default configuration use the following defines:

- `VIDEO_IN_FRAME_WIDTH`   - the input video stream frame width in pixels
- `VIDEO_IN_FRAME_HEIGHT`  - the input video stream frame height in pixels
- `VIDEO_OUT_FRAME_WIDTH`  - the output video stream frame width in pixels
- `VIDEO_OUT_FRAME_HEIGHT` - the output video stream frame height in pixels
- `VIDEO_FRAME_RATE`       - the video frame rate in frames per second

The default streaming duration is indefinite. To change this, use:

- `VIDEO_STREAM_DURATION` - sets the streaming duration in seconds (0: stream indefinitely)
