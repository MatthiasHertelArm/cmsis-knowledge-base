---
id: "alp-yolo-on-himax-web-toolkit-connect-to-the-grove-vision-ai"
type: "concept"
domain: "edge-ai"
title: "Run a computer vision model on a Himax microcontroller: Run additional models in the web toolkit: Connect to the Grove Vision AI"
summary: "Select Grove Vision AI(V2) in the top-right hand corner and press Connect button. Follow the instructions to set up the connection. You should see a video feed with a bounding box showing identified objects, poses or face detection."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/yolo-on-himax/web-toolkit.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/yolo-on-himax/web-toolkit/#connect-to-the-grove-vision-ai"
license: "CC-BY-SA-4.0"
mode: "V"
---

Select `Grove Vision AI(V2)` in the top-right hand corner and press `Connect` button. Follow the instructions to set up the connection. You should see a video feed with a bounding box showing identified objects, poses or face detection.

(figure: Himax web UI)

The images below are captured images from the models run in the toolkit.

### Objection detection
(figure: object_detection)

The Frames Per Second (FPS) index represents the number of ML inferences the hardware can complete per second. A higher number indicates better performance. The colored bounding boxes represent the objects identified by YOLO. The name of the object is labeled in the top left-hand corner of the box, and the number in parentheses is the confidence level as a percentage. This example shows that it can identify 9.53 frames per second with a confidence level of 64% for the 'CPU' object.

### Face detection
(figure: object_detection)

Similar to the previous example, the bounding boxes identify the areas in the image that contain faces and recognize the positions of different facial features. This image shows that YOLO has identified a face with 99% confidence. It has marked the mouth with a yellow line segment and used different colors to mark the eyebrows, eyes, and nose. Within the bounding box for the eyes, it has further identified the gaze direction vector.
