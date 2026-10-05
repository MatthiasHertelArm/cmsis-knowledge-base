---
id: "ceed-environment-variables-reference-console-output-ceedling-decorators"
type: "concept"
domain: "test"
title: "Environment Variables Reference: Console output — `CEEDLING_DECORATORS`"
summary: "Forces Ceedling's console logging decorators (fancy Unicode characters, emoji, and color) on or off."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/reference/environment-vars.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/environment-vars/#console-output-ceedling-decorators"
license: "MIT"
mode: "V"
---

Forces Ceedling's console logging decorators (fancy Unicode characters, emoji,
and color) on or off.

!!! warning "`CEEDLING_DECORATORS` cannot be set with `:environment`"
    Ceedling's logger must load before any environment variables are processed 
    in your project configuration. As such, `CEEDLING_DECORATORS` can only be set 
    in your environment before Ceedling runs.

By default, Ceedling makes an educated guess as to which platforms can best
support decorators. Some platforms (we're looking at you, Windows) do not
typically have default font support in their terminals for these features. So,
by default this feature is disabled on problematic platforms while enabled on
others.

Set `CEEDLING_DECORATORS` to `true` (`1`) to force decorators on, or `false`
(`0`) to force them off.

Example with decorators enabled:

```
-----------------------
❌ OVERALL TEST SUMMARY
-----------------------
TESTED:  6
PASSED:  5
FAILED:  1
IGNORED: 0
```

If you find a monospaced font that provides emojis, etc. and works with Windows'
command prompt, you can (1) Install the font (2) change your command prompt's
font (3) set `CEEDLING_DECORATORS` to `true`.
