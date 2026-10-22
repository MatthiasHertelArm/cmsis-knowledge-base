---
id: "ceed-environment"
type: "concept"
domain: "test"
title: "`:environment:`"
summary: "Ceedling creates environment variables from any key / value pairs in the :environment section of project configuration."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/environment.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/environment/"
license: "MIT"
mode: "V"
---

**Insert environment variables into the shells running tools**

Ceedling creates environment variables from any key / value pairs in the 
`:environment` section of project configuration.

Keys become an environment variable name in uppercase. Values are strings 
assigned to those environment variables. These value strings are either simple 
string values as provided in the YAML or they are a concatenation of a YAML 
array of strings.

`:environment` is a list of single key / value pair entries processed in the 
configured list order.

!!! note "`:environment` is a key / value YAML hash"
    `:environment` is a list of key / value pairs. Only one key per entry
    is allowed, and that key must be a `:`_<symbol>_. `:environment` is 
    not unusual YAML, but it is a use of YAML unlike other sections of
    project configuration.

`:environment` variable value strings can include 
[inline Ruby string expansion][inline-ruby-string-expansion]. Thus, later 
entries can reference earlier entries.
