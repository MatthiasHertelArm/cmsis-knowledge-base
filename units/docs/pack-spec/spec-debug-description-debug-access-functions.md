---
id: "spec-debug-description-debug-access-functions"
type: "concept"
domain: "pack"
title: "Debug Description: Writing debug access sequences / Debug access functions"
summary: "Part of: Writing debug access sequences"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

_Part of: Writing debug access sequences_

Debug access functions can be called in expressions in order to interact with the target device
and the user. Parameters to functions can again be expressions.

By default, a debugger must abort the execution of a debug access sequence if a function call fails.
However, this behavior can be controlled from a sequence by the __errorcontrol debug access variable.



The following table describes the existing debug access functions, their parameters and the
debug access variables which are evaluated for the function call.



  | 
    Function | 
    Description | 
  

  | 
    
Sequence("name") | 
    
      Execute a debug access sequence.
      Calling a sequence by this function causes the modifiable debug access variables **__dp**,
      **__ap**, **__apid**, and **__errorcontrol** to be pushed on a sequence execution stack. Returning
      from such a call will restore the state of these variables.

      

      **Parameters:**

      - name: Name of the sequence to execute. It must be enclosed by quotes.
      
      **Return Value:**

      Always returns `0`.

      **Code Example:**

	  Refer to sequenceExample
     | 
  

  | 
    
Read8(addr) | 
    
      Read an 8-bit value from target memory.
      **A device must support native 8-bit memory accesses for this function to succeed.**

      

      **Parameters:**

      - addr: Memory address to read from.
      
      **Debug Access Variables:**

      
      If **no** access port elements exist:

      - __dp: The debug port to use for this memory access.
      - __ap: The access port to use for this memory access.

      If access port elements exist:

      - __apid: The ID of the access port element to use for this memory access.
      
      **Return Value:**

      The 8-bit value as read from target memory.

      **Code Example:**

	  Refer to userTraceStart
     | 
  

  | 
    
Read16(addr) | 
    
      Read an 16-bit value from target memory.
      **A device must support native 16-bit memory accesses for this function to succeed.**

      

      **Parameters:**

      - addr: Memory address to read from.
      
      **Debug Access Variables:**


      If **no** access port elements exist:

      - __dp: The debug port to use for this memory access.
      - __ap: The access port to use for this memory access.
      
      If access port elements exist:

      - __apid: The ID of the access port element to use for this memory access.

      **Return Value:**

      The 16-bit value as read from target memory.
     | 
  

  | 
    
Read32(addr) | 
    
      Read an 32-bit value from target memory.
      **A device must support native 32-bit memory accesses for this function to succeed.**

      

      **Parameters:**

      - addr: Memory address to read from.
      
      **Debug Access Variables:**


      If **no** access port elements exist:

      - __dp: The debug port to use for this memory access.
      - __ap: The access port to use for this memory access.

      If access port elements exist:

      - __apid: The ID of the access port element to use for this memory access.

      **Return Value:**

      The 32-bit value as read from target memory.

      **Code Example:**

      Refer to resetSystem
     | 
  

  | 
    
Read64(addr) | 
    
      Read an 64-bit value from target memory.
      **A device must support native 64-bit memory accesses for this function to succeed.**

      

      **Parameters:**

      - addr: Memory address to read from.
      
      **Debug Access Variables:**


      If **no** access port elements exist:

      - __dp: The debug port to use for this memory access.
      - __ap: The access port to use for this memory access.
      
      If access port elements exist:

      - __apid: The ID of the access port element to use for this memory access.

      **Return Value:**

      The 64-bit value as read from target memory.
     | 
  

  | 
    
ReadAP(addr) | 
    
      Read a 32-bit value from an access port register.

      

      **Parameters:**

      - addr: AP register address to read from. Addresses larger than `0xF` automatically cause
      an AP register bank switch. 
      
      **Debug Access Variables:**


      If **no** access port elements exist:

      - __dp: The debug port to use for this memory access.
      - __ap: The access port to use for this memory access.
      
      If access port elements exist:

      - __apid: The ID of the access port element to use for this memory access.

      **Return Value:**

      The 32-bit value as read from the AP register.

      **Code Example:**

      Refer to userDebugDeviceUnlock
     | 
  

  | 
    
ReadAccessAP(addr) | 
    
      Read a 32-bit value from an address in the system's APv2 (ADIv6) top-level access port space.

      

      **Parameters:**

      - addr: Address within the system's top-level AP address space.
      
      **Debug Access Variables:**

      - __dp: The debug port to use for this access.

      **Return Value:**

      The 32-bit value as read from the top-level AP address.

      **Code Example:**

      Refer to DebugDeviceUnlock
     | 
  

  | 
    
ReadDP(addr) | 
    
      Read a 32-bit value from a debug port register.

      

      **Parameters:**

      - addr: DP register address to read from.
      
      **Debug Access Variables:**

      - __dp: The debug port to use for this memory access.

      **Return Value:**

      The 32-bit value as read from the DP register.

      **Code Example:**

      Refer to debugPortSetup
     | 
  

  | 
    
Write8(addr, val) | 
    
      Write an 8-bit value to target memory.
      **A device must support native 8-bit memory accesses for this function to succeed.**

      

      **Parameters:**

      - addr: Memory address to write to.
      - val: Value to write.
      
      **Debug Access Variables:**


      If **no** access port elements exist:

      - __dp: The debug port to use for this memory access.
      - __ap: The access port to use for this memory access.

      If access port elements exist:

      - __apid: The ID of the access port element to use for this memory access.

      **Return Value:**

      Always returns `0`.

      **Code Example:**

	  Refer to userTraceStart
     | 
  

  | 
    
Write16(addr, val) | 
    
      Write a 16-bit value to target memory.
      **A device must support native 16-bit memory accesses for this function to succeed.**

      

      **Parameters:**

      - addr: Memory address to write to.
      - val: Value to write.
      
      **Debug Access Variables:**


      If **no** access port elements exist:

      - __dp: The debug port to use for this memory access.
      - __ap: The access port to use for this memory access.

      If access port elements exist:

      - __apid: The ID of the access port element to use for this memory access.

      **Return Value:**

      Always returns `0`.
     | 
  

  | 
    
Write32(addr, val) | 
    
      Write a 32-bit value to target memory.
      **A device must support native 32-bit memory accesses for this function to succeed.**

      

      **Parameters:**

      - addr: Memory address to write to.
      - val: Value to write.
      
      **Debug Access Variables:**


      If **no** access port elements exist:

      - __dp: The debug port to use for this memory access.
      - __ap: The access port to use for this memory access.

      If access port elements exist:

      - __apid: The ID of the access port element to use for this memory access.

      **Return Value:**

      Always returns `0`.

      **Code Example:**

      Refer to debugCoreStart
     | 
  

  | 
    
Write64(addr, val) | 
    
      Write a 64-bit value to target memory.
      **A device must support native 64-bit memory accesses for this function to succeed.**

      

      **Parameters:**

      - addr: Memory address to write to.
      - val: Value to write.
      
      **Debug Access Variables:**


      If **no** access port elements exist:

      - __dp: The debug port to use for this memory access.
      - __ap: The access port to use for this memory access.

      If access port elements exist:

      - __apid: The ID of the access port element to use for this memory access.

      **Return Value:**

      Always returns `0`.
     | 
  

  | 
    
WriteAP(addr, val) | 
    
      Write a 32-bit value to an access port register.
      Addresses larger than 0xF automatically cause an AP register bank switch.

      

      **Parameters:**

      - addr: Memory address to write to.
      - val: Value to write.
      
      **Debug Access Variables:**


      If **no** access port elements exist:

      - __dp: The debug port to use for this memory access.
      - __ap: The access port to use for this memory access.

      If access port elements exist:

      - __apid: The ID of the access port element to use for this memory access.

      **Return Value:**

      Always returns `0`.

      **Code Example:**

      Refer to hwReset
     | 
  

  | 
    
WriteAccessAP(addr) | 
    
      Write a 32-bit value to an address in the system's APv2 (ADIv6) top-level access port space.

      

      **Parameters:**

      - addr: Address within the system's top-level AP address space.
      
      **Debug Access Variables:**

      - __dp: The debug port to use for this access.

      **Return Value:**

      Always returns `0`.

      **Code Example:**

      Refer to DebugDeviceUnlock
     | 
  

  | 
    
WriteDP(addr, val) | 
    
      Write a 32-bit value to a debug port register.

      

      **Parameters:**

      - addr: Memory address to write to.
      - val: Value to write.
      
      **Debug Access Variables:**

      - __dp: The debug port to use for this memory access.

      **Return Value:**

      Always returns `0`.

      **Code Example:**

      Refer to debugPortStart
     | 
  

  | 
    
FlashWriteBuffer(addr, offs, len, mode) | 
    
      Write flash buffer contents into target memory.
      A debugger fills the flash buffer before it executes a flash programming sequence.

      

      **Parameters:**

      - addr: Target memory buffer or register interface address to write the flash buffer contents. Must be a multiple of
	    the number of bytes as specified by access size in parameter **mode.**
      - offs: Offset into the flash buffer to start writing from. Must be a multiple of the number of bytes as specified by
	    access size in parameter **mode.**
      - len : Number of bytes to write to the target. If **offs** + **len** exceeds the flash buffer length set in
	    variable **__FlashLen**, then the remaining bytes are filled with the pattern as specified by attribute
		**filler** of the block element. Must be a multiple of the number of bytes as specified
		by access size in parameter **mode.**
      - mode: Target access mode. The following bit map applies:
        - Bit 0..8: Debug access size. One of `8`, `16`, `32` and `64`. The specified debug access
		  size must be supported by the target debug access port.
        - Bit 0: Additionally, set this Bit to `1` to increment the target address after each debug write access of the
		  specified size.
        - Bit 9..63: Reserved

      **Debug Access Variables:**


      If **no** access port elements exist:

      - __dp: The debug port to use for this memory access.
      - __ap: The access port to use for this memory access.

      If access port elements exist:

      - __apid: The ID of the access port element to use for this memory access.

      **Return Value:**

      Number of bytes written from flash buffer to target.

      **Note:** Previous versions of the specification falsely named this function `FlashBufferWrite`. All known
            implementations of this specification correctly use `FlashWriteBuffer` already.

      **Note:**
      Previous versions specified to always return `0` in case of success. This
      was changed for consistency with other debug access functions handling buffers.

     | 
  

  | 
    
DAP_Delay(delay) | 
    
      Debug probe command to wait for a specific delay.

      

      **Parameters:**

      - delay: Wait time in microseconds.

      **Return Value:**

      Always returns `0`.

      **Code Example:**

      Refer to userDebugDeviceUnlock
     | 
  

  | 
    
DAP_WriteABORT(value) | 
    
      Debug probe command to write an abort request to the CoreSight
      ABORT register of the target debug port.

      

      **Parameters:**

      - value: 32-bit value to write into the CoreSight ABORT register.
      
      **Debug Access Variables:**

      - __dp: The debug port to use for this memory access.

      **Return Value:**

      Always returns `0`.
     | 
  

  | 
    
DAP_SWJ_Pins(pinout, pinselect, pinwait) | 
    
      Debug probe command to monitor and control the I/O Pins including the nRESET
      device reset line.

      **I/O Pin Mapping** for **pinout**, **pinselect**, and **pinwait**:
        - Bit 0: SWCLK/TCK
        - Bit 1: SWDIO/TMS
        - Bit 2: TDI
        - Bit 3: TDO
        - Bit 5: nTRST
        - Bit 7: nRESET
      
      

      The **pinwait** time is useful in systems where the nRESET pin is implemented as open-drain
      output. After nRESET is de-asserted by the debugger, external circuit may still hold the
      target Device under reset for a time. Using the **pinwait** time, the debugger may monitor
      selected I/O Pins and wait until they the expected value appears or a timeout expires.

      

      **Parameters:**

      - pinout: Value for selected output pins.
      - pinselect: Selects which output pins will be modified.
      - pinwait: Wait timeout for the selected output to stabilize. A debugger must extend this timeout
        to the closest possible time granularity.
        - 0 = no wait
        - 1 .. 3000000 = time in microseconds (max 3s)

      **Return Value:**

      The state of the I/O Pins at the end of this operation. If a debugger is not
      capable of monitoring the I/O Pins, it must return a value of `0xFFFFFFFF`.
     | 
  

  | 
    
DAP_SWJ_Clock(val) | 
    
      Debug probe command to set the clock frequency for JTAG and SWD communication mode.

      

      **Parameters:**

      - val: Maximum SWD/JTAG Clock (SWCLK/TCK) value in Hz.

      **Return Value:**

      Always returns `0`.

      **Code Example:**

      Refer to resetHardware
     | 
  

  | 
    
DAP_SWJ_Sequence(cnt, val) | 
    
      Debug probe command to generate required SWJ sequences, e.g. for SWD/JTAG Reset, SWD<->JTAG
      switch and Dormant operation.

      

      **Parameters:**

      - cnt: Number of bits in sequence: 1..64. Larger sequences need to be implemented by multiple
        subsequent **DAP_SWJ_Sequence** calls. Such a sequence of **DAP_SWJ_Sequence** commands
        must be encapsulated in an atomic **block** to ensure correct execution.
      - val: Sequence generated on SWDIO/TMS (with clock \@SWCLK/TCK), LSB transmitted first.
      
      **Return Value:**

      Always returns `0`.

      **Code Example:**

      Refer to debugPortSetup
     | 
  

  | 
    
DAP_JTAG_Sequence(cnt, tms, tdi) | 
    
      Debug probe command to generate a JTAG sequence with fixed TMS value and capture TDO.

      

      **Parameters:**

      - cnt: Length of the JTAG sequence (number of TCK cycles and TDI bits): 1..64
      - tms: Fixed TMS value: 0..1
      - tdi: Data generated on TDI with one bit per TCK cycle, LSB transmitted first.
      
      **Return Value:**

      Data captured from TDO with one bit per TCK cycle, LSB captured first and padded with `0`s.
     | 
  

  | 
    
Query(type, "message", default) | 
    
      Query user input. The sequence execution stalls depending on the used **type**. If the
      debugger runs in a batch mode, this function returns the value **default**.

      

      **Parameters:**

      - type: Query type. Can be one of:
        - `0` : **Query_Ok**, displays an informative message which has to be confirmed by the user. This
          type allows the result **OK**.
        - `1` : **Query_YesNo**, displays a query with the allowed results **Yes** and **No**.
        - `2` : **Query_YesNoCancel**, displays a query with the allowed results **Yes**, **No**,
          and **Cancel**.
        - `3` : **Query_OkCancel**, displays a query with the allowed results **OK** and **Cancel**.
      - message: A constant string with the query message to display. It must not be an expression and it must be
        enclosed by quotes.
      - default: The default value to return if the debugger runs in batch mode. See **Return Values**
        for a list of allowed values.
      
      **Return Value:**

      The result of the query. The user input maps to the following numbers:
      - Error  : `0`
      - OK     : `1`
      - Cancel : `2`
      - Yes    : `3`
      - No     : `4`

      **Code Example:**

      Refer to debugPortSetup
     | 
  

  | 
    
QueryValue("message", default) | 
    
      Query input value from user. The sequence execution stalls until the user has entered a value or canceled the query.
      This function returns the **default** value if the user canceled the query or if the debugger runs in a batch mode.

      

      **Parameters:**

      - message: A constant string with the query message to display. It must not be an expression and it must be
        enclosed by quotes.
      - default: The default value to return if the user cancels the query or if the debugger runs in batch mode.

      **Return Value:**

      The queried value.

     | 
  

  | 
    
Message(type, "format", ...) | 
    
      Outputs a message to a log window.

      

      **Parameters:**

      - type: Message type. Can be one of:
        - `0` : **Info**, outputs an informative message.
        - `1` : **Warning**, outputs a warning.
        - `2` : **Error**, outputs an error and aborts the execution of the current sequence and its callers.
      - format: A constant string with the message format. It must not be an expression and it must be
                 enclosed by quotes. The string has the following format:

```
                 %[flags][width][.precision]specifier
```
        - Specifiers:
          - `\%u`: 32-bit unsigned decimal integer.
          - `\%llu`: 64-bit unsigned decimal integer.
          - `\%x`: 32-bit unsigned hexadecimal integer, lower case letters.
          - `\%llx`: 64-bit unsigned hexadecimal integer, lower case letters.
          - `\%X`: 32-bit unsigned hexadecimal integer, upper case letters.
          - `\%llX`: 64-bit unsigned hexadecimal integer, upper case letters.
          - `\%o`: 32-bit unsigned octal integer.
          - `\%llo`: 64-bit unsigned octal integer.
          - `\%b`: 32-bit unsigned binary integer.
          - `\%llb`: 64-bit unsigned binary integer.
          - `\%f`: Single-precision (32-bit) floating point value.
          - `\%Lf`: Double-precision (64-bit) floating point value.
          - `\%s`: Constant character string. Must not be an expression.
          - `\%\%`: Print `\%` character.
        - Flags:
          - `0`: Pad the displayed value with zeros instead of spaces if padding is required by
                       the `width` option.
        - Width: Minimum number of displayed characters. If `width` is less than the number of characters
                         of the value, then the value is padded with spaces to the left.
        - .Precision:
          - **Integer**: Minimum number of displayed digits. Padded with zeros to the left if the
                             value has less digits than specified with `.precision`.
          - **Floating Point**: Number of displayed digits after decimal point. Defaults to `6`
                                    if not specified.
          - **Constant String**: Maximum number of displayed characters.
      - ... : Additional function parameters to replace format string specifiers. Each parameter can be
             a constant string, or an expression that resolves to an unsigned 64-bit integer. A parameter
             type must match the corresponding specifier type.

      **Return Value:**

      Always returns `0`.

      **Note:**
      For 32-bit specifiers the **Message** command must print the lower 32 Bit of a 64 Bit debug access variable.

     | 
  

  | 
    
LoadDebugInfo("file") | 
    
      Loads DWARF debug information from an application executable.

      

      **Parameters:**

      - file: A constant string with the path to the executable. The path must be relative to the root folder of the pack and
	    use the format **path/name.extension**. It must not be an expression and it must be enclosed by quotes.
              
      **Return Value:**

      Returns `0` after successful debug information load.

      Returns `1` if debug information load failed.

     | 
  

  | 
    **Functions for communicating with external tools** | 
  

  | 
    
BufferSet (buffID, buffOffset, count, size, value) | 
    
        Fill a buffer with a specific value pattern. A new buffer of required size is created if it does not exist. An
		existing buffer is extended if it is too small.

        

        **Parameters:**

        - buffID: Numeric buffer ID. Must be a constant number.
        - buffOffset: First byte in the buffer to start writing the specified **value** pattern. Must be a multiple of **size.**
        - count: Number of **size** items to write with the specified **value** pattern.
        - size: Size of a single item to set. Must be in the range of 1 - 8.
        - value: Value pattern to set. The **size** least significant bytes of **value** are used as value pattern for writing
		  the buffer.
        
        **Return Value:**

        Number of written bytes (written bytes * access size).
        
     | 
  

  | 
    
BufferGet (buffID, buffOffset, size) | 
    
        Get a data item from the buffer.

        

        **Parameters:**

        - buffID: Numeric buffer ID. Must be a constant number. Function fails if buffer does not exist.
        - buffOffset: Buffer offset in bytes to get the data item from. Must be a multiple of **size.**
        - size: Size of a single item to get. Must be in the range of 1 - 8.

        **Return Value:**

        Data value of specified size at buffer offset.
     | 
  

  | 
    
BufferSize (buffID) | 
    
        Get the current size of a data buffer.

        

        **Parameters:**

        - buffID: Numeric buffer ID. Must be a constant number.
        
        **Return Value:**

        Current buffer size in bytes. Return value is `0` if a buffer does not exist.
     | 
  

  | 
    
BufferRead (buffID, buffOffset, addr, length, mode) | 
    
        Read data from target and store in buffer. A new buffer of required size is created if it does not exist. An existing
		buffer is extended if it is too small.

        

        **Parameters:**

        - buffID: Numeric buffer ID. Must be a constant number.
        - buffOffset: First byte in the buffer to store the read data. Must be a multiple of the number of bytes as specified
		  by access size in **mode.**
        - addr: Target address to start reading from. Must be a multiple of the number of bytes as specified by access size
		  in **mode.**
        - length: Number of bytes to read from target. Must be a multiple of the number of bytes as specified by access size
		  in **mode.**
        - mode: The target access mode.
          - Bit 0..8: Debug access size. One of 8, 16, 32 and 64. Specified debug access size must be supported by the target
		    hardware. For example a DP register access must always be 32-Bit.
          - Bit 0: Additionally set this Bit to 1 to increment the target address after each debug read access of the
		    specified size.
          - Bit 9: Target address space.
            - `0`: Access target memory using the access port specified by **__ap** or **__apid**.
            - `1`: Access an address in the system's APv2 (ADIv6) top-level access port space.

              This address space only supports 32-bit accesses. The debugger must generate an error if a different debug access size is specified.
          - Bit 10..63: Reserved
                
        **Debug Access Variables:**

  
        If **no** access port elements exist:

        - __dp: The debug port to use for this access.
        - __ap: The access port to use if Bit 9 of **mode** is `0`.
  
        If access port elements exist:

        - __apid: The ID of the access port element to use for this memory access. If Bit 9 of **mode** is `1`,
          only the debug port referenced by **__apid** is used.

        **Return Value:**

        Always `0`. Function causes fatal error if not successful.

        **Code Example:**

        Refer to Calculating a hash sum
     | 
  

  | 
    
BufferWrite(buffID, buffOffset, addr, length, mode) | 
    
        Write data from buffer into target.

        

        **Parameters:**

        - buffID: Numeric buffer ID. Must be a constant number. Function fails if buffer does not exist.
        - buffOffset: First byte in the buffer to transfer into target. Must be a multiple of the number of bytes as
		  specified by access size in **mode.**
        - addr: Target address to start writing to. Must be a multiple of the number of bytes as specified by access size in
		  **mode.**
        - length: Number of bytes to write to the target. Must be a multiple of the number of bytes as specified by access
		  size in **mode.** If size of valid buffer data is less than (**buffOffset** + **length)** then the function ends early
		  and returns the number of actually written bytes.
        - mode: The target access mode.
          - Bit 0..8: Debug access size. One of 8, 16, 32 and 64. Specified debug access size must be supported by the target
		    hardware. For example a DP register access must always be 32-Bit.
          - Bit 0: Additionally set this Bit to `1` to increment the target address after each debug write access of
		    the specified size.
          - Bit 9: Target address space.
            - `0`: Access target memory using the access port specified by **__ap** or **__apid**.
            - `1`: Access an address in the system's APv2 (ADIv6) top-level access port space.

              This address space only supports 32-bit accesses. The debugger must generate an error if a different debug access size is specified.
          - Bit 10..63: Reserved
                
        **Debug Access Variables:**

  
        If **no** access port elements exist:

        - __dp: The debug port to use for this access.
        - __ap: The access port to use if Bit 9 of **mode** is `0`.
  
        If access port elements exist:

        - __apid: The ID of the access port element to use for this memory access. If Bit 9 of **mode** is `1`,
          only the debug port referenced by **__apid** is used.

        **Return Value:**

        Number of bytes written from buffer to target. Function causes fatal error if not successful.

        **Note:**
        Previous versions specified to always return `0` in case of success. This
        was changed for consistency with other debug access functions handling buffers.

        **Code Example:**

        Refer to Calculating a hash sum
     | 
  

  | 
    
BufferStreamIn (buffID, buffOffset, length, path, mode, timeout) | 
    
        Stream data from an external source, e.g. a file, into a buffer. A new buffer of required size is created if it does
		not exist. An existing buffer is extended if it is too small.

        

        **Parameters:**

        - buffID: Numeric buffer ID. Must be a constant number.
        - buffOffset: First byte in the buffer to store the received data.
        - length: Maximum number of bytes to stream in. Use value 0xFFFFFFFFFFFFFFFF to for example read a complete file of
		  unknown size.
        - path: Constant string value representing the source from which to stream data in. Refer to
		  character sequences for path/file name place holders.
        - mode: Specifies how to treat the data source in the specified mode.
          - Bit 0..3: Format of the data source:

		    `0` - Binary File

			Others - Reserved

          - Bit 4..7: Communication options for data source:

		    Reserved
        - timeout: Timeout of file operation in microseconds. If `0`, then synchronously wait for the operation to finish.
        
        **Return Value:**

        Number of bytes streamed into buffer. Can be less than **length** if the data source signals its end.

        **Code Example:**

        Refer to Calculating a hash sum
     | 
  

  | 
    
BufferStreamOut (buffID, buffOffset, length, path, mode, timeout) | 
    
        Stream data from a buffer to an external data sink, e.g. a file.

        

        **Parameters:**

        - buffID: Numeric buffer ID. Must be a constant number. Function fails if buffer does not exist.
        - buffOffset: First byte in the buffer to transfer to the external data sink.
        - length: Maximum number of bytes to stream out.
        - path: Constant string value representing the destination to which to stream data.
          - For the Binary File format, refer to character sequences for path/file name place holders.
          - For the Trace Buffer format, this is the **name** of a specified `<trace_tracebuffer>` element representing
            a data pipe into the debugger. If there is only a single unnamed **tracebuffer** element then an empty string may be used.
        - mode: Specifies how to treat the data sink in the specified mode.
          - Bit 0..3: Format of the data sink:

		    `0` - Binary File: The sequence writes the data to a binary file in the host filesystem.

		    `1` - Trace Buffer: The sequence sends the data to a debugger-internal trace buffer for further processing.

			Others - Reserved

          - Bit 4..7: File write option (only applies to Binary File format; ignored for Trace Buffer format):

		    `0` - Overwrite

		    `1` - Append

			Others - Reserved

        - timeout: Timeout in microseconds. If `0`, then synchronously wait for the operation to finish.

          - This does not include file-system delays, e.g. between creation and visibility in a file browser. Use **FilePathExists**
            debug access function to wait for a new file to become accessible.
        
        **Return Value:**

        Number of bytes streamed to data sink.

        **Code Example:**

        Refer to Calculating a hash sum
     | 
  

  | 
    
TraceBufferSelected(name) | 
    
        Check whether a trace buffer is selected in the trace configuration.

        

        **Parameters:**

        - name: Constant string that identifies a named trace buffer. An empty string identifies the unnamed trace
          buffer.
        

        Use the **name** attribute of the matching `<trace_tracebuffer>` element for a named trace buffer.
        Use an empty string for the unnamed **tracebuffer** element. If no applicable **trace** element is
        specified, the default configuration provides the unnamed trace buffer; its
        selection corresponds to bit 2 of __traceout.

        

        **Return Value:**

        Returns `1` if the identified trace buffer is selected; otherwise returns `0`. An empty **name** is an
        error if the selected trace configuration contains multiple trace buffers.

        **Code Example:**

```
        <control if="TraceBufferSelected(&quot;MyTraceBuffer&quot;)">
          <block>
            // Read and forward trace data from the trace buffer called 'MyTraceBuffer'
          </block>
        </control>
```
     | 
  

  | 
    
RunApplication (appPath, arguments, workDirectory, timeout) | 
    
        Run an external application.

        

        **Parameters:**

        - appPath: Constant string representing the application path. Refer to character sequences
		  for path/file name place holders.
        - arguments: Constant string with arguments to pass to the command line. Same placeholder
		  character sequences apply as for **appPath.**
        - workDirectory: A constant string with the work directory for the command line tool. An empty string means that the
		  work directory is the current project folder. Same placeholder character sequences apply
		  as for **appPath.**
        - timeout: Timeout in microseconds
        
        **Return Value:**

        Application specific exit code.

        **Code Example:**

        Refer to Calculating a hash sum
     | 
  

  | 
    
RunPythonScript (scriptPath, arguments, workDirectory, timeout) | 
    
        Run a Python script using a Python interpreter available on the host system.

        

        **Parameters:**

        - scriptPath: Constant string representing the Python script path. Refer to character sequences
          for path/file name place holders.
        - arguments: Constant string with arguments to pass to the script command line. Same placeholder
          character sequences apply as for **scriptPath**.
        - workDirectory: A constant string with the work directory for running the script. An empty string means that the
          work directory is the current project folder. Same placeholder character sequences apply
          as for **scriptPath**.
        - timeout: Timeout in microseconds.

        **Return Value:**

        Script specific exit code.
     | 
  

  | 
    
FilePathExists(path, timeout) | 
    
        Check if a path exists. If timeout is other than `0` then check the path until it becomes valid or until the
		timeout has elapsed.

        

        **Parameters:**

        - path: Constant string with the path to check. Refer to character sequences for path/file
		  name place holders.
        - timeout: Timeout in microseconds:

          If `0`, then the path is checked once before the function returns.

		  If other than `0`, the function checks the path until it is valid or until the function times out. If **timeout** is hit
		  while executing a check, then the function completes the check and returns its result.

        
        **Return Value:**

        `0` - Path exists

		`1` - Path not found

		Others - Reserved


        **Code Example:**

        Refer to Calculating a hash sum
     | 
  

  | 
    
FlashLoadAlgorithm(algoPath, ramStart, ramSize) | 
    
      Select an FLM flash algorithm for the current flash erase or program phase. This function is valid only in a
      **FlashEraseSetup** or **FlashProgramSetup** sequence. The selected algorithm is loaded by the debugger when
      the corresponding phase is performed.

      

      **Parameters:**

      - algoPath: Constant string representing the path to an FLM file. Refer to character sequences
        for path/file name place holders.
      - ramStart: Start address of target RAM available to the FLM algorithm. The address must be in a defined RAM region.
      - ramSize: Size, in bytes, of target RAM available to the FLM algorithm. If the range extends beyond the containing
        RAM region, the debugger limits it to the available RAM.

      **Return Value:**

      `0` - Flash algorithm selected successfully.

      `1` - Flash algorithm could not be selected.

      

      If this function returns `1`, the current erase or program phase fails. It does not fall back to flash debug
      sequences.
     | 
  



**Note:**
- Target memory access functions must perform a debug access of the size indicated by their name. The target system must
  support debug accesses of this size.
- Results of all functions are casted to 64-bit unsigned integer values.
- Some target access functions determine the used debug and access port by the current values of the **__dp** and
  **__ap**, and the **__apid** debug access variables. If a target access requires a different debug or access port than the default ones, it
  must change these values. This change is held until finishing the sequence the change has occurred in.
- If the debug description describes access port elements then use of **__dp** is limited to the **ReadDP()**, **WriteDP()**, and **DAP_WriteABORT()** debug access functions. All other debug access functions determine the used debug port from the access port element referenced by **__apid**.
- If the debug description describes access port elements then **__ap** must not be used. Use **__apid** instead.
- A call to **WriteDP()** to change the DP SELECT register does not implicitly change the value of the debug access variables
  **__ap** or **__apid**. Those need to be explicitly updated to select a different AP for subsequent AP register and memory accesses.
- If a debug access function fails with an error, and if this error is not ignored by configuration of the **__errorcontrol** debug access variable, then the current sequence and its callers abort.
