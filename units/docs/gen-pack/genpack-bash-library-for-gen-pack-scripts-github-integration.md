---
id: "genpack-bash-library-for-gen-pack-scripts-github-integration"
type: "concept"
domain: "pack"
title: "Bash library for gen-pack scripts: GitHub Integration"
summary: "For running Bash scripts based on gen-pack library within a GitHub Action workflow one could rely on the reusable action available at Open-CMSIS-Pack/gen-pack-action."
status: "draft"
collection: "gen-pack"
source: "Open-CMSIS-Pack/gen-pack@2fc9447:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/gen-pack/blob/2fc9447/README.md#github-integration"
license: "Apache-2.0"
mode: "V"
---

### Open-CMSIS-Pack/gen-pack-action

For running Bash scripts based on gen-pack library within a GitHub Action workflow one could rely on the reusable
action available at [Open-CMSIS-Pack/gen-pack-action](https://github.com/Open-CMSIS-Pack/gen-pack-action).

### Auto-update library reference

Once a new version of the gen-pack library is released, one need to update all scripts `REQUIRED_GEN_PACK_LIB``
variable to make use of the new version. This can be semi-automated via the shared workflow provided in
[update-lib.yml](https://github.com/Open-CMSIS-Pack/gen-pack/blob/update-scripts-workflow/.github/workflows/update-lib.yml).

This shared workflow can be run within the user's repo via a cron schedule:

```yml
name: Update library in gen-pack scripts
on:
  workflow_dispatch:
  schedule:
    - cron: "30 9 * * *"

permissions:
  contents: write
  pull-requests: write

jobs:
  update-workflows:
    uses: Open-CMSIS-Pack/gen-pack/.github/workflows/update-lib.yml@update-scripts-workflow
    secrets:
      TOKEN_ACCESS: ${{ secrets.TOKEN_WORKFLOW_UPDATE }}
```

The workflow requires write permissions the default `GITHUB_TOKEN` does not have for
security reasons. Hence, one needs to register Personal Access Token as a repository secret, which has

- Contents: read and write
- Pull requests: read and write
