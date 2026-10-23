---
id: "unity-unity-getting-started-how-to-build-and-run-a-test-file"
type: "concept"
domain: "test"
title: "Unity - Getting Started: How to Build and Run A Test File"
summary: "This is the single biggest challenge to picking up a new unit testing framework, at least in a language like C or C++. These languages are REALLY good at getting you \"close to the metal\" (why is the phrase metal?"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityGettingStartedGuide.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityGettingStartedGuide.md#how-to-build-and-run-a-test-file"
license: "MIT"
mode: "V"
---

This is the single biggest challenge to picking up a new unit testing framework, at least in a language like C or C++.
These languages are REALLY good at getting you "close to the metal" (why is the phrase metal? Wouldn't it be more accurate to say "close to the silicon"?).
While this feature is usually a good thing, it can make testing more challenging.

You have two really good options for toolchains.
Depending on where you're coming from, it might surprise you that neither of these options is running the unit tests on your hardware.
There are many reasons for this, but here's a short version:

- On hardware, you have too many constraints (processing power, memory, etc),
- On hardware, you don't have complete control over all registers,
- On hardware, unit testing is more challenging,
- Unit testing isn't System testing. Keep them separate.

Instead of running your tests on your actual hardware, most developers choose to develop them as native applications (using gcc or MSVC for example) or as applications running on a simulator.
Either is a good option.
Native apps have the advantages of being faster and easier to set up.
Simulator apps have the advantage of working with the same compiler as your target application.
The options for configuring these are discussed in the configuration guide.

To get either to work, you might need to make a few changes to the file containing your register set (discussed later).

In either case, a test is built by linking unity, the test file, and the C file(s) being tested.
These files create an executable which can be run as the test set for that module.
Then, this process is repeated for the next test file.
This flexibility of separating tests into individual executables allows us to much more thoroughly unit test our system and it keeps all the test code out of our final release!

*Find The Latest of This And More at [ThrowTheSwitch.org][]*

[generate_test_runner.rb]: ../auto/generate_test_runner.rb
[ThrowTheSwitch.org]: https://throwtheswitch.org
