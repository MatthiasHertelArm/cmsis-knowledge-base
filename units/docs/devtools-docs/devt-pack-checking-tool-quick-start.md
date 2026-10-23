---
id: "devt-pack-checking-tool-quick-start"
type: "concept"
domain: "pack"
title: "Pack Checking Tool: Quick Start"
summary: "This tutorial aims to get you up and running with packchk using CMake. We recommend this tutorial as a starting point. In order to build packchk and run related tests. Please employ the sequence of steps mentioned here."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/packchk/README.md#quick-start"
license: "Apache-2.0"
mode: "V"
---

This tutorial aims to get you up and running with `packchk` using **CMake**. We
recommend this tutorial as a starting point. In order to build `packchk` and
run related tests. Please employ the sequence of steps mentioned
[here](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/packchk/../../README.md).

> [!NOTE]
> For the schema check, `packchk` searches for a `PACK.xsd` file in
> `./, ../etc/, ../../etc/` relative to `cmsis-toolbox/bin`. Alternatively, use
> `--xsd` to specify the location of the schema file.

### Usage Examples

Run `packchk` on the package description file called `MyVendor.MyPack.pdsc`.
It runs a schema check and verifies the file against the Software Pack that is located in the same directory.

```bash
packchk MyVendor.MyPack.pdsc
```

Run `packchk` on the package description file called MyVendor.MyPack.pdsc in the
current directory and try to resolve conditions using the RefVendor.RefPack.pdsc file
based in another directory.

```bash
packchk MyVendor.MyPack.pdsc -i /path/to/reference/pdsc/RefVendor.RefPack.pdsc
```

Run `packchk` on the package description file called `MyVendor.MVCM3.pdsc`,
verify the URL to the Pack Server, and generate a ASCII text file with the
standardized name of the Software Pack.

```bash
packchk "MyVendor.MVCM3.pdsc" -u "http://www.myvendor.com/pack" -n packname.txt
```

Run `packchk` on the package description file called MyVendor.MVCM3.pdsc.
Suppress validation messages M304 and M331.

```bash
packchk MyVendor.MVCM3.pdsc --diag-suppress M304,M331   // messages as a list
packchk MyVendor.MVCM3.pdsc -x M304 -x M331             // option repeated
```
