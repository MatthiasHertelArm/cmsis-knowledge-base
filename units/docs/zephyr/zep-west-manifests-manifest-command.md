---
id: "zep-west-manifests-manifest-command"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Command"
summary: "The west manifest command can be used to manipulate manifest files. It takes an action, and action-specific arguments."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

The `west manifest` command can be used to manipulate manifest files.
It takes an action, and action-specific arguments.

The following sections describe each action and provides a basic signature for
simple uses. Run `west manifest --help` for full details on all options.


### Resolving Manifests


The `--resolve` action outputs a single manifest file equivalent to your
current manifest and all its imported manifests:

```none

west manifest --resolve [-o outfile]
```
The main use for this action is to see the "final" manifest contents after
performing any `import`\ s.

To print detailed information about each imported manifest file and how
projects are handled during manifest resolution, set the maximum verbosity
level using `-v`:

```console

west -v manifest --resolve
```

### Freezing Manifests


The `--freeze` action outputs a frozen manifest:

```none

west manifest --freeze [-o outfile]
```
A "frozen" manifest is a manifest file where every project's revision is a SHA.
You can use `--freeze` to produce a frozen manifest that's equivalent to your
current manifest file. The `-o` option specifies an output file; if not
given, standard output is used.


### Validating Manifests


The `--validate` action either succeeds if the current manifest file is valid,
or fails with an error:

```none

west manifest --validate
```
The error message can help diagnose errors.

Here, "invalid" means that the syntax of the manifest file doesn't follow the
rules documented on this page.

If your manifest is valid but it's not working the way you want it to, turning
up the verbosity with `-v` is a good way to get detailed information about
what decisions west made about your manifest, and why:

```none

west -v manifest --validate
```

### Get the manifest path


The `--path` action prints the path to the top level manifest file:

```none

west manifest --path
```
The output is something like `/path/to/workspace/west.yml`. The path format
depends on your operating system.
