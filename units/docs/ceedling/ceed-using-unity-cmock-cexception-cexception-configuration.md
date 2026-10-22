---
id: "ceed-using-unity-cmock-cexception-cexception-configuration"
type: "concept"
domain: "test"
title: "Using Unity, CMock & CException: CException Configuration"
summary: "Like Unity, CException is wholly compiled C code. As such, its configuration is entirely controlled by a variety of #define symbols. These can be configured in Ceedling’s :cexception ↳ :defines project settings."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/frameworks.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/frameworks/#cexception-configuration"
license: "MIT"
mode: "V"
---

Like Unity, CException is wholly compiled C code. As such, its 
configuration is entirely controlled by a variety of `#define` symbols. 
These can be configured in Ceedling’s `:cexception` ↳ `:defines` project 
settings.

Unlike Unity which is always available in test builds and CMock that 
defaults to available in test builds, CException must be enabled
if you wish to use it in your project.

### Example CException configurations

```yaml
:project:
  # Enable CException for both test and release builds
  :use_exceptions: TRUE

:cexception:
  :defines:
    # Possible exception codes of -127 to +127 
    - CEXCEPTION_T='signed char'

```

[Unity]: http://github.com/ThrowTheSwitch/Unity
[CMock]: http://github.com/ThrowTheSwitch/CMock
[CException]: http://github.com/ThrowTheSwitch/CException
