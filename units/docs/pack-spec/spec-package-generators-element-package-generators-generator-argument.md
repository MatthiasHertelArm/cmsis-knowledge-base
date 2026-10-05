---
id: "spec-package-generators-element-package-generators-generator-argument"
type: "concept"
domain: "pack"
title: "/package/generators element: /package/generators/generator/.../argument"
summary: "This element describes one or multiple arguments passed along with the parent element."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/generators_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element describes one or multiple arguments passed along with the parent element.

**Example**
```
<generators>
    <generator id = "MyGen">
      <gpdsc name ="$P/RTE/MyGen/myGen.gpdsc"/>
      <exe>
        <command host = "win">MyGen.bat</command>
        <command host = "linux">MyGen.script</command>
        <argument>$P/RTE/MyGen/myGen.gpdsc</argument>
        <argument host="linux" switch="--device=">$D</argument>
        <argument host="win"   switch="/device=">$D</argument>
        <argument mode="dry-run">--dry-run</argument>
      </exe>

      <eclipse plugin="com.mygen.plugin" class="com.mygen.plugin.generator.launcher" method="launch" >
        <argument>$D</argument>
        <argument>$P/RTE/MyGen/myGen.gpdsc</argument>
      </eclipse >

      <web url="http://mygen.com/mygen">
        <argument switch="device">$D</argument>
        <argument switch="gpdsc">$P/RTE/MyGen/myGen.gpdsc</argument>
      </web>
    </generator>
</generators>
```


 



  | 
    Parent | 
    Element Chain | 
  

  | 
    exe, eclipse, web | 
    element_gen_exe, element_gen_eclipse, element_gen_web | 
  

  | 
    Current | 
    Description | 
    Type | 
  

  | 
    argument | 
    value of argument without command line switch | 
    xs:string | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    mode | 
    Specifies the execution mode. Possible values are `normal` and `dry-run.` If set, the argument is only passed
        to the generator if the value matches the mode the generator is started in. For example, an argument with mode
        set to `dry-run` is only passed to the generator if it is started in dry-run mode. Arguments not specifying
        mode are always passed to the generator. In `dry-run` mode, the generator must not generate any files. Instead
        of writing the GPDSC file to disk, its contents is written to standard output (stdout), enclosed within the
        marks `\---\--BEGIN GPDSC\---\--` and `\---\--END GPDSC\---\--`. Only available with element \ref
        element_gen_exe "exe". | 
    xs:string | 
    optional | 
  

  | 
    host | 
    Specifies the host operating system. Possible values are `all,` `win,` `linux,` `mac,` `other.` Only available
        with element exe. | 
    xs:string | 
    optional | 
  

  | 
    switch | 
    Specifies the command line switch separated from the argument value. Not available with element
        eclipse. | 
    xs:string | 
    optional |
