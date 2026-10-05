---
id: "ceed-ceedling-cipher-quest-project-release-build"
type: "concept"
domain: "test"
title: "Ceedling Cipher Quest Project: Release Build"
summary: "The :defines: :release: section in project.yml is intentionally empty. A plain ceedling release will fail at the compilation of main.c with a descriptive error:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/snapshot/examples/cipher_quest/README.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/snapshot/examples/cipher_quest/#release-build"
license: "MIT"
mode: "V"
---

The `:defines: :release:` section in `project.yml` is intentionally empty.
A plain `ceedling release` will **fail** at the compilation of `main.c` with
a descriptive error:

```
error: "cipher_quest: No feature defined. An agent needs tools. ..."
```

To build a release binary, supply one or more feature symbols via a mixin.

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

### Using a mixin file (optional `@` sigil)

```sh
# ROT13 variant
ceedling release --mixin=@mixin/release_rot13.yml

# Caesar cipher variant
ceedling release --mixin=@mixin/release_caesar.yml

# Analysis variant
ceedling release --mixin=@mixin/release_analyze.yml

# Full-featured: All capabilities enabled
ceedling release --mixin=@mixin/release_full.yml
```

Mixin files are simple YAML fragments that merge into the project
configuration. For example, `mixin/release_rot13.yml` contains:

```yaml
:defines:
  :release:
    - CIPHER_ROT13
```

Ceedling deep-merges this with `project.yml`, adding `CIPHER_ROT13` to the
release compilation flags without modifying the base project file.

### Using inline YAML mixin (`=` sigil)

Rather than referencing a file, YAML can be supplied directly on the command
line using the `=` sigil prefix. Quote the value to protect YAML special
characters (colons, brackets, spaces) from shell interpretation:

```sh
# ROT13 variant
ceedling release --mixin "=defines: {release: [CIPHER_ROT13]}"

# Caesar cipher variant
ceedling release --mixin "=defines: {release: [CIPHER_CAESAR]}"

# All features enabled
ceedling release --mixin "=defines: {release: [CIPHER_ROT13, CIPHER_CAESAR, ANALYZER_ENABLED]}"
```

Multiple `--mixin` values can be combined and are processed left-to-right:

```sh
ceedling release --mixin @mixin/release_rot13.yml --mixin "=project: {build_root: ci_build}"
```

---
