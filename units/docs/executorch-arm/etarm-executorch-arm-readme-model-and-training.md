---
id: "etarm-executorch-arm-readme-model-and-training"
type: "concept"
domain: "edge-ai"
title: "executorch-arm README: Model and training"
summary: "The model architecure is based on the approach laid out in [1], with a few modifications."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/person_detection_example_cortex_m/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/person_detection_example_cortex_m/README.md#model-and-training"
license: "BSD-3-Clause"
mode: "V"
---

The model architecure is based on the approach laid out in [1], with a few modifications. The class channel C is removed since there is
only one class predicted, and a finer 7x7 grid with one single box is used rather than the suggested 5x5 grid and two boxes. Using the `SxSx(C + B*5)` formula his reduces the number of parameters from `5x5x(1+2*5)=275` to `7x7x(1*5)=245`, and it simplifies the training since a cell detection is binary true/false, rather than assigned to a particular box. When tested over the validation set, this representation leads to a decrease around 3% in the ability to match the true lables, which is minor compared to
the final accuracy loss of the constrained model.

The model backbone goes through a pretraining phase on Caltech256 [2] in `training/pretrain.py`, and the full training is then done one Open Images V7 Person detection [3] in `training/training.py` with custom image transforms and loss function. To support the pruning applied in the paper, a mask is increasingly applied during the last 100 epochs of training. The model is then compacted using the `training/pruning.py` script which halves the number of channels of the model as it removes masked columns.

To test the capabilities of the trained model, `training/test_model.py` by default will output one random image from Open Images Person detection annotated by the model, or if you have access to a webcamera you may use `training/test_model.py --webcam` to test it on completely live data. Since the model is based on a work-in-progress paper under heavy constraints the accuracy is not expected to be top quality (~27mAP@0.5 reported on the COCO dataset in the original paper, ~20mAP@0.5 seen over Open Images V7), but simpler samples provided by e.g. a webcam with one-three people present are generally well detected from experience.
