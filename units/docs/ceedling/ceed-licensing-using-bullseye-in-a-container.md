---
id: "ceed-licensing-using-bullseye-in-a-container"
type: "concept"
domain: "test"
title: "Licensing: Using Bullseye in a container"
summary: "Ceedling's madsciencelab-plugins Docker images do not include Bullseye. No Ceedling image can. Bullseye is commercial software, and distributing its executables requires a license that a freely available image cannot carry. Shipping the tools unlicensed is not possible either."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/bullseye/licensing.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/licensing/#using-bullseye-in-a-container"
license: "MIT"
mode: "V"
---

Ceedling's `madsciencelab-plugins` Docker images do not include Bullseye. No
Ceedling image can. Bullseye is commercial software, and distributing its
executables requires a license that a freely available image cannot carry.
Shipping the tools unlicensed is not possible either.

Download Bullseye yourself and add it to a container. There are two ways to do
that. Extend the image when you want a reusable environment. Install into a
running container when you want a one-off.

!!! note "Check the image's Ceedling version"
    Adding Bullseye to an image is only half of what you need. This plugin
    requires Ceedling 1.2.0 or newer. Releases before that ship it disabled and
    refuse to load it. Run `ceedling version` against your image to check.

!!! warning "Never commit a license key"
    Supply your key through a build argument, an environment variable, or a
    secret. A key committed to a repository is a key you have to rotate. Treat
    any image carrying an activated Bullseye license as private to your
    organization, and never push one to a public registry.

### Extending the image

Build your own layer on top of `madsciencelab-plugins`. This is the better
option for repeated use and for CI, because the install happens once at image
build time rather than on every container start.

Place your downloaded Bullseye installer beside this `Dockerfile`.

```dockerfile
FROM throwtheswitch/madsciencelab-plugins:latest

# Your downloaded, unpacked Bullseye installer directory
COPY --chown=dev:nonroot BullseyeCoverage-9.25.9 /tmp/bullseye-installer

# Supplied at build time, never baked into the Dockerfile itself
ARG BULLSEYE_LICENSE_KEY

RUN /tmp/bullseye-installer/install \
      --prefix /home/dev/bullseye \
      --key "$BULLSEYE_LICENSE_KEY" \
      --search "/usr/bin:/usr/local/bin" \
    && rm -rf /tmp/bullseye-installer

ENV PATH="/home/dev/bullseye/bin:${PATH}"
```

Build it with your key passed in.

```shell
 > docker build --build-arg BULLSEYE_LICENSE_KEY="$BULLSEYE_LICENSE_KEY" -t my-ceedling-bullseye .
```

Then run your project against the image you built.

```shell
 > docker run --rm -v /path/to/your/project:/home/dev/project my-ceedling-bullseye ceedling bullseye:all
```

!!! note "Build arguments are recorded in image history"
    `docker build --build-arg` leaves the value visible in the built image's
    metadata. Use BuildKit secrets instead if that matters to you, or build the
    image somewhere its history stays private.

### Installing into a running container

Mount your installer into a stock `madsciencelab-plugins` container and install
it there. Nothing persists after the container exits, so this suits a quick
experiment rather than repeated use.

`--prefix` installs somewhere writable, which avoids needing root.

```shell
 > docker run -it --rm \
     -e BULLSEYE_LICENSE_KEY \
     -v /path/to/your/project:/home/dev/project \
     -v /path/to/BullseyeCoverage-9.25.9:/opt/bullseye-installer:ro \
     throwtheswitch/madsciencelab-plugins:latest
```

Inside the container, install and put the tools on `PATH`.

```shell
 > /opt/bullseye-installer/install \
     --prefix /home/dev/bullseye \
     --key "$BULLSEYE_LICENSE_KEY" \
     --search "/usr/bin:/usr/local/bin"
 > export PATH=/home/dev/bullseye/bin:$PATH
 > ceedling bullseye:license
```
