---
id: "alp-observing-ethos-u-on-nxp-4-environment-setup-for-macos-build-executorch-in"
type: "concept"
domain: "edge-ai"
title: "4 environment setup: For macOS: build ExecuTorch in a Docker container"
summary: "On macOS, it’s easiest to build ExecuTorch in an Ubuntu container."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/4-environment-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/4-environment-setup/#for-macos-build-executorch-in-a-docker-container"
license: "CC-BY-SA-4.0"
mode: "V"
---

On macOS, it’s easiest to build ExecuTorch in an Ubuntu container. This keeps your toolchain consistent with the rest of the Learning Path and avoids gaps in macOS-native cross-compilers (for example, the Arm GNU Toolchain doesn’t provide an “AArch64 GNU/Linux target” for macOS).

This container isn’t part of the runtime deployment. It’s a build environment that produces the artifacts you later move onto the FRDM i.MX 93:

- Prebuilt ExecuTorch libraries you link into Cortex-M33 firmware
- `.pte` model files compiled for Ethos-U65

Keeping this step reproducible helps you focus on the actual bring-up milestone: booting custom firmware on Cortex-M33 and using Ethos-U65 for inference.

Start by installing and launching [Docker Desktop](https://www.docker.com/).

Next, create a working directory for your container build:

   ```bash
   mkdir ubuntu-24-container
   ```

Now create a `Dockerfile` and switch into the directory:

   ```bash
   cd ubuntu-24-container
   touch Dockerfile
   ```

Add the following content to your `Dockerfile` to install a few basic tools in the image:

   ```dockerfile
   FROM ubuntu:24.04

   ENV DEBIAN_FRONTEND=noninteractive

   RUN apt update -y && \
       apt install -y \
       software-properties-common \
       curl vim git
   ```

   The `ubuntu:24.04` container image includes Python 3.12, which you use later in this Learning Path.

   Build the container image:

   ```bash
   docker build -t ubuntu-24-container .
   ```

Run the container and open an interactive shell:

   ```bash { output_lines = "2-3" }
   docker run -it ubuntu-24-container /bin/bash
   # Output will be the Docker container prompt
   root@<CONTAINER ID>:/#
   ```

If you already created a container before, reuse it instead of creating a new one.

First, list your containers to find the container ID:

```bash { output_lines = "2-4" }
docker ps -a
# Output
CONTAINER ID  IMAGE                    COMMAND      CREATED        STATUS                       PORTS  NAMES
0123456789ab  ubuntu-24-container  "/bin/bash"  27 hours ago   Exited (255) 59 minutes ago.        container_name
```

Then start the container and attach a shell:

```bash
docker start 0123456789ab
docker exec -it 0123456789ab /bin/bash
```

Once you’re inside the container, move to your home directory:

```bash
cd /root
```
