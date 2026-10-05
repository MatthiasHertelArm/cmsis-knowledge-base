---
id: "ceed-module-generator-configuration"
type: "concept"
domain: "test"
title: "Module Generator: Configuration"
summary: "Enable the plugin in your project.yml by adding module_generator to the list of enabled plugins."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#configuration"
license: "MIT"
mode: "V"
---

Enable the plugin in your project.yml by adding `module_generator`
to the list of enabled plugins.

Then, like much of Ceedling, you can just run as-is with the defaults, or you can override those
defaults for your own needs. For example, new source and header files will be automatically
placed in the `src/` folder while tests will go in the `test/` folder. That's great if your project
follows the default ceedling structure... but what if you have a different structure?

```yaml
:module_generator:
  :naming: :bumpy
  :includes: 
    - :src: []
    - :inc: []
    - :tst: []
  :boilerplates:
    - :src: ""
    - :inc: ""
    - :tst: ""
```

Now I've redirected the location where modules are going to be generated.

### Includes

You can make it so that all of your files are generated with a standard include list. This is done
by adding to the `:includes` array. For example:

```yaml
:module_generator:
  :includes:
    :tst:
      - defs.h
      - board.h
    :src:
      - board.h
```

### Boilerplates

You can specify the actual boilerplate used for each of your files. This is the handy place to
put that corporate copyright notice (or maybe a copyleft notice, if that's your preference?)

Notice there is a separate template for source files, include files, and test files. Also, 
your boilerplates can optionally contain `%1$s` which will inject the filename into that spot.

```yaml
:module_generator:
  :boilerplates: 
    :src: |
      /***************************
      * %1$s
      * This file is Awesome.
      * That is All.
      ***************************/
    :inc: |
      /***************************
      * Header. Woo.             *
      ***************************/
    :tst: |
      /***************************
      * My Awesome Test For %1$s
      ***************************/
```

### Test Defines

You can specify the "#ifdef TEST" at the top of the test files with a custom define.
This example will put a "#ifdef CEEDLING_TEST" at the top of the test files.  

```yaml
:module_generator:
  :test_define: CEEDLING_TEST
```

### Naming Convention

Finally, you can force a particular naming convention. Even if someone calls the generator
with something like `MyNewModule`, if they have the naming convention set to `:caps`, it will
generate files like `MY_NEW_MODULE.c`. This keeps everyone on your team behaving the same way.

Your options for `:naming:` are as follows:

    - `:bumpy` - BumpyFilesLooksLikeSo
    - `:camel` - camelFilesAreSimilarButStartLow
    - `:snake` - snake_case_is_all_lower_and_uses_underscores
    - `:caps`  - CAPS_FEELS_LIKE_YOU_ARE_SCREAMING
