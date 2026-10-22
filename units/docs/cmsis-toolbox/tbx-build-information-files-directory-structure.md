---
id: "tbx-build-information-files-directory-structure"
type: "concept"
domain: "project"
title: "Build Information Files: Directory Structure"
summary: "The csolution based projects are portable across different host computers and therefore use relative file references."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#directory-structure"
license: "Apache-2.0"
mode: "V"
---

The `csolution` based projects are portable across different host computers and therefore use **relative file references**.

- All file references use relative paths to the base directory of the related `*.yml` file.  Files that are within the file structure of the `csolution` base directory are also referenced using relative paths, i.e. `../layers/layer1/source-file1.c`.

- Files that are located in the [CMSIS-Pack root directory](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/installation.md#environment-variables) are prefixed with `${CMSIS_PACK_ROOT}`.

!!! Note
    All file references to user source code should be relative paths. The prefixes `${CMSIS_PACK_ROOT}` and `${CMSIS_COMPILER_ROOT}` are used to refer to base directories of files that relate to software packs and compiler-specific files. These base directories can also be on different filesystem drives.

- Files outside of the directory structure of a `csolution` based application use absolute paths. If absolute paths are used, a `warning` is issued in the `*.cbuild-idx.yml` file.

A typical directory structure of a `csolution` based application that uses common layers source files is shown below.

```yml
📦 # csolution base directory
 ┣ myapp.csolution.yml
 ┣ myapp.cbuild-idx.yml
 ┣ myapp.cbuild-pack.yml
 ┣ myapp.cbuild-set.yml
 ┣ myapp.cbuild-mlops.yml
 ┣ 📂 project1
 ┃  ┣  mypro1.cproject.yml                 # file references are relative to directory project1
 ┣ 📂 project2
 ┃  ┣  mypro2.cproject.yml                 # file references are relative to directory project
 ┣ 📂 layer
 ┃  ┣  mylayer.clayer.yml                  # file references are relative to directory layer
 ┣ 📂 out
 ┃  ┣  myapp+Target.cbuild-run.yml         # file references are relative to directory out
 ┣  ┣ 📂 mypro1\Target\Debug
 ┣  ┣  ┣  mypro1.cbuild.Debug+Target.yml   # file references are relative to directory out\mypro1\Target\Debug
 ┣  ┣ 📂 mypro2\Target\Debug
 ┣  ┣  ┣  mypro2.cbuild.Debug+Target.yml   # file references are relative to directory out\mypro2\Target\Debug
 
```
