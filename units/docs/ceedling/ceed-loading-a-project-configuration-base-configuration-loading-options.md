---
id: "ceed-loading-a-project-configuration-base-configuration-loading-options"
type: "concept"
domain: "test"
title: "Loading a Project Configuration: Base Configuration Loading Options"
summary: "You have three options for telling Ceedling what single base project configuration to load. These options are ordered below according to their precedence. If an option higher in the list is present, it is used."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/loading.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/loading/#base-configuration-loading-options"
license: "MIT"
mode: "V"
---

You have three options for telling Ceedling what single base project 
configuration to load. These options are ordered below according to their
precedence. If an option higher in the list is present, it is used.

1. Command line option flags
1. Environment variable
1. Default file in working directory

### `--project` command line flags

Many of Ceedling’s [application commands](https://throwtheswitch.github.io/Ceedling/configuration/loading/../getting-started/command-line.md) include an 
optional `--project` flag. When provided, Ceedling will load as its base 
configuration the YAML filepath provided.

Example: `ceedling --project=my/path/build.yml test:all`

!!! warning "Path relationships"
    Ceedling loads any relative paths within your configuration in
    relation to your working directory. This can cause a disconnect between
    configuration paths, working directory, and the path to your project 
    file.

If the filepath does not exist, Ceedling terminates with an error.

### Environment variable `CEEDLING_PROJECT_FILE`

If a `--project` flag is not used at the command line, but the 
environment variable `CEEDLING_PROJECT_FILE` is set, Ceedling will use
the path it contains to load your project configuration. The path can
be absolute or relative (to your working directory).

If the filepath does not exist, Ceedling terminates with an error.

### Default _project.yml_ in your working directory

If neither a `--project` command line flag nor the environment variable
`CEEDLING_PROJECT_FILE` are set, then Ceedling tries to load a file 
named _project.yml_ in your working directory.

If this file does not exist, Ceedling terminates with an error.
