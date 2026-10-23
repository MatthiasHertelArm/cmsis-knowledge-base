---
id: "ceed-dependencies-cookbook"
type: "concept"
domain: "test"
title: "Dependencies: Cookbook"
summary: "Each recipe below pairs a dependency’s configuration with the commands that work with it. Any of them can sit alongside the others in one :deps list."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#cookbook"
license: "MIT"
mode: "V"
---

Each recipe below pairs a dependency’s configuration with the commands that work with
it. Any of them can sit alongside the others in one `:deps` list.

### A tagged release from git, built with Make

Your drone flight controller firmware uses an open-source sensor fusion library, which
blends accelerometer and gyroscope readings into an orientation. Its maintainers publish
tagged releases on GitHub and build it with a makefile.

Pin a library to a release tag so every developer and CI run builds the same code. The
clone is shallow, which keeps it quick.

```yaml
:dependencies:
  :deps:
    - :name: Sensor Fusion
      :paths:
        :fetch:    third_party/fusion
        :artifact: third_party/fusion/out
      :fetch:
        :method: :git
        :source: https://github.com/example/sensor-fusion.git
        :tag:    v2.4.1
      :build:
        - make lib OUT=out
      :artifacts:
        :static_libraries:
          - libfusion.a
        :includes:
          - ../include/**
```

```sh
ceedling dependencies:make     # Clone v2.4.1 if needed, then build libfusion.a
ceedling release               # Link it into the release build
```

To move to a new tag, change `:tag`, then fetch a fresh copy, since a fetched dependency
is not fetched again:

```sh
ceedling dependencies:clean:SensorFusion dependencies:make:SensorFusion
```

### A vendor archive with environment settings

Your chip vendor ships its real-time operating system as a zip archive, which your team
keeps on a shared file server. It builds with an autotools configure script, which must
be told to cross-compile for your ARM Cortex-M4 target.

Unpack a zip from a shared location and build it with the vendor’s own configure script,
passing settings through the environment of that build alone.

```yaml
:dependencies:
  :deps:
    - :name: VendorRTOS
      :paths:
        :fetch:    third_party/rtos/source
        :build:    third_party/rtos/source/build
        :artifact: third_party/rtos/install
      :fetch:
        :method: :zip
        :source: /mnt/vendor/rtos-5.2.zip
      :environment:
        - CC=arm-none-eabi-gcc
        - CFLAGS+= -mcpu=cortex-m4
      :build:
        - ./configure --prefix=../install
        - make install
      :artifacts:
        :static_libraries:
          - lib/librtos.a
        :includes:
          - include
```

```sh
ceedling dependencies:fetch:VendorRTOS   # Unpack the archive
ceedling dependencies:make:VendorRTOS    # Configure and build with CC and CFLAGS set
```

### A sibling Ceedling project

Your repository holds two Ceedling projects side by side: the main application and a
supervisor module that watches over it. The supervisor is developed and unit tested in
its own project, and the application links it as a library.

Build a library from another Ceedling project in the same repository, using that
project’s own release build. It is never fetched, so cleaning removes only its build
outputs.

```yaml
:dependencies:
  :deps:
    - :name: Supervisor
      :paths:
        :source:   ../supervisor
        :build:    ../supervisor/build
        :artifact: ../supervisor/build/release
      :fetch:
        :method: :none
      :build:
        - ceedling clobber release
      :artifacts:
        :static_libraries:
          - libsupervisor.a
        :includes:
          - ../../src/supervisor.h
```

```sh
ceedling dependencies:make:Supervisor    # Run the sibling project’s release build
ceedling test:all                        # Test against its library and header
ceedling dependencies:clean:Supervisor   # Remove only its release outputs
```

### A shared library deployed beside the release

Your Linux-based product decodes audio with a third-party codec, built as a shared
library the application loads when it starts. You keep the codec’s source release in the
project’s `downloads` folder.

Build a dynamic library and copy it beside the release executable, which loads it at run
time.

```yaml
:dependencies:
  :deps:
    - :name: Codec
      :paths:
        :fetch:    third_party/codec
        :artifact: third_party/codec/lib
      :fetch:
        :method: :tar_gzip
        :source: ../../downloads/codec-1.8.tar.gz
      :build:
        - make shared
      :artifacts:
        :dynamic_libraries:
          - libcodec.so
        :includes:
          - ../include
```

```sh
ceedling release dependencies:deploy   # Build, link, then copy libcodec.so beside the executable
```

The archive’s relative `:source` resolves from inside the fetch path, which is why it
climbs two folders.

### Build tools deployed to a shared folder

`packer` is an in-house utility your tools team keeps in its own git repository. It
bundles a compiled firmware image with its version metadata into a signed update file,
and its companion `packer-verify` checks such a file. Your release scripts run both from
the project’s `tools/bin` folder, so every developer and CI agent needs them built from
the same tagged version and installed there.

Build tools from source and install them where your build scripts or CI agents expect
them. Ceedling builds them for a release, never links them, and never cleans the deploy
folder.

```yaml
:dependencies:
  :deps:
    - :name: Packer
      :paths:
        :fetch:  third_party/packer
        :build:  third_party/packer/build
        :deploy: tools/bin
      :fetch:
        :method: :git
        :source: https://github.com/example/firmware-packer.git
        :tag:    v1.3.0
      :build:
        - make all BUILD=build
      :artifacts:
        :executables:
          - packer
          - packer-verify
```

```sh
ceedling dependencies:deploy:Packer   # Clone, build, then copy both tools to tools/bin
```

### A small library compiled by Ceedling

A colleague’s CRC routines live in your company’s Subversion repository: a C file and
a header, with no makefile and no library of their own. Your firmware checks its data
packets with them.

Pin a few C files from Subversion and let `:build_lib` compile and archive them, with no
build system of their own.

```yaml
:dependencies:
  :deps:
    - :name: CRC Utils
      :paths:
        :fetch: third_party/crc
        :build: third_party/crc/build
      :fetch:
        :method:   :svn
        :source:   https://svn.example.com/repos/crc/trunk
        :revision: '1287'
      :build:
        - :build_lib
      :artifacts:
        :static_libraries:
          - libcrc.a
        :includes:
          - ../crc.h
      :defines:
        - CRC_TABLE_IN_ROM
```

```sh
ceedling dependencies:make:CRCUtils   # Check out revision 1287, then compile and archive
ceedling files:dependencies           # Confirm third_party/crc/build/libcrc.a is listed
```
