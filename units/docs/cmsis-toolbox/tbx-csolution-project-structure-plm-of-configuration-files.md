---
id: "tbx-csolution-project-structure-plm-of-configuration-files"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Directory Structure / PLM of Configuration Files"
summary: "Configurable source and header files use an effective version during Project Lifetime Management (PLM). A file may specify its own version; otherwise, it inherits the component version or, when that is absent, the pack version."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#plm-of-configuration-files"
license: "Apache-2.0"
mode: "V"
---

_Part of: Directory Structure_

Configurable source and header files use an effective version during Project Lifetime Management (PLM). A file may specify its own version; otherwise, it inherits the component version or, when that is absent, the pack version. This version identifies changes when a newer or older pack is selected.

Depending on the PLM status of the application, `csolution` performs the following operation for configuration files:

1. **Add** a software component for the first time.
2. **Upgrade** (or downgrade) a software component.

#### **Add**

When adding a software component for the first time, the related config file is copied twice into the related `RTE`
project directory. The first copy can be modified by the user with the parameters for the user application. The
second copy is an unmodified  backup file with the format `<configfile>.<ext>.base@version`.

**Example:** A configuration file `ConfigFile.h` at version `1.2.0` is copied:

```c
./RTE/component_class/ConfigFile.h                  // user editable configuration file
./RTE/component_class/ConfigFile.h.base@1.2.0       // current unmodified configuration file with version
                                                    // information; used as a base for version comparison
```

`csolution` shows a user notification to indicate that files have been added:

```text
./RTE/component_class/ConfigFile.h -  info: component 'name' added configuration file version '1.2.0'
```

!!! Note
    The unmodified files with `@version` information should be committed to the repository of the version control system as these files are used to upgrade configuration information using merge utilities.

#### **Upgrade**

When upgrading (or downgrading) a software component, the effective version and file contents are considered. Selecting or installing another pack version alone does not overwrite the user-editable configuration file; the following processing occurs only when the RTE files are updated. A configuration file does not require a dedicated version in the pack description file (`*.pdsc`); when omitted, the version of its parent component is used, or the pack version if the component has no version.

- If the version of the unmodified backup file `<configfile>.<ext>.base@<version>` is identical, no operation is performed.
- If the version differs, the new configuration file is copied with the format `<configfile>.<ext>.update@<version>`.

In addition to version comparison, the contents of the `base` file and the corresponding file in the newly resolved pack are compared. If both files are identical, the unmodified `base` file is rebased to the new effective version without changing the user-editable file, and no `update` file is created. If the pack content differs, the new pack file is written as `update@<version>` for review and merging; the user-editable file is still not overwritten. This automatic rebase mechanism prevents unchanged configuration files without an explicit version from being incorrectly marked as out-of-date when using newer pack releases.

**Example:** after updating the configuration file `ConfigFile.h` to version `1.3.0`, the directory contains these files:

```c
./RTE/component_class/ConfigFile.h                  // user editable configuration file (based on the current version)
./RTE/component_class/ConfigFile.h.update@1.3.0     // new configuration file; used to start a 3-way merge
./RTE/component_class/ConfigFile.h.base@1.2.0       // current unmodified configuration file with version
                                                    // information; used as a base for version comparison
```

`csolution` displays a user notification to indicate that configuration files have changed:

```text
warning csolution: update recommended for file './RTE/component_class/RTX_Config.h' from component 'Cclass:Cgroup&Cvariant'.
Merge content from update file, rename update file to base file and remove previous base file
```

**User action to complete upgrade**

The user now has several options (outside of `csolution`) to merge the configuration file information. A potential way could be to use a 3-way merge utility. After merging the configuration file, the original `base@version` file should be deleted, and the new unmodified version should become the new `base@version`. The previous configuration file may be stored as a backup, as shown below.

```c
./RTE/component_class/ConfigFile.h                  // new configuration file with merge configuration
./RTE/component_class/ConfigFile.h.bak              // previous configuration file stored as backup
./RTE/component_class/ConfigFile.h.base@1.3.0       // current unmodified configuration file with version
                                                    // information; used as a base for version comparison
```

#### Multiple Instances of Configuration files

The system is also capable of handling multiple instances of configuration files as explained in the CMSIS-Pack specification under [Component Instances](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#Component_Instances). In this case, the instance %placeholder% is expanded as shown below.

```c
./RTE/component_class/ConfigFile_0.h
./RTE/component_class/ConfigFile_0.h.base@1.2.0
./RTE/component_class/ConfigFile_1.h
./RTE/component_class/ConfigFile_1.h.base@1.2.0
```
