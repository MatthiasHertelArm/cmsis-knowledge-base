---
id: "armsw-foundation-components-for-mlops-sy-continuous-integration-ci"
type: "concept"
domain: "edge-ai"
title: "Foundation Components for MLOps Systems: Continuous Integration (CI)"
summary: "Four workflows examplify how to create docker images and equip with licenses suitable for build and test typical MLOps applications."
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/AVH-MLOps@4a1c76f:README.md"
doc_source: "https://github.com/ARM-software/AVH-MLOps/blob/4a1c76f/README.md#continuous-integration-ci"
license: "Apache-2.0"
mode: "V"
---

Four workflows examplify how to create docker images and equip with licenses suitable for build and test typical MLOps applications.

| 
 CI Workflow files                       | Description |
|---                                                                      |---  |
| [base_image_build.yml](https://github.com/ARM-software/AVH-MLOps/blob/4a1c76f/.github/workflows/base_image_build.yml)          | Build a docker image that has all ARM tools mentioned before installed and configured. It will be stored on the Github docker registry for fast access to the image. |
| [licensed_image_build.yml](https://github.com/ARM-software/AVH-MLOps/blob/4a1c76f/.github/workflows/licensed_image_build.yml)  | By using the Base docker image, this workflow adds your own license supplied by Arm for the commercial tools. It is rebuilt every night and serves as the base image from which the actual container runtime environments are generated. It will also be stored on the Github docker registry. |
| [licensed_image_test.yml](https://github.com/ARM-software/AVH-MLOps/blob/4a1c76f/.github/workflows/licensed_image_test.yml)    | Test the licensed docker image with the necessary tools and dependencies for an ML project. |
| [licensed_image_build_community.yml](https://github.com/ARM-software/AVH-MLOps/blob/4a1c76f/.github/workflows/licensed_image_build_community.yml)  | By using the Base docker image, this workflow adds your own community license supplied by Arm for the commercial tools. It is rebuilt every night and serves as the base image from which the actual container runtime environments are generated. It will also be stored on the Github docker registry. |
