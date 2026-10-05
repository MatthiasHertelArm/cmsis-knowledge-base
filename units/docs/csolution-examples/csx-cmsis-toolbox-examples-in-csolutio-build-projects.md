---
id: "csx-cmsis-toolbox-examples-in-csolutio-build-projects"
type: "concept"
domain: "project"
title: "CMSIS-Toolbox Examples in *csolution project format*: Build Projects"
summary: "The project files contain a list of software packs that are used. When using the cbuild tool option --packs these packs are downloaded during the build process as shown in the following example command line:"
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/README.md#build-projects"
license: "Apache-2.0"
mode: "V"
---

The project files contain a list of software packs that are used. When using the `cbuild` tool option `--packs` these packs are downloaded during the build process as shown in the following example command line:

```txt
> cbuild Hello/Hello.csolution.yml --packs --toolchain AC6 --rebuild
```
