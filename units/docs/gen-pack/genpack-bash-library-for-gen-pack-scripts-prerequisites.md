---
id: "genpack-bash-library-for-gen-pack-scripts-prerequisites"
type: "concept"
domain: "pack"
title: "Bash library for gen-pack scripts: Prerequisites"
summary: "This library is written for Bash v5 or later and uses a couple of standard \\nix commands:"
status: "draft"
collection: "gen-pack"
source: "Open-CMSIS-Pack/gen-pack@2fc9447:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/gen-pack/blob/2fc9447/README.md#prerequisites"
license: "Apache-2.0"
mode: "V"
---

This library is written for Bash v5 or later and uses a couple of standard
\*nix commands:

- basename
- cp
- curl
- dirname
- dos2unix (optional)
- echo
- find
- git (optional)
- gh (optional)
- grep
- mac2unix (optional)
- mkdir
- mv
- patch (optional)
- realpath
- sed
- sha1sum
- tar
- test
- unix2dos (optional)
- unix2mac (optional)
- xmllint (optional)

In addition the `packchk` utility from [CMSIS-Toolbox](https://github.com/Open-CMSIS-Pack/cmsis-toolbox)
is required for verification.

### Linux

This library shall be well prepared to run on any standard Linux with Bash v5 or later.

```sh
$ sudo apt install \
    curl \
    libxml2-utils
```

### MacOS

This library requires Bash v5 and some additional GNU tools to be installed using [Homebrew](https://brew.sh/):

```sh
$ brew install \
    bash \
    coreutils \
    gnu-tar \
    grep
```

### Windows

The following tools need to be installed on Windows machines.

#### Bash v5

- [git for Windows](https://gitforwindows.org/) offers a Bash v5 compliant shell.
- Alternatively, you may use a [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/).

#### xmllint

xmllint is provided by the [Chocolatey](https://chocolatey.org/install) [xsltproc package](https://chocolatey.org/packages/xsltproc).
Installing choco and xsltproc can be done from an administrative PowerShell prompt:

```ps
> Set-ExecutionPolicy Bypass -Scope Process -Force
> [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
> iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
> choco install xsltproc
```

Alternatively, [xmllint](http://xmlsoft.org/xmllint.html) can be installed manually using the
[libxml library](https://www.zlatkovic.com/pub/libxml/). Download the following ZIP files:

- iconv-1.9.2.win32.zip
- libxml2-2.7.8.win32.zip
- libxmlsec-1.2.18.win32.zip
- zlib-1.2.5.win32.zip

Extract the /bin directory of each ZIP file to a directory, for example C:\xmllint and add this directory to the
Windows PATH environment variable.

#### 7-Zip

The compression tool [7-Zip](http://www.7-zip.org/) supports command line calls and can be used in generation scripts
like gen_pack.sh for automated pack file creation. Download the appropriate installer for your Windows system. Use
defaults for your installation.
