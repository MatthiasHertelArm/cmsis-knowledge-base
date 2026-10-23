---
id: "ceed-dependencies-so-how-does-all-this-magic-work"
type: "concept"
domain: "test"
title: "Dependencies: So how does all this magic work?"
summary: "Enable the plugin in your project configuration, then list your dependencies under :dependencies ↳ :deps. Each dependency has a series of fields, most of them optional. If you don’t need a feature, leave its field out."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#so-how-does-all-this-magic-work"
license: "MIT"
mode: "V"
---

Enable the plugin in your project configuration, then list your dependencies under
`:dependencies` ↳ `:deps`. Each dependency has a series of fields, most of them optional.
If you don’t need a feature, leave its field out. In the end, it looks something like
this:

```yaml
:plugins:
  :enabled:
    - dependencies

:dependencies:
  :deps:
    - :name: WolfSSL
      :paths:
        :fetch:    third_party/wolfssl/source
        :source:   third_party/wolfssl/source
        :build:    third_party/wolfssl/build
        :artifact: third_party/wolfssl/install
      :fetch:
        :method: :zip
        :source: \\shared_drive\third_party_libs\wolfssl\wolfssl-4.2.0.zip
      :environment:
        - CFLAGS+=-DWOLFSSL_DTLS_ALLOW_FUTURE
      :build:
        - autoreconf -i
        - ./configure --enable-tls13 --enable-singlethreaded
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
