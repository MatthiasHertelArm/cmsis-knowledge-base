---
id: "intr-building-an-on-device-embedded-tes-building-the-tests"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Building the Tests"
summary: "The user handles this. The testing framework just provides an object that expects communication API and can register test - how that is assembled into a firmware is up to the user."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#building-the-tests"
license: "CC-BY-SA-4.0"
mode: "V"
---

The user handles this. The testing framework just provides an object that expects communication API and can register test - how that is assembled into a firmware is up to the user.

The idea is that single 'testing firmware' will collect multiple tests registered into one reactor.
It's up to the user to orchestrate the build process in a sensible way.

In the case of CMake, I decided to split the application itself into "application library" and "main executable." 
Most of the logic of the firmware is in the application library, and the main executable just implements the main function and starts up the application library.

The main executable of tests uses that library to prepare and set up tests.
Note that the idea is that there are multiple test binaries with different tests.
I don't assume that all the tests would fit into one binary.

This way, any test firmware is closely similar to the application executable - just with a different main file.

From the controller's perspective, it can be just a simple application that is meant to be executed on GPOS.
