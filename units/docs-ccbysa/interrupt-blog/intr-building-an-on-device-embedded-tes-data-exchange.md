---
id: "intr-building-an-on-device-embedded-tes-data-exchange"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Data Exchange"
summary: "The framework provides mechanics to exchange data between the controller and reactor."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#data-exchange"
license: "CC-BY-SA-4.0"
mode: "V"
---

The framework provides mechanics to exchange data between the controller and reactor.

Tests running on the embedded device can request test data from the controller as a form of input.
However, it's up to the user how the controller gets/provides that data.
The request is a blocking communication operation - the input is not stored on the side of the reactor.

The controller can also collect data from the embedded device, as reactors have an API to send data to the controller.
The controller stores the data during test execution, and it is passed to the user once the test is done in test_result.

In the case of input, I use a simple key/value mechanism.
In the case of the collected data, these can be organized into a tree, where each node has key/value pair.

That is, each data point is made of a 'key' that identifies it and its corresponding 'value.'

To give some flexibility, the types are:

- **key**

   can be either string or integer

- **value**

   can be string, integer, bool, unsigned

In each case, the framework can serialize (thanks to the `emlabcpp::protocol` library) and deserialize any types and send them over the communication channel.

As for the strings: These are limited by size to 32 characters, as this way, I can use static buffers for them, and they do not have to be allocated.
