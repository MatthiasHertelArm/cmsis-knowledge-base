---
id: "devt-svd-validation-and-generation-tool-usage"
type: "concept"
domain: "pack"
title: "SVD Validation and Generation Tool: Usage"
summary: "--generate=sfr is supported only on Windows and requires SfrCC2.exe from Keil MDK/uVision in the same directory as svdconv.exe. On Linux and macOS, SVDConv reports error M133 and returns exit code 2. The intermediate .sfd file may still be generated."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/svdconv/SVDConv/README.md#usage"
license: "Apache-2.0"
mode: "V"
---

```bash
  svdconv.exe [OPTION...] positional parameters

  -o, --outdir arg            Output directory
      --generate arg          Generate header, partition or SFD/SFR file
                              (SFR: Windows only)
      --fields arg            Specify field generation:
                              enum/macro/struct/struct-ansic
      --suppress-path         Suppress inFile path on check output
      --create-folder         Always create required folders
      --show-missingEnums     Show SVD elements where enumerated values
                              could be added
      --strict                Strict error checking (RECOMMENDED!)
  -b, --log arg               Log file
  -x, --diag-suppress arg     Suppress Messages
      --suppress-warnings     Suppress all WARNINGs
  -w arg                      Warning level (default: all)
      --allow-suppress-error  Allow to suppress error messages
  -v, --verbose               Verbose mode. Prints extra process
                              information
      --under-test            Use when running in cloud environment
      --nocleanup             Do not delete intermediate files
      --quiet                 No output on console
      --debug arg             Add information to generated files:
                              struct/header/sfd/break
      --version               Show program version
  -h, --help                  Print usage
```

`--generate=sfr` is supported only on Windows and requires `SfrCC2.exe` from Keil MDK/uVision
in the same directory as `svdconv.exe`. On Linux and macOS, SVDConv reports error M133 and
returns exit code 2. The intermediate `.sfd` file may still be generated.
Use `--generate=sfd` to generate SFD output on any supported platform.
SVDConv supports Cortex-M devices with register and field ranges within 32 bits. Wider intermediate arithmetic
prevents overflow; it does not add support for 64-bit input or output. SFD/SFR rejects wider ranges with M226 before
SFD file creation. SFR compilation is skipped when SFD generation fails.

Dimension expansion has a cumulative limit of 1,000,000 generated indices and model copies per input file.
Nested arrays, inherited content, and repeated expansion share this limit. Exceeding it reports M249 and stops
processing that input before any output generator runs. This bounds expansion work, not the XML file size or total
process memory. Invalid dimension index ranges and overflowing expansion addresses report M250.
