---
id: "alp-deploy-mobilesam-on-ethos-u-prepare-the-environment-choose-how-to-run-the-example"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Prepare the ExecuTorch and Arm environment: Choose how to run the example"
summary: "To run preparation, export, build, FVP execution, and validation together, use the example's script without arguments:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment/#choose-how-to-run-the-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

To run preparation, export, build, FVP execution, and validation together, use the example's script without arguments:

```bash
./examples/arm/mobilesam_prompt_segmentation_example_ethos_u/run.sh
```

The expected output at the end of a successful run is:

```output
MobileSAM example: PASS
```

The comparison image, `fvp_comparison.png`, is saved under `arm_test/mobilesam/result/`. After the script completes, continue to [Validate the MobileSAM segmentation result](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment/../validate-the-results/) to inspect the artifacts.

To work through each stage manually, skip this script and continue to the next page. The following pages explain the same preparation, export, build, and validation steps. Continue only after each command succeeds; files from an earlier run can remain after a failed command.
