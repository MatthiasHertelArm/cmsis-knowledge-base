---
id: "ceed-ceedling-installation-set-up"
type: "concept"
domain: "test"
title: "Ceedling Installation & Set Up"
summary: "Once Ceedling is installed, you interact with it as a command line utility (ceedling ...)."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/getting-started/installation.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/installation/"
license: "MIT"
mode: "V"
---

**How Exactly Do I Get Started?**

!!! tip
    You will see various references to Ruby. You do not need to know Ruby
    to use Ceedling! Ruby is simply the implementation language and 
    software packaging for Ceedling as a tool.

    Once Ceedling is installed, you interact with it as a command line
    utility (`ceedling ...`).

You have two good options for installing and running Ceedling:

1. The Ceedling Ruby Gem
1. Prepackaged _MadScienceLab_ Docker images

One way to get started is to 
[install Ceedling as a Ruby gem](#installation-as-a-ruby-gem). Gems are 
simply prepackaged Ruby-based software. Other options exist, but the 
Ceedling Gem is perhaps the simplest option for local installation.
However, please note that you will also need a compiler toolchain 
installed (e.g. GCC — GNU Compiler Collection) plus any supporting tools 
used by any Ceedling plugins you enable.

If you are familiar with the virtualization technology Docker, our premade
Docker images will get you started with Ceedling and all the accompanying
tools lickety split. Install Docker, pull down one of the
[_MadScienceLab_](#madsciencelab-docker-images) images and go.
