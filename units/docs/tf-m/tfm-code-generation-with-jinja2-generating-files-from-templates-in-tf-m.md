---
id: "tfm-code-generation-with-jinja2-generating-files-from-templates-in-tf-m"
type: "concept"
domain: "security"
title: "Code Generation With Jinja2: Generating files from templates in TF-M"
summary: "Some of the files in TF-M are generated from template files. The files to be generated are listed in tools/tfm_generated_file_list.yaml. For each generated file <path_to_file>/<filename> the template file is <path_to_file>/<filename>.template."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/software/tfm_code_generation_with_jinja2.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/tfm_code_generation_with_jinja2.html#generating-files-from-templates-in-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

Some of the files in TF-M are generated from template files. The files to be
generated are listed in `tools/tfm_generated_file_list.yaml`. For each
generated file `<path_to_file>/<filename>` the template file is
`<path_to_file>/<filename>.template`. The templates are populated with
partition information from the partition manifests. The manifests to be used for
the generation are listed in `tools/tfm_manifest_list.yaml`.
