---
id: "cmock-cmock-argumentvalidation-informing-cmock-about-our-assertion"
type: "concept"
domain: "test"
title: "CMock ArgumentValidation: Informing CMock about our Assertion"
summary: "CMock needs to know which header file(s) contain your custom assertions. Set the :unity_helper_path option in your CMock configuration to point at the helper header:"
status: "draft"
collection: "cmock"
source: "ThrowTheSwitch/CMock@f2a70b4:docs/CMock_ArgumentValidation.md"
doc_source: "https://github.com/ThrowTheSwitch/CMock/blob/f2a70b4/docs/CMock_ArgumentValidation.md#informing-cmock-about-our-assertion"
license: "MIT"
mode: "V"
---

CMock needs to know which header file(s) contain your custom assertions.
Set the `:unity_helper_path` option in your CMock configuration to point
at the helper header:

```yaml
:cmock:
  :unity_helper_path:
    - test/support/my_types_helper.h
```

Or from Ruby:

```ruby
CMock.new(unity_helper_path: ['test/support/my_types_helper.h'])
      .setup_mocks('my_module.h')
```

CMock parses each listed file, finds every `UNITY_TEST_ASSERT_EQUAL_*`
macro definition, and uses those macros automatically when it generates
mocks for parameters or return values of the matching types.

Done!

**Bonus:** Once you've created a custom assertion, you can use it
with `:treat_as`, just like any other standard type! This is 
particularly useful when there is a custom type which is a pointer
to a custom type.

For example, let's say you have these types:

```
typedef struct MY_STRUCT_T_
{
    int a;
    const char* b;
} MY_STRUCT_T;

typedef MY_STRUCT_T* MY_STRUCT_POINTER_T;
```

Also, let's assume you've created the following assertion:

```
UNITY_TEST_ASSERT_EQUAL_MY_STRUCT_T(e,a,l,m)
```

You can use `:treat_as` like so:

```
:treat_as:
  MY_STRUCT_POINTER_T: MY_STRUCT_T*
```

Option 4: Callback
------------------

Finally, You can choose to avoid the use of `_Expect` calls altogether
for challenging types, and use a `Callback` instead. The advantage is that
you can fill in whichever assertions make sense for that particular test,
instead of needing to rely on reusable assertions as used elsewhere. 
Typically, this option is also less work than option 3.
