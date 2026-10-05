---
id: "ceed-dependencies-so-how-does-all-this-magic-work"
type: "concept"
domain: "test"
title: "Dependencies: So how does all this magic work?"
summary: "First, you need to add the Dependencies plugin to your list of enabled plugins. Then, we'll add a new comfiguration section called :dependencies. There, you can list as many dependencies as you desire."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#so-how-does-all-this-magic-work"
license: "MIT"
mode: "V"
---

First, you need to add the Dependencies plugin to your list of enabled plugins. Then, we'll 
add a new comfiguration section called `:dependencies`. There, you can list as many 
dependencies as you desire. Each has a series of fields that help Ceedling to understand 
your needs. Many of them are optional. If you don't need that feature, just don't include 
it! In the end, it'll look something like this:

```yaml
:plugins:
  :enabled:
    - dependencies

:dependencies:
  :deps:
    - :name: WolfSSL
      :paths:
        :fetch:        third_party/wolfssl/source
        :source:       third_party/wolfssl/source
        :build:        third_party/wolfssl/build
        :artifact_lib: third_party/wolfssl/install
        :artifact_inc: third_party/wolfssl/install
      :fetch:
        :method: :zip
        :source: \\shared_drive\third_party_libs\wolfssl\wolfssl-4.2.0.zip
      :environment:
        - CFLAGS+=-DWOLFSSL_DTLS_ALLOW_FUTURE
      :build:
        - "autoreconf -i"
        - "./configure --enable-tls13 --enable-singlethreaded"
        - make
        - make install
      :artifacts:
        :static_libraries:
          - lib/wolfssl.a
        :dynamic_libraries:
          - lib/wolfssl.so
        :includes:
          - include/**
```
