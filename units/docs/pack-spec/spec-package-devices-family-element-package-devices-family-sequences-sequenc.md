---
id: "spec-package-devices-family-element-package-devices-family-sequences-sequenc"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../sequences/sequence"
summary: "Describes a Debug Access Sequence which contains control and block elements. block elements contains statements including calls to Debug Access Functions. A Debug Access Sequence overrides or extends the default functionality of a development tool. Refer to usageofsequences for details."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes a Debug Access Sequence which contains **control** and
**block** elements. **block** elements contains statements
including calls to Debug Access Functions. A Debug
Access Sequence overrides or extends the default functionality of a development tool.
Refer to usage_of_sequences for details.


**Note:**
- **control** elements can contain other **control** and **block**
  elements. **The maximum nesting of **control** elements is 10.**

**Example**
```
<family Dfamily="Generic Family" Dvendor="Generic:5">
  ...
  <sequences>
    ...
    <sequence name="UserSequence">
      
      <block info="Define variables and do debug accesses">
        __var tpWidth = (__traceout &amp; 0x003F0000) >> 16;
        ...
      </block>
      
      <control if="__traceout &amp; 0x2" info="Parallel Trace Port enabled">
      
        <block>
          // Do something generic for parallel trace port trace
          ...
        </block>
        
        <control if="tpWidth == 1" info="Configure device for 1-bit TPIU trace.">
        
          <block>
            // Do debug accesses
            ...
          </block>
          
        </control>
        
        <control if="tpWidth == 2" info="Configure device for 2-bit TPIU trace.">
        
          <block>
            // Do debug accesses
            ...
          </block>
          
        </control>
        
        <control if="tpWidth == 4" info="Configure device for 4-bit TPIU trace.">
        
          <block>
            // Do debug accesses
            ...
          </block>
          
        </control>

      </control>
      ...
    </sequence>
    ...
  </sequences>
  ...
</family>
```


 		



  | 
    Parents | 
    Element Chain | 
  

  | 
    sequences | 
    element_sequences | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Name of the Debug Access Sequence:

    - Pre-defined names are executed by the development tool described under usage_of_sequences.
    - Any Debug Access Sequence can be executed the debug access function **Sequence**.
     | 
    xs:string | 
    required | 
  

  | 
    Pname | 
    
      Reference to a processor identifier as specified for a **processor** element. If **Pname** is set
      for this **sequence** element, a debugger executes the debug access sequence only for a debug connection
      to the referenced processor. Otherwise, it is executed for all processors.
      **This attribute must be set if defining multiple implementations of the same debug access sequence.**
      Only alphabetical characters, decimal digits, '-' and '_' are allowed. 
     | 
    RestrictedString | 
    optional | 
  

  | 
    disable | 
    Disables execution of the Predefined Debug Access Sequence. | 
    xs:boolean | 
    optional | 
  

  | 
    info | 
    Descriptive text to display for example for error diagnostics. | 
    xs:string | 
    optional | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    control | 
    
      Describe a debug access sequence flow control element.
     | 
    SequenceControlType | 
    0..* | 
  

  | 
    block | 
    
      Describe a block of debug accesses.
     | 
    SequenceBlockType | 
    0..* |
