---
id: "dar-debug-adapter-registry-template-development"
type: "concept"
domain: "debug"
title: "debug-adapter-registry: Template Development"
summary: "The .adapter.json files provide snippets to be injected into the workspace launch.json and tasks.json files:"
status: "draft"
collection: "debug-adapter-registry"
source: "Open-CMSIS-Pack/debug-adapter-registry@2692b50:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/debug-adapter-registry/blob/2692b50/README.md#template-development"
license: "Apache-2.0"
mode: "V"
---

### Template input files

The `.adapter.json` files provide snippets to be injected into the workspace `launch.json` and `tasks.json` files:

```json
{
  "data": {
    "cwd": "${workspaceFolder}/<%= solution_folder %>"
  },
  "launch": {
    "singlecore-launch": {},
    "singlecore-attach": {},
    "multicore-start-launch": {},
    "multicore-start-attach": {},
    "multicore-other": {}
  },
  "tasks": [
    {
      "label": "CMSIS Erase"
    },
    {
      "label": "CMSIS Load"
    },
    {
      "label": "CMSIS Run"
    },
    {
      "label": "CMSIS Load+Run"
    },
    {
      "label": "CMSIS TargetInfo"
    }
  ]
}
```

```txt
  JSON Node                  Value Type         Description
 ---------------------      ------------------ -----------------------------------------------------------------------
  data                       object             User data processed on a global scope
  launch                     object             Template launch configurations
  ┣ singlecore-launch        object             Launch template for launching a single core debug session
  ┣ singlecore-attach        object             Launch template for attaching to a single core debug session
  ┣ multicore-start-launch   object             Launch template for launching a multi core debug session
  ┣ multicore-start-attach   object             Launch template for attaching to the primary core of a multi core debug session
  ┗ multicore-other          object             Launch template for attaching to other cores of a multi core debug session
  tasks                      array of objects   Template tasks
  ┗ label                    string             Unique name to identify the task, specific names are used for CMSIS debug related tasks
```

### Template processing

All string elements are processed one-by-one with the [ETA JS template engine](https://eta.js.org/). The `data` section
is processed in the first pass and the result is passed into subsequent template processing. Hence, one can collect
reused parts under `data` section to avoid duplication.

Arrays-of-strings loaded from the template are joined into a multi-line string, processed at once and split based on linebreaks after processing.
This can be used to generate arrays using a multiline template if required:

```json
{
  "template": ["<% for elem in array %> {", "<%= elem.name %>\\n", "<% } %>"]
}
```

Notice the explicit newline character inserted after the template tag. The implicit newline resulting from
concatenation is swallowed by the template processing if a template output data tag runs until the end of a line.

Template output data tags are typically used to create strings, similar to JavaScript format strings (backtick notation).
When outputting objects or arrays, these are stringified using JavaScript Object Notation (JSON). If JSON is detected
in a resulting launch or task configuration object, its converted back. E.g., one can achieve the following:

```json
{
  "data": {
    "shell": {
      "win32": {
        "executable": "cmd.exe",
        "args": ["/d", "/c"]
      },
      "linux": {
        "executable": "/bin/bash",
        "args": ["-c"]
      },
      "darwin": {
        "executable": "/bin/bash",
        "args": ["-c"]
      }
    }
  },
  "tasks": [
    {
      "options": {
        "shell": "<%= data.shell[process.platform] %>"
      }
    }
  ]
}
```

To be transformed into

```json
{
  "tasks": [
    {
      "options": {
        "shell": {
          "executable": "cmd.exe",
          "args": ["/d", "/c"]
        }
      }
    }
  ]
}
```

Plain numbers and boolean representation strings are converted to plain data type by default.
If instead the value is required as a quoted string, this needs to be enforced explicitly.

```json
{
  "data": {
    "number": "3000",
    "flag": "true"
  },
  "tasks": [
    {
      "options": {
        "plain-num": "<%= data.number %>",
        "quoted-num": "\"<%= data.number %>\"",
        "plain-bool": "<%= data.flag %>",
        "quoted-bool": "\"<%= data.flag %>\""
      }
    }
  ]
}
```

To be transformed into

```json
{
  "tasks": [
    {
      "options": {
        "plain-num": 3000,
        "quoted-num": "3000",
        "plain-bool": true,
        "quoted-bool": "true"
      }
    }
  ]
}
```

### Dynamic data structure

The following data structure is available to the templates:

```yml
data: { <custom data as specified> }
platform: <JavaScript process.platform>
solution_path: <path to .csolution.yml relative to workspace>
solution_folder: <base directory of .csolution.yml relative to workspace>
device_name: <name of target device>
target_type: <name of active csolution target-type>
start_pname: <processor name of primary processor if multi core device>
image_files: # image files used to program the device (image, image+symbol)
  - file: <image file name relative to solution_folder>
    pname: <processor name>
symbol_files: # symbol files with debug information (symbol, image+symbol)
  - file: <symbol file name relative to solution_folder>
    pname: <processor name>
ports: # GDB debug port mapping for all processors
  <pname>: <gdb-port>
config: # entire debugger node from .cbuild-run.yml
processors: # List of processors on a multi-core system
  - <pname>
```

In template expressions all functions in JavaScript global scope can be used. In addition, the following helper functions are available:

| Function                                                 | Description                                                                          |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `Array<T>.groupedBy((e: T) => string): Map<string, T[]>` | Group elements of an array into a Map according to the given key-generator function. |
| `Map<K, V>.every((v: V, k: K) => boolean): boolean`      | Determines if all elements satisfy the given condition.                              |
| `Map<K, V>.mapValues<T>((v: V, k: K) => T): Map<K, T>`   | Transforms all elements with given function.                                         |
| `Map<K, V>.toObject(): Record<string, T>`                | Converts the Map into a JavaScript object                                            |
