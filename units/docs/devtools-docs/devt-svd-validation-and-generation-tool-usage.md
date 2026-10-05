---
id: "devt-svd-validation-and-generation-tool-usage"
type: "concept"
domain: "pack"
title: "SVD Validation and Generation Tool: Usage"
summary: "--generate=sfr is supported only on Windows and requires SfrCC2.exe from Keil MDK/uVision in the same directory as svdconv.exe. On Linux and macOS, SVDConv reports error M133 and returns exit code 2. The intermediate .sfd file may still be generated."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/svdconv/SVDConv/README.md#usage"
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
