---
id: "tfm-tf-m-manifest-tool-user-guide-arguments"
type: "concept"
domain: "security"
title: "TF-M Manifest Tool User Guide: Arguments"
summary: "Required. At least one item must be provided."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_manifest_tool_user_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_manifest_tool_user_guide.html#arguments"
license: "BSD-3-Clause"
mode: "V"
---

The tool takes 5 arguments at most.

```bash

tfm_parse_manifest_list.py [-h] -o out_dir
                           -m manifest list [manifest list ...]
                           -f file-list [file-list ...]
                           -c config-files [config-files ...]
                           [-q]
```
**-o/--outdir**

Required.

The directory to hold the output files.

**-m/--manifest-lists**

Required. At least one item must be provided.

A list of TF-M Secure Partition manifest lists which contain one or more
Secure Partition manifests in each.
See Manifest List for details.

**-f/--file-list**

Required. At least one item must be provided.

A list of files that describe what files the tool should generate.
See Generated File List for details.

**-c/--config-files**

Required. At least one item must be provided.

A list of header files which contain build configurations such as isolation
level and Secure Partition enabled status.
See Configuration Header File for details.

**-q/--quiet**

Optional.

Reduces log messages, only warnings and errors will be printed.


### Manifest List

A manifest list is a YAML [3]_ file that describes a list of Secure Partition
manifests.
Refer to the TF-M default manifest list [4]_ as an example.

Each manifest list must contain a `manifest_list` attribute which collects the
descriptions of Secure Partition manifests.
Following are the supported attributes of in the manifest lists.

- `description`

  Required.

  Descriptive information for the tool to refer to the Secure Partition, for
  example in logs.

- `manifest`

  Required.

  The manifest file of the Secure Partition.
  Both absolute path and relative path to the manifest list are supported.
  Environment variables are supported.

- `output_path`

  Optional.

  The directory to hold the Secure Partition specific output files.
  See Generated File List for more details.

  Both absolute path and relative path to the directory specified by
  `-o/--outdir` are supported.
  Environment variables are supported.

  It is set to the directory specified by `-o/--outdir` if omitted.

- `conditional`

  Optional.

  The configuration to enable or disable this Secure Partition.
  The value must be defined in one of the Configuration Header File.
  If it is omitted, the Secure Partition is always enabled.

- `pid`

  Optional.

  The Secure Partition ID (PID).

  **For non-test purpose Secure Partitions, it is required.**
  See Adding Secure Partition
  for the PID allocations.

  For test purpose Secure Partitions, this attribute is optional.
  The manifest tool assigns one for the Secure Partition.
  The value is not guaranteed to the same for different builds.

- `linker_pattern`

  Optional.

  The information for linker to place the symbols of the Secure Partition.
  It is only required if you are using the linker scripts provided by TF-M.
  Each Secure Partition is expected to be built as a library.
  The name of the library must follow the format of
  `tfm_<type>_partition_<name>`.
  The valid value for `<type>` is `[psa_rot, app_rot]` corresponding to the
  type of the Secure Partitions.
  The `<name>` is any string to distinguish the Secure Partition from others.

  Supported patterns are:

  - `library_list`, must be `*tfm_*partition_<name>.*`.
  - `object_list`

    Any object files containing symbols belonging to the Secure Partition that
    are not included in the Secure Partitions library.

- `non_ffm_attributes`

  Optional.

  TF-M defines some special manifest attributes for TF-M dedicated Secure Partitions.
  Those special attributes are not compliant to FF-M.
  Using the specific attributes requires explicit registration by adding them to
  this `non_ffm_attributes`.
  The purpose is to ensure that developers are aware of the compliance issue.
  The manifest tool will report errors if unregistered Non-FFM attributes are detected.
  This attribute is for TF-M specific Secure Partitions and using TF-M-specific attributes
  is not encouraged.


### Generated File List

A generated file list is a YAML file that describes the files to be generated
by the manifest tool.
Refer to TF-M default generated file list [5]_ as an example.

Each one must contain a `file_list` attribute which collects the files to
generate.
Each item in the `file_list` must contain the following attributes.

- `template`

  This attribute is the file path of a Jinja2 [6]_ template.
  The TF-M manifest tool uses Jinja2 template engine for file generations.
  It can be a relative path to TF-M root directory or an absolute path.
  Environment variables are supported.

- `output`

  The output file of the `template`.
  Both absolute path and relative path to the directory specified by
  `-o/--outdir` are supported.
  Environment variables are supported.

**The tfm_generated_file_list.yaml is essential to build TF-M.**

There are several files that are required for each Secure Partition,
so they are not in any generated file lists since one template generates
multiple files.

- `psa_manifest/<manifestfilename>.h`

  `manifestfilename` is the file name of the manifest.
  This file contains internal definitions for the Secure Partition
  implementation, such as RoT Service signals and Secure Functions.
  Refer to FF-M [1]_ for more details.
  The corresponding template is `manifestfilename.template`

- `intermedia_<manifestfilename>.c`

  TF-M specific, which holds the stacks of Secure Partitions.
  This file must be built with the Secure Partition libraries.
  The corresponding template is `partition_intermedia.template`.

- `load_info_<manifestfilename>.c`

  TF-M specific, which contains the load information of Secure Partitions.
  This file must be built with the TF-M SPM library.
  The corresponding template is `partition_load_info.template`.

These files are generated to `output_path` specified by each Secure Partition
in the manifest lists.


### Configuration Header File

The format of each configuration item must be

```

#define CONFIG_NAME   VALUE
```
The following format is also supported for boolean type configurations.

```

#define CONFIG_NAME
```
The configurations can be divided into two categories.

- Generic configurations:

  - `PSA_FRAMEWORK_ISOLATION_LEVEL`

    The isolation level, required. Valid values are `[1, 2, 3]`.

  - `CONFIG_TFM_SPM_BACKEND`

    The backend of SPM, required. Valid values are `[SFN, IPC]`.
    See SPM backends
    for details of backends.

- Secure Partition enablement configurations

  Configurations used to enable or disable Secure Partitions.
  The configuration names must match the values of `conditional` attributes in
  Manifest List. Valid values are `[0, 1]`.
  It's optional for a Secure Partition which does not have the `conditional`
  attribute.

The configurations can be split to multiple files corresponding to the multiple
manifest lists.
