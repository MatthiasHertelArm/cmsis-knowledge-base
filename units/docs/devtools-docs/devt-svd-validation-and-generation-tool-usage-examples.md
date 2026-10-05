---
id: "devt-svd-validation-and-generation-tool-usage-examples"
type: "concept"
domain: "pack"
title: "SVD Validation and Generation Tool: Usage Examples"
summary: "2. Perform a consistency check by passing only the SVD file name. Errors and warnings are printed on screen."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/svdconv/SVDConv/README.md#usage-examples"
license: "Apache-2.0"
mode: "V"
---

1. Retrieve help information on screen.

   ```bash
   svdconv
   ```

2. Perform a consistency check by passing only the SVD file name. Errors and warnings are printed on screen.

   ```bash
   svdconv ARM_Example.svd 
   ```

   The result is printed on screen:

   ```bash
   MVCM3110.svd(1688) : info
   `<description>` missing for value '2 : MODE2'
   MVCM3110.svd(1692) : info
   `<description>` missing for value '3 : MODE3'
   MVCM3110.svd(1696) : info
   `<description>` missing for value '4 : MODE4'
   Area of improvements:
   * Description contains 267 `<fields>` defined without associated `<enumeratedValues>
   Found 0 Errors and 1 Warnings
   Return Code: 1 (WARNINGS)
   ```

3. Generate the header file. Performs a consistency check. Errors and warnings are printed on screen.

   ```bash
   svdconv ARM_Example.svd --generate=header
   ```

   Code snippet from the generated header file showing the structure for **TIMER0**.

   ```C
   /* ================                     TIMER0                     ================ */
   typedef struct {                                    
     __IO uint32_t  CR;                                
     __IO uint16_t  SR;                                
     __I  uint16_t  RESERVED0[5];
     __IO uint16_t  INT;                               
     __I  uint16_t  RESERVED1[7];
     __IO uint32_t  COUNT;                             
     __IO uint32_t  MATCH;                             
     union {
       __O  uint32_t  PRESCALE_WR;                     
       __I  uint32_t  PRESCALE_RD;                     
     };
     __I  uint32_t  RESERVED2[9];
     __IO uint32_t  RELOAD[4];                         
   } TIMER0_Type;
   ```

4. Generate the header file containing bit fields. Performs a consistency check. Errors and warnings are printed on screen.

   ```bash
   svdconv ARM_Example.svd --generate=header --fields=struct
   ```

   Code snippet from the generated header file showing the structure for **TIMER0**.
   Compare to the code snippet above.

   ```C
   /* ================                     TIMER0                     ================ */
   typedef struct {                                    
     union {
       __IO uint32_t  CR;                              
       struct {
         __IO uint32_t  EN         :  1;               
         __O  uint32_t  RST        :  1;               
         __IO uint32_t  CNT        :  2;               
         __IO uint32_t  MODE       :  3;               
         __IO uint32_t  PSC        :  1;               
         __IO uint32_t  CNTSRC     :  4;               
         __IO uint32_t  CAPSRC     :  4;               
         __IO uint32_t  CAPEDGE    :  2;               
              uint32_t             :  2;
         __IO uint32_t  TRGEXT     :  2;               
              uint32_t             :  2;
         __IO uint32_t  RELOAD     :  2;               
         __IO uint32_t  IDR        :  2;               
              uint32_t             :  3;
         __IO uint32_t  S          :  1;               
       } CR_b;                                         
     };
     
     union {
       __IO uint16_t  SR;                              
       struct {
         __I  uint16_t  RUN        :  1;               
              uint16_t             :  7;
         __IO uint16_t  MATCH      :  1;               
         __IO uint16_t  UN         :  1;               
         __IO uint16_t  OV         :  1;               
              uint16_t             :  1;
         __I  uint16_t  RST        :  1;               
              uint16_t             :  1;
         __I  uint16_t  RELOAD     :  2;               
       } SR_b;                                         
     };
     __I  uint16_t  RESERVED0[5];
     
     union {
       __IO uint16_t  INT;                             
       struct {
         __IO uint16_t  EN         :  1;               
              uint16_t             :  3;
         __IO uint16_t  MODE       :  3;               
       } INT_b;                                        
     };
     __I  uint16_t  RESERVED1[7];
     __IO uint32_t  COUNT;                             
     __IO uint32_t  MATCH;                             
     union {
       __O  uint32_t  PRESCALE_WR;                     
       __I  uint32_t  PRESCALE_RD;                     
     };
     __I  uint32_t  RESERVED2[9];
     __IO uint32_t  RELOAD[4];                         
   } TIMER0_Type;
   ```

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD013 -->
