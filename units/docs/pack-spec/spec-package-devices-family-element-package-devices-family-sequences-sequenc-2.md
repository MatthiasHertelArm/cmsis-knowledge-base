---
id: "spec-package-devices-family-element-package-devices-family-sequences-sequenc-2"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../sequences/sequence/control"
summary: "Describes flow control like if and while blocks for debug access sequences."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes flow control like **if** and **while** blocks for debug access sequences.

**Example**
```
<family Dfamily="Generic Family" Dvendor="Generic:5">
  ...
  <sequences>
    ...
    <sequence name="UserSequence">
      ...
      <block info="Define variables and do debug accesses">
        __var doIfBlock      = 1;
        __var whileCondition = 1;
        ...
      </block>
      ...
      <control if="doIfBlock">
      
        <block>
          // Do debug accesses
          ...
        </block>
        
      </control>
      ...
      <control while="whileCondition" timeout="5000">
      
        <block>
          // Execute while "whileCondition" different from '0' with a timeout of 5ms
          whileCondition = 0;
        </block>
        
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
    sequence | 
    element_sequence | 
  

  | 
    control | 
    element_seq_control | 
  

  | 
    Attribute | 
    Description | 
    Type | 
    Use | 
  

  | 
    if | 
    
      Expression describing the condition under which to execute this sequence block.
      The block is skipped if the condition resolved to `false`. Defaults to
      `true` if not set.
      Refer to Expression Rules for the syntax.
     | 
    ExpressionType | 
    optional | 
  

  | 
    while | 
    
      Expression describing a while-condition. The execution of the block contents is
      repeated while the condition resolves to `true`, or until an optional
      **timeout** is reached.
      Refer to Expression Rules for the syntax.
     | 
    ExpressionType | 
    optional | 
  

  | 
    timeout | 
    
      Timeout in microseconds for a **block** with a **while** condition. A debugger must
      extend the timeout to the closest possible time granularity. If the timeout is reached,
      the current iteration including a last evaluation of the **while** condition must
      finish. A value of `0` disables the timeout.

      This attribute defaults to `0`.
     | 
    xs:unsignedInt | 
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
