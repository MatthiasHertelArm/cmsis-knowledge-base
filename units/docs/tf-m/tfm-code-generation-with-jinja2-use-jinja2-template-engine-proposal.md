---
id: "tfm-code-generation-with-jinja2-use-jinja2-template-engine-proposal"
type: "concept"
domain: "security"
title: "Code Generation With Jinja2: Use Jinja2 template engine - proposal"
summary: "The proposal is to eliminate the template parser and substituter scripts, and call the Jinja2 template engine library from tools/tfm_parse_manifest_list.py to do the substitution."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/software/tfm_code_generation_with_jinja2.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/tfm_code_generation_with_jinja2.html#use-jinja2-template-engine-proposal"
license: "BSD-3-Clause"
mode: "V"
---

The proposal is to eliminate the template parser and substituter scripts, and
call the Jinja2 template engine library from
`tools/tfm_parse_manifest_list.py` to do the substitution.

More information on jinja2: https://jinja.palletsprojects.com/en/stable/


### Changes needed:


- `tools/tfm_parse_manifest_list.py` have to be modified to call the Jinja2
  library instead of the custom scripts. The data structure required by the
  library is very similar to the one required by the current scripts.
- template files needs to be rewritten to the Jinja syntax: The control
  characters to be replaced (like `@!` -> `{%`) and `for` statements to be
  added to iterate over the substitutions.


### Improvements over the current solution


- Compatible with Python 2.7 and Python 3, while current solution only supports
  Python 2.7
- More advanced functionality: direct control over the list of items for a
  keychain, meta information on that list (like length)
- Well documented (see website)
- Jinja2 is free and open-source software, BSD licensed, just like TF-M. It is a
  well established software in contrast with the current proprietary solution.
