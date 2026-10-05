---
id: "intr-saving-bandwidth-with-delta-firmwa-delta-updates-explained"
type: "concept"
domain: "debug"
title: "Saving bandwidth with delta firmware updates: Delta Updates Explained"
summary: "The concept behind delta updates is intuitive. When we put together a new version of our firmware, we do not change every single line of code."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-09-ota-delta-updates.md"
doc_source: "https://interrupt.memfault.com/blog/ota-delta-updates#delta-updates-explained"
license: "CC-BY-SA-4.0"
mode: "V"
---

> Note: the next few sections provide an overview of delta updates, why it
> matters, and how it works. If you'd like to skip straight to implementation,
> click
> [here](#delta-updates-implementation).

The concept behind delta updates is intuitive. When we put together a new
version of our firmware, we do not change every single line of code. Instead, we
edit specific sections of the code to change the behavior of the code and
introduce a new feature or fix a bug.

This means that our new firmware is largely made up of the old firmware, plus a
few changes.



Wouldn't it be neat if we could collect only the code changes and send those
down to the device, rather than the full firmware update? This is exactly what
delta updates allow us to do.

The process is broken up into two steps. First, we need to extract the bits that
have changed from our new image, we'll call it DIFF.



Then we reconstruct our image from our original firmware and our delta image,
which we'll call PATCH.



### Pros and Cons of Delta Updates

#### Pros

The obvious advantage of delta updates is the small size of the resulting image.
Delta images are often one to two orders of magnitude smaller than full system
images. The size reduction has multiple beneficial effects:

1. OTA updates become possible over very low bandwidth links (e.g. LoRaWAN).
2. Updates are much faster over low bandwidth links. For example, a 10MB image
   may take over 15 minutes to download over a BLE connection to a mobile phone,
   even at [peak throughput](https://interrupt.memfault.com/blog/ble-throughput-primer). A
   delta update would take less than 1 minute to download, leading to a much
   better customer experience and less risk of power loss mid-update.
3. The lifetime of flash memory can be extended, as fewer writes are needed to
   install a delta image than a full image.
4. OTA consumes less power, thanks to the reduced communication and flash
   writing required.

#### Cons

However, there is no such thing as a free lunch! Delta updates come with some
downsides worth considering:

1. More complexity! Your firmware update code now needs to implement the
   patching algorithm, which creates more opportunities for bugs.
2. Delta updates require more code space to implement the patching algorithm,
   so if you are constrained already it may not be appropriate for your project.
3. Managing delta updates creates more complexity on the backend and in the
   release process.

That last point bears elaborating a bit. Unlike all system images, each delta
image is only compatible with a single original version. In other words, while a
system image for firmware v1.2.0 can upgrade any prior version to v1.2.0, a
delta update for "v1.1.0→v1.2.0" can only upgrade devices running v1.1.0 to
v1.2.0. As you can imagine this creates a serious challenge at the QA stage,
since the combination of things to test is much larger than with a system image.

This also means that your OTA backend needs to be sophisticated enough to
present delta updates when devices are running compatible versions, and in all
other cases present a full system update. And each firmware release requires
you to compile and upload several delta images for your versions in the
field.

> Our OTA backend at [Memfault](https://memfault.com) supports delta updates!
> You can read more about it in our
> [documentation](https://docs.memfault.com/docs/platform/ota/#delta-releases).

### Jojodiff

One of the key components of a delta update system is a binary diff and patch
system. There are remarkably few libraries that provide this functionality. The
excellent BSDiff[^bsdiff], and XDelta[^xdelta] both require too much memory to
work on most embedded systems without modification. This leaves
Jojodiff[^jojodiff], which has been helpfully reimplemented by Jan
Jongboom[^jan] in his JanPatch library[^janpatch] optimized for embedded
systems.

While Jojodiff is neither the fastest nor the most efficient, it requires constant
space, linear time complexity, and can patch a file in place. These features
make it well suited to limited environments such as MCU-based devices.

> Note: we've heard from some teams that they have successfully modified XDelta
> and BSDiff to do in-place, fixed memory delta patching. This was more effort
> than made sense in the context of this blog post, but it may be the right
> approach for your project. As always, your mileage may vary!
