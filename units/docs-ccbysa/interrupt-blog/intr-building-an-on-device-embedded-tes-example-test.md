---
id: "intr-building-an-on-device-embedded-tes-example-test"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Example Test"
summary: "I tried to prepare a simple interface for the registration of tests, as I believe that tests should be easy to write."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#example-test"
license: "CC-BY-SA-4.0"
mode: "V"
---

I tried to prepare a simple interface for the registration of tests, as I believe that tests should be easy to write.
I generally do not mind some cost of setting up the library, but I think that adding tests should be easy. 

To guide the explanation, let's assert we are testing a wending machine:

```cpp
   emlabcpp::testing_basic_reactor rec{"test suite for wending machine"};

   rec.register_callable("my simple test", [&]( emlabcpp::testing_record & rec){

      int product_id = rec.get_arg<int>("product_id");

      rec.expect( product_id < MAX_PRODUCTS_N );

      wending_machine::release_product(product_id);

      rec.collect( "released: ", product_id );

      bool occupied = wending_machine::is_takeout_area_occupied();

      rec.expect( occupied );
   });
```

What happens here is that the lambda function is registered as a test.
That test is identified by the "my simple test" string, used to identify it from the controller.

Once the test is executed (the controller tells the reactor to execute it), it is provided with a `testing_record` object that serves as an API between the test and the reactor.

The testing code should use the record to get any data from the controller, collect any data during the test, and primarily, provide information whenever the test failed or succeeded.

In the example, you can see the usage of all the primitives:
 - `rec.get_arg<int>("product_id")` tells the reactor to ask the controller for an argument with key `product_id` and retrieve it as integer type
 - `rec.expect( product_id < MAX_PRODUCTS_N )` is a form checking properties in the test - if `false` is passed to the `expect(bool)` method the test is marked as failed.
 - `rec.collect("released: ", product_id )` collects the data `product_id` with key `released: ` and sends it to the controller.
