---
id: "spec-package-repository-element"
type: "concept"
domain: "pack"
title: "/package/repository element"
summary: "The element specifies the URL (HTTPS required) of the public repository the pack originates from. The attribute 'type' specifies the repository technology and therefore the tools required to be used with this repository."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_repository.html"
license: "Apache-2.0"
mode: "V"
---

The element specifies the URL (HTTPS required) of the public repository the pack originates from. The attribute 'type'
specifies the repository technology and therefore the tools required to be used with this repository.


**Example:**
```
<package>
  ...
  <repository type="git">https://github.com/ARM-software/CMSIS-Driver.git</repository>
    ...
  </releases>
  ...
</package>
```


 



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| package | element_package |  |  |
| Attributes | Description | Type | Use |
| type | Repository management technology used by the specified public repository (e.g. git, svn). | git svn other | optional |



**Example:**

Contributing to a software pack hosted on GitHub:

- Open the URL specified by the `\<repository>` element in a browser.
- Create a fork of the repository.
- Clone the fork on your machine (you may want to checkout the `tag` specified in the \`<release>` element).
- Create a branch for your modifications.
- Develop and test the modifications of your branch and push the branch to GitHub.
- Create a pull request of your branch into the upstream repository.
