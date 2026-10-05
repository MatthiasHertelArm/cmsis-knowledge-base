---
id: "view-theory-of-operation-software-component-variants"
type: "concept"
domain: "trace"
title: "Theory of operation: Software Component Variants"
summary: "The software packs for MDK-Middleware and CMSIS already contain SCVD files that match the related event annotations in the C source code. However, you need to select the right component Variant."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/event_recorder.md#software-component-variants"
license: "Apache-2.0"
mode: "V"
---

The software packs for MDK-Middleware and CMSIS already contain SCVD files that match the related event annotations in the C
source code. However, you need to select the right component **Variant**. For MDK-Middleware, you need to select
the **Debug** variants, whereas for Keil RTX5, you need to add the **Source** variant.

The example below enables event recording for the MDK-Middleware **File System** component:

(figure: Select debug variant)
