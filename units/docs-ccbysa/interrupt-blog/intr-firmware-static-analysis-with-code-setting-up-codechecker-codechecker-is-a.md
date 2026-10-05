---
id: "intr-firmware-static-analysis-with-code-setting-up-codechecker-codechecker-is-a"
type: "concept"
domain: "debug"
title: "Firmware Static Analysis with CodeChecker: Setting up CodeChecker CodeChecker is a combination of two tools:"
summary: "That last piece is crucial: static analyzers often generate loads of issues as well as some false positives when you first start using them."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-19-static-analysis-with-codechecker.md"
doc_source: "https://interrupt.memfault.com/blog/static-analysis-with-codechecker#setting-up-codechecker-codechecker-is-a-combination-of-two-tools"
license: "CC-BY-SA-4.0"
mode: "V"
---

1. The command-line `CodeChecker` tool which can be used to start analysis runs
   on your firmware project
2. The CodeChecker database which collects data from your runs and lets you
   track false positives, and new issues as they crop up.

That last piece is crucial: static analyzers often generate loads of issues as
well as some false positives when you first start using them. By tracking them
in a database, you can look at what **new** issues are discovered in new
changes and pull requests, and you can mute false positives rather than
continuously see them in your results.

We’ll first install the command-line tool, and run it on our project.

### Linux CLI Installation

`CodeChecker` is currently available on Linux and MacOSX.  Windows is not
officially supported, though your mileage may vary.

> Note: on Mac, CodeChecker requires disabling SIP, as it uses a
> man-in-the-middle approach to instrumenting your build. It does not currently
> work on M1 chips.

On Linux, here are some simple instructions from the CodeChecker
documentation[^codechecker_howto]:

```bash
# Install mandatory dependencies for a development and analysis environment.
# NOTE: clang or clang-tidy can be any sufficiently fresh version, and need not
#       come from package manager!
sudo apt-get install clang clang-tidy build-essential curl doxygen gcc-multilib \
      git python3-dev python3-venv

# Install nodejs dependency for web. In case of Debian/Ubuntu you can use the
# following commands. For more information see the official docs:
# https://nodejs.org/en/download/package-manager/
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs

# Check out CodeChecker source code.
git clone https://github.com/Ericsson/CodeChecker.git --depth 1 ~/codechecker
cd ~/codechecker

# Create a Python virtualenv and set it as your environment.
make venv
source $PWD/venv/bin/activate

# Build and install a CodeChecker package.
make package

# For ease of access, add the build directory to PATH.
export PATH="$PWD/build/CodeChecker/bin:$PATH"

cd ..
```

> Note: CodeChecker depends on Node 12.x, which is why you cannot simply
> install the latest node package from default repositories.

You should now be able to run `CodeChecker` from the command line:

```
$ CodeChecker -h
CodeChecker
usage: CodeChecker [-h] {analyze,analyzer-version,analyzers,check,checkers,cmd,fixit,log,parse,server,store,version,web-version} ...

Run the CodeChecker sourcecode analyzer framework.
Please specify a subcommand to access individual features.

[...]
```

Thereafter, you will need to `source` the Python virtual env in the codechecker
folder every new session before you use the tool:

```
$ source ~/codechecker/venv/bin/activate
(CodeChecker venv) $ CodeChecker -h
```
