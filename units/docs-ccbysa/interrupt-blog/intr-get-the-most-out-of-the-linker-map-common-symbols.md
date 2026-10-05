---
id: "intr-get-the-most-out-of-the-linker-map-common-symbols"
type: "concept"
domain: "debug"
title: "Get the most out of the linker map file: Digging into the map files / Common symbols"
summary: "That section does not appear in our map file but it deserves its own paragraph."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-09-get-the-most-out-of-the-linker-map-file.md"
doc_source: "https://interrupt.memfault.com/blog/get-the-most-out-of-the-linker-map-file#common-symbols"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Digging into the map files_

That section does not appear in our map file but it deserves its own paragraph.

Common symbols are non-constant global variables that can be used everywhere in your code. You might know that using global variables is usually not a good practice as they make the code harder to maintain. Indeed, the scope is global and each extern module can modify the value of any global variable, which must be taken into account when accessed. Isolation of variables into a module, using the `static` keyword, is often better to make sure the module creating the variable is entirely responsible of its state.

Now if you want to make your program safer and prevent accessibility of some global variables, go take a look into that map file section. If some variables don't need to be declared as global, you might want to convert them to static variables.

---

Several usages of the map file are possible. Most of the time, you will have an address and you will want to resolve the function behind. It can be the Program Counter in the Hard Fault handler for example. Some other times you will be debugging some undefined behavior to finally find out that your program is accidentally writing into an out-of-bounds array. Whenever you have the ELF file, `arm-none-eabi-nm` is pretty useful for those things too, and it comes with options to sort symbols by size, [check out this article from François](https://interrupt.memfault.com/blog/best-firmware-size-tools).

But some other times, it will be useful even before you have an executable ready...
