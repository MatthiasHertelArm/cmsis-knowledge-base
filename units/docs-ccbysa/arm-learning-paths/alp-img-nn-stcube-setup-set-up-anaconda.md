---
id: "alp-img-nn-stcube-setup-set-up-anaconda"
type: "concept"
domain: "edge-ai"
title: "Build and run an image classification NN model on an STM32L4 Discovery board: Prepare environment: Set up Anaconda"
summary: "Anaconda is a Python distribution for data science and machine learning. With Anaconda, you can easily install open-source machine learning packages."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/img_nn_stcube/setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/img_nn_stcube/setup/#set-up-anaconda"
license: "CC-BY-SA-4.0"
mode: "V"
---

Anaconda is a Python distribution for data science and machine learning. With Anaconda, you can easily install open-source machine learning packages.

1. Visit the [Anaconda website](https://www.anaconda.com/) and download the installer

2. Run the installer with the default options

With Anaconda installed, you can install the necessary `conda` packages for data collection and machine learning, including [Jupyter notebook](https://jupyter.org/).

Follow the steps as shown below:

1. First open Anaconda Prompt

2. Create an environment by typing:

```console
conda create -n ml_lab python=3.8
```
3. Activate your environment by typing:

```console
conda activate ml_lab
```
4. Add conda-forge channel to install packages:

```console
conda config --add channels conda-forge
```
5. Then install python packages:

```console
conda install jupyter pandas tensorflow matplotlib numpy 
```
6. Users have reported issues where the steps below result in `dead kernel` errors. To fix the problem, [described as a GitHub issue](https://github.com/dmlc/xgboost/issues/1715), use:

```console
conda install nomkl
```
