---
id: "intr-building-an-on-device-embedded-tes-basic-implementation-details"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Basic Implementation Details"
summary: "Both the reactor and the controller are C++ objects, testing_reactor and testing_controller respectively. They also expect to be provided with user-supplied objects that implement the interfaces testing_reactor_interface and testing_controller_interface."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#basic-implementation-details"
license: "CC-BY-SA-4.0"
mode: "V"
---

Both the reactor and the controller are C++ objects, `testing_reactor` and `testing_controller` respectively. They also expect to be provided with user-supplied objects that implement the interfaces `testing_reactor_interface` and `testing_controller_interface`.
The interfaces are implemented by the user and define how the object interacts with its environment.

In the case of the embedded firmware, one creates an instance of the reactor, registers tests into it, and passes control to the reactor.
This is done in a way that still gives the user some control over the main loop:
```cpp
emlabcpp::testing_basic_reactor rec{"test suite name"};
my_reactor_interface rif{..};
// register tests

while(true){
   rec.tick(rif);
}
```

The reactor expects that its `tick` method is called repeatedly and that the method contains one iteration of the reactor's control loop.
It either answers the reactor in the control loop or executes the entire test during one `tick` call. This means it can block for a while.

The `controller` has similar behavior and interface. With the exception that the `controller_interface` also contains customization points for additional features:
- methods to provide input data for tests on request
- `on_test(emlabcpp::testing_result)` method that is called with results of one test call
- `on_error` method is called once an error happens in the library.

It's up to the user to implement the interface for the specific use case or use existing implementations (the library may provide some).
