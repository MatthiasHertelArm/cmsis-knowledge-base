---
id: "avh-vstream-via-vsi-vstream-drivers"
type: "concept"
domain: "test"
title: "vStream via VSI: vStream Drivers"
summary: "Directory source contains CMSIS-Driver vStream implementations for audio input/output and video input/output streaming."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@60f78be:interface/vstream/README.md"
doc_source: "https://github.com/ARM-software/AVH/blob/60f78be/interface/vstream/README.md#vstream-drivers"
license: "Apache-2.0"
mode: "V"
---

Directory `source` contains CMSIS-Driver vStream implementations for audio input/output
and video input/output streaming.

**Audio Drivers**:

- `vstream_audio_in.c/h`  - vStream_AudioIn implementation
- `vstream_audio_out.c/h` - vStream_AudioOut implementation

**Video Drivers**:

- `vstream_video_in.c/h`  - vStream_VideoIn implementation
- `vstream_video_out.c/h` - vStream_VideoOut implementation

### Configuration for vStream Drivers

Directory `config` contains configuration headers for vStream drivers.

Configuration enables user to configure basic audio and video stream parameters
to adapt vStream driver to embedded application expectation.

**Configuration Files**:

- `vstream_audio_in_config.h`  - configures vStream_AudioIn
- `vstream_audio_out_config.h` - configures vStream_AudioOut
- `vstream_video_in_config.h`  - configures vStream_VideoIn
- `vstream_video_out_config.h` - configures vStream_VideoOut

**Audio Stream Configuration**:

Configuration options for configuring vStream audio drivers are:

| Parameter                 | Description                                          | Available Options               | Configuration Macro          |
|---------------------------|------------------------------------------------------|---------------------------------|------------------------------|
| Number of channels        | Defines the number of audio channels in stream       | Mono (1), Stereo (2)            | `AUDIO_[IN/OUT]_CHANNELS`    |
| Number of bits per sample | Defines number of bits of information in each sample | 8-bit, 16-bit, 24-bit, 32-bit   | `AUDIO_[IN/OUT]_SAMPLE_BITS` |
| Sample rate               | Defines the number of samples per second             | 8 kHz, 16 kHz, 44.1 kHz, 48 kHz | `AUDIO_[IN/OUT]_SAMPLE_RATE` |

**Video Stream Configuration**:

Configuration options for configuring vStream Video drivers are:

| Parameter    | Description                                              | Available Options               | Configuration Macro           |
|--------------|----------------------------------------------------------|---------------------------------|-------------------------------|
| Frame width  | Defines the video stream frame width in pixels           | User-defined (e.g., 320, 640)   | `VIDEO_[IN/OUT]_FRAME_WIDTH`  |
| Frame height | Defines the video stream frame height in pixels          | User-defined (e.g., 240, 480)   | `VIDEO_[IN/OUT]_FRAME_HEIGHT` |
| Frame rate   | Defines the video stream frame rate in frames per second | User-defined (e.g., 15, 30, 60) | `VIDEO_[IN/OUT]_FRAME_RATE`   |
| Color format | Defines the video frame color space                      | Grayscale, RGB888, BGR565       | `VIDEO_[IN/OUT]_FRAME_COLOR`  |

**Common Configuration**:

Besides stream configuration there are configuration options related to stream source selection. The below table shows possible stream sources:

| Stream Type   | Stream Source         | Description                                   | Configuration                            |
|---------------|-----------------------|-----------------------------------------------|------------------------------------------|
| **Audio In**  | System Default Input  | Uses the system's default audio input device  | `AUDIO_IN_DEVICE = -1`                   |
|               | Specific Audio Device | Uses a specific audio input device by index   | `AUDIO_IN_DEVICE = <device_index>`       |
|               | Audio File            | Reads audio data from a file                  | `AUDIO_IN_FILENAME = "path/to/file.wav"` |
| **Audio Out** | System Default Output | Uses the system's default audio output device | `AUDIO_OUT_DEVICE = -1`                  |
|               | Specific Audio Device | Uses a specific audio output device by index  | `AUDIO_OUT_DEVICE = <device_index>`      |
|               | Audio File            | Writes audio data to a file                   | `AUDIO_OUT_FILENAME = "path/to/file.wav"`|
| **Video In**  | System Default Input  | Uses the system's default video input device  | `VIDEO_IN_DEVICE = -1`                   |
|               | Specific Input Device | Uses a specific camera device by index        | `VIDEO_IN_DEVICE = <device_index>`       |
|               | Video File            | Reads video frames from a file                | `VIDEO_IN_FILENAME = "path/to/file.mp4"` |
| **Video Out** | Display Window        | Displays video frames in a window             | No device configuration needed           |
|               | Video File            | Writes video frames to a file                 | `VIDEO_OUT_FILENAME = "path/to/file.mp4"`|

> [!NOTE]
>
> OpenCV is not able to automatically detect system default device. Instead it enumerates devices, for example:
>
> - 0 being the internal camera
> - 1 is the first external camera
