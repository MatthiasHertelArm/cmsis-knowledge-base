---
id: "ceed-using-unity-cmock-cexception-cmock-configuration"
type: "concept"
domain: "test"
title: "Using Unity, CMock & CException: CMock Configuration"
summary: "CMock is enabled in Ceedling by default. However, no part of it enters a test build unless mock generation is triggered in your test files. Triggering mock generation is done by an #include convention."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/frameworks.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/frameworks/#cmock-configuration"
license: "MIT"
mode: "V"
---

CMock is enabled in Ceedling by default. However, no part of it enters a
test build unless mock generation is triggered in your test files. 
Triggering mock generation is done by an `#include` convention. See the
section on [Ceedling conventions and behaviors](https://throwtheswitch.github.io/Ceedling/testing-guide/frameworks/conventions.md) for more.

You are welcome to disable CMock in the `:project` block of your Ceedling
configuration file. This is typically only useful in special debugging
scenarios or for Ceedling development itself.

CMock is a mixture of Ruby and C code. CMock’s Ruby components generate
C code for your unit tests. CMock’s base C code is compiled and linked into 
a test executable in the same way that any C file is — including Unity, 
CException, and generated mock C code, for that matter. 

CMock’s code generation can be configured using YAML similar to Ceedling 
itself. Ceedling’s project file is something of a container for CMock’s 
YAML configuration (Ceedling also uses CMock’s configuration, though).

See the documentation for the top-level [`:cmock`][cmock-yaml-config] 
section within Ceedling’s project file.

[cmock-yaml-config]: ../configuration/reference/cmock.md

Like Unity and CException, CMock’s C components are configured at 
compilation with symbols managed in your Ceedling project file’s 
`:cmock` ↳ `:defines` section.

### Example CMock configurations

```yaml
:project:
  # Shown for completeness -- CMock enabled by default in Ceedling
  :use_mocks: TRUE

:cmock:
  :when_no_prototypes: :warn
  :enforce_strict_ordering: TRUE
  :defines:
    # Memory alignment (packing) on 16 bit boundaries
    - CMOCK_MEM_ALIGN=1
  :plugins:
    - :ignore
  :treat_as:
    uint8:    HEX8
    uint16:   HEX16
    uint32:   UINT32
    int8:     INT8
    bool:     UINT8
```
