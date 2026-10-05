---
id: "vsi-hello-video-vsi-example"
type: "concept"
domain: "debug"
title: "Hello Video VSI Example"
summary: "This example uses the Virtual Streaming Interface (VSI) to simulate an input from a peripheral video sensor."
status: "draft"
collection: "avh-vsi"
source: "Arm-Examples/AVH-VSI@b897fa6:hello_video_vsi/README.md"
doc_source: "https://github.com/Arm-Examples/AVH-VSI/blob/b897fa6/hello_video_vsi/README.md"
license: "Apache-2.0"
mode: "V"
---

This example uses the [Virtual Streaming Interface (VSI)](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vsi.html) to simulate an input from a peripheral video sensor.

Application firmware defines video input configuration in app.c file. The video vsi python scripts read the specified image/video file and send it to the application running on an [AVH FVP Model](https://arm-software.github.io/AVH/main/overview/html/index.html) where it gets displayed on the model LCD screen.

See [Video over VSI documentation](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vsi__video.html) for more information about the implementation of video driver for AVH FVPs.

This is a minimal example of how to use Video over VSI, and you can modify the python script and the video driver in order to match your use case.
