---
id: "armsw-foundation-components-for-mlops-sy-customize-this-repository"
type: "concept"
domain: "edge-ai"
title: "Foundation Components for MLOps Systems: Customize this repository"
summary: "First create a fork into a user account or organization of your own (or commit to a new private repository). On your fork you need to make a couple of modifications:"
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/AVH-MLOps@4a1c76f:README.md"
doc_source: "https://github.com/ARM-software/AVH-MLOps/blob/4a1c76f/README.md#customize-this-repository"
license: "Apache-2.0"
mode: "V"
---

First create a fork into a user account or organization of your own (or commit to a new private repository). On your fork you need to make a couple of modifications:

1. Add own Activation Code (Arm UBL license)
The activation code is passed to the docker build process in a Github Actions secret called ARM_UBL_LICENSE_IDENTIFIER.
To set a secret called ARM_UBL_LICENSE_IDENTIFIER to a repository in Github, go to the repository's main page, click on "Settings", then "Secrets", and "New repository secret". Enter "ARM_UBL_LICENSE_IDENTIFIER" as the name and the activation code for the Arm UBL license as the value. Click on "Add secret". 

2. Customize Base Docker Image
Additional installations for custom tools you can add those to docker_base/Dockerfile. If you are new to Docker find a good starting point in the [Docker manual](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

Check the Actions view to verify the execution of all 4 workflows.
