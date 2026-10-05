---
id: "ceed-cipher-quest-release-builds"
type: "concept"
domain: "test"
title: "`cipher_quest`: Release builds"
summary: "The release build requires symbol definitions not active in the default project configuration. That is, without specifying at least one symbol corresponding to a feature set, the release build will fail."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/getting-started/example-projects/cipher-quest.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/cipher-quest/#release-builds"
license: "MIT"
mode: "V"
---

The release build requires symbol definitions not active in the default project
configuration. That is, without specifying at least one symbol corresponding to
a feature set, the release build will fail. The test build is configured such
that each set of tests enables the symbol needed by the source under test.

Symbols needed by the release build can be provided by:

1. Editing the [`:defines` section](https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/cipher-quest/../../configuration/reference/defines.md)
   of the example project file.
2. Making use of [Mixins](https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/cipher-quest/../../configuration/mixins.md)
   to selectively enable the needed symbols. The example project includes 
   mixin files, and the project README provides examples of enacting all 
   availble Mixin features.

---

Below is example help output produced by running the executable with no
command line arguments. This executable was a result of a release build 
with `CIPHER_ROT13` defined.

```shell
> build/release/cipher_quest.out

Usage: cipher_quest <command> [args...]

Core commands (always available):
  reverse <text>             Reverse the characters
  upper <text>               Convert to uppercase
  lower <text>               Convert to lowercase
  trim <text>                Strip leading/trailing whitespace
  palindrome <text>          Simple palindrome check (exact characters)
  wordcount <text>           Count words

Cipher: ROT13
  rot13 <text>               Encode or decode (ROT13 is its own inverse)
```
