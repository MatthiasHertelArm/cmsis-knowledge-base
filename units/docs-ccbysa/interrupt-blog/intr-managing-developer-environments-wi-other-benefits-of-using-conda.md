---
id: "intr-managing-developer-environments-wi-other-benefits-of-using-conda"
type: "concept"
domain: "debug"
title: "Managing Developer Environments with Conda: Other Benefits of Using Conda"
summary: "The more I used Conda, the more I enjoyed the subtle but enormous benefits. They have all saved me hours of time both for myself and my co-workers. I have compiled my favorite benefits below."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-01-07-conda-developer-environments.md"
doc_source: "https://interrupt.memfault.com/blog/conda-developer-environments#other-benefits-of-using-conda"
license: "CC-BY-SA-4.0"
mode: "V"
---

The more I used Conda, the more I enjoyed the subtle but enormous benefits. They
have all saved me hours of time both for myself and my co-workers. I have
compiled my favorite benefits below.

### Easily Re-Create Environments

It's not uncommon for your build environment to stop working. Maybe a package
becomes corrupted, or a package is accidentally installed or uninstalled. Or
maybe you run into a problem locally and want to confirm that it _isn't_ your
build environment before reaching out to your teammates.

With Conda, this becomes incredibly simple! You can very quickly delete and
re-create your environment using

```
$ conda env remove -n my_env
$ conda env create -n my_env -f environment.yml
$ conda activate my_env
```

This will remove the old environment **in its entirety** and re-create it. The
process takes about 30 seconds. In comparison, re-provisioning a virtual machine
or your computer's operating system could take an hour or a whole day
respectively.

### Bouncing Between Projects and Commits

If you change projects, commits, or branches often, it's simple to make sure
that all packages are installed and with the correct versions.

```
$ git checkout <build from 9 months ago>
$ conda env update -f environment.yml
$ make
```

### Easier Git Bisect

For those who have used `git bisect` over a large date range (3+ months), you
might recall how difficult it can be. This is because for every commit, you need
install the versions of the packages that were required **at that time**. Some
teams do this through a revision controlled wiki page, change-log in the
README.md, or through a (sigh) guess-and-check method. If it builds, it works,
right? (No)

With Conda, the build and test loop becomes simple!

```
# Update all required packages
$ conda env update -f environment.yml

# Build and flash the firmware
$ make && flash

# Test the system

# Mark as good or bad
$ git bisect [good|bad]

# Repeat many times...
```

### Distributing a Conda Environment

If you want to be able to export and distribute a Conda environment, including
Python, pip packages, and system packages, this is possible using the official
Conda package called [Conda Pack](https://conda.github.io/conda-pack/).

This is useful when you need to give a build or test environment to an end
customer, a vendor, or a factory in China. It is also useful where the recipient
has limited or no access to the Internet. These packaged environments can be
used **without** installing Python, Conda, or any other packages on the host
machine.
