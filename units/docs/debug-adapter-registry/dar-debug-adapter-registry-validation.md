---
id: "dar-debug-adapter-registry-validation"
type: "concept"
domain: "debug"
title: "debug-adapter-registry: Validation"
summary: "The CI worklow validates the debugger adapter registry and templates by running linter and schema checker. Such validation steps can be reproduced in the local environment according to the following instructions."
status: "draft"
collection: "debug-adapter-registry"
source: "Open-CMSIS-Pack/debug-adapter-registry@d5ffe88:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/debug-adapter-registry/blob/d5ffe88/README.md#validation"
license: "Apache-2.0"
mode: "V"
---

The [CI worklow](https://github.com/Open-CMSIS-Pack/debug-adapter-registry/blob/d5ffe88/.github/workflows/ci.yml) validates the debugger adapter registry and templates by running linter and
schema checker. Such validation steps can be reproduced in the local environment according to the following
instructions.

> **prerequisite:**
> [`npm`](https://nodejs.org/en/download) to be installed in the system.

### Linter

tl:dr

```sh
npm install
npm run lint
```

Install [`eslint`](https://www.npmjs.com/package/eslint) and json/yaml plugins:

```sh
npm install --save-dev eslint eslint-plugin-jsonc eslint-plugin-yml eslint-formatter-compact
```

Lint debug adapters registry:

```sh
npx eslint --no-config-lookup --format compact --parser yaml-eslint-parser --plugin yml --ext .yml \
  --rule 'yml/quotes: ["error", { prefer: "double" }]' \
  --rule 'yml/indent: ["error", 2]' \
  --rule 'no-trailing-spaces: "error"' \
  registry
```

Lint templates:

```sh
npx eslint --no-config-lookup --format compact --parser jsonc-eslint-parser --plugin jsonc --ext .json \
  --rule 'jsonc/quotes: ["error", "double"]' \
  --rule 'jsonc/indent: ["error", 4]' \
  --rule 'no-trailing-spaces: "error"' \
  templates
```

### Schema check

tl:dr

```sh
npm install
npm run schema
```

Install [`ajv`](https://www.npmjs.com/package/ajv):

```sh
npm install --save-dev ajv ajv-cli
```

Check debug adapters registry schema:

```sh
npx ajv -s schemas/debug-adapters.schema.json -d registry/debug-adapters.yml --strict=false
```

Check templates schema:

```sh
npx ajv -s schemas/templates.schema.json -d "templates/*.json" --strict=false
```
