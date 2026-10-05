---
id: "dsp-overview-variations-between-the-architectures"
type: "concept"
domain: "optimization"
title: "Overview: Variations between the architectures"
summary: "Some algorithms may give slightlty different results on different architectures (like M0 or M4/M7 or M55). It is a tradeoff made for speed reasons and to make best use of the different instruction sets."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/mainpage.md#variations-between-the-architectures"
license: "Apache-2.0"
mode: "V"
---

Some algorithms may give slightlty different results on different architectures (like M0 or M4/M7 or M55). It is a tradeoff made for speed reasons and to make best use of the different instruction sets.

All algorithms are compared with a double precision reference and the different versions (for different architectures) have the same characteristics when compared to the double precision (SNR bound, max bound for sample error ...) 

As consequence, the small differences that may exists between the different architecture implementations should be too small to have any practical consequences.

Also, when targeting Helium or Neon, some functions have  different APIs.

### Different API for Helium
* Biquad F32 and F16 : A different init function must be used
* FIR F32, F16, Q31, Q15 and Q7 : Coefficient array must be padded with zeros

### Different API for Neon
* MFCC F32, F16, Q31 and Q15 : Additional temporary buffer required for the functions
* CFFT F32, F16, Q31 and Q15 : Additional temporary buffer required for the functions
* RFFT F32, F16, Q31 and Q15 : Additional temporary buffer required for the functions. Different arguments for the init function of Q31 and Q15 RFFT

For CFFT and RFFT, a new Neon specific initialization function is available to be able to use longer FFTs.

For CFFT, this new Neon specific initialization allows to use FFT lengths with factor of 3 and 5 in the length (but must still be a multiple of 4 length).
