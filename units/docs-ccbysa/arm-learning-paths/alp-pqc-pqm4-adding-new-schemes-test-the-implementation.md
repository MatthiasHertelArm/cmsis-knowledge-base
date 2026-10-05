---
id: "alp-pqc-pqm4-adding-new-schemes-test-the-implementation"
type: "concept"
domain: "core"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Add a KEM implementation to pqm4: Test the implementation"
summary: "Make sure your virtual environment is active, then run the automated test script to verify correctness."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/adding-new-schemes.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/adding-new-schemes/#test-the-implementation"
license: "CC-BY-SA-4.0"
mode: "V"
---

Make sure your virtual environment is active, then run the automated test script to verify correctness.

#### Physical board

Run the automated test script on a physical board:

```bash
python3 test.py -p nucleo-l476rg --uart /dev/tty.usbmodemXXXX newhope512cpa
```

#### QEMU

Run the automated test script on QEMU:

```bash
python3 test.py -p mps2-an386 newhope512cpa
```

The output is similar to:

```output
newhope512cpa - m4 SUCCESSFUL
```
