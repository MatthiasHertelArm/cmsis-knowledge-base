---
id: "alp-migration-4-development-environmen-run-the-container"
type: "concept"
domain: "project"
title: "Development environment: Run the container"
summary: "Finally, run the aarch64 container on the x86_64 machine. Because the application will open a few X windows to display the image results, you need to enable graphical display when launching the container."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/migration/4_development_environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/migration/4_development_environment/#run-the-container"
license: "CC-BY-SA-4.0"
mode: "V"
---

Finally, run the `aarch64` container on the `x86_64` machine. Because the application will open a few X windows to display the image results, you need to enable graphical display when launching the container. 

Run the commands below:

```bash
xhost +local:*
docker run -it --rm --platform linux/aarch64 --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_gcc_example /bin/bash
```

Now that you have the development environment running, you can port the Sobel filter application.
