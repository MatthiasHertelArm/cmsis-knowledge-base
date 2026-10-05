---
id: "drv-nand-interface-arm-nand-ecc-info"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_ECC_INFO"
summary: "Stores the characteristics of a ECC (Error Correction Code) algorithm and provides the information about necessary application data handling in order to protect stored data from NAND bit errors."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_NAND_ECC_INFO
```



Stores the characteristics of a ECC (Error Correction Code) algorithm and provides the information about necessary
application data handling in order to protect stored data from NAND bit errors.

ECC algorithms applied on NAND memory typically operate on NAND device page level which is virtually divided to multiple
main and spare areas. Data from main and spare area is taken into account when generating ECC data which is also stored
into spare area. ECC codeword defines how much data will be protected and how much ECC data will be generated.

To describe how application data must be organized, ECC information structure specifies protection **type** which
defines the protected part of data. As main and spare are of different size, two different algorithms could be
provided, we can describe them as ECC0 and ECC1. Type can then have the following values:

Type| Description 
:---|:-----------
 0  | ECC algorithm not used
 1  | ECC0 algorithm protects main data
 2  | ECC0 algorithm protects main and spare data
 3  | ECC0 algorithm protects main and ECC1 algorithm protects spare data

Virtual page division is described with page layout (**page_layout),** number of pages (**page_count)** and
virtual page size (**page_size** or **virtual_page_size).** Virtual page size used by ECC algorithm can be defined
by either **page_size** or **virtual_page_size,** depending on the **page_size** values:

Value| Main + Spare size
:----|:-----------
 0   | 512 + 16
 1   | 1024 + 32
 2   | 2048 + 64
 3   | 4096 + 128
 4   | 8192 + 256
 8   | 512 + 28
 9   | 1024 + 56
 10  | 2048 + 112
 11  | 4096 + 224
 12  | 8192 + 448
 15  | Not used, use virtual_page_size

Structure member **virtual_page_size** is an array of two 16-bit values. First field of array (i.e. **virtual_page_size[0])**
contains main area size while second (i.e. **virtual_page_size[1])** contains spare area size. Number of virtual pages N
is defined with **page_count** and must be calculated as N = 2 ^ page_count.

Page layout defines main and spare ordering and two different page layouts are possible. First ordering assumes that
spare area follows after every main area, while in second case all main areas build one contiguous region followed by
contiguous region of spare areas. This is defined by member **page_layout:**

Layout| Description 
:-----|:-----------
 0    | Single spare follows after single main: Main0,Spare0 ... MainN-1,SpareN-1
 1    | Contiguous spare follows after contiguous main: Main0 ... MainN-1,Spare0 ... SpareN-1

ECC codeword size defines the size of data that is protected by ECC algorithm and is different for main and spare
area. All structure members that define the codeword are therefore arrays of two 16-bit values. Codeword offset defines
where ECC protected data starts in main (**codeword_offset[0])** or spare (**codeword_offset[1])** area, codeword
size (**codeword_size)** defines the number of data that is protected i.e. data over which ECC is calculated and
codeword gap (**codeword_gap)** defines the space between two consecutive codeword regions.

Generated ECC data is stored into spare area and is described similar as codeword, with offset from start of spare area
(**ecc_offset),** size of generated data (**ecc_size)** and gap (**ecc_gap)** between two consecutive ECC data regions.

Number of bits that ECC algorithm can correct per codeword is defined with **correctable_bits.**

**Parameter for:**
  - ARM_NAND_InquireECC
****************************************************************************************************************
