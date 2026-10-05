---
id: "tbx-theory-of-operation-cmake-script-integration-with-executes"
type: "concept"
domain: "project"
title: "Theory of Operation: CMake Script Integration with `executes:`"
summary: "The executes: node in the csolution project files allows the integration of other CMake projects or scripts."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-operation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/#cmake-script-integration-with-executes"
license: "Apache-2.0"
mode: "V"
---

The [`executes:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md#executes) node in the *csolution project* files allows the integration of other CMake projects or scripts.

### Example

The following `CMakeLists.txt` file integrates the [FCARM file converter](https://arm-software.github.io/MDK-Middleware/latest/Network/group__nw__sw__util__fcarm.html) that is part of the MDK-Middleware. The FCARM file converter reformats all web files into a single C-file which is then included and compiled into the project.

```cmake
# CMakeLists.txt for calling FCARM
# Find input files in the input base directory and in its subfolders using recursive scanning
# Format arguments and generate a steering command file, overcoming any command line length limitation
# Call FCARM using the steering command file, generating the source file in the expected output
#
# Configuration Step: ${CMAKE_COMMAND} -G <generator> -S <source directory> -B <build directory> -DINPUT_DIRECTORY=<input base directory> -DOUTPUT=<output source file>
# Build Step: ${CMAKE_COMMAND} --build <build directory>
#
# <generator>: underlying generator build system, e.g. Ninja
# <source directory>: directory where this CMakeLists.txt resides
# <build directory>: directory for temp files
# <input base directory>: directory where input data is located
# <output source file>: path and filename of source file to be generated

cmake_minimum_required(VERSION 3.22)
include(ExternalProject)

project("FCARM" NONE)

file(GLOB_RECURSE INPUT ${INPUT_DIRECTORY}/*)

foreach(ITEM ${INPUT})
  cmake_path(RELATIVE_PATH ITEM BASE_DIRECTORY ${INPUT_DIRECTORY} OUTPUT_VARIABLE FILE)
  list(APPEND FILES ${FILE})
endforeach()
string(REPLACE ";" ",\n" FILES "${FILES}")

cmake_path(RELATIVE_PATH OUTPUT BASE_DIRECTORY ${INPUT_DIRECTORY} OUTPUT_VARIABLE RELATIVE_OUTPUT)
cmake_path(GET INPUT_DIRECTORY FILENAME INPUT_DIRECTORY_NAME)
cmake_path(GET INPUT_DIRECTORY PARENT_PATH WORKING_DIRECTORY)

set(COMMAND_FILE "${CMAKE_CURRENT_BINARY_DIR}/Auto_FcArm_Cmd.inp")
file(WRITE ${COMMAND_FILE} "${FILES}\nTO ${RELATIVE_OUTPUT} RTE NOPRINT ROOT(${INPUT_DIRECTORY_NAME})\n")

add_custom_target(FCARM ALL DEPENDS ${OUTPUT})
add_custom_command(OUTPUT ${OUTPUT} DEPENDS ${INPUT}
  COMMAND fcarm @${COMMAND_FILE}
  WORKING_DIRECTORY ${WORKING_DIRECTORY}
)
```

Integration in a *csolution project*. In this case, it is part of the `*.csolution.yml`, but it may also be part of the `*.cproject.yml` file that uses the source file `Web.c` as input. The CMake build system checks for project dependencies and schedules the overall build process.

```yml
solution:
  :

  executes:
    - execute: Run-FCARM
      run: ${CMAKE_COMMAND} -G Ninja -S ${INPUT_0} -B ${CMAKE_CURRENT_BINARY_DIR}/fcarm-cmake -DINPUT_DIRECTORY=${INPUT_1} -DOUTPUT=${OUTPUT} && ${CMAKE_COMMAND} --build ${CMAKE_CURRENT_BINARY_DIR}/fcarm-cmake -- --quiet
      always:
      input:
        - fcarm-cmake    # CMake script directory
        - Web            # Input directory with "web files" for FCARM
      output:
        - project/Web.c  # Output file for FCARM
```
