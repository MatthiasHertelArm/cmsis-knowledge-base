---
id: "abi-semihosting-for-aarch32-and-aarch6-about-this-document"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: About this document"
summary: "The following support level definitions are used by the Arm ABI specifications:"
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Change control



#### Current status and anticipated changes


The following support level definitions are used by the Arm ABI specifications:

**Release**
   Arm considers this specification to have enough implementations, which have
   received sufficient testing, to verify that it is correct. The details of these
   criteria are dependent on the scale and complexity of the change over previous
   versions: small, simple changes might only require one implementation, but more
   complex changes require multiple independent implementations, which have been
   rigorously tested for cross-compatibility. Arm anticipates that future changes
   to this specification will be limited to typographical corrections,
   clarifications and compatible extensions.

**Beta**
   Arm considers this specification to be complete, but existing
   implementations do not meet the requirements for confidence in its release
   quality. Arm may need to make incompatible changes if issues emerge from its
   implementation.

**Alpha**
   The content of this specification is a draft, and Arm considers the
   likelihood of future incompatible changes to be significant.

All content in this document is at the **Release** quality level.


#### Change history


If there is no entry in the change history table for a release, there are no
changes to the content of the document for that release.


+---------+------------------+------------------------------------------------------+
| Issue   | Date             | Change                                               |
+=========+==================+======================================================+
|   2.0   | 16 December 2016 | Semihosting extensions incorporated and text updated |
+---------+------------------+------------------------------------------------------+
|  2019Q4 | 30 January 2020  | In the `Requirements for semihosting callers`        |
|         |                  | example, change `_` to `-` in                        |
|         |                  | `:semihosting-features`.                             |
+---------+------------------+------------------------------------------------------+
|  2020Q4 | 21\ `st`    | - document released on Github                        |
|         | December 2020    | - new Licence_: CC-BY-SA-4.0                         |
|         |                  | - new sections on Contributions_,                    |
|         |                  |   Trademark notice, and Copyright_                |
+---------+------------------+------------------------------------------------------+
|  2023Q3 | 6\ `st`     | Specify SYS_TIME return value as unsigned            |
|         | October 2023     |                                                      |
+---------+------------------+------------------------------------------------------+

### Terms and abbreviations


The ABI for the Arm Architecture uses the following terms and abbreviations.


AAPCS
   Procedure Call Standard for the Arm Architecture.

ABI
   Application Binary Interface:

   #. The specifications to which an executable must conform in
      order to execute in a specific execution environment. For
      example, the Linux ABI for the Arm Architecture.

   #. A particular aspect of the specifications to which
      independently produced relocatable files must conform in
      order to be statically linkable and executable.
      For example, the AAELF32, RTABI32, ...

AEABI
   (Embedded) ABI for the Arm architecture (this ABI...)

Arm-based
   ... based on the Arm architecture ...

core registers
   The general purpose registers visible in the Arm architecture’s
   programmer’s model, typically r0-r12, SP, LR, PC, and CPSR.

EABI
   An ABI suited to the needs of embedded, and deeply embedded (sometimes
   called free standing), applications.

Q-o-I
   Quality of Implementation – a quality, behavior, functionality, or
   mechanism not required by this standard, but which might be provided by
   systems conforming to it.  Q-o-I is often used to describe the
   toolchain-specific means by which a standard requirement is met.

VFP
   The Arm architecture’s Floating Point architecture and instruction set.
   In this ABI, this abbreviation includes all floating point variants
   regardless of whether or not vector (V) mode is supported.
