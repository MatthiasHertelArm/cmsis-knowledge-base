---
id: "zep-basics-workspace-concepts"
type: "concept"
domain: "project"
title: "Basics: Workspace concepts"
summary: "Here are the basic concepts you should understand about this structure. Additional details are in west-workspaces."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/basics.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/basics.rst"
license: "Apache-2.0"
mode: "V"
---

Here are the basic concepts you should understand about this structure.
Additional details are in west-workspaces.

topdir
  Above, `zephyrproject` is the name of the workspace's top level
  directory, or *topdir*. (The name `zephyrproject` is just an example
  -- it could be anything, like `z`, `my-zephyr-workspace`, etc.)

  You'll typically create the topdir and a few other files and directories
  using west init.

.west directory
  The topdir contains the `.west` directory. When west needs to find
  the topdir, it searches for `.west`, and uses its parent directory.
  The search starts from the current working directory (and starts again from
  the location in the `ZEPHYR_BASE` environment variable as a
  fallback if that fails).

configuration file
  The file `.west/config` is the workspace's :ref:`local configuration
  file <west-config>`.

manifest repository
  Every west workspace contains exactly one *manifest repository*, which is a
  Git repository containing a *manifest file*. The location of the manifest
  repository is given by the :ref:`manifest.path configuration option
  <west-config-index>` in the local configuration file.

  For upstream Zephyr, `zephyr` is the manifest repository, but you can
  configure west to use any Git repository in the workspace as the manifest
  repository. The only requirement is that it contains a valid manifest file.
  See west-topologies for information on other options, and
  west-manifests for details on the manifest file format.

manifest file
  The manifest file is a YAML file that defines *projects*, which are the
  additional Git repositories in the workspace managed by west. The manifest
  file is named `west.yml` by default; this can be overridden using the
  `manifest.file` local configuration option.

  You use the west update command to update the
  workspace's projects based on the contents of the manifest file.

projects
  Projects are Git repositories managed by west. Projects are defined in the
  manifest file and can be located anywhere inside the workspace. In the above
  example workspace, `zcbor` and `net-tools` are projects.

  By default, the Zephyr build system uses west to get
  the locations of all the projects in the workspace, so any code they contain
  can be used as modules. Note however that modules and projects
  are conceptually different.

extensions
  Any repository known to west (either the manifest repository or any project
  repository) can define west-extensions. Extensions are extra west
  commands you can run when using that workspace.

  The zephyr repository uses this feature to provide Zephyr-specific commands
  like west build. Defining these as extensions keeps
  west's core agnostic to the specifics of any workspace's Zephyr version,
  etc.

ignored files
  A workspace can contain additional Git repositories or other files and
  directories not managed by west. West basically ignores anything in the
  workspace except `.west`, the manifest repository, and the projects
  specified in the manifest file.
