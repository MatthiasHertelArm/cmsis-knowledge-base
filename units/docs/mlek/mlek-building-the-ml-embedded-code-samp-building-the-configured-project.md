---
id: "mlek-building-the-ml-embedded-code-samp-building-the-configured-project"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Build process / Building the configured project"
summary: "If the CMake command succeeds, build the application as follows:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/building.md#building-the-configured-project"
license: "Apache-2.0"
mode: "V"
---

_Part of: Build process_

If the CMake command succeeds, build the application as follows:

```commandline
make -j4
```

To see compilation and link details, add `VERBOSE=1`.

Results of the build are placed underÂ `build/bin`Â folder, for example:

```tree
bin
 ├── mlek_<use_case_name>.axf
 ├── mlek_<use_case_name>.htm
 ├── mlek_<use_case_name>.map
 └── sectors
        ├── images.txt
        └── <use_case>
                ├── ddr.bin
                └── itcm.bin
```

Where for each implemented use-case under the `source/use-case` directory, the following build artifacts are created:

- `mlek_<use-case name>.axf`: The built application binary for an ML use-case.

- `mlek_<use-case name>.map`: Information from building the application. For example: Libraries used, what was
  optimized, and location of objects.

- `mlek_<use-case name>.htm`: Human readable file containing the call graph of application functions.

- `sectors/<use-case>`: Folder containing the built application. Split into files for loading into different FPGA
  memory regions.

- `images.txt`: Tells the FPGA which memory regions to use for loading the binaries in the `sectors/..`
  folder.

> **Note:**  For the specific use-case commands, refer to the relative section in the use-case documentation.
