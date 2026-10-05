---
id: "x-cmsis-pack-docs-3"
type: "pattern"
domain: "bring-up"
title: "Citing a target document with edition and page"
status: "draft"
extracted_from: "proc-cmsis-pack-docs"
source: "cmsis-pack-docs/SKILL.md"
---

Cite `<doc id> <edition> p.<n>` with the section from the hit, for example `stm32u5xx-dfp/rm0456 p.519 §11.8.29 RCC_AHB2ENR1` or `arm/ihi0031-latest h p.108 §B4.3 Dormant state`. The edition is printed in brackets in every hit and page header (`arm/ddi0553-latest [B.z] p.1207`); never omit it for a fetched document — the bring-up knowledge contracts require "document edition/revision and section/page". For a pack PDF with no edition in the output, name the pack version instead (`Keil::STM32U5xx_DFP@2.1.0`). Never cite a snippet alone; read the page.
