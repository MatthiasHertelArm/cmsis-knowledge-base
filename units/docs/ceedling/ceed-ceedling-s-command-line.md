---
id: "ceed-ceedling-s-command-line"
type: "concept"
domain: "test"
title: "Ceedling’s Command Line"
summary: "Every action in Ceedling is accomplished via the command line. We'll cover project conventions and how to actually configure your project in other sections."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/getting-started/command-line.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/command-line/"
license: "MIT"
mode: "V"
---

**Now what? How do I make it _Go_?**

Every action in Ceedling is accomplished via the command line. We'll 
cover project conventions and how to actually configure your project 
in other sections.

For now, let’s talk about the command line.

To run tests, build your release artifact, etc., you will be using the
trusty command line. Ceedling is transitioning away from being built
around Rake. As such, right now, interacting with Ceedling at the 
command line involves two different conventions:

1. **Application Commands.** Application commands tell Ceedling what to
   to do with your project. These create projects, load project files, 
   begin builds, output version information, etc. These include rich 
   help and operate similarly to popular command line tools like `git`.
1. **Build & Plugin Tasks.** Build tasks actually execute test suites, 
   run release builds, etc. These tasks are created from your project 
   file. These are generated through Ceedling’s Rake-based code and 
   conform to its conventions — simplistic help, no option flags, but 
   bracketed arguments.

In the case of running builds, both come into play at the command line.

The two classes of command line arguments are clearly labelled in the
summary of all commands provided by `ceedling help`.

!!! note "Documentation convention"
    The `*` used in the headings below is a stand-in for documentation 
    purposes. It signifies either:

    - Freeform text provided by the user at the command line (e.g. a filename
      or matching pattern).
    - A variant of the command itself (e.g. naming a subsection beneath `:paths`
      in your project configuration.)
