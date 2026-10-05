---
id: "alp-tflow-nn-stcube-setup-set-up-anaconda"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Prepare development environment: Set up Anaconda"
summary: "Anaconda is a distribution of Python language for data science and machine learning. With Anaconda, you can easily install open-source machine learning packages."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/setup/#set-up-anaconda"
license: "CC-BY-SA-4.0"
mode: "V"
---

Anaconda is a distribution of Python language for data science and machine learning. With Anaconda, you can easily install open-source machine learning packages.

1. Visit the official [Anaconda](https://www.anaconda.com/) page.
2. Download the Anaconda Installer, and install using default options.

With Anaconda installed, you will now install the necessary `conda` packages for data collection and machine learning including [Jupyter notebook](https://jupyter.org/).

Follow the steps as shown below:

1. Open `Anaconda Prompt`
2. Create an environment with:
```console
conda create -n ml_lab python=3.8
```
3. Activate your environment with:
```console
conda activate ml_lab
```
4. Add `conda-forge` channel to install packages:
```console
conda config --add channels conda-forge
```
5. Then install necessary python packages:
```console
conda install jupyter pandas pyserial scikit-learn tensorflow matplotlib
```
