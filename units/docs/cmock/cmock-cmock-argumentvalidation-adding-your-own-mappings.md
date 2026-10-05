---
id: "cmock-cmock-argumentvalidation-adding-your-own-mappings"
type: "concept"
domain: "test"
title: "CMock ArgumentValidation: Adding Your Own Mappings"
summary: "While CMock has its own list of :treat_as mappings, you can add your own pairings to this list. This works especially well for the following types:"
status: "draft"
collection: "cmock"
source: "ThrowTheSwitch/CMock@f2a70b4:docs/CMock_ArgumentValidation.md"
doc_source: "https://github.com/ThrowTheSwitch/CMock/blob/f2a70b4/docs/CMock_ArgumentValidation.md#adding-your-own-mappings"
license: "MIT"
mode: "V"
---

While CMock has its own list of `:treat_as` mappings, you can
add your own pairings to this list. This works especially well for
the following types:

  - aliases of standard types using `#define` or `typedef`
  - `enum` types (works well as `INT8` or whatever size your enums are)
  - function pointers often work well as `PTR` comparisons
  - `union` types sometimes make sense to treat as the largest type...
    but this is a judgement call

Your entries **merge** with the defaults — you are only adding or
overriding specific types, not replacing the entire list. To remove
a default mapping, set its value to `nil`.

Here is a YAML configuration example:

```yaml
:cmock:
  :treat_as:
    MY_BOOL:    INT           # typedef bool MY_BOOL → compare as int
    MY_U8:      HEX8          # typedef uint8_t MY_U8 → compare as hex byte
    MY_U16:     HEX16
    MY_U32:     HEX32
    STATUS_T:   INT8          # small enum → compare as signed byte
    HANDLE_T:   PTR           # opaque pointer → compare pointer addresses
    float:      nil           # remove the default float mapping (unusual)
```

Or from Ruby:

```ruby
CMock.new(
  treat_as: {
    'MY_BOOL'  => 'INT',
    'STATUS_T' => 'INT8',
    'HANDLE_T' => 'PTR',
  }
).setup_mocks('my_module.h')
```
