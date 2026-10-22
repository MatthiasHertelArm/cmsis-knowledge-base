---
id: "ceed-paths-example-paths-yaml"
type: "concept"
domain: "test"
title: "`:paths`: Example `:paths` YAML"
summary: "Globs and inline Ruby string expansion can require trial and error to arrive at your intended results. Ceedling provides as much validation of paths as is practical."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/paths.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/paths/#example-paths-yaml"
license: "MIT"
mode: "V"
---

!!! note "Path standardization"
    Ceedling standardizes paths for you. Internally, all paths use forward
    slash `/` path separators (including on Windows) and trailing path 
    separators are cleaned up. This should have no impact on your project
    regardless of platform, but you will see the effects in logging.

### Simple entries

```yaml
:paths:
  # All <dirs>/*.<source extension> => test/release compilation input
  :source:
    - project/src/            # Resulting source list has just two relative directory paths
    - project/aux             # (Traversal goes no deeper than these simple paths)

  # All <dirs> => compilation search paths + mock search paths
  :include:                   # All <dirs> => compilation input
    - project/src/inc         # Include paths are subdirectory of src/
    - /usr/local/include/foo  # Header files for a prebuilt library at fully qualified path

  # All <dirs>/<test prefix>*.<source extension> => test compilation input + test suite executables
  :test:                
    - ../tests                # Tests have parent directory above working directory
```

### Common globs with subtractive entries

```yaml
:paths:
  :source:              
    - +:project/src/**    # Recursive glob yields all subdirectories of any depth plus src/
    - -:project/src/exp   # Exclude experimental code in exp/ from release or test builds
                          # `+:` is decoration for pretty alignment; only `-:` changes a list

  :include:
    - +:project/src/**/inc   # Include every subdirectory inc/ beneath src/
    - -:project/src/exp/inc  # Remove header files subdirectory for experimental code
```

### Advanced entries with globs and string expansion

```yaml
:paths:
  :test:                             
    - test/**/f???             # Every 4 character "f-series" subdirectory beneath test/

  :my_things:                  # Custom path list
    - "#{PROJECT_ROOT}/other"  # Inline Ruby string expansion using Ceedling global constant
```

```yaml
:paths:
  :test:                             
    - test/{foo,b*,xyz}  # Path list will include test/foo/, test/xyz/, and any subdirectories 
                         # beneath test/ beginning with 'b', including just test/b/
```

Globs and inline Ruby string expansion can require trial and error to arrive at
your intended results. Ceedling provides as much validation of paths as is
practical.

!!! tip "Troubleshooting paths"
    * Use the `ceedling paths:*` and `ceedling files:*` command line tasks to 
      verify your settings. (Here `*` is shorthand for `test`, `source`, `include`,
      etc. Confusing? Sorry.)
    * `ceedling dumpconfig` can also help your troubleshoot your configuration. 
      This application command causes Ceedling to fully process your configuration
      (e.g. Mixins, any string expansion, etc.) and write the result to another 
      YAML file for your inspection.
