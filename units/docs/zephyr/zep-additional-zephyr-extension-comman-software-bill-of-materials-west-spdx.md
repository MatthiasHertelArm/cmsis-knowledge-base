---
id: "zep-additional-zephyr-extension-comman-software-bill-of-materials-west-spdx"
type: "concept"
domain: "project"
title: "Additional Zephyr extension commands: Software bill of materials: `west spdx`"
summary: "This command generates a Software Bill of Materials (SBOM) for a Zephyr build as a set of SPDX documents. It records the source files that went into the build, the build artifacts they produced, and the relationships between them."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/zephyr-cmds.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/zephyr-cmds.rst"
license: "Apache-2.0"
mode: "V"
---

This command generates a Software Bill of Materials (SBOM) for a Zephyr build as a set of SPDX
documents. It records the source files that went into the build, the build artifacts they produced,
and the relationships between them. The license and copyright of every file are scanned and filled
into the documents, together with file hashes.


### Choosing an SPDX version


`west spdx` can emit either of the two major SPDX specification families. SPDX 2.3 is the default;
select another version with the `--spdx-version` option.

SPDX 2.3 is a superset of 2.2 and adds fields such as `PrimaryPackagePurpose`. Pick SPDX 2.x for
compatibility with tooling that does not yet understand SPDX 3; pick SPDX 3.0 or above for the
richer, machine-readable build provenance described in west-spdx-build-profile.


**Note:** SPDX 3.1 support is experimental: the SPDX 3.1 specification is still in development.


### Generating SPDX documents


#. Enable `CONFIG_BUILD_OUTPUT_META` in your project, so that the build
   records what `west spdx` needs.

#. Build your application:

```bash

west build -d BUILD_DIR [...]
```
#. Generate SPDX documents using this build directory:

```bash

west spdx -d BUILD_DIR
```
   This generates SPDX 2.3 tag-value documents by default. To generate SPDX 2.2
   or 3.0 documents instead, pass `--spdx-version`:

```bash

west spdx -d BUILD_DIR --spdx-version 3.0
```

**Note:** When building with sysbuild, make sure you target the actual application which you want to generate the SBOM for. For example, if the application is named `hello_world`: .. code-block:: bash west build --sysbuild -d BUILD_DIR west spdx -d BUILD_DIR/hello_world


### Output documents


The documents are written to `BUILD_DIR/spdx/` (override with `-s`). The same set of
bill-of-materials (BOM) documents is produced regardless of the SPDX version; only the file
extension differs: `.spdx` for the SPDX 2.x tag-value format and `.jsonld` for the SPDX 3.0
JSON-LD format:

- `app`: BOM for the application source files used for the build
- `zephyr`: BOM for the specific Zephyr source code files used for the build
- `build`: BOM for the built output files
- `modules-deps`: BOM for modules dependencies. Check :ref:`modules
  <modules-vulnerability-monitoring>` for more details.

For SPDX 3.0, every document declares conformance to the Core, Software and Simple Licensing
profiles, and `build.jsonld` additionally declares the :ref:`Build profile
<west-spdx-build-profile>` that captures how the artifacts were produced. Element IDs are full
IRIs under the namespace prefix (`-n`), so the documents of separate builds, such as the images
of a sysbuild build, can be combined into one graph as long as each build has its
own prefix, which the default prefix guarantees.

Every file in the bill-of-materials is scanned so that its hashes (SHA512, SHA256 and SHA1) can be
recorded, together with its license and copyright.

Both are resolved with the third-party `reuse` tool from the REUSE group, so `west spdx`
honours every way the REUSE specification allows them to be declared: an
`SPDX-License-Identifier` and `SPDX-FileCopyrightText` comment in the file itself, a
`.license` file sitting next to it, or a `REUSE.toml` at the root of the repository
annotating whole sets of paths at once. That last form is the only way to license a file that
cannot hold a comment of its own, binary blobs in particular.

What is found is written out as `LicenseInfoInFile`, `LicenseConcluded` and
`FileCopyrightText` (SPDX 2.x), or as the element's license and copyright properties (SPDX 3.0).


**Note:** Copyright extraction uses heuristics that may not capture complete notice text, so `FileCopyrightText` content is best-effort. This aligns with SPDX specification recommendations.


### Package identification


Every package records where it came from, so that the SBOM can be matched against vulnerability
databases:

- a **PURL** (Package URL) built from the repository the sources were checked out from, pinned to
  the release tag when the checked-out revision is tagged and to the revision itself otherwise. It
  identifies the exact tree that was built, which for a fork is the fork's own repository.

- a **CPE** (Common Platform Enumeration) name, which identifies the product and version rather
  than the checkout, and so does not depend on which remote the sources came from.

For Zephyr itself, the CPE is `cpe:2.3:o:zephyrproject:zephyr:<version>:<update>:*:*:*:*:*:*`,
built from the version reported by Zephyr's `VERSION` file. Any `EXTRAVERSION`
becomes the CPE `update` field, so a release candidate is recorded as
`cpe:2.3:o:zephyrproject:zephyr:4.4.0:rc3:*:*:*:*:*:*` and a final release as
`cpe:2.3:o:zephyrproject:zephyr:4.4.0:-:*:*:*:*:*:*`. Both the `zephyr` source package and the
Zephyr entry in `modules-deps` carry it.

Modules are identified the same way, and can additionally declare curated references (for instance
the upstream project's CPE, when the module is a fork) in their `zephyr/module.yml`. See
modules.


### Relationships


SPDX relationships are created to indicate dependencies between CMake build targets, build targets
that are linked together, and source files that are compiled to generate the built library files.

The two specification families express build provenance differently:

- In **SPDX 2.x**, each generated artifact carries file-level `GENERATED_FROM` relationships
  pointing back at the source (and, with `--analyze-includes`, header) files it was compiled from.

- In **SPDX 3.0**, that provenance is carried by the Build profile
  instead, using `hasInput`/`hasOutput`/`usesTool` relationships scoped to the `build`
  lifecycle.


### Build profile (SPDX 3.0)


When generating SPDX 3.0 documents, `west spdx` populates the SPDX 3.0 Build profile so the
SBOM records not just *what* was built but *how* it was built. The information is collected
automatically from the CMake file-API, and lives in `build.jsonld`.

The profile adds a `build_Build` element describing the overall build: its build type, the CMake
generator and build configuration, and selected environment variables such as `BOARD` and
`ARCH`. The toolchain (CMake, the compilers, assembler, linker and archiver) is recorded as
`Tool` elements, each with its path and version. Build-scoped relationships then link the build to
its inputs (the source packages and compiled files), its outputs (the final image) and the tools it
used.

Each intermediate target, such as a static library, also gets its own sub-build capturing the exact
sources, tools and compile flags that produced its artifact, so any output can be traced back to how
it was built.


### Command-line options


`west spdx` accepts these additional options:

- `-i`, `--init`: create the CMake file-based API query in a build directory before it is
  configured. Deprecated, and to be removed in Zephyr 5.0: a build with
  `CONFIG_BUILD_OUTPUT_META` now requests the query itself.

- `-n PREFIX`: a prefix for the Document Namespaces that will be included in
  the generated SPDX documents. See SPDX specification clause 6 for
  details. If `-n` is omitted, a default namespace will be generated
  according to the default format described in section 2.5 using a random UUID.

- `-s SPDX_DIR`: specifies an alternate directory where the SPDX documents
  should be written instead of `BUILD_DIR/spdx/`.

- `--spdx-version {2.2,2.3,3.0,3.1}`: specifies which SPDX specification version to use.
  Defaults to `2.3`. See west-spdx-versions for the differences between
  the versions.

- `--analyze-includes`: in addition to recording the compiled source code
  files (e.g. `.c`, `.S`) in the bills-of-materials, also attempt to
  determine the specific header files that are included for each `.c` file.

  This takes longer, as it performs a dry run using the C compiler for each
  `.c` file using the same arguments that were passed to it for the actual
  build.

- `--include-sdk`: with `--analyze-includes`, also create a fourth SPDX
  document, `sdk.spdx` (or `sdk.jsonld`), which lists header files
  included from the SDK.


**Warning:** The generation of SBOM documents for the `native_sim` platform is currently not supported.

.. _SPDX 3.0 Build profile:
   https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Build/
