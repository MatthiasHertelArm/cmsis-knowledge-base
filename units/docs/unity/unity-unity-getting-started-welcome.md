---
id: "unity-unity-getting-started-welcome"
type: "concept"
domain: "test"
title: "Unity - Getting Started: Welcome"
summary: "Congratulations. You're now the proud owner of your very own pile of bits! What are you going to do with all these ones and zeros? This document should be able to help you decide just that."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityGettingStartedGuide.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityGettingStartedGuide.md#welcome"
license: "MIT"
mode: "V"
---

Congratulations.
You're now the proud owner of your very own pile of bits!
What are you going to do with all these ones and zeros?
This document should be able to help you decide just that.

Unity is a unit test framework.
The goal has been to keep it small and functional.
The core Unity test framework is three files: a single C file and a couple header files.
These team up to provide functions and macros to make testing easier.

Unity was designed to be cross-platform.
It works hard to stick with C standards while still providing support for the many embedded C compilers that bend the rules.
Unity has been used with many compilers, including GCC, IAR, Clang, Green Hills, Microchip, and MS Visual Studio.
It's not much work to get it to work with a new target.

### Overview of the Documents

#### Unity Assertions reference

This document will guide you through all the assertion options provided by Unity.
This is going to be your unit testing bread and butter.
You'll spend more time with assertions than any other part of Unity.

#### Unity Assertions Cheat Sheet

This document contains an abridged summary of the assertions described in the previous document.
It's perfect for printing and referencing while you familiarize yourself with Unity's options.

#### Unity Configuration Guide

This document is the one to reference when you are going to use Unity with a new target or compiler.
It'll guide you through the configuration options and will help you customize your testing experience to meet your needs.

#### Unity Helper Scripts

This document describes the helper scripts that are available for simplifying your testing workflow.
It describes the collection of optional Ruby scripts included in the auto directory of your Unity installation.
Neither Ruby nor these scripts are necessary for using Unity.
They are provided as a convenience for those who wish to use them.

#### Unity License

What's an open source project without a license file?
This brief document describes the terms you're agreeing to when you use this software.
Basically, we want it to be useful to you in whatever context you want to use it, but please don't blame us if you run into problems.

### Overview of the Folders

If you have obtained Unity through Github or something similar, you might be surprised by just how much stuff you suddenly have staring you in the face.
Don't worry, Unity itself is very small.
The rest of it is just there to make your life easier.
You can ignore it or use it at your convenience.
Here's an overview of everything in the project.

- `src` - This is the code you care about! This folder contains a C file and two header files.
  These three files _are_ Unity.
- `docs` - You're reading this document, so it's possible you have found your way into this folder already.
  This is where all the handy documentation can be found.
- `examples` - This contains a few examples of using Unity.
- `extras` - These are optional add ons to Unity that are not part of the core project.
  If you've reached us through James Grenning's book, you're going to want to look here.
- `test` - This is how Unity and its scripts are all tested.
  If you're just using Unity, you'll likely never need to go in here.
  If you are the lucky team member who gets to port Unity to a new toolchain, this is a good place to verify everything is configured properly.
- `auto` - Here you will find helpful Ruby scripts for simplifying your test workflow.
  They are purely optional and are not required to make use of Unity.
