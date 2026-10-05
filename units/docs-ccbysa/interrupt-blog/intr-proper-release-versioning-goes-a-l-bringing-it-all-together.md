---
id: "intr-proper-release-versioning-goes-a-l-bringing-it-all-together"
type: "concept"
domain: "debug"
title: "Proper Release Versioning Goes a Long Way: Bringing It All Together"
summary: "Now that we've discussed each of the three versioning items that I like to include in my firmware projects, we should now discuss how to do the deed."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-01-19-release-versioning.md"
doc_source: "https://interrupt.memfault.com/blog/release-versioning#bringing-it-all-together"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we've discussed each of the three versioning items that I like to include in my firmware projects, we should now discuss how to do the deed.

### Setting MAJOR.MINOR.PATCH

Ultimately, you will want to set the MAJOR, MINOR, and PATCH numbers in macros. Whether these are defined using an auto-generated header file or defined as a CFLAG using `-D` is up to you. Where these values come from is the more exciting bit.

#### Git Tags & CI

If you have your [continuous integration](https://interrupt.memfault.com/blog/continuous-integration-for-firmware) system set up to build your firmware, pulling the SemVer from the Git tag is a great way to go.

I like to configure my CI systems to watch tags that start with `release-*`. That way, I can tag and push releases with a few simple Git commands and a script in CI which parses the SemVer and sets build variables

```
$ git checkout release-1.0
$ git tag 1.0.0
$ git push origin 1.0.0
```

Before CI builds this tag, it will pull out 1.0.0 from the tag name, set a few CFLAGS (`FW_VERSION_MAJOR`, `FW_VERSION_MINOR`, etc.), and build the firmware.

#### Manually Set Versions

Another way I've seen versions get built is by setting a `fw_version.h` header manually.

```
// fw_version.h

#define FW_VERSION_MAJOR 1
#define FW_VERSION_MINOR 0
#define FW_VERSION_PATCH 0
```

A developer would make this change in a commit on its own and push it to a branch for CI to build.

### Baking Versions Into Binary Header

François, in his [Device Firmware Update Cookbook](https://interrupt.memfault.com/blog/device-firmware-update-cookbook) post, describes how to [include metadata](https://interrupt.memfault.com/blog/device-firmware-update-cookbook#image-metadata) in both ELF files and into a header of loadable firmware binaries.

With the version in the ELF file, we can investigate the metadata within GDB:

```
$ arm-none-eabi-gdb-py --se build/fwup-example-app.elf
Reading symbols from build/fwup-example-app.elf...
(gdb) p image_hdr
$1 = {
  image_magic = 51966,
  image_hdr_version = 1,
  crc = 0,
  data_size = 0,
  image_type = 2 '\002',
  version_major = 1 '\001',
  version_minor = 0 '\000',
  version_patch = 1 '\001',
  vector_addr = 134348832,
  reserved = 0,
  git_sha = "70859a3"
}
```

And when working with our `.bin` files, we can print the metadata using Python's `struct` package.

```python
def print_metadata(bin_filename):
    IMAGE_HDR_SIZE_BYTES = 32

    with open(bin_filename, "rb") as f:
        image_hdr = f.read(IMAGE_HDR_SIZE_BYTES)
        data = f.read()

    image_magic, image_hdr_version, \
        crc, data_size, image_type, \
        major, minor, patch, \
        vector_addr, reserved, \
        git_sha = struct.unpack("<HHLLBBBBLL8s", image_hdr)

    print("Version: {}.{}.{}".format(major, minor, patch))
    print("Git SHA: {}".format(git_sha.decode('utf-8')))
```

```
$ python ~/print_header.py build/fwup-example-app.bin
Version: 1.0.1
Git SHA: 70859a3
```

### Detecting Downgrades

One of the most unpleasant and avoidable ways of bricking a device is to allow it to install incompatible versions, such as downgrades. If SemVer is followed closely, almost all dangerous downgrade paths could be avoided without much logic or defensive work.

Although using `sscanf` isn't really recommended due to code-size bloat, here is a simple example snippet of code to detect firmware downgrades for those that use Semantic Versioning.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char *current_ver = "1.1.0";
    char *new_ver = "1.0.0";

    int currentMajor = 0, currentMinor = 0, currentPatch = 0;
    int newMajor, newMinor, newPatch;

    sscanf(current_ver, "%d.%d.%d", &currentMajor, &currentMinor, &currentPatch);
    sscanf(new_ver, "%d.%d.%d", &newMajor, &newMinor, &newPatch);

    if (newMajor < currentMajor || newMinor < currentMinor) {
        // Downgrade detected. Do not perform the "update".
    }
}
```

If you use another versioning scheme, you should still try to detect downgrades, whether that is by using, a timestamp, commit number, or anything else that is roughly stable and sequential.
