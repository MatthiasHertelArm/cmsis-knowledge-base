---
id: "aig-install-guides-rust-embedded-how-do-i-install-rust-for-embe"
type: "concept"
domain: "project"
title: "Rust for Embedded Applications: How do I install Rust for Embedded Applications?"
summary: "Run the following command to download and install Rust:"
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/rust_embedded.md"
doc_source: "https://learn.arm.com/install-guides/rust_embedded/#how-do-i-install-rust-for-embedded-applications"
license: "CC-BY-SA-4.0"
mode: "V"
---

### How do I download and install Rust?

Run the following command to download and install Rust:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
```

Start a new shell or run the following command to continue:

```bash
source "$HOME/.cargo/env"
```
To confirm the installation is complete, run the following (`cargo` is the Rust package manager):

```bash { env_source="~/.bashrc" }
rustc --version
cargo version
```

The output is similar to:
```output
rustc 1.98.0 (88d9e12ae 2026-08-18)
cargo 1.98.0 (797e8a9bc 2026-08-05)
```

### How do I add Arm cross-compilation support?

Add cross compilation support for the required Arm Architectures. For example, to add support for Armv7-M architecture, you can use:
```bash
rustup target add thumbv7m-none-eabi
```
For a full list of supported architectures, use:
```bash
rustup target list
```

### How do I install cargo-generate?

To generate a project from a template, you need `cargo-generate`. Install it with:

```bash
sudo apt install -y libssl-dev pkg-config build-essential
cargo install cargo-generate
```

### How do I install cargo-binutils? (optional)

Other utilities are also available. For completeness, install them with:

```bash
cargo install cargo-binutils
rustup component add llvm-tools
```

You are now ready to build an embedded application in Rust.
