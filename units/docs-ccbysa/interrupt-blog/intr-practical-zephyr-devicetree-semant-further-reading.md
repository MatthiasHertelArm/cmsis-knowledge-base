---
id: "intr-practical-zephyr-devicetree-semant-further-reading"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Further reading"
summary: "The following are great resources when it comes to Zephyr and are worth a read or watch:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#further-reading"
license: "CC-BY-SA-4.0"
mode: "V"
---

The following are great resources when it comes to Zephyr and are worth a read _or watch_:

- As we've seen, the [official Devicetree specification](https://www.devicetree.org/specifications/) also contains information on Devicetree _bindings_.
- Second, of course, [Zephyr's official documentation on Devicetree](https://docs.zephyrproject.org/latest/build/dts/index.html) is still a go-to reference.
- The course [nRF Connect SDK Fundamentals](https://academy.nordicsemi.com/courses/nrf-connect-sdk-fundamentals/) in Nordic's [DevAcademy](https://academy.nordicsemi.com/) guides you through some examples using the _Devicetree API_ and is therefore highly recommended.
- Definitely watch the presentation [Zephyr Devicetree Mysteries, Solved](https://www.youtube.com/watch?v=w8GgP3h0M8M&list=PLzRQULb6-ipFDwFONbHu-Qb305hJR7ICe) by Martí Bolívar.
- More _Devicetree_ examples can also be found in the [API documentation](https://docs.zephyrproject.org/latest/build/dts/api/api.html), but also in Zephyr's tests, e.g., `zephyr/dts/bindings/test` and `zephyr/tests/lib/devicetree/api/src/main.c`.
- Advanced usage of the _Devicetree API_ is shown in the [documentation about instance-based APIs](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-inst-apis).
- The [Tutorial: Mastering Zephyr Driver Development](https://www.youtube.com/watch?v=o-f2qCd2AXo) by Gerard Marull Paretas from the Zephyr Development Summit 2022 is also a great resource if you want to learn more about device driver development in Zephyr.

Finally, have a look at the files in the [accompanying GitHub repository](https://github.com/lmapii/practical-zephyr) and I hope I'll see you again in the next article, where we'll finally see a practical application of everything we've learned in this article!
