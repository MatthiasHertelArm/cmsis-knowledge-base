---
id: "svd-svd-file-validation-and-usage"
type: "concept"
domain: "pack"
title: "SVD File Validation and Usage"
summary: "The description quality is key to success of the CMSIS-SVD format. Aspects of quality are: - Syntactical and structural compliance with the specified CMSIS-SVD format. - Consistency and correctness. - Completeness. - Level of detail."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/svd_validate_file_pg.html"
license: "Apache-2.0"
mode: "V"
---

The description quality is key to success of the CMSIS-SVD format. Aspects of
quality are:
  - Syntactical and structural compliance with the specified CMSIS-SVD format.
  - Consistency and correctness.
  - Completeness.
  - Level of detail.


Validation
Automated validations are done on two levels:

-# **The CMSIS-SVD Schema File**:
XML tools use the schema file for checking the syntactical and structural correctness of an XML file that
claims compliance with a certain format. The schema file _CMSIS-SVD.xsd_ is located in
the folder **.\\CMSIS\\Utilities** of the **ARM::CMSIS** Pack.
\n\n
-# **SVD Conversion Utility:** The conversion utility svd_SVDConv_pg checks the semantics and consistency of the data contained in a CMSIS-SVD file.
**SVDConv** is included in the CMSIS distribution.


Usage
CMSIS-SVD files can be used to generate:
 -# CMSIS-compliant device header files from a CMSIS-SVD description. Refer to the conversion tool svd_SVDConv_pg for details.
  CMSIS device header files are developed and maintained by the silicon vendors. Therefore, the expectation is that this conversion is only of interest to
  these parties.
 -# Debug dialogs that communicate with a debugger. See below.

**System Views**
\n\n A number of tool vendors support the CMSIS-SVD format with their products.
  Refer to the tools documentation to find out how to use CMSIS-SVD descriptions with the debugger of your choice.
  Please regularly check for updates to the CMSIS Device Family Packs from the silicon vendor to
  to use the latest versions of the CMSIS-SVD files.
  \n \n
  **Generated Debug Dialog:**
  " "uVision Debug Window generated from ARM_Example.svd"
\n
