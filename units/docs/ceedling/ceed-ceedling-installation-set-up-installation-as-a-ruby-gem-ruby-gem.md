---
id: "ceed-ceedling-installation-set-up-installation-as-a-ruby-gem-ruby-gem"
type: "concept"
domain: "test"
title: "Ceedling Installation & Set Up: Installation as a [Ruby Gem][ruby-gem]"
summary: "[ruby-gem]: http://docs.rubygems.org/read/chapter/1 [ruby-install]: http://www.ruby-lang.org/en/downloads/ [rubygems-repo]: http://rubygems.org [command-line]:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/getting-started/installation.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/installation/#installation-as-a-ruby-gem-ruby-gem"
license: "MIT"
mode: "V"
---

!!! warning "Use `--no-document` for gem installation"
    `--no-document` opts out of the RDoc tool’s automatic scanning of
    Ceedling source code during installation. This documentation step is not 
    needed by a user, and, more importantly, RDoc can cause installation 
    failures due to bugs or language incompatibilities in RDoc’s custom 
    language parser.

1. [Download and install Ruby][ruby-install]. Ruby 3 is required.
1. Use Ruby‘s command line gem package manager to install Ceedling from
   the public [RubyGems repository][rubygems-repo]: `gem install ceedling --no-document`.
    * Unity and CMock come along with Ceedling at no extra charge.
    * Installing from the official RubyGems repository will automatically 
      install Ceedling‘s dependencies.
1. Use [Ceedling’s command line][command-line] to export an example 
   project (`ceedling examples` for a listing) or create an empty Ceedling 
   project with `ceedling new`. Of course, executing `ceedling help` first 
   is, well, helpful.

[ruby-gem]: http://docs.rubygems.org/read/chapter/1
[ruby-install]: http://www.ruby-lang.org/en/downloads/
[rubygems-repo]: http://rubygems.org
[command-line]: 

### Gem install notes

Steps 1–2 above are a one-time affair for your local environment. 
When steps 1-2 are completed once, only step 3 is needed for each new 
code project.

If you are working with prerelease versions of Ceedling or some other 
off-the-beaten-path installation scenario, you may want to directly 
install the Ceedling .gem file attached to any of the Github releases.
No problem.

The steps are similar to the preceding with two changes:

1. `gem install --local <ceedling .gem filepath> --no-document`
1. Any missing dependencies must be manually installed before 
   installation of the local Ceedling gem will succeed. A local 
   installation attempt will complain about any missing dependencies. 
   Simply `gem install` them by name.
