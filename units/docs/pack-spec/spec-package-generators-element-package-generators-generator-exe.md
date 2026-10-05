---
id: "spec-package-generators-element-package-generators-generator-exe"
type: "concept"
domain: "pack"
title: "/package/generators element: /package/generators/generator/exe"
summary: "This element contains information about the generation binary/executable."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/generators_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element contains information about the generation binary/executable.

**Example:**
```
<exe>
  <command host = "win">MyGen.bat</command>
  <command host = "linux">MyGen.script</command>
  <argument>$P/RTE/MyGen/myGen.gpdsc</argument>
  <argument host="linux" switch="--device=">$D</argument>
  <argument host="win"   switch="/device=">$D</argument>
</exe>
```

 



| Parent | Chain |  |  |
|---|---|---|---|
| generator | element_generator |  |  |
| Child Elements | Description | Type | Occurrence |
| command | Invocation command for the generator tool. Command line options should be passed via `\<arguments>.` GeneratorCommandType | 1..4 |  |
| argument | Arguments passed along with the `\<command>` of the format `\<argument` `switch="-data">myFileName\</argument>.` Path information for files can be specified absolute or relative to the location (path) of the GPDSC file. GeneratorCommandArgumentType | 1..* |  |
