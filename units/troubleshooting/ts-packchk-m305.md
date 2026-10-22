---
id: "ts-packchk-m305"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M305: No releases (\"<release>\" elements in a <releases>-tag) found in PDSC file!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M305"
symptoms: ["M305", "No releases (\"<release>\" elements in a <releases>-tag) found in PDSC file!"]
symptom_regex: "^No releases \\(\"<release>\" elements in a <releases>\\-tag\\) found in PDSC file!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "At least one package release shall be specified in the PDSC file, but none was not found. Use `<release>` tag to specify release information in `<releases>` element. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release)."
summary: "packchk found no <release> elements inside the <releases> element of the PDSC file."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M305`
`No releases ("<release>" elements in a <releases>-tag) found in PDSC file!`

## Cause

packchk found no <release> elements inside the <releases> element of the PDSC file. The PDSC must list at least one package release in <releases> so the pack has a version history; this message is printed when that list is missing or empty.

## Fix

Open the PDSC file and add at least one <release> entry inside <releases>, for example <releases><release version="1.0.0" date="YYYY-MM-DD"/></releases>, using the pack's actual version and release date. Then run packchk again. See the Open-CMSIS-Pack specification for the <releases> element.

## Note

The source lines were not available, so the trigger location and handling could not be checked. The README text says 'none was not found', which is a double negative; the intended meaning is that no release was found. The cause and fix above come from the message text and the README, not from the code.
