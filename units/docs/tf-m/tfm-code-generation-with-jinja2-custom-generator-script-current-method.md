---
id: "tfm-code-generation-with-jinja2-custom-generator-script-current-method"
type: "concept"
domain: "security"
title: "Code Generation With Jinja2: Custom generator script - Current method"
summary: "tools/tfm_parse_manifest_list.py Python script is used to generate files from the templates. This script calls the tools/generate_from_template.py to parse the template files, and uses tools/keyword_substitution.py to substitute the keychains with actual values from the manifest files."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/tfm_code_generation_with_jinja2.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/tfm_code_generation_with_jinja2.html#custom-generator-script-current-method"
license: "BSD-3-Clause"
mode: "V"
---

`tools/tfm_parse_manifest_list.py` Python script is used to generate files
from the templates. This script calls the `tools/generate_from_template.py` to
parse the template files, and uses `tools/keyword_substitution.py` to
substitute the keychains with actual values from the manifest files.
