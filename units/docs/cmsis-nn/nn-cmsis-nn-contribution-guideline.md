---
id: "nn-cmsis-nn-contribution-guideline"
type: "concept"
domain: "optimization"
title: "CMSIS NN: Contribution Guideline"
summary: "First, a thank you for the contribution. Here are some guidelines and good to know information to get started."
status: "draft"
collection: "cmsis-nn"
source: "ARM-software/CMSIS-NN@18bb0fd:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-NN/blob/18bb0fd/README.md#contribution-guideline"
license: "Apache-2.0"
mode: "V"
---

First, a thank you for the contribution. Here are some guidelines and good to know information to get started.

### Coding Guideline
By default, follow the style used in the file. You'll soon start noticing a pattern like
* Variable and function names are lower case with an underscore separator.
* Hungarian notation is not used. Well, almost.
* If the variable names don't convey the action, then add comments.

### New Files
One function per file is followed in most places. In those cases, the file name must match the function name. Connect
the function to an appropriate Doxygen group as well.

### Doxygen
Function prototypes must have a detailed comment header in Doxygen format. You can execute the doxygen document generation
script in the Documentation/Doxygen folder to check that no errors are introduced.

### Unit Tests
For any new features and bug fixes, new unit tests are needed. Improvements have to be verifed by unit tests. If you do
not have the means to execute the tests, you can still make the PR and comment that you need help in completing/executing
the unit tests.

The repository also provides a `vcpkg-configuration.json` used to provision the
tool environment required by the unit-test and CI flows. This is consumed by
the `vcpkg` package manager, locally or in the cloud, to avoid manual setup of
CMSIS-Toolbox, compilers, and FVP dependencies. The same setup is used by the
GitHub Actions CI workflows that run the unit-test regressions on pushes and
pull requests.

### Version & Date
Each File has a version number and a date field that must be updated when making any change to that file. The versioning
follows Semantic Versioning 2.0.0 format. For details check: https://semver.org/
