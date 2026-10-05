---
id: "spec-algorithm-functions"
type: "concept"
domain: "pack"
title: "Algorithm Functions"
summary: "The following functions are available for creating new Flash programming algorithms: Function Name |Indication |Description -----------------|-----------|----------- BlankCheck |optional |Check and compare patterns. EraseChip |optional |Delete entire Flash memory content. EraseSector |mandatory |Delete Flash memory content of a specific sector."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/flash_algorithms.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/algorithmFunc.html"
license: "Apache-2.0"
mode: "V"
---

The following functions are available for creating new Flash programming algorithms:
Function Name    |Indication |Description 
-----------------|-----------|-----------
BlankCheck  |optional   |Check and compare patterns.
EraseChip   |optional   |Delete entire Flash memory content.
EraseSector |mandatory  |Delete Flash memory content of a specific sector.
Init        |mandatory  |Initialize and prepare device for Flash programming.
ProgramPage |mandatory  |Write the application into the Flash memory.
UnInit      |mandatory  |De-initialize the microcontroller after one of the Flash programming steps.
Verify      |optional   |Compare Flash memory content with the program code.

The following diagrams show how the functions of the **Flash Programming Algorithms** are executed by a development tool.

The **Flash Erase** sequence is executed to erase the Flash content.

 "Flash Erase"

The **Flash Program** sequence is executed to program the Flash memory.

 "Flash Program"

The **Flash Verify** sequence is executed to verify the content after flash programming.

 "Flash Verify"
