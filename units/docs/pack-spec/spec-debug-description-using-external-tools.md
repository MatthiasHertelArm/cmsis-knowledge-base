---
id: "spec-debug-description-using-external-tools"
type: "concept"
domain: "pack"
title: "Debug Description: Writing debug access sequences / Using external tools"
summary: "Part of: Writing debug access sequences"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

_Part of: Writing debug access sequences_

Some functionality cannot be implemented by debug sequences, for example checksum/hash calculations or debug authentication.
It is supposed to be provided or implemented by external tools or applications. To communicate with external tools, debug
sequences currently provide input/output files. To create these files, buffers are used (see below). To run an external
application, use the `RunApplication` function. To run a Python script, use the `RunPythonScript` function. To check the
availability of an external resource (for example a file), use the `FilePathExists` function.

**Buffer** **handling**

Buffers are hidden inside the sequence engine. They can be accessed only via the following functions:
- For direct buffer access (for example for initialization or "memset" operations): `BufferSet,` `BufferGet,` and
  `BufferSize.`
- For interaction with the target's memory: `BufferRead` and `BufferWrite.`
- For external interaction via file stream: `BufferStreamIn` and `BufferStreamOut.`
- Buffer sizes are adjusted as per operations. They cannot get smaller during a sequence execution, only larger.
- Buffers can internally have a size of '0', causing an error if calling BufferWrite/BufferStreamOut without having
  previously filled the buffer.
- Newly allocated buffer space is filled with 0's, e.g. for an initial call to BufferRead with a buffer offset.
- Buffers are only valid within the sequence creating them. When calling for example a "ChildSequence", it does not see
  buffers from the caller (even when using the same buffer ID). All buffer operations are only valid for buffers of the
  "ChildSequence".  
	
 **Character** **sequences**

For communication with external tools, you sometimes need to specify file names and paths to the files that contain the data
to be exchanged. The following character sequences can be used as placeholders:

- `$P:` Software project path including trailing slash
- `\#P:` Software project path + project name, e.g. /project_path/project_name
- `$L:` Folder path of the main output file of a software project including trailing slash
- `\%L:` Full path to the main output file of a software project including file ending
- `$S:` Path to the device support pack including trailing slash
- `$D:` Name of the selected device

**Note:**
Characters '$', '#', and '\%' must be duplicated to escape them, i.e. if a path contains the '$' character it must be written
as '$$'.

 **Code Example: Calculating a hash sum**

The following code example shows how to call an external tool to calculate a hash for an image file.

```
<block>
  __var length     = 0;
  __var exitCode   = 0;
  __var fileExists = 0;
  
  BufferRead     (0, 0, 0x0080C000, 0xE0, (32|1));   // Implicit allocation of buffer 0
  BufferStreamOut(0, 0, 0xE0, "$P/SAML11_SHA256_BOCOR_input.bin", 0, 0);
  exitCode   = RunApplication ("$S/Tools/CalcSHA256.exe", "$P/SAML11_SHA256_BOCOR_input.bin --some-SHA256-parameters --out $P/SAML11_SHA256_BOCOR_output.bin", "$P", 10000000);  // Timeout is 10 seconds
</block>

<control if="exitCode == 0" info="0 means OK">
  <block>
    fileExists = (FilePathExists("$P/SAML11_SHA256_BOCOR_output.bin", 5000000) == 0);
  </block>
  <control if="fileExists">
    <block>
      BufferStreamIn(0, 0xE0, 0x20, "$P/SAML11_SHA256_BOCOR_output.bin", 0, 10000000);  // Append to buffer, timeout 10s
      BufferWrite   (0, 0, 0x0080C000, 0x100, (32|1));
    </block>
  </control>
</control>

<control if="(exitCode != 0) || (fileExists == 0)">
  <block>
    Message(2, "Error while creating hashsum. Aborting sequence.");
  </block>
</control>

```
