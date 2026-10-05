---
id: "alp-pqc-pqm4-running-tests-and-benchm-use-scripts-to-automate-testin"
type: "concept"
domain: "edge-ai"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Run pqm4 tests and benchmarks: Use scripts to automate testing and benchmarking"
summary: "pqm4 includes Python scripts that automate flashing, running, and checking results across multiple implementations."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/running-tests-and-benchmarks.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/running-tests-and-benchmarks/#use-scripts-to-automate-testing-and-benchmarking"
license: "CC-BY-SA-4.0"
mode: "V"
---

pqm4 includes Python scripts that automate flashing, running, and checking results across multiple implementations.

Before running any Python scripts in this section, make sure your virtual environment is active:

```bash
source venv/bin/activate
```

### Run functional tests

The `test.py` script runs the test binary on your chosen platform and checks correctness automatically.

#### NUCLEO-L476RG

Run functional tests on NUCLEO-L476RG:

```bash
python3 test.py -p nucleo-l476rg --uart /dev/tty.usbmodemXXXX ml-kem-768
```

#### QEMU

Run functional tests on QEMU:

```bash
python3 test.py -p mps2-an386 ml-kem-768
```

The output after running functional tests is similar to:

```output
ml-kem-768 - m4fspeed SUCCESSFUL
ml-kem-768 - m4fstack SUCCESSFUL
ml-kem-768 - clean SUCCESSFUL
test: 100%|#############################################| 3/3 [00:12<00:00,  4.29s/it, ml-kem-768 - clean]
```

### Run test vectors

The `testvectors.py` script generates test vectors on your chosen platform and compares them with host-side results.

#### NUCLEO-L476RG

Run test vector validation on NUCLEO-L476RG:

```bash
python3 testvectors.py -p nucleo-l476rg --uart /dev/tty.usbmodemXXXX ml-kem-768
```

#### QEMU

Run test vector validation on QEMU:

```bash
python3 testvectors.py -p mps2-an386 ml-kem-768
```

The output after running test vector validation is similar to:

```output
ml-kem-768 - m4fspeed SUCCESSFUL
ml-kem-768 - m4fstack SUCCESSFUL
ml-kem-768 - clean SUCCESSFUL
test: 100%|#############################################| 3/3 [00:12<00:00,  4.29s/it, ml-kem-768 - clean]
```

### Run benchmarks

The `benchmarks.py` script runs speed and stack benchmarks and stores the results in a `benchmarks/` directory.

#### NUCLEO-L476RG

Run benchmarks on NUCLEO-L476RG:

```bash
python3 benchmarks.py -p nucleo-l476rg --uart /dev/tty.usbmodemXXXX ml-kem-768
```

#### QEMU

Run benchmarks on QEMU:

```bash
python3 benchmarks.py -p mps2-an386 ml-kem-768
```

The output of running benchmarks is similar to:

```output
speed:  33%|################              | 1/3 [00:20<00:40, 20.00s/it, ml-kem-768 - m4fspeed]
speed:  66%|###########################   | 2/3 [00:40<00:20, 20.00s/it, ml-kem-768 - m4fstack]
speed: 100%|##############################| 3/3 [01:00<00:00, 20.00s/it, ml-kem-768 - clean]
```

Results are saved to `benchmarks.csv`. The screenshot shows an example of the benchmark output:

(figure: Screenshot of benchmarks.csv showing cycle counts and stack usage for ML-KEM-768 implementations including the m4fspeed, m4fstack, and clean variants#center)
