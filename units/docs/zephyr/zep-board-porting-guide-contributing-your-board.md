---
id: "zep-board-porting-guide-contributing-your-board"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Contributing your board"
summary: "If you want to contribute your board to Zephyr, first -- thanks!"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

If you want to contribute your board to Zephyr, first -- thanks!

There are some extra things you'll need to do:

#. Make sure you've followed all the porting-general-recommendations.
   They are requirements for boards included with Zephyr.

#. Add documentation for your board using the template file
   `doc/templates/board.tmpl`. See zephyr_doc for
   information on how to build your documentation before submitting
   your pull request.

#. Prepare a pull request adding your board which follows the
   contribute_guidelines.
