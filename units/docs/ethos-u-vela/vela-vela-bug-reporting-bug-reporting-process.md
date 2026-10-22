---
id: "vela-vela-bug-reporting-bug-reporting-process"
type: "concept"
domain: "edge-ai"
title: "Vela Bug Reporting: Bug Reporting Process"
summary: "The entire process of handling a bug is summarized in the following steps."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:BUGS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/BUGS.md#bug-reporting-process"
license: "Apache-2.0"
mode: "V"
---

The entire process of handling a bug is summarized in the following steps.

1. Discovering the bug
    * A user notices a discrepancy in the functionality of Vela.
    This can be as simple as Vela crashing upon runtime,
    where an error message is printed out for the user to read.
    However, in certain cases the bug is much harder to spot.
    For example, Vela might run gracefully but optimize a network incorrectly.
    Thus the error will manifest in a silent error, such as incorrect outputs.
    In this case, as much information about the system and settings
    should be noted. This will be used later on when handling the root cause.
    A sufficient documentation of the problem is crucial when dealing with
    these silent errors.

2. Sharing the existence of the bug
    * In order to resolve the issue, its existence needs to be shared
    with the Vela community.  Even though the user could fix it by themselves
    in the first step, it is important that is is shared with the community.
    This step will be detailed in the following sections.

3. The community tackles the problem
    * When the bug has been properly detailed, the Vela community will try to
    find a solution. During this phase, further information may be requested
    or shared through the corresponding bug ticket. If a solution is found,
    the ticket will be updated with the relevant information.

As mentioned, the second step is detailed below.

### Opening the form

To add a new bug report, navigate to the
[Vela issue tracker](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/issues).

Click the button "New issue" or navigate to
[the following page](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/issues/new)

### Title

Write a title that describes the problem in a short and meaningful way.
An example of a good title is "AssertionError in weight_compressor.py
when optimizing DS-CNN". An example of a poor title is "Vela crashes on Linux".

### Type

'Issue' will be preselected and the only option.

### Description

This section should contain as much information as possible,
in order to allow someone else to reproduce the issue.

Please provide the following details:

- Vela command line and options.

- Configuration files. If these contain information that you
do not wish to make public then please upload them using Arm's
[ML Model Review](https://www.arm.com/resources/contact-us/ml-model-review)
process described below.

- Version of Vela used.

- Error messages or other console output from Vela.

- Link to a publicly accessible copy of the input network.
If this is not possible then you will need to upload the network using Arm's
[ML Model Review](https://www.arm.com/resources/contact-us/ml-model-review)
process described below.

- License files related to your network, if applicable.

Attached to the description you can find a toolbox, which contains a button to
upload files. This shall not be used to upload any network files, instead use
[ML Model Review](https://www.arm.com/resources/contact-us/ml-model-review).

### Confidential issues

The Vela project and the issue tracker are public forums.
As such, anyone can see information posted to them.

Thus, any proprietary information you wish to share should be done using Arm's
[ML Model Review](https://www.arm.com/resources/contact-us/ml-model-review)
described below.

Hence, the content of the report should be freely viewable to the public
and thus the "This issue is confidential..." option should not be selected.

### Submitting the report

Submit the report by clicking the "Create issue" button.

A confirmation e-mail will be sent out to the linked e-mail address.
Any further changes to the report will be sent out in the same way.

If you also have a fix for the issue being reported then please follow the
[Vela Contributions Guide](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/CONTRIBUTING.md) to submit your patch. Also, please
include a link to your merge request in the issue description.
