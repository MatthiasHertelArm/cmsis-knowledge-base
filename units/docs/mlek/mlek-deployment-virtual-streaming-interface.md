---
id: "mlek-deployment-virtual-streaming-interface"
type: "concept"
domain: "edge-ai"
title: "Deployment: Fixed Virtual Platform / Virtual Streaming Interface"
summary: "Virtual Streaming Interface is available on certain FVPs and allows streaming data from the host machine into the application running on the FVP."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/deployment.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/deployment.md#virtual-streaming-interface"
license: "Apache-2.0"
mode: "V"
---

_Part of: Fixed Virtual Platform_

[Virtual Streaming Interface](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vsi.html) is available
on certain FVPs and allows streaming data from the host machine into the application running on the FVP.

#### VSI Requirements

For details and up-to-date requirements, see
[Python environment setup](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vsi__pyenv.html)
which mentions:

> The following packages are required on Linux systems (Ubuntu 20.04 and later):
>   - libatomic1
>   - python3.9
>   - python3-pip

In addition to the above, the VSI Python scripts depend on `opencv-python` package. We recommend using
a virtual environment and installing this with pip.

```shell
$ pip install opencv-python "numpy<2.0.0"
```

**NOTE**: The requirement for Python version is driven by the FVP executable. Versions <= 11.26 require
Python3.9 but this may change for future releases.


#### Deployment with Virtual Streaming Interface

If the applications have been configured with `-DFVP_VSI_ENABLED=ON`, FVP deployment needs an additional
parameter to point to the Python scripts it should use.

To run the VSI enabled application, append the command line with the `v_path` argument. For example:

- Arm® MPS3 based FVPs (Arm® Corstone™-300 and Arm® Corstone™-310):

```shell
  $ FVP_install_location/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 \
    <other-arguments> \
    -C mps3_board.v_path=dependencies/avh/interface/video/python
  ```

- Arm® MPS4 based FVPs (Arm® Corstone™-315 and Arm® Corstone™-320):

```shell
  $ <path_to_installed_FVP> \
    FVP_install_location/models/Linux64_GCC-9.3/FVP_Corstone_SSE-315 \
    <other-arguments>
    -C mps4_board.v_path=dependencies/avh/interface/video/python
```
