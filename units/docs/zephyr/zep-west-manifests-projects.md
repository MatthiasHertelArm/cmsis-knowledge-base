---
id: "zep-west-manifests-projects"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Files / Projects"
summary: "The projects subsection contains a sequence describing the project repositories in the west workspace. Every project has a unique name."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Manifest Files_

The `projects` subsection contains a sequence describing the project
repositories in the west workspace. Every project has a unique name. You can
specify what Git remote URLs to use when cloning and fetching the projects,
what revisions to track, and where the project should be stored on the local
file system. Note that west projects :ref:`are different from modules
<modules-vs-projects>`.

Here is an example. We'll assume the `remotes` given above.

.. Note: if you change this example, keep the equivalent manifest below in
   sync.

```yaml

manifest:
  # [... same remotes as above...]
  projects:
    - name: proj1
      description: the first example project
      remote: remote1
      path: extra/project-1
    - name: proj2
      description: |
        A multi-line description of the second example
        project.
      repo-path: my-path
      remote: remote2
      revision: v1.3
    - name: proj3
      url: https://github.com/user/project-three
      revision: abcde413a111
    - name: proj4
      url: https://github.com/user/project-four
      revision: pull/69/head # GitHub Pull Request
```
In this manifest:

- `proj1` has remote `remote1`, so its Git fetch URL is
  `https://git.example.com/base1/proj1`. The remote `url-base` is appended
  with a `/` and the project `name` to form the URL.

  Locally, this project will be cloned at path `extra/project-1` relative to
  the west workspace's root directory, since it has an explicit `path`
  attribute with this value.

  Since the project has no `revision` specified, `master` is used by
  default. The current tip of this branch will be fetched and checked out as a
  detached `HEAD` when west next updates this project.

- `proj2` has a `remote` and a `repo-path`, so its fetch URL is
  `https://git.example.com/base2/my-path`. The `repo-path` attribute, if
  present, overrides the default `name` when forming the fetch URL.

  Since the project has no `path` attribute, its `name` is used by
  default. It will be cloned into a directory named `proj2`. The commit
  pointed to by the `v1.3` tag will be checked out when west updates the
  project.

- `proj3` has an explicit `url`, so it will be fetched from
  `https://github.com/user/project-three`.

  Its local path defaults to its name, `proj3`. Commit `abcde413a111` will
  be checked out when it is next updated.

The available project keys and their usage are in the following table.
Sometimes we'll refer to the `defaults` subsection; it will be described
next.


* - Key(s)
  - Description

* - `name`
  - Mandatory; a unique name for the project. The name cannot be one of the
    reserved values "west" or "manifest". The name must be unique in the
    manifest file.

* - `description`
  - Optional, an informational description of the project. Added in
    west v1.2.0.

* - `remote`, `url`
  - Mandatory (one of the two, but not both).

    If the project has a `remote`, that remote's `url-base` will be
    combined with the project's `name` (or `repo-path`, if it has one)
    to form the fetch URL instead.

    If the project has a `url`, that's the complete fetch URL for the
    remote Git repository.

    If the project has neither, the `defaults` section must specify a
    `remote`, which will be used as the project's remote. Otherwise,
    the manifest is invalid.

* - `repo-path`
  - Optional. If given, this is concatenated on to the remote's
    `url-base` instead of the project's `name` to form its fetch URL.
    Projects may not have both `url` and `repo-path` attributes.

* - `revision`
  - Optional. The Git revision that `west update` should
    check out. This will be checked out as a detached HEAD by default, to
    avoid conflicting with local branch names. If not given, the
    `revision` value from the `defaults` subsection will be used if
    present.

    A project revision can be any fetchable git reference: branch, tag, SHA, pull request,...

    The default `revision` is `master` if not otherwise specified.

    Using `HEAD~0` [#f1]_ as the `revision` will cause west to keep the current
    state of the project.

* - `path`
  - Optional. Relative path specifying where to clone the repository
    locally, relative to the top directory in the west workspace. If missing,
    the project's `name` is used as a directory name.

* - `clone-depth`
  - Optional. If given, a positive integer which creates a shallow history
    in the cloned repository limited to the given number of commits. This
    can only be used if the `revision` is a branch or tag.

* - `west-commands`
  - Optional. If given, a relative path to a YAML file within the project
    which describes additional west commands provided by that project. This
    file is named `west-commands.yml` by convention. See

* - `import`
  - Optional. If `true`, imports projects from manifest files in the
    given repository into the current manifest. See

* - `groups`
  - Optional, a list of groups the project belongs to. See

* - `submodules`
  - Optional. You can use this to make `west update` also update `Git
    submodules`_ defined by the project. See

* - `userdata`
  - Optional. The value is an arbitrary YAML value. See
.. [#f1] In git, HEAD is a reference, whereas HEAD~<n> is a valid revision but
         not a reference. West fetches references, such as refs/heads/main or
         HEAD, and commits not available locally, but will not fetch commits if
         they are already available.
         HEAD~0 is resolved to a specific commit that is locally available, and
         therefore west will simply checkout the locally available commit,
         identified by HEAD~0.
