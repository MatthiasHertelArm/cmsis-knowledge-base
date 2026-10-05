---
id: "tbx-csolution-project-format-pre-post-build-steps"
type: "concept"
domain: "project"
title: "CSolution Project Format: Pre/Post Build Steps"
summary: "The CMSIS-Toolbox supports pre-build and post-build steps that utilize external tools or scripts. Such external commands can be used for various tasks such as:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#pre-post-build-steps"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Toolbox supports pre-build and post-build steps that utilize external tools or scripts. Such external commands can be used for various tasks such as:

- pre-process source files.
- add checksums to a binary file.
- combine multiple ELF files into a single image.
- add a timestamp to an image (`always:` ensures execution in every build).
- sign images for a bootloader.

### `executes:`

Execute an external command for pre or post-build steps used in the `*.csolution.yml` and `*.cproject.yml` files. The `input:` and `output:` files are used for dependency checking and scheduling the execution (as a pre-build or post-build step) during the build process of an application (option `--context` is not used).

Other CMake build scripts may be integrated into the overall build process using the `executes:` node. Refer to [Build Operation: CMake Script Integration with `executes:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-operation.md#cmake-script-integration-with-executes) for an example that utilizes a file converter for website images.

The structure of the `executes:` node is:

`executes:`                                               |              | Content
:---------------------------------------------------------|:-------------|:------------------------------------
`- execute:`                                              | **Required** | The identifier is used as a CMake target name and must not contain spaces and special characters; recommended is less than 32 characters.
    `run:`                                 | **Required** | Command string with the name of the program or script (optionally with path) along with argument string.
    `always:`                              |   Optional   | When present, the build step always runs and bypasses check for outdated `output:` files.
    `input:`                               |   Optional   | A list of input files (may contain [Access Sequences](#access-sequences)).
    `output:`                              |   Optional   | A list of output files (may contain [Access Sequences](#access-sequences)).
    [`for-context:`](#for-context)         |   Optional   | Run command for a list of *build* and *target* types (only supported in `*.cproject.yml`).
    [`not-for-context:`](#not-for-context) |   Optional   | Exclude run command for a list of *build* and *target* types  (only supported in `*.cproject.yml`).

The `run:` command string uses these sequences to access input files and output files:

`run:` command file access                  | Description
:-------------------------------------------|:-------------------------------------------------
`$input$`                                   | List of all input files separated by semicolon (;) character.
`$input(<n>)$`                              | Input file in the list with index `<n>`; first item is `<n>=0`.
`$output$`                                  | List of all output files separated by semicolon (;) character.
`$output(<n>)$`                             | Output file in the list with index `<n>`; first item is `<n>=0`.

The `run:` command string also accepts these [access sequences](#access-sequences): $Bname$, $Dname$, $Pname$, $BuildType$, $TargetType$, $Compiler$, $Solution$, $Project$. It does not accept [access sequences](#access-sequences) that reference directories or files as this bypasses the [project dependency check](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#project-dependency). Instead use the `input:` list to pass files or directories.

Consider the following:

- The `execute:` node is processed by the CMake build system. The order of execution depends on `$input$` and `$output$` files and is evaluated by CMake.

- The `execute:` node is processed only for an application build when no `--context` option is specified. The option `--active` can select a target-set for the application build.

- CMake uses Linux-style path names with `/` characters; it does not accept the Windows-style `\` characters in the `run:` node to specify the location of an executable tool.

- [CMake provides several builtin command-line tools](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-a-command-line-tool) (copy, checksum, etc.) that run on every Host OS. Consider using these command-line tools instead of Windows or Linux-specific commands. Use `CMake -E help` to list the available commands.

- The base directory for execution is not controlled by the CMSIS-Toolbox and is typically the `tmp` directory. The commands specified by `run:` should be in the path of the Host OS or the path/tool should be passed using an `$input(<n>)$` argument.

- At the `*.csolution.yml` level `for-context:` and `not-for-context:` is not evaluated.

**Examples:**

The tool `gen_image` combines multiple input images. It is called together with the list of [elf files](#output) that are created by the various projects. It runs when `cbuild` executes a solution build (option `--context` is not used).

```yml
solution:                                     # executed as part of a complete solution build
    :
  executes:
    - execute: GenImage                       # generate final download image
      run: gen_image $input$ -o $output$ --sign    # command string
      input:
        - $elf(Application)$                  # combine these project parts
        - $elf(TFM)$
        - $elf(Bootloader)$
      output:
        - $SolutionDir()$/$Solution$.out      # output file name
```

The Windows batch file `KeyGen.bat` converts an input file `keyfile.txt` to a C source file. combines multiple input images. It is called together with the list of [elf files](#output) that are created by the various projects. It runs when `cbuild` executes a solution build (option `--context` is not used).

```yml
project:                                      # executed as part of a project build
  executes:
    - execute: GenerateEncryptionKeys
      run: $input(1)$ $input(0)$ -o $output$
      always:                                 # always generate the keyfile.c as it has a timestamp
      input:
        - $ProjectDir()$/keyfile.txt          # contains the key in text format
        - $SolutionDir()$/KeyGen.bat
      output:
        - $ProjectDir()$/keyfile.c            # output as C source file that is part of this project
```

The built-in CMake command-line tool `copy` is used to copy the `ELF` output file.

```yml
project:                       # executed as part of a project build
  executes:
    - execute: copy-elf
      run: ${CMAKE_COMMAND} -E copy $input$ $output$
      input:
        - $elf()$
      output:
        - $OutDir()$/Project.out
      for-context: .Release
```

For examples of integrating CMake scripts, refer to [Build Operation—CMake Integration](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-operation.md).
