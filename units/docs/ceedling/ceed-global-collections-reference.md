---
id: "ceed-global-collections-reference"
type: "concept"
domain: "test"
title: "Global Collections Reference"
summary: "Collections are Ruby arrays and Rake FileLists (that act like arrays). Ceedling populates and assembles these by processing the project configuration, using internal knowledge, expanding path globs, etc. at startup."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/reference/global-collections.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/global-collections/"
license: "MIT"
mode: "V"
---

Collections are Ruby arrays and Rake FileLists (that act like 
arrays). Ceedling populates and assembles these by
processing the project configuration, using internal knowledge, 
expanding path globs, etc. at startup.

Collections are globally available Ruby constants and are 
typically used in Rakefiles, plugins, and Ruby scripts where 
the contents tend to be especially handy for crafting custom 
functionality.

!!! warning "Collections are no longer a core component of Ceedling"
    As Ceedling has grown in sophistication and as many of its 
    features now operate per test executable, the utility of and
    number of collections has dwindled.
    
    Once upon a time, nearly all Ceedling actions happened in 
    bulk and with the same collections used for all tasks. This 
    is no longer true.
