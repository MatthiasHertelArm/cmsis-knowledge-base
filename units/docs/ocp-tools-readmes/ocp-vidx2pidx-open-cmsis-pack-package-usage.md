---
id: "ocp-vidx2pidx-open-cmsis-pack-package-usage"
type: "concept"
domain: "pack"
title: "vidx2pidx: Open-CMSIS-Pack Package Index Generator Tool: Usage"
summary: "Now the generated index.pidx can be used with cpackget to validate that all listed packs can be installed:"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/vidx2pidx@2147c19:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vidx2pidx/blob/2147c19/README.md#usage"
license: "Apache-2.0"
mode: "V"
---

- update your `vendor.pidx` file as [documented](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html#packIndexFile)

  ```xml
  <?xml version="1.0" encoding="UTF-8" ?>
  <index schemaVersion="1.0.0" xs:noNamespaceSchemaLocation="PackIndex.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance">
    <vendor>MyVendor</vendor>
    <url>https://www.MyVendor.com/pack/</url>
    <timestamp>2024-08-15T15:00:10</timestamp>
    <pindex>
      <pdsc url="https://www.MyVendor.com/pack/mypack/" vendor="MyVendor" name="MyPack" version="1.1.0"/>
      ...
    </pindex>
  </index>
  ```

- create a vendor index file as documented

  ```xml
  <?xml version="1.0" encoding="UTF-8" ?>
  <index schemaVersion="1.0" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="PackIndex.xsd">
    <vendor>MyVendor</vendor>
    <url>www.MyVendor.com/pack</url>
    <timestamp>2024-08-T15:30:00</timestamp>
    <vindex>
      <pidx url="https://www.MyVendor.com/pack/" vendor="MyVendor" />
      ...
    </vindex>
  </index>
  ```

- invoke `vidx2pidx vendor.vidx`

  ```bash
  $ vidx2pidx <index>.vidx

  Options:

    -h, --help        show usage and help info
    -V, --version     show version and copyright info
    -v, --verbose     show progress details
    -o, --output      specify index file directory and name
    -c, --cachedir    specify directory where downloaded pidx and pdsc files are stored (default ./.idxcache)
    -f, --force       force update – ignore timestamp information
  ```

Now the generated `index.pidx` can be used with cpackget to validate that all listed packs can be installed:

- invoke `cpackget init ./index.pidx -R ./pack_root_test` to use the generated index.pidx in
 pack_root_test/.Web/index.pidx
- invoke `cpackget --public -R /pack_root_test` to list all latest public pack versions
