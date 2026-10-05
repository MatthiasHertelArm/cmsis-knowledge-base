---
id: "alp-avh-balena-3install-verify-your-device-is-ready"
type: "concept"
domain: "project"
title: "Deploy IoT applications with Balena Cloud and Arm Virtual Hardware: Install Balena OS on AVH: Verify your device is ready"
summary: "You now have access to the console and are presented with a log in prompt."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_balena/3install.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_balena/3install/#verify-your-device-is-ready"
license: "CC-BY-SA-4.0"
mode: "V"
---

You now have access to the console and are presented with a log in prompt. 

Log in with the username `root`. If a password is required, use `balena`.

Balena OS uses a container engine to manage applications.

Verify `balena` available by running:

```console
balena version
```

You'll see output similar to:

```output
Client:
 Version:           v20.10.38
 API version:       1.41
 Go version:        go1.16.2
 Git commit:        8f374c29395adff1f6f7796b06418e593a479a7d
 Built:             Mon Jul  3 14:00:08 2023
 OS/Arch:           linux/arm64
 Context:           default
 Experimental:      true

Server:
 Engine:
  Version:          v20.10.38
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.16.2
  Git commit:       8f374c29395adff1f6f7796b06418e593a479a7d
  Built:            Mon Jul  3 14:00:08 2023
  OS/Arch:          linux/arm64
  Experimental:     true
 containerd:
  Version:          1.6.6+unknown
  GitCommit:
 runc:
  Version:          unknown
  GitCommit:
 balena-engine-init:
  Version:          0.13.0
  GitCommit:        949e6fa-dirty
```

Return to your Balena Cloud dashboard and refresh the `Devices` page.

You'll see your newly deployed device is registered and connected to your fleet. You're now ready to deploy applications to your device!

(figure: Balena Cloud dashboard showing the Devices page with one Raspberry Pi 4 device connected, online, and ready to receive application deployments in the AVH-Testing fleet#center)
