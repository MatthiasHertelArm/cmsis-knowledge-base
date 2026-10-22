---
id: "devt-svd-validation-and-generation-tool-data-check-errors"
type: "concept"
domain: "pack"
title: "SVD Validation and Generation Tool: Error and Warning Messages / Data Check Errors"
summary: "SVD Validation and Generation Tool: Error and Warning Messages / Data Check Errors"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/svdconv/SVDConv/README.md#data-check-errors"
license: "Apache-2.0"
mode: "V"
---

_Part of: Error and Warning Messages_

| Message Number |  Type |  Message Text |  Action|
|----------------|---------|---------------|--------|
|  M301 |  ERROR |  Interrupt number 'NUM' : 'NAME' already defined: 'NAME2' 'LINE' |  |
|  M302 |  ERROR |  Size of Register 'NAME':'NUM' must be 8, 16 or 32 Bits |  |
|  M303 |  WARNING |  Register name 'NAME' is prefixed with Peripheral name 'NAME2' |  RegName = USART_CR ==>` USART->USART_CR|
|  M304 |  WARNING |  Interrupt number overwrite: 'NUM' : 'NAME' 'LINE' |  |
|  M305 |  ERROR |  Name not C compliant: 'NAME' : 'HEX', replaced by '_' |  |
|  M306 |  ERROR |  Schema Version not set for `<device>`. |  |
|  M307 |  ERROR |  Name is equal to Value: 'NAME' |  |
|  M308 |  ERROR |  Number of `<dimIndex>` Elements 'NUM' is different to number of `<dim>` instances 'NUM2' |  |
|  M309 |  ERROR |  Field 'NAME': Offset error: 'NUM' |  |
|  M310 |  ERROR |  Field 'NAME': BitWidth error: 'NUM' |  |
|  M311 |  ERROR |  Field 'NAME': Calculation: MSB or LSB == -1 |  |
|  M312 |  ERROR |  Address Block missing for Peripheral 'NAME' |  |
|  M313 |  ERROR |  Field 'NAME': LSB > MSB: BitWith calculates to 'NUM' |  |
|  M314 |  ERROR |  Address Block: `<offset>` or `<size>` not set. |  |
|  M315 |  ERROR |  Address Block: `<size>` is zero. |  |
|  M316 |  ERROR |  'LEVEL' `<name>` not set. |  |
|  M317 |  WARNING |  'LEVEL' `<description>` not set. |  |
|  M318 |  WARNING |  'LEVEL' 'NAME' `<'TAG'>` is equal to `<name>` |  |
|  M319 |  WARNING |  'LEVEL' `<'TAG'>` 'NAME' ends with newline, is this intended? |  |
|  M320 |  WARNING |  'LEVEL' `<description>` 'NAME' is not very descriptive |  |
|  M321 |  WARNING |  'LEVEL' `<'ITEM'>` 'NAME' starts with '_', is this intended? |  |
|  M322 |  ERROR |  'LEVEL' 'ITEM' 'NAME' is meaningless text. Deleted. |  |
|  M323 |  WARNING |  'LEVEL' `<'ITEM'>` 'NAME' contains text 'TEXT' |  |
|  M324 |  ERROR |  Field 'NAME' 'BITRANGE' does not fit into Register 'NAME2':'NUM' 'LINE' |  |
|  M325 |  ERROR |  CPU Revision is not set" |  |
|  M326 |  ERROR |  Endianess is not set, using default (little) |  |
|  M327 |  ERROR |  NVIC Prio Bits not set or wrong value, must be 2..8. Using default (4) |  |
|  M328 |  WARNING |  'LEVEL' 'NAME' has no Registers, ignoring 'LEVEL'. |  |
|  M329 |  ERROR |  CPU Type is not set, using default (Cortex-M3) |  |
|  M330 |  ERROR |  Interrupt 'NAME' Number not set. |  |
|  M331 |  ERROR |  Interrupt 'NAME' Number 'NUM' greater 239. |  |
|  M332 |  WARNING |  'LEVEL' 'NAME' has only one Register. |  |
|  M333 |  ERROR |  Duplicate `<enumeratedValue>` 'NUM': 'NAME' ('USAGE'), already used by 'NAME2' ('USAGE2') 'LINE' |  |
|  M334 |  WARNING |  'LEVEL' `<'ITEM'>` 'NAME' is very long, use `<description>` and a shorter `<name>` |  |
|  M335 |  ERROR |  Value 'NAME':'NUM' does not fit into field 'NAME2' 'BITRANGE'. |  |
|  M336 |  ERROR |  'LEVEL' 'NAME' already defined 'LINE' |  |
|  M337 |  ERROR |  'LEVEL' 'NAME' already defined 'LINE' |  |
|  M338 |  ERROR |  Field 'NAME' 'BITRANGE' ('ACCESS') overlaps 'NAME2' 'BITRANGE2' ('ACCESS2') 'LINE' |  |
|  M339 |  ERROR |  Register 'NAME' ('ACCESS') (@'ADDRSIZE') has same address or overlaps 'NAME2' ('ACCESS2') (@'ADDRSIZE2') 'LINE' |  |
|  M340 |  ERROR |  No Devices found. |  |
|  M341 |  ERROR |  More than one devices found, only one is allowed per SVD File. |  |
|  M342 |  ERROR |  Dim-extended 'LEVEL' 'NAME' must not have `<headerStructName>` |  |
|  M343 |  ERROR |  'LEVEL' 'NAME' (@'ADDR') has same address as 'NAME2' 'LINE' |  |
|  M344 |  ERROR |  Register 'NAME' (@'ADDRSIZE') is outside or does not fit any `<addressBlock>` specified for Peripheral 'NAME2' 'TEXT' |  |
|  M345 |  ERROR |  Field 'NAME' 'BITRANGE' does not fit into Register 'NAME2':'NUM' |  |
|  M346 |  WARNING |  Register 'NAME' (@'ADDR') offset is equal or is greater than it's Peripheral base address 'NAME2' (@'ADDR2'), is this intended? |  |
|  M347 |  WARNING |  Field 'NAME' (width < 6Bit) without any `<enumeratedValue>` found. |  |
|  M348 |  ERROR |  Alternate 'LEVEL' 'NAME' does not exist at 'LEVEL' address (@'ADDR') |  |
|  M349 |  ERROR |  Alternate 'LEVEL' 'NAME' is equal to 'LEVEL' name 'NAME2' |  |
|  M350 |  WARNING |  Peripheral 'NAME' (@'ADDR') is not 4Byte-aligned. |  |
|  M351 |  WARNING |  Peripheral 'TYPE' 'NAME' is equal to Peripheral name. |  |
|  M352 |  WARNING |  AddressBlock of Peripheral 'NAME' (@'ADDR') 'TEXT' overlaps 'NAME2' (@'ADDR2') 'TEXT2' 'LINE' |  |
|  M353 |  WARNING |  Peripheral group name 'NAME' should not end with '_' |  |
|  M354 |  ERROR |  Interrupt ''NUM':'NAME' specifies a Core Interrupt. Core Interrupts must not be defined, they are set through `<cpu><name>`. |  |
|  M355 |  ERROR |  No Interrupts found on pos. 0..15. External (Vendor-)Interrupts possibly defined on position 16+. External Interrupts must start on position 0 |  |
|  M356 |  WARNING |  No Interrupt definitions found. |  |
|  M357 |  ERROR |  Core Interrupts found. Interrupt Numbers are wrong. Internal Interrupts must not be described, External Interrupts must start at 0. |  |
|  M358 |  ERROR |  AddressBlock of Peripheral 'NAME' 'TEXT' overlaps AddressBlock 'TEXT2' in same peripheral 'LINE' |  |
|  M359 |  ERROR |  Address Block: `<usage>` not set. |  |
|  M360 |  ERROR |  Address Block: found `<'TAG'>` ('HEXNUM') > 'HEXNUM2'. |  |
|  M361 |  ERROR |  'LEVEL' 'ITEM' 'NAME': 'RESERVED' items must not be defined. |  |
|  M362 |  WARNING |  'LEVEL' 'ITEM' 'NAME': 'RESERVED' items must not be defined. |  |
|  M363 |  ERROR |  CPU: `<sauNumRegions>` not set. |  |
|  M364 |  ERROR |  CPU: `<sauNumRegions>` value 'NUM' greater than SAU max num ('NUM2') |  |
|  M365 |  WARNING |  Register 'NAME' ('ACCESS') (@'ADDRSIZE') has same address or overlaps 'NAME2' ('ACCESS2') (@'ADDRSIZE2') 'LINE' |  |
|  M366 |  ERROR |  Register 'NAME' size ('NUM'Bit) is greater than `<dimIncrement>` * `<addressBitsUnits>` ('NUM2'Bit). |  |
|  M367 |  WARNING |  Access Type: Field 'NAME' ('ACCESS') does not match Register 'NAME2' ('ACCESS2') |  |
|  M368 |  WARNING |  'LEVEL' 'NAME' (@'ADDR') has same address as 'NAME2' 'LINE' |  |
|  M369 |  ERROR |  Enumerated Value 'NAME': `<value>` not set. |  |
|  M370 |  ERROR |  'LEVEL' 'NAME': `<offset>` not set. |  |
|  M371 |  ERROR |  'LEVEL' 'NAME' `<headerStructName>` is equal to hierarchical name |  |
|  M372 |  ERROR |  'LEVEL' `<'TAG'>` 'NAME' already defined 'LINE' |  |
|  M373 |  ERROR |  'LEVEL' `<'TAG'>` 'NAME' already defined 'LINE' |  |
|  M374 |  WARNING |  `<enumeratedValues>` can be one `<enumeratedValues>` container for all `<enumeratedValue>`s, where `<usage>` can be read, write, or read-write or two `<enumeratedValues>` containers, where one is set to `<usage>` read and the other is set to `<usage>` write |  |
|  M375 |  ERROR |  'LEVEL' 'NAME' (`<enumeratedValues>` 'NAME2'): Too many `<enumeratedValues>` container specified. |  |
|  M376 |  ERROR |  'LEVEL' 'NAME' (`<enumeratedValues>` 'NAME2'): 'USAGE' container already defined in 'LINE'. |  |
|  M377 |  ERROR |  'LEVEL' 'NAME' (`<enumeratedValues>` 'NAME2'): 'USAGE' container conflicts with 'NAME3' 'LINE'. |  |
|  M378 |  ERROR |  Register Array: Register 'NAME' size ('NUM'Bit) does not match `<dimIncrement>` ('NUM2'Bit). |  |
|  M379 |  ERROR |  XBin Number 'NAME' too large, skipping evaluation. |  |
|  M380 |  ERROR |  AddressBlock of Peripheral 'NAME' (@'ADDR') 'TEXT' does not fit into 32Bit Address Space. |  |
|  M381 |  ERROR |  Interrupt 'NAME' Number 'NUM' greater or equal deviceNumInterrupts ('NUM2'). |  |
|  M382 |  ERROR |  'LEVEL' 'NAME': 'NAME2' 'HEXNUM' does not fit into 'LEVEL' width: 'NUM' Bit. |  |
