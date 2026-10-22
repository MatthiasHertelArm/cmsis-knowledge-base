---
id: "ceed-the-mighty-ceedling-project-config-some-yaml-learnin"
type: "concept"
domain: "test"
title: "The Mighty Ceedling Project Configuration File: Some YAML Learnin’"
summary: "We recommend Wikipedia’s entry on YAML and educative.io’s advanced YAML cheatsheet for a simple overview of YAML and its syntax sufficient for understanding your Ceedling project configuration."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/project-file.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/project-file/#some-yaml-learnin"
license: "MIT"
mode: "V"
---

We recommend [Wikipedia’s entry on YAML](http://en.wikipedia.org/wiki/Yaml)
and [educative.io’s advanced YAML cheatsheet](https://www.educative.io/blog/advanced-yaml-syntax-cheatsheet)
for a simple overview of YAML and its syntax sufficient for 
understanding your Ceedling project configuration.

!!! tip "`ceedling dumpconfig` to verify your YAML"
    Ceedling provides a means to export the final result of YAML
    processing for your inspection via [`dumpconfig`](https://throwtheswitch.github.io/Ceedling/configuration/project-file/../getting-started/command-line.md#ceedling-dumpconfig-filepath-sections).
    Dump output includes the resolution of advanced YAML features and 
    Ceedling’s own manipulations. This is a good way to troubleshoot 
    your project configuration.

### YAML highlights & overview

A few points from the preceding references:

* YAML streams are encoded using the set of printable Unicode
  characters, either in UTF-8 or UTF-16.

* White space indentation is used to denote structure; however,
  tab characters are never allowed as indentation.

* Comments begin with the number sign (`#`), can start anywhere
  on a line, and continue until the end of the line unless enclosed
  by quotes.

* List members are denoted by a leading hyphen (`-`) with one member
  per line, or enclosed in square brackets (`[...]`) and separated
  by comma space (`, `).

* Hashes are represented using colon space (`: `) in the form
  `key: value`, either one per line or enclosed in curly braces
  (`{...}`) and separated by comma space (`, `).

* Strings (scalars) are ordinarily unquoted, but may be enclosed
  in double-quotes (`"`), or single-quotes (`'`).

* YAML requires that colons and commas used as list separators
  be followed by a space so that scalar values containing embedded
  punctuation can generally be represented without needing
  to be enclosed in quotes.

### YAML anchors, aliases, and extensions

YAML provides several “shortcuts” for referencing and modifying blocks
of YAML so you can avoid duplication. This is advanced YAML and 
well beyond the scope of Ceedling documentation. However, know that
Ceedling’s YAML parser is entirely capable of handling these advanced 
aspects of YAML.

See this [cheatsheet entry](https://www.educative.io/blog/advanced-yaml-syntax-cheatsheet#anchors) 
and [this guide](https://blog.daemonl.com/2016/02/yaml.html)
for much more on these powerful but finicky features.
