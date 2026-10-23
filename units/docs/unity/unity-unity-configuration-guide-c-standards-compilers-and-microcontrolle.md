---
id: "unity-unity-configuration-guide-c-standards-compilers-and-microcontrolle"
type: "concept"
domain: "test"
title: "Unity Configuration Guide: C Standards, Compilers and Microcontrollers"
summary: "The embedded software world contains its challenges. Compilers support different revisions of the C Standard. They ignore requirements in places, sometimes to make the language more usable in some special regard. Sometimes it's to simplify their support."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityConfigurationGuide.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityConfigurationGuide.md#c-standards-compilers-and-microcontrollers"
license: "MIT"
mode: "V"
---

The embedded software world contains its challenges.
Compilers support different revisions of the C Standard.
They ignore requirements in places, sometimes to make the language more usable in some special regard.
Sometimes it's to simplify their support.
Sometimes it's due to specific quirks of the microcontroller they are targeting.
Simulators add another dimension to this menagerie.

Unity is designed to run on almost anything that is targeted by a C compiler.
It would be awesome if this could be done with zero configuration.
While there are some targets that come close to this dream, it is sadly not universal.
It is likely that you are going to need at least a couple of the configuration options described in this document.

All of Unity's configuration options are `#defines`.
Most of these are simple definitions.
A couple are macros with arguments.
They live inside the unity_internals.h header file.
We don't necessarily recommend opening that file unless you really need to.
That file is proof that a cross-platform library is challenging to build.
From a more positive perspective, it is also proof that a great deal of complexity can be centralized primarily to one place to provide a more consistent and simple experience elsewhere.

### Using These Options

It doesn't matter if you're using a target-specific compiler and a simulator or a native compiler.
In either case, you've got a couple choices for configuring these options:

1. Because these options are specified via C defines, you can pass most of these options to your compiler through command line compiler flags. Even if you're using an embedded target that forces you to use their overbearing IDE for all configuration, there will be a place somewhere in your project to configure defines for your compiler.
2. You can create a custom `unity_config.h` configuration file (present in your toolchain's search paths).
  In this file, you will list definitions and macros specific to your target. All you must do is define `UNITY_INCLUDE_CONFIG_H` and Unity will rely on `unity_config.h` for any further definitions it may need.

Unfortunately, it doesn't usually work well to just #define these things in the test itself.
These defines need to take effect where ever unity.h is included.
This would be the test, the test runner (if you're generating one), and from unity.c when it's compiled.
