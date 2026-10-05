---
id: "intr-building-nordic-nrf-connect-sdk-pr-optional-switch-to-application-manifest"
type: "concept"
domain: "debug"
title: "Building Nordic nRF-Connect SDK Projects with GitHub Actions: Optional: Switch to Application Manifest"
summary: "It's not required, but if this were a real project we'd want to split our sample project into its own repository. We'll need to add a west.yml Zephyr manifest, making our project the manifest repository."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-18-ncs-github-actions.md"
doc_source: "https://interrupt.memfault.com/blog/ncs-github-actions#optional-switch-to-application-manifest"
license: "CC-BY-SA-4.0"
mode: "V"
---

It's not required, but if this were a real project we'd want to split our sample
project into its own repository. We'll need to add a `west.yml` Zephyr manifest,
making our project the manifest repository. See the [Zephyr
documentation](https://docs.zephyrproject.org/3.5.0/develop/west/workspaces.html#t2-star-topology-application-is-the-manifest-repository)
which describes some of the "workspace topologies" Zephyr supports; we're going
to be using a "T2" topology.

```bash
# create a new Zephyr workspace, and a folder for our project
$ mkdir -p zephyr-workspace/memfault-nrfconnect-ci-app
$ cd zephyr-workspace/memfault-nrfconnect-ci-app
# initialize a git repo in the new folder
$ git init
# copy the contents of the sample project into the new folder
$ cp -r /path/to/ncs/workspace/nrf/samples/debug/memfault/* .
# let's save our work before making any modifications, so we can diff later if
# we need to
$ git add .
$ git commit -m "Initial commit, copied from: https://github.com/nrfconnect/sdk-nrf/tree/v2.5.1/samples/debug/memfault"
# now create a blank west.yml manifest file
$ touch west.yml
```

I edited the `west.yml` file to contain the following:

```yaml
manifest:
  version: "0.10"
  projects:

    # Specify the nRF-Connect SDK as a project dependency.
    - name: sdk-nrf
      path: nrf
      url: https://github.com/nrfconnect/sdk-nrf.git
      revision: v2.5.1
      import: true

    # Specify a newer version of the Memfault Firmware SDK, overriding the one
    # specified in the nRF-Connect SDK manifest.
    - name: memfault-firmware-sdk
      url: https://github.com/memfault/memfault-firmware-sdk
      path: modules/lib/memfault-firmware-sdk
      revision: 1.6.0
```

> Note: I'm using the `url:` specifier, instead of the `remotes` shorthand
> (which is what the nRF-Connect SDK does), since I only have two projects
> imported.

> Note #2: we could make use of the
> [`name-allowlist`](https://docs.zephyrproject.org/3.5.0/develop/west/manifest.html#option-3-mapping)
> key when importing the nRF-Connect SDK, to only import the projects we need.
> This can be very useful to reduce the size of the workspace, but it's not
> required. It looks something like this:
>
> ```yaml
>     - name: sdk-nrf
>       path: nrf
>       url: https://github.com/nrfconnect/sdk-nrf.git
>       revision: v2.5.1
>       import:
>         name-allowlist:
>           - hostap
>           - zephyr
>           - mcuboot
>           - mbedtls
>           - nrfxlib
>           - cmsis
>           - hal_nordic
> ```
>
> It can be a little tricky to figure out which projects are required. The `west
> manifest --resolve` command can be helpful to print out all the projects
> selected by the manifest. I recommend saving the full list to a file, then
> start pruning and rebuilding the workspace until the minimal set is found.

Let's save our work and push it to a new GitHub repository:

```bash
$ git add .
$ git commit -m "Add west.yml manifest"
# use the gh cli to create a new GitHub repository. can also be done via the
# web ui if you're not as lazy as me 😅
$ gh repo create --public noahp/memfault-nrfconnect-ci-app --source .
$ git push
```

At this point it's also worth adding our own `README.md` file, since we still
have the original Nordic `README.rst` file. I just added a file with these
contents:

```markdown
# Memfault nRF-Connect SDK CI Example

Sample project based on the [nRF-Connect SDK Memfault
Sample](https://github.com/nrfconnect/sdk-nrf/tree/v2.5.1/samples/debug/memfault)
```

Save and push that too:

```bash
$ git add README.md
$ git commit -m "Add README.md"
$ git push
```

The last piece we can do now that we have our application as the manifest
repository is to test that we can build it using the `west` command. We'll need
to update the `west` workspace to use our new manifest repository, and then we
can build the project:

```bash
# first go up a level, to our "zephyr-workspace/" directory
$ cd ..
# now set our new project up as a "local" manifest repository
$ west init -l memfault-nrfconnect-ci-app
# now run west update and wait 😮‍💨
$ west update
# finally, build the project using the same command as before, but pointing to
# the new project path
$ west build \
  --board nrf7002dk_nrf5340_cpuapp \
  --pristine=always memfault-nrfconnect-ci-app \
  -- \
  -DCONFIG_MEMFAULT_NCS_PROJECT_KEY=\"DUMMY\"
```

Now we have a directory setup that looks like this:

```bash
# most of the folders below are downloaded when we run `west update`, and are
# from the nRF-Connect SDK's manifest
$ tree -L 2
.
├── bootloader
├── build  # build folder; this is where build artifacts are placed (by default)
├── memfault-nrfconnect-ci-app  # our mighty little project!
│   ├── README.md  # the README.md we created
│   └── west.yml  # the Zephyr manifest we created
├── modules
├── nrf
├── nrfxlib
├── test
├── tools
└── zephyr
```

Now we're ready to start setting up our GitHub Actions workflow!
