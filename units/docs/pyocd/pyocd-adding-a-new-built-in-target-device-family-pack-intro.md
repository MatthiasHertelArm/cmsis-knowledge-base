---
id: "pyocd-adding-a-new-built-in-target-device-family-pack-intro"
type: "concept"
domain: "debug"
title: "Adding a new built-in target: Device Family Pack intro"
summary: "The instructions below assume you have a CMSIS Device Family Pack (DFP) available for your target. See the list of all publicly available Packs to find and download the DFP for your target."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/adding_new_targets.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/adding_new_targets.md#device-family-pack-intro"
license: "Apache-2.0"
mode: "V"
---

The instructions below assume you have a CMSIS Device Family Pack (DFP) available for your target. See the
[list of all publicly available Packs](https://www.keil.com/dd2/pack/) to find and download the DFP for your
target.

A DFP is simply a zip file with a .pack extension. To extract the contents you can change the extension to
.zip and extract with your favourite archive utility.

For this context, the most important thing inside the DFP are .FLM files that contain the flash programming
algorithms used in step 5 below. The .pdsc file can also be useful. It is an XML file that contains details
such as the memory map for the target devices described by the DFP.
