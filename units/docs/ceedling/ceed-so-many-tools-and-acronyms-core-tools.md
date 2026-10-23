---
id: "ceed-so-many-tools-and-acronyms-core-tools"
type: "concept"
domain: "test"
title: "So Many Tools and Acronyms: Core tools"
summary: "[Ruby] is a handy scripting language like Perl or Python."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/overview/tools-and-frameworks.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/overview/tools-and-frameworks/#core-tools"
license: "MIT"
mode: "V"
---

### Ruby

[Ruby] is a handy scripting language like Perl or Python. It's a modern, 
full featured language that happens to be quite handy for accomplishing 
tasks like code generation or automating one's workflow while developing 
in a compiled language such as C.

[Ruby]: http://www.ruby-lang.org/en/

### Rake

!!! warning "Migrating away from Rake"
    Ceedling would not exist today if not for the help Rake provided to
    get off the ground. As Ceedling matured it became apparent that 
    Rake had become a limitation. The project is slowly removing its
    dependency on Rake.

[Rake] is a utility written in Ruby for accomplishing dependency 
tracking and task automation common to building software. It's a modern, 
more flexible replacement for [Make].

Rakefiles are Ruby files, but they contain build targets similar
in nature to that of Makefiles (but you can also run Ruby code in
your Rakefile).

[Rake]: http://rubyrake.org/
[Make]: http://en.wikipedia.org/wiki/Make_(software)

### YAML

[YAML] is a "human friendly data serialization standard for all
programming languages." It's kinda like a markup language but don't
call it that. With a YAML library, you can [serialize] data structures
to and from the file system in a textual, human readable form. Ceedling
uses a serialized data structure as its configuration input.

YAML has some advanced features that can greatly 
[reduce duplication][yaml-anchors-aliases] in a configuration file 
needed in complex projects. YAML anchors and aliases are beyond the scope
of this document but may be of use to advanced Ceedling users. Note that 
Ceedling does anticipate the use of YAML aliases. It proactively flattens 
YAML lists to remove any list nesting that results from the convenience of
aliasing one list inside another.

[YAML]: http://en.wikipedia.org/wiki/Yaml
[serialize]: http://en.wikipedia.org/wiki/Serialization
[yaml-anchors-aliases]: https://blog.daemonl.com/2016/02/yaml.html

---
