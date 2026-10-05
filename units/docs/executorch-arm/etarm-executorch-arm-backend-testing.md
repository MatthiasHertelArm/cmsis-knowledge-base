---
id: "etarm-executorch-arm-backend-testing"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch Arm® Backend: Testing"
summary: "There are two approaches for running the tests for the Arm backend. This section will explain these two approaches:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:backends/arm/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/backends/arm/README.md#testing"
license: "BSD-3-Clause"
mode: "V"
---

There are two approaches for running the tests for the Arm backend. This section will explain these two approaches:

### Using test_arm_backend.sh

The backend provides a script `backends/arm/test/test_arm_backend.sh`, which is used in the `trunk` CI workflow.
This approach is useful for checking your change against this workflow on your own machine.
These scripts also install the necessary dependencies to run the tests.
Below is an overview of some of the testing options this script provides:

| Command                                              | Description                                                  |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| `test_arm_backend.sh test_pytest_ops_no_target`    | Runs operator unit tests for non-target specific use-cases.  |
| `test_arm_backend.sh test_pytest_models_no_target` | Runs model unit tests for non-target specific use-cases.     |
| `test_arm_backend.sh test_pytest_ops_tosa`         | Runs operator unit tests for TOSA specific use-cases.        |
| `test_arm_backend.sh test_pytest_models_tosa`      | Runs model unit tests for TOSA specific use-cases.           |
| `test_arm_backend.sh test_run_tosa`                | Runs end-to-end unit tests for TOSA specific use-cases.      |
| `test_arm_backend.sh test_pytest_ops_ethos_u55`    | Runs operator unit tests for Ethos-U55 specific use-cases.   |
| `test_arm_backend.sh test_pytest_models_ethos_u55` | Runs model unit tests for Ethos-U55 specific use-cases.      |
| `test_arm_backend.sh test_run_ethos_u55`           | Runs end-to-end unit tests for Ethos-U55 specific use-cases. |
| `test_arm_backend.sh test_pytest_ops_ethos_u85`    | Runs operator unit tests for Ethos-U85 specific use-cases.   |
| `test_arm_backend.sh test_pytest_models_ethos_u85` | Runs model unit tests for Ethos-U85 specific use-cases.      |
| `test_arm_backend.sh test_run_ethos_u85`           | Runs end-to-end unit tests for Ethos-U85 specific use-cases. |
| `test_arm_backend.sh test_pytest_ops_vkml`         | Runs operator unit tests for VKML/VGF specific use-cases.    |
| `test_arm_backend.sh test_pytest_models_vkml`      | Runs model unit tests for VKML/VGF specific use-cases.       |
| `test_arm_backend.sh test_run_vkml`                | Runs end-to-end unit tests for VKML/VGF specific use-cases.  |
| `test_arm_backend.sh test_model_smollm2_135M_ethos_u85`      | Runs smollm2_135M for Ethos-U85 specific use-cases.                          |
| `test_arm_backend.sh test_ootb_tests_ethos_u`      | Runs out-of-the-box tests for Ethos-U.                       |
| `test_arm_backend.sh test_ootb_tests_tosa`         | Runs out-of-the-box tests for TOSA.                          |
| `test_arm_backend.sh test_ootb_tests_vgf`          | Runs out-of-the-box tests for VKML/VGF.                      |
| `test_arm_backend.sh test_deit_e2e_ethos_u`        | Runs DEiT end-to-end tests on Ethos-U.                       |
| `test_arm_backend.sh test_smaller_stories_llama_tosa` | Runs Llama model tests for TOSA.                          |
| `test_arm_backend.sh test_smaller_stories_llama_vkml` | Runs Llama model tests for VKML/VGF.                      |
| `test_arm_backend.sh test_runtime_ethos_u`       | Runs runtime tests for Ethos-U specific targets    |

For more information, please refer to the `backends/arm/test/test_arm_backend.sh` script.

### Using pytest

The Arm backend uses `pytest` to run the unit test suite in `backends/arm/test`.
This option offers flexibility, allowing a specific test or a particular subset of the testsuite to be run.
Below provides some examples of how to use it:

- To run all the unit tests run the following command:

  ```
  pytest -v -n auto backends/arm/test/
  ```

- To run a specific test in a file:

  ```
  pytest -v backends/arm/test/ops/test_add.py -k test_add_tensor_tosa_INT_3
  ```

#### Testing Dependencies

Some tests, with `u55`, `u85` and `vgf` in the name require external dependencies to run if you use `pytest`:

- When a test contains `u55` or `u85`, you must run the following to setup the executor_runner:
  ```
  ./backends/arm/scripts/build_executorch.sh
  ./backends/arm/test/setup_testing.sh
  ```
- When a test contains `vgf`, you must run the following to install the ML SDK:
  ```
  ./backends/arm/scripts/build_executorch.sh
  ./backends/arm/test/setup_testing_vkml.sh
  ```

In addition, some model tests in the Arm backend require third-party libraries or packages.
To run these tests, install the required dependencies directly:

```
bash backends/arm/scripts/install_models_for_test.sh
```

Installing model test dependencies is a standalone process. The script installs
only the dependencies needed for model tests, skipping all other setup
procedures.
