---
id: "threadx-chapter-1-introduction-to-threadx-safety-certifications"
type: "concept"
domain: "rtos"
title: "Chapter 1 - Introduction to ThreadX: Safety Certifications"
summary: "ThreadX has been certified by SGS-TÜV Saar for use in safety-critical systems, according to IEC-61508 SIL 4."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter1.md#safety-certifications"
license: "MIT"
mode: "V"
---

### TÜV Certification

ThreadX has been certified by SGS-TÜV Saar for use in safety-critical systems, according to IEC-61508 SIL 4. The certification confirms that ThreadX can be used in the development of safety-related software for the highest safety integrity levels of IEC-61508 for the "Functional Safety of electrical, electronic, and programmable electronic safety-related systems." SGS-TUV Saar, formed through a joint venture of Germany's SGS-Group and TUV Saarland, has become the leading accredited, independent company for testing, auditing, verifying, and certifying embedded software for safety-related systems worldwide.

(figure: TÜV Certification)

- IEC 61508 up to SIL 4

### MISRA C Compliant

MISRA C is a set of programming guidelines for critical systems using the C programming language. The original MISRA C guidelines were primarily targeted toward
automotive applications; however, MISRA C is now widely recognized as being applicable to any safety critical application. ThreadX is compliant with all "required" and "mandatory" rules of MISRA-C:2004 and MISRA C:2012. ThreadX is also compliant with all but three "advisory" rules. Refer to the **_ThreadX_MISRA_Compliance.pdf_**.
document for more details.

### UL Certification

ThreadX has been certified by UL for compliance with UL 60730-1 Annex H, CSA E60730-1 Annex H, IEC 60730-1 Annex H, UL 60335-1 Annex R, IEC 60335-1 Annex R, and UL 1998 safety standards for software in programmable components. Along with IEC/UL 60730-1, which has requirements for "Controls Using Software" in its Annex H, the IEC 60335-1 standard describes the requirements for "Programmable Electronic Circuits" in its Annex R. IEC 60730 Annex H and IEC 60335-1 Annex R address the safety of MCU hardware and software used in appliances such as washing machines, dishwashers, dryers, refrigerators, freezers, and ovens.

(figure: UL Certification)

_UL/IEC 60730, UL/IEC 60335, UL 1998_
