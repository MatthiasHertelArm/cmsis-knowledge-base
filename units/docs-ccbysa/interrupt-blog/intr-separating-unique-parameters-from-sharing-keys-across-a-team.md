---
id: "intr-separating-unique-parameters-from-sharing-keys-across-a-team"
type: "concept"
domain: "debug"
title: "Separating Unique Parameters from Firmware Binaries: Sharing Keys Across a Team"
summary: "We have created a relatively tidy folder structure, but if these files are stored locally on a single developer's machine or checked into a git repository, you will still have a mess on your hands!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-10-06-separating-unique-parameters.md"
doc_source: "https://interrupt.memfault.com/blog/separating-unique-parameters#sharing-keys-across-a-team"
license: "CC-BY-SA-4.0"
mode: "V"
---

We have created a relatively tidy folder structure, but if these files are
stored locally on a single developer's machine or checked into a git repository,
you will still have a mess on your hands!

The solution to this problem is simply to use a cloud-storage synced folder for
storing the keys (Dropbox, Drive, Onedrive, etc). This will also give you a safe
backup of these important files, and an easy way to share them across a team.

If you are sharing sensitive keys, such as private keys used for secure
connections to a cloud provider, it would also be advised to encrypt these files
and folders at rest using a passphrase or to use a secret key management
service such as Hashicorp Vault.
