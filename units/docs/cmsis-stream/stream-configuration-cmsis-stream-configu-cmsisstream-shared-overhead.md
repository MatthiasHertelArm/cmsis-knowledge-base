---
id: "stream-configuration-cmsis-stream-configu-cmsisstream-shared-overhead"
type: "concept"
domain: "cmsis-stream"
title: "Configuration {#cmsis_stream_configuration}: CMSISSTREAM_SHARED_OVERHEAD"
summary: "Additional memory required by std::allocate_shared."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Doxygen/src/03_configuration.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Doxygen/src/03_configuration.md#cmsisstream-shared-overhead"
license: "Apache-2.0"
mode: "V"
---

Additional memory required by `std::allocate_shared`.

When allocating an object of type `T` with `std::allocate_shared<T>`, enough
memory is needed for `T` and some additional memory required by the
implementation of `std::shared_ptr`. This parameter defines the additional
memory required.

Default value:

```C
#define CMSISSTREAM_SHARED_OVERHEAD 16
```
