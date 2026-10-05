---
id: "alp-cmsisdsp-dev-with-python-how-to-8-remaining-issues"
type: "concept"
domain: "project"
title: "Getting started with CMSIS-DSP using Python: Develop your knowledge: Remaining issues"
summary: "While the CMSIS-DSP Python package makes prototyping and conversion to C relatively easy, there are additional challenges when moving toward real-world applications. Here are a few remaining challenges to consider:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsisdsp-dev-with-python/how-to-8.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsisdsp-dev-with-python/how-to-8/#remaining-issues"
license: "CC-BY-SA-4.0"
mode: "V"
---

While the CMSIS-DSP Python package makes prototyping and conversion to C relatively easy, there are additional challenges when moving toward real-world applications. Here are a few remaining challenges to consider:

- This Learning Path has shown how the package helps to design and translate a DSP function working on a block of samples from Python to C. But in a real application, you receive a continuous stream of samples, not predefined blocks. You'll need to split the stream into blocks before processing, and later recombine them to reconstruct the signal.

- Part of the difficulty in this Learning Path comes from splitting and recombining the signal. Porting the block-handling logic from Python to C introduces additional complexity.

[CMSIS-Stream](https://github.com/ARM-software/CMSIS-Stream) can help with this. It's a platform-independent technology designed to simplify the use of block-processing functions with sample streams. 

If you're planning to deploy your DSP algorithms in streaming, real-time systems, it's worth exploring CMSIS-Stream. It can greatly simplify handling streams of data with block-based processing, offering a clean and efficient way to bridge the gap between theory and deployment.

You should now have a better idea of what the CMSIS-DSP Python package is capable of, and how it relates to its C equivalent.
