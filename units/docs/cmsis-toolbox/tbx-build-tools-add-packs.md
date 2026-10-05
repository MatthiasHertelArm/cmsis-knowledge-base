---
id: "tbx-build-tools-add-packs"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Add packs"
summary: "There are different ways to install software packs."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#add-packs"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

There are different ways to install software packs.

#### Install public packs

The commands below install software packs from a public web service. The available packs along with download URL and version information are listed in the **Pack Index File**.

When adding a public pack, `cpackget` updates the public index when its daily update is due. It downloads or refreshes only the PDSC files required for the requested pack and its dependencies; a local copy of every PDSC file listed in the public index is not required. Other PDSC files already cached in `.Web` are not refreshed by this operation. The default output summarizes the index operation and reports progress for PDSC files that were actually updated. It does not check local pack repositories during this automatic update. If downloading a valid new `index.pidx` fails, `cpackget` issues a warning and uses the existing index, when available.

Check if a pack is installed. If not, install the latest version of a public software pack:

```shell
cpackget add Vendor.PackName                   # or
cpackget add Vendor::PackName
```

Update an installed pack to the latest version of a public software pack:

```shell
cpackget add Vendor.PackName@latest           # or
cpackget add Vendor::PackName@latest
```

Install a specific version of a public software pack:

```shell
cpackget add Vendor.PackName.x.y.z            # or
cpackget add Vendor::PackName@x.y.z
cpackget add Vendor::PackName@>=x.y.z         # check if there is any version greater  or equal to x.y.z, install latest
```

Install latest version of a public software pack with the same major version or same major/minor version. Within the rules of semantic versioning only compatible packs are used.

```shell
cpackget add Vendor::PackName@^x.y.z         # check if there is any version greater or equal to x.y.z, but with same major version x
cpackget add Vendor::PackName@~x.y.z         # check if there is any version greater or equal to x.y.z, but with same major/minor version x.y
```

#### Install a list of software packs

Frequently, a list of software packs should be installed that are used by a project. A text file can specify a list of packs, whereby each line specifies a single pack, optionally with version information as shown above:

```shell
cpackget add -f list-of-packs.txt
```

Content of `list-of-packs.txt`:

```txt
ARM::CMSIS
ARM::CMSIS-Driver
ARM::CMSIS-FreeRTOS@10.4.6
ARM::mbedTLS@1.7.0
AWS::backoffAlgorithm@1.0.0-Beta
  :
```

#### Accept End User License Agreement (EULA) from the command line

Some packs come with licenses. By default, `cpackget` will prompt the user's acceptance of this license agreement. For
automated installation of software packs, this user prompting can be suppressed with the command line flag `--agree-embedded-license`:

```shell
cpackget add -f list-of-packs.txt --agree-embedded-license
```

In some cases, the user might want to only extract the license agreement of the software pack. This is supported by the
command line flag `--extract-embedded-license`:

```shell
cpackget add --extract-embedded-license Vendor.PackName
```

The extracted license file will be placed next to the pack. For example, if Vendor.PackName.x.y.z had a license file named `LICENSE.txt`, cpackget would extract it to `.Download/Vendor.PackName.x.y.z.LICENSE.txt`.

#### Work behind a proxy

Sometimes, `cpackget` seems to be unable to download software packs, for example, when used behind a corporate firewall. Typically this is indicated by error messages such as:

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD013 -->

```txt
E: Get "<url>/<pack-name>.pack": dial tcp <ip-address>: connectex: No connection could be made because the target machine actively refused it.
E: failed to download the file
```

<!-- markdownlint-restore -->

In such cases, accessing the Internet via a proxy might be required. This can be done via environment variables that are used by `cpackget`:

```shell
# Windows
set HTTP_PROXY=http://my-proxy         # proxy used for HTTP requests
set HTTPS_PROXY=https://my-https-proxy # proxy used for HTTPS requests

# Unix
export HTTP_PROXY=http://my-proxy         # proxy used for HTTP requests
export HTTPS_PROXY=https://my-https-proxy # proxy used for HTTPS requests
```

Then **all** HTTP/HTTPS requests will be going through the specified proxy.

#### Install a private software pack

A software pack can be distributed via different methods, such as file exchange systems.

Once the software pack is available on the local computer, it can be installed by referring to the `*.pack` file
itself:

```shell
cpackget add <path>/Vendor.PackName.x.y.z.pack
```

For a local `*.pack` file, `cpackget` automatically skips the public-index update. The installation therefore works without a network connection; no offline option is required. Pack dependencies must already be locally available, or the pack can be installed with `--no-dependencies` when resolving them is not required.

A software pack that is available for download via a URL can be downloaded and installed with:

```shell
cpackget add https://vendor.com/example/Vendor.PackName.x.y.z.pack
```

#### Install a repository

During the development of a software pack, it is possible to mark the content of a local directory (that typically reflects the repository of the software pack) as a software pack.  In this case, the `*.pdsc` file is specified as shown below:

```shell
cpackget add <local_path>/Vendor.PackName.pdsc
```

Example:

```shell
cpackget add /work/IoT_Socket/MDK-Packs.IoT_Socket.pdsc
```
