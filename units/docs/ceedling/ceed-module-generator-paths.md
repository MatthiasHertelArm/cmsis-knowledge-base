---
id: "ceed-module-generator-paths"
type: "concept"
domain: "test"
title: "Module Generator: Paths"
summary: "The directories found in the project :paths: are reused. You can also specify an alternative default generation path using:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#paths"
license: "MIT"
mode: "V"
---

The directories found in the project `:paths:` are reused. You can also specify an alternative default generation path using: 

```yaml
:module_generator:
  :path_src: src/
  :path_inc: src/
  :path_tst: test/
```

But what if I don't want it to place my new files in the default location?

It can do that too! You can give it a hint as to where to find your files. The pattern matching
here is fairly basic, but it is usually sufficient. It works perfectly if your directory structure
matches a common pattern. For example, let's say you issue this command:

```sh
ceedling module:create[lab:SecretLair,mch]
```

Say your directory structure looks like this:

```yaml
:paths:
  :source:
    - lab/src
    - lair/src
    - other/src
  :test:
    - lab/test
    - lair/test
    - other/test
```

In this case, the `lab:` hint would make the module generator guess you want your files here:

- source files: `lab/src` (because it's a close match)
- include files: `lab/src` (because no include paths were listed)
- test files: `lab/test` (because it's a close match)

Instead, if your directory structure looks like this:

```yaml
:paths:
  :source:
    - src/**   #this might contain subfolders lab, lair, and other
  :include:
    - inc/**   #again, this might contain subfolders lab, lair, other, and shared
  :test:
    - test
```

In this case, the `lab:` hint would make the module generator guess you want your files here:

- source files: `src/lab` (because it's a close match)
- include files: `inc/lab` (because it's a close match)
- test files: `test` (because there wasn't a close match, and this was the first entry on our list)

You can see that more complicated structures will have files placed in the wrong place from time to
time... no worries... you can move the file after it's created... but if your project has any kind of 
consistent structure, the guessing engine does a good job of making it work.

A few more quick notes about the path-matching:

1. You can give multiple ordered hints that map roughly to folder nesting! `lab:secret:lair` will 
   happily match to put `lair.c` in a folder like `my/lab/secret/`.

2. If the matcher isn't given any path information or it finds multiple equally good candidates, 
   it will always guess in the order you have the paths listed in your project.yml file

3. If the matcher completely fails to find a good candidate, it will return an error, allowing you
   to rectify the situation.

4. What path is "first" when you're using `**` pattern in your `:paths:` specifications? The parent
   folder is used first, then its children alphabetically, and so on. This is important when 
   considering where files (or especially subfolders... see below) will be generated.

### Adding to Paths

In addition to the pattern matching above, you can add slashes (`/`) to your filename specification.
When a slash is used instead of a colon (`:`), it will stop using pattern matching and assume the
subdirectory is supposed to be there. If the subdir is NOT there, it will automatically add it.

Let's try an example with our previous path specification:

```yaml
:paths:
  :source:
    - src/**   #this might contain subfolders lab, lair, and other
  :include:
    - inc/**   #again, this might contain subfolders lab, lair, other, and shared
  :test:
    - test
```

Then, use the following command:

```sh
ceedling module:create[newlab/SecretLair]
```

This will create the following 3 files:

- `src/newlab/SecretLair.c`
- `inc/newlab/SecretLair.h`
- `test/newlab/TestSecretLair.c`

Technically, you can start with a colon and specify part of a path, then use a slash
to specify the remainder of the path to use. In most circumstances, this should work... however
it suffers from the same potential issues as the matcher above, with the added joy of creating 
new subdirectories for you without asking. 

It's important to note the module generator doesn't care if these new subdirectories are covered 
by the current path specification. This allows you to create the files before updating the
`project.yml` file if desired, but it also means you might accidentally think you've created
a file that Ceedling can see, when it can't.
