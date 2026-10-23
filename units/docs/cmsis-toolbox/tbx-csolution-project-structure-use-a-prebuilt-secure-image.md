---
id: "tbx-csolution-project-structure-use-a-prebuilt-secure-image"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Project Examples / Use a Prebuilt Secure Image"
summary: "A non-secure project may use a secure image that is not part of the active target set. This is useful when the secure application is built and released separately. The non-secure application typically needs two matching artifacts:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#use-a-prebuilt-secure-image"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Examples_

A non-secure project may use a secure image that is not part of the active target set. This is useful when the secure
application is built and released separately. The non-secure application typically needs two matching artifacts:

- The secure image, for example a HEX file that is loaded together with the non-secure application.
- The CMSE import library that describes the secure callable interface and is linked with the non-secure project.

List the non-secure project before the prebuilt secure image in the target set so that debuggers and simulation models
load the executable before overlaying the HEX file:

```yml
solution:
  target-types:
    - type: AVH-NS-only
      target-set:
        - set: Debug
          images:
            - project-context: Project_NS.Debug
            - image: out/Project_S/AVH/Debug/Project_S.hex
              load: image
```

Reference the corresponding CMSE import library as a regular file in the non-secure project:

```yml
project:                                 # Non-secure project
  groups:
    - group: CMSE Library
      files:
        - file: ../out/Project_S/AVH/$BuildType$/Project_S_CMSE_Lib.o
          for-context: +AVH-NS-only
```

Unlike the `$cmse-lib(Project_S)$` access sequence, these file references do not establish a project dependency or
build the secure project. Create the secure artifacts before building the non-secure context. Both builds must use
compatible build types, toolchains, memory layouts, and secure callable interfaces.

```txt
> cbuild My.csolution.yml --context Project_S.Debug+AVH --toolchain AC6
> cbuild My.csolution.yml --context Project_NS.Debug+AVH-NS-only --toolchain AC6
```

The [SimpleTrustZone example](https://github.com/Open-CMSIS-Pack/csolution-examples/tree/main/SimpleTrustZone#use-an-existing-secure-image)
demonstrates this workflow and provides target sets for running the complete application and the non-secure project
with an existing secure image.
