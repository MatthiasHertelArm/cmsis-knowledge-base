---
id: "avh-vstream-via-vsi-virtual-streaming-interface-for-python"
type: "concept"
domain: "test"
title: "vStream via VSI: Virtual Streaming Interface for Python"
summary: "Directory python contains Python scripts that implement VSI for Python and execute on host PC. Audio and video servers are implemented independently to support access to audio and video streams."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:interface/vstream/README.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/interface/vstream/README.md#virtual-streaming-interface-for-python"
license: "Apache-2.0"
mode: "V"
---

Directory `python` contains Python scripts that implement [VSI for Python](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vsi__py.html)
and execute on host PC. Audio and video servers are implemented independently to support access to audio and video streams.

**VSI scripts for Python**:

The `arm_vsi*.py` files provide VSI implementations for different channels.

- `arm_vsi0.py` and `arm_vsi1.py` implement Audio streaming channels
- `arm_vsi4/vsi5/vsi6/vsi7.py` - implement Video streaming channels

**Audio Server**:

- `vsi_audio_server.py` and
- `vsi_audio.py`

  implement Python server and client for audio streaming using PyAudio.

**Video Server**:

- `vsi_video_server.py` and
- `vsi_video.py`

  implement Python server and client for video streaming using OpenCV.

### Audio Server

The Audio Server implements a TCP-based server for audio streaming operations using PyAudio. It provides comprehensive audio I/O capabilities for both real-time audio devices and file-based streaming.

**Key Features**:

- Supports both audio input (microphone/file recording) and audio output (speaker/file playback)
- Supports automatic detection and configuration of system audio devices
- Supports WAV file reading and writing
- Allows multiple client connections

### Video Server

The Video Server implements a TCP-based server for video streaming operations using OpenCV. It provides video I/O capabilities for accessing cameras and video files.

**Key Features**:

- Supports both video input (camera/file capture) and video output (display/file recording)
- Supports access to system cameras and USB video devices
- Supports multiple video formats (AVI, MP4, WMV) and image formats (BMP, PNG, JPG)
- Supports frame-by-frame processing with automatic format conversion
- Allows multiple client connections
