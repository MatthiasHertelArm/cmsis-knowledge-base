---
id: "x-start-cmsis-project-1"
type: "concept"
domain: "project"
title: "Dname:Pname for multi-core devices"
status: "draft"
extracted_from: "proc-start-cmsis-project"
source: "start-cmsis-project/SKILL.md"
license: "Apache-2.0"
---

A device with several processors (the DFP lists more than one `Pname`, as the MCXN947 does with `cm33_core0` and `cm33_core1`) needs `Dname:Pname`: take the core the user named, otherwise ask which one; when the user does not care, the first core the DFP lists is the boot core, say so in the report
