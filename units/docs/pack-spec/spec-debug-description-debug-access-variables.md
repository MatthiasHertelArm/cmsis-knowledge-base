---
id: "spec-debug-description-debug-access-variables"
type: "concept"
domain: "pack"
title: "Debug Description: Writing debug access sequences / Debug access variables"
summary: "Part of: Writing debug access sequences"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

_Part of: Writing debug access sequences_

Debug access variables hold 64-bit unsigned integer values and are used in debug access sequences to query debugger settings
and states. They are **read-only** within a sequence except from a limited set of the
pre-defined debug access variables. Use the **debugvars** element to specify additional
user-defined debug access variables.

User-defined debug access variable names must not be reused for local sequence variables. To avoid name clashes,
pre-defined debug access variables and local variables used by debugger-provided default sequence implementations
should use the `__` prefix. Local variables in DFP-provided sequences should not use the `__` prefix,
including when a DFP copies and adapts a default sequence shown in this specification. If a debugger
implementation copies a default sequence from this specification, it should add the `__` prefix to
local variable names.

 **Table: Pre-defined Debug Access Variables**

A debugger needs to support a set of pre-defined debug access variables. These are described in the following table.



  | 
    Variable | 
    Access | 
    Description | 
    Value= | 
  

  | 
    
__protocol | 
    Read-Only | 
    
      Debug protocol selection and parameters for target connection.
     | 
    
      The following bit map applies:

      - Bit 0..15: Type
        - `0`: Error

        - `1`: JTAG

        - `2`: Serial Wire Debug (SWD)

        - `3`: CJTAG

      - Bit 16: SWJ-DP
      - Bit 17: Switch through dormant state
      - Bit 18..63: Reserved
     | 
  

  | 
    
__connection | 
    Read-Only | 
    
      Target connection configuration.
     | 
    
      The following bit map applies:

      - Bit 0..7: Connection type
        - `0`: Error or target is disconnected.
        - `1`: Connection for target debug.
        - `2`: Connection for downloading application to flash.
      - Bit 8..15: Reset type
        - `0`: Error.
        - `1`: Hardware Reset (debugger reset line).
        - `2`: System Reset Request.
        - `3`: Processor Reset Request ("Vector Reset").
      - Bit 16: Connection under Hardware Reset (debugger reset line)
      - Bit 17: Hardware Reset is executed as a pre-connection reset (only used for debugger calls to `ResetHardware)`
      - Bit 18: Reset sequence is expected to finish with the CPU halted in Debug state (only used for debugger calls to reset sequences)
      - Bit 19..63: Reserved
     | 
  

  | 
    
__dp | 
    Read/Write | 
    
      Debug Port selected for target accesses.

      This variable is initialized when entering a pre-defined debug access
      sequence on a debug event. The initialization value
      is the **__dp** as defined for the used **debug** element.
      

      If access port elements exist then use of **__dp** is limited to the **ReadDP()**,
      **WriteDP()**, and **DAP_WriteABORT()** debug access functions.
     | 
    
      Debug port ID as specified in a **debugport** element or
      `0` if no **debugport** element exists.
     | 
  

  | 
    
__ap | 
    Read/Write | 
    
      Access Port selected for target accesses.

      This variable is initialized when entering a pre-defined debug access
      sequence on a debug event. The initialization value
      is the **__ap** as defined for the used **debug** element.
      

      Must not be used if access port elements exist. Use **__apid** instead.
     | 
    
      Access Port index.
     | 
  

  | 
    
__apid | 
    Read/Write | 
    
      Access Port selected for target accesses.

      This variable is initialized when entering a pre-defined debug access
      sequence on a debug event. The initialization value
      is the **__apid** as defined for the used **debug** element.
     | 
    
      Access Port ID as defined in an access port element.
     | 
  

  | 
    
	
	
__traceout | 
    Read-Only | 
    
      Activated trace outputs (sinks). Additionally holds information on the selected port width if
      a parallel trace port is enabled.
     | 
    
      The following bit map applies:

      - Bit 0: Serial Wire Output (SWO) Trace enabled.
      - Bit 1: Parallel Trace Port enabled.
      - Bit 2: Trace Buffer enabled.
      - Bit 3..15: Reserved.
      - Bit 16..21: Selected Parallel Trace Port size.
      - Bit 22..63: Reserved.
     | 
  

  | 
    
	
	
__traceclockin | 
    Read-Only | 
    
      The frequency of the clock that drives the trace output component.

      Can for example be used in combination with __traceclockout to calculate
      prescaler values for the output component.
     | 
    
      Clock frequency in Hz. A value of `0` means that no frequency is provided by the debugger, e.g. because trace is disabled.
     | 
  

  | 
    
	
	
__traceclockout | 
    Read-Only | 
    
      The frequency of the trace output signal.

      Can for example be used in combination with __traceclockin to calculate prescaler
      values for the output component.
     | 
    
      Clock frequency in Hz. A value of `0` means that no frequency is provided by the debugger, e.g. because trace is disabled or because the user did not specify it.
      In the latter case **__traceclockout** must be assumed to equal __traceclockin which effectively means a prescaler value of `1`.
     | 
  

  | 
    
	
	
__errorcontrol
	 | 
    Read/Write | 
    
      Control variable for debug access error handling. All of its bit
      fields are intialized to `0` when entering a pre-defined
      debug access sequence because of a debug event.
     | 
    
      The following bit map applies:

      - Bit 0: Skip errors if set to `1`. A debugger must
               continue the sequence execution.
      - Bit 1..63: Reserved
     | 
  

  | 
    
__Result | 
    Read/Write | 
    
      Sequence result. A debugger sets this variable to `0` before it calls a sequence.
      The sequence implementation sets it to its result.
     | 
    
      The following values apply:

      - 0: Success
      - (-1): Error
	  - Other - reserved.
     | 
  

  | 
    
__FlashOp | 
    Read-Only | 
    
      Type of the currently executed Flash operation. A debugger sets this value to `0`
      if the executed sequence is not part of a Flash operation.
     | 
    
      The following values apply:

      - 0: No flash operation
      - 1: Erase
      - 2: Program
      - 3: Verify
      - Other - reserved.
     | 
  

  | 
    
__FlashAddr | 
    Read-Only | 
    
      Start address for the current Flash operation. A debugger sets this value to `0`
      if the executed sequence is not part of a Flash operation.
     | 
    
      Memory-mapped target address the currently programmed block is visible at.
     | 
  

  | 
    
__FlashLen | 
    Read-Only | 
    
      Flash buffer length for the current flash operation. A debugger sets this value to `0`
      if the executed sequence is not part of a flash operation.
     | 
    
     | 
  

  | 
    
__FlashArg | 
    Read-Only | 
    
      Argument for the flash operation as specified in block. A debugger sets this value to `0`
      if the executed sequence is not part of a flash operation.
     | 
    
      The argument encoding is specific to the debug description for the target device.
     |
