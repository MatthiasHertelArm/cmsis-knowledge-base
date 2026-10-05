---
id: "dv-cmsis-driver-validation-build-cmsis-driver-validation-as-open-cm"
type: "concept"
domain: "drivers"
title: "CMSIS-Driver Validation: Build CMSIS-Driver Validation as Open-CMSIS-Pack"
summary: "A generator script gen_pack.sh is provided for building the CMSIS-Driver Validation as Open-CMSIS-Pack using the gen-pack library. Simply follow the steps below:"
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:README.md"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/README.html"
license: "Apache-2.0"
mode: "V"
---

A generator script [`gen_pack.sh`](https://arm-software.github.io/CMSIS-Driver_Validation/latest/./gen_pack.sh) is provided for building the CMSIS-Driver Validation as [Open-CMSIS-Pack](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html) using the [gen-pack library](https://github.com/Open-CMSIS-Pack/gen-pack). Simply follow the steps below:
  
 - Verify that following tools are installed on the PC:
   - git bash (e.g. for Windows: https://gitforwindows.org/)
   - ZIP archive creation utility (e.g. [7-Zip](http://www.7-zip.org/download.html))
   - Doxygen version 1.13.2 (https://sourceforge.net/projects/doxygen/files/rel-1.13.2/)
 - Checkout this repository. For example in git bash with:
    ```git clone https://github.com/ARM-Software/CMSIS-Driver_Validation```
 - In the local repository folder execute `./gen_pack.sh` in the bash shell.
   - this creates a pack file in the local `output` folder. For example `./output/ARM.CMSIS-Driver_Validation.3.0.1-dev12+g3725082.pack`.

## License

Arm CMSIS-Driver Validation is licensed under [Apache 2.0 license](https://opensource.org/licenses/Apache-2.0).

## Useful resources

| Link                        | Description                                                 |
|:--------------------------- |:----------------------------------------------------------- |
| [CMSIS](https://github.com/ARM-software/cmsis_5)               | CMSIS GitHub repository  |
| [CMSIS-Driver Specification](https://arm-software.github.io/CMSIS_5/latest/Driver/html/index.html) | Specification of CMSIS-Driver API    |
| [CMSIS-Driver](https://github.com/ARM-software/CMSIS-Driver)   |  Reference CMSIS-Driver implementations for external peripheral devices |
| [Open-CMSIS-Pack](https://www.open-cmsis-pack.org)  |  Overview of the Open-CMSIS-Pack project|
