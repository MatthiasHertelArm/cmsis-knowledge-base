---
id: "alp-migration-4-development-environmen"
type: "concept"
domain: "project"
title: "Development environment"
summary: "The original application uses GNU Compiler Collection (GCC) so you want to create a development environment with this compiler and with the same version (when possible)."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/migration/4_development_environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/migration/4_development_environment/"
license: "CC-BY-SA-4.0"
mode: "V"
---

The original application uses GNU Compiler Collection ([GCC](https://gcc.gnu.org/)) so you want to create a development environment with this compiler and with the same version (when possible). To migrate the application to `aarch64`, you can use the same `x86_64` machine you used to run the application. You can use an `aarch64` container for your development environment which allows you to compile and run the ported application on the `x86_64` machine.

See [Docker Engine](https://learn.arm.com/install-guides/docker/docker-engine/) for instructions how to install Docker in your Linux environment.
