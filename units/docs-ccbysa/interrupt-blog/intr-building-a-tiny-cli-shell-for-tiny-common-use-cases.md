---
id: "intr-building-a-tiny-cli-shell-for-tiny-common-use-cases"
type: "concept"
domain: "debug"
title: "Building a Tiny CLI Shell for Tiny Firmware: Common Use Cases"
summary: "There are many reasons to build a command-line shell to a device. Here are the most common reasons I have found."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-09-firmware-shell.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-shell#common-use-cases"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are many reasons to build a command-line shell to a device. Here are the
most common reasons I have found.

### Inspections, Validations, & Overrides

Using a device shell is a great way for a developer to bypass the layers and
systems that would normally be in place in production. For example, a device
might communicate directly with a centralized cloud service or mobile phone to
receive its up-to-date configuration, such as its name or individual function
within a collection of devices.

When doing internal development, these extra layers are usually not important
for certain tasks, such as bringing up a peripheral or low-level system like a
file system. You would be better off setting the configuration yourself or even
mocking it out. It could also be the case that the cloud infrastructure or
mobile phone companion application isn't ready yet.

Below are some example commands that would normally be set through formalized
infrastructure but are easily set through a shell and make it easy for a
developer to configure the device quickly.

```
$ device_name set "Kitchen Timer"
> OK

$ bluetooth_address get
> F0:5C:12:E3:02:BC

$ wifi set MyHotSpot WPA2 mypassword
> OK
```

A problem that some might find with the shell is that it isn't testing the
production interfaces or processes. For example, if a device's name is normally
set through a web portal and sent down to the device over Wi-Fi, adding a
command in the shell to set the device name could be seen as a bad idea. By
doing so, developers aren't testing the normal path that customers will use and
the process may inadvertently break due to lack of testing.

In practice, this is a rare occurrence given the end-to-end flows are formally
tested in QA or automated tests. A CLI allows developers to configure their
devices quickly and get to work without standing up a massive amount of
infrastructure.

### Assembly Line Provisioning & Testing

Along a factory assembly line, it is common to talk to devices on the line over
UART because they work on Windows, Linux, and macOS and do not require an
Internet connection. Trying to work with USB, Ethernet, or other protocols
introduces complexity to the process and increases the failure rate.

During assembly, different stations will perform tasks on a single unit, such as
populating various chips or buttons and testing them, provisioning private keys
into a device's persistent storage, or burning in the device's serial number.
Each station needs to be able to communicate with the device, run several
commands or verifications, and receive a pass or fail response.

Each of these stations could run a set of shell commands and automate the
validation of responses to ensure a device meets expectations.

### Integration & Automated Tests

Every firmware project ultimately wants to have a way to perform tests on real
hardware. Software unit testing can cover the vast majority of software testing,
but it can not reproduce 100% what is happening on a real device. There are also
methods to do "hardware unit testing", where a single module (e.g. Bluetooth
chip) is controlled by a test harness.

The easiest way to interact with a device to run a suite of tests that exercise
the full stack is to write shell commands that return pass or fail status codes.

For example, a basic test that can be run is a factory reset. Almost every
firmware has one, and it is a feature that should never, ever break. We can
assume we have a command on our shell called `factory_reset`, and it will either
return `OK` or `FAIL,<code>`

```
$ factory_reset
> OK

$ factory_reset
> FAIL,6
```

This test can be one of many run in QA, and since it runs on the device you can
be 99% sure that it works properly. The only missing piece that isn't tested
through the shell is a button combination or a settings menu that would normally
trigger the reset.
