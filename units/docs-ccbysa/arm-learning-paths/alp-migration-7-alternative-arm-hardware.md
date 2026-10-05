---
id: "alp-migration-7-alternative-arm-hardware"
type: "concept"
domain: "project"
title: "Migrating x86_64 workloads to aarch64: Evaluating performance on Arm hardware (Optional): Arm hardware"
summary: "The following Arm hardware has been selected due to their high availability.  Remote hardware  AWS EC2 instances are easily accessible  Physical hardware  Raspberry Pi 4 is a popular off-the-shelf single-board computer"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/migration/7_alternative.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/migration/7_alternative/#arm-hardware"
license: "CC-BY-SA-4.0"
mode: "V"
---

The following Arm hardware has been selected due to their high availability.
* Remote hardware
  * [AWS EC2](https://aws.amazon.com/ec2/) instances are easily accessible
* Physical hardware
  * [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) is a popular off-the-shelf single-board computer

### AWS EC2 with Graviton processors

AWS EC2 instances with Graviton processors use the `aarch64` architecture. Graviton2 and Graviton3 have different vector engine technologies.

* Graviton2 (c6g.medium)
  * Ubuntu 22.04.2 LTS,
  * 16GB storage (default is 8GB)
  * [Arm Neoverse N1](https://www.arm.com/products/silicon-ip-cpu/neoverse/neoverse-n1)
    * 2 x Neon engine 128b vector width
* Graviton3 (c7g.medium)
  * Ubuntu 22.04.2 LTS
  * 16GB storage (default is 8GB)
  * [Arm Neoverse V1](https://www.arm.com/products/silicon-ip-cpu/neoverse/neoverse-v1)
    * 2 x SVE engine 256b vector width (4 x Neon engine 128b vector width support)

For more information on Graviton, refer to [Getting Started with AWS](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/aws/) and the [AWS Graviton Technical Guide](https://github.com/aws/aws-graviton-getting-started).

Create a Graviton instance and connect using `ssh` with the `-X` option to allow for display forwarding. 

Replace `INSERT_KEY_PEM_FILE` and `INSERT_GRAVITON_INSTANCE_IP_ADDRESS` with your SSH key and public IP address: 

```bash
ssh -X -i "INSERT_KEY_PEM_FILE" ubuntu@INSERT_GRAVITON_INSTANCE_IP_ADDRESS
```

Install [Docker Engine](https://learn.arm.com/install-guides/docker/docker-engine/) on the EC2 instance.

### Raspberry Pi 4

The Raspberry Pi is set up like a normal desktop computer and the following is assumed:
* Running Raspberry Pi OS (64-bit)
* Docker is installed
* MicroSD card inserted
* Display, mouse and keyboard connected
* Internet connection

Refer to [Get started with the Raspberry Pi 4](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/rpi/) for more information about using the Raspberry Pi 4 for software development, including how to install Docker engine.
