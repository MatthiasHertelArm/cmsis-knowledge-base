---
id: "intr-saving-bandwidth-with-delta-firmwa-building-our-delta-update-image"
type: "concept"
domain: "debug"
title: "Saving bandwidth with delta firmware updates: Delta Updates Implementation / Building our Delta Update Image"
summary: "First things first, let's create a new version of our firmware. As an example, I added a print line that says \"This application was patched!\" at boot when our Application runs."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-09-ota-delta-updates.md"
doc_source: "https://interrupt.memfault.com/blog/ota-delta-updates#building-our-delta-update-image"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Delta Updates Implementation_

First things first, let's create a new version of our firmware. As an example, I
added a print line that says "This application was patched!" at boot when our
Application runs.

To make things easy, I create a `.patch` file that I can apply and un-apply
from my codebase. I can then build my new firmware image with the following
`make` commands:

```
$(BUILD_DIR)/$(PROJECT)-app-patched.elf: $(SRCS_APP) $(PATCH_FILE) $(OPENCM3_LIB)
	# Apply patch file to the codebase
	$(GIT) apply $(PATCH_FILE)
	# Create the build folders
	$(MKDIR) -p $(BUILD_DIR)
	# Compile the ELF file for the new firmware
	$(CC) $(CFLAGS) $(LDFLAGS_APP) $(SRCS_APP) $(OPENCM3_LIB) -o $@
	# Un-apply the patch file
	$(GIT) apply -R $(PATCH_FILE)
```

We can then convert the image to a `.bin` file, sign it, and stick a header to
the start of it as we did in previous posts.

Now that I have my new image `app-patched.bin` and my original firmware
`app.bin`, I need to create my delta image. To do so, we can either use the
original Jojodiff or Jan's JS version, `jdiff`[^jdiff], which can be installed
via NPM (`npm install -g jdiff`). I chose the latter.

Jdiff's syntax is simple:

```
$ jdiff <base-image> <new-image> <output-patch-bin>
```

This translates to the following `make` commands:

```
$(BUILD_DIR)/patch.bin: $(BUILD_DIR)/$(PROJECT)-app.bin $(BUILD_DIR)/$(PROJECT)-app-patched.bin
	$(JDIFF) $^ $@ &>/dev/null # prints useless warning from emscripten, so ignore it
```

The resulting `patch.bin` is 1252 bytes, down from 7908 bytes for the full app
image. This is only a ~6x reduction in size but, in practice, you will see much
better results on larger and more complex applications.

Since we're not concerned with downloading the image from the cloud for the sake
of this blog post, we just hardcode the patch.bin inside of our Loader image
using `objcopy` as we explained in previous posts.

> Note: C23 which was just finalized will include a new `#embed` preprocessor
> directive which makes embedded binary and other files inside of a C program
> much easier. We'll use that instead of objcopy in the future!
