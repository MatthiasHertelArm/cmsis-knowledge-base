---
id: "intr-building-an-on-device-embedded-tes-the-code"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: The Code"
summary: "The testing library is part of emlabcpp - my personal library, which purpose is for me to have an up-to-date collection of tools for my development."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#the-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

The testing library is part of emlabcpp - my personal library, which purpose is for me to have an up-to-date collection of tools for my development. 
I restrain myself from saying "it should be used by others," as I don't want to care about backward compatibility outside of my projects.

The primary example of the testing library is an example file: [emlabcpp/tests/testing](https://github.com/koniarik/emlabcpp/blob/v1.2/tests/testing_test.cpp)

The interface to the library itself is in: [emlabcpp/include/emlabcpp/experimental/testing](https://github.com/koniarik/emlabcpp/tree/v1.2/include/emlabcpp/experimental/testing)
