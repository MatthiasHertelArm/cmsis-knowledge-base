---
id: "cmlek-mlek-video-application-object-detection-application"
type: "concept"
domain: "edge-ai"
title: "MLEK Video Application: Object Detection Application"
summary: "This example uses a neural network model that specialises in detecting human faces in images. The input size for these images is 192x192 (monochrome) and the smallest face that can be detected is of size 20x20."
status: "draft"
collection: "cmsis-mlek-packs"
source: "Arm-Examples/cmsis-mlek@6d60f43:docs/templates_video.md"
doc_source: "https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/docs/templates_video.md#object-detection-application"
license: "Apache-2.0"
mode: "V"
---

This example uses a neural network model that specialises in detecting human faces in images.
The input size for these images is 192x192 (monochrome) and the smallest face that can be detected is of size 20x20. The output of the application will be co-ordinates for rectangular bounding boxes for each detection.

### Build Types
The Object Detection example defines four build types that control debug information and the video source:

| Build Type | Description |
|------------|-------------|
| **Debug-Live_Stream** | Capture frames from a camera in real time. Debug information enabled. |
| **Release-Live_Stream** | Capture frames from a camera in real time. With optimizations for performance. |
| **Debug-Data_Array** |  Built-in image data for regression testing with debug information. |
| **Release-Data_Array** | Built-in image data with release optimizations. |

Use the Debug build types during development and the Release build types for performance measurements. Switch between *Live_Stream* and *Data_Array* depending on whether you want real-time video or a fixed sample. On Arm Virtual Hardware Targets, the Live_Stream is utilizing the VSI interface
