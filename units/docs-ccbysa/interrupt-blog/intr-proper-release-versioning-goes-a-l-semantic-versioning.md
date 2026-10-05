---
id: "intr-proper-release-versioning-goes-a-l-semantic-versioning"
type: "concept"
domain: "debug"
title: "Proper Release Versioning Goes a Long Way: Semantic Versioning"
summary: "Semantic Versioning, or SemVer for short, is likely the most popular versioning scheme in software today. It was built to solve the versioning story for a single package, but also how a single package interoperates with dependencies."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-01-19-release-versioning.md"
doc_source: "https://interrupt.memfault.com/blog/release-versioning#semantic-versioning"
license: "CC-BY-SA-4.0"
mode: "V"
---

[Semantic Versioning](https://semver.org/), or SemVer for short, is likely the most popular versioning scheme in software today. It was built to solve the versioning story for a single package, but also how a single package interoperates with dependencies.

SemVer uses a sequence of three digits, MAJOR.MINOR.PATCH, and also allows for an optional pre-release tag and build metadata tag. Altogether, a version looks like:

```
MAJOR.MINOR.PATCH-[pre-release-tag]+[build-meta-tag]
```

The MAJOR, MINOR, and PATCH digits are sorted numerically (1.1.11 > 1.1.10), the pre-release tag is sorted alphanumerically (rc > beta > alpha), and the build-meta-tag is ignored completely when determining sort order or equality (1.1.1+abcd == 1.1.1+efgh). Each should be incremented when the following occurs, according to the spec:

- MAJOR when you make incompatible API changes
- MINOR when you add functionality in a backward-compatible manner
- PATCH when you make backward-compatible bug fixes

Although it might seem pedantic, let's dig into when a release lead might want to increment each field for a firmware project.

### Incrementing MAJOR

Example: 1.0.0 → 2.0.0

For most firmware projects, the MAJOR field might *never* be incremented. If I'm writing firmware for an nRF52, and it is the only MCU in my hardware product, it doesn't have to interact or communicate with many other pieces of software or hardware, so there shouldn't be any incompatible API changes!

There is one occasion where I would seriously consider incrementing the MAJOR field, and that is when our firmware becomes **incompatible with a version of itself**. Let me explain.

Normal software packages can be updated at any time, with almost no repercussions. If incompatibility arises, just revert the change and continue. However, on firmware devices, the firmware updates itself. If there is an incompatibility, it might require a re-install, a factory reset, or in the worst of cases, the device might be bricked!

With firmware updates, you also can't expect every device to install every single version (unless that is a hard requirement of the update flow). If you deploy version 1.0.0, version 1.1.0, and version 1.2.0, your firmware should be able to update from 1.0.0 → 1.2.0 and skip 1.1.0 entirely. If a user puts your device in their nightstand and pulls it out 6 months later, this is exactly what should happen.

However, keeping that backward compatibility can weigh down our firmware, especially if we need to keep migration code in our firmware. Migration code adds complexity, code space, and increases our QA test matrix dramatically.

Let's take the Pebble Smartwatch firmware as an example. The Pebble 2.0.0 firmware was released in early 2014. Over the next year, we released versions all the way up to 2.9.1. Within all of these versions, we were changing *a lot* of stuff. We changed our file system (from Contiki's Coffee[^coffee] to an internally built one), re-wrote persistent data structures that were stored on internal and external flash, and completely re-architected how we stored our BLE bonding information. All of these things were critical to the functionality of our firmware, and at no point could we lose any of this data.

Despite all of these changes, a user could update directly from 2.0.0 to 2.9.1, and the boot-up sequence on the latter firmware would perform all the migrations (that was quite a long boot-up time).

When we were looking to revamp our firmware for a new product update, we decided to throw out all of the migration code from the 2 years before and move it into a "migration firmware" which users had to update through. With this, our 3.x set of firmwares had a clean slate with no backward-compatibility requirements! It was a breath of fresh air, and our firmware was thousands of lines of code smaller.

This was a backward-incompatible firmware update, and I believe it warranted the MAJOR increase from 2 to 3.

### Incrementing MINOR

Example: 1.1.0 → 1.2.0

In the context of firmware, this is likely what most of your firmware version updates will be, especially if they contain new features and functionality. A MINOR update means that your device can upgrade from a version with the same MAJOR to any *newer* version with the same MAJOR. For example, as we discussed in the MAJOR section, any firmware in the 2.x release train should be able to update to any newer 2.x version, such as 2.0.0 → 2.5.0.

A MINOR update does not need to allow downgrading firmware versions, which is going from a firmware version to an older one, such as 2.5 → 2.0. Speaking from experience, this is a nightmare to deal with, and you should disable this behavior from ever happening, *at least in production*. Allowing downgrades in a limited form on pre-release software will help your developers and QA teams test the upgrade path between two versions more easily.

We provide a [code snippet](#detecting-downgrades) later in the article to help prevent against downgrades at the installer level.

### Incrementing PATCH

Example: 1.1.0 → 1.1.1

On past firmware projects that I've worked on, PATCH updates are usually hot-fixes, which are quickly tested and released after a critical bug is discovered upon releasing a prior firmware update. Each patch-fix might fix one or two bugs, and the amount of time needed to test and verify that the firmware works can be minimized.

Ideally, nothing that should prevent a downgrade from occurring should be placed in a patch upgrade. This means no persistent data structure changes, no migration paths, and no changes in how the device communicates with external devices or services.

Since there are minimal to no breaking changes, these firmware updates can be upgraded and downgraded to without harm.

### Pre-release Tag Best Practices

The pre-release tag is any series of dot separated identifiers consisting of ASCII letters and numbers.

The most common pre-release tags are 'alpha', 'beta', and 'rc', which should satisfy most of your versioning requirements.

- Use 'alpha' when the release branch is first cut from master or another release branch. It's pretty much assumed that 'alpha' builds are unstable and should be treated as broken-by-default.
- Use 'beta' when the API is stable, there are no longer any breaking changes and features being pushed into the release, and the stabilization phase has begun.
- Use 'rc' (release-candidate) when you think everything is stable and QA should start doing rigorous testing because it might turn out that this build could be "the one".

I've seen many developers create out-of-order pre-release tags, so be sure to [read the spec](https://semver.org/#spec-item-11) and test your assumptions.

### Scripting and Testing SemVer

In all of my scripts that parse SemVer and when I need to quickly test version comparisons, I turn to the [python-semver](https://github.com/python-semver/python-semver) package.

```
$ pip install semver
$ python
>>> semver.parse_version_info('1.1.1-alpha.1') \
    < semver.parse_version_info('1.1.1-alpha.11')
True
```

### Missing Pieces of Semantic Versioning

Semantic Versioning provides a plethora of benefits to our firmware and release management workflows, but it doesn't solve all of our requirements. One of our requirements was to be able to reference a specific build of a firmware, which SemVer does not help with.

For example, if two developers locally compile a "1.1.1" firmware, we now have two builds of "1.1.1" with no way to tell the difference between the two! They could be based upon two entirely different revisions of software or even built with a different compiler. We could use pre-release tags or build meta tags, but we also don't want to pollute our SemVer string with data that could be better solved by other versions.

Let's now look at Git revisions, which will help us identify the software revisions that our firmware is built from.
