---
id: "intr-practical-zephyr-devicetree-basics-about-aliases-and-chosen"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): About `/aliases` and `/chosen`"
summary: "There are two standard nodes that are important to know when talking about Devicetree: /aliases and /chosen."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#about-aliases-and-chosen"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are two standard _nodes_ that are important to know when talking about *Devicetree*: `/aliases` and `/chosen`. We'll see them again in the next article about Devicetree bindings, but since they are quite prominent in Zephyr's DTS files, we can't just leave them aside for now.


### `/aliases`

Let's have a look at `/aliases` first. The [DTSpec](https://www.devicetree.org/specifications/) specifies that the `/aliases` node is a child node of the root node. The following is specified for its properties:

> Each property of the `/aliases` node defines an alias. The property _"name"_ specifies the _alias name_. The property _"value"_ specifies the _full **path** to a node in the Devicetree_. [[DTSpec]](https://www.devicetree.org/specifications/)

Simply put, `/aliases` are just yet another way to get the full path to nodes _in your application_. In the [previous section](#path-phandles-and-phandle-array), we've learned that outside of `<` and `>` a reference to another node is expanded to that node's full path. Thus, for any alias, we can specify its **value of type `path`** using references or a plain string, as shown in the example below:

```dts
/ {
  aliases {
    alias-by-label = &label_a;
    alias-by-path = &{/node_a};
    alias-as-string = "/node_a";
  };
  label_a: node_a {
    /* Empty. */
  };
};
```

So what's the point of having an alias? Can't we use labels instead? Well, yes - but also no. As mentioned, _for the application_ there is no real difference between referring to a node via its label, its full path - or using its alias. We'll learn about the Devicetree API in Zephyr in the next article. For now, know that there are three macros `DT_ALIAS`, `DT_LABEL`, and `DT_PATH` in `zephyr/include/zephyr/devicetree.h` that you can use to get a node's identifier.

Why the emphasis on "_the application_" and what exactly doesn't work? It's important to know that `/aliases` is just another node with properties that are compiled accordingly. You can**not** use aliases in the Devicetree itself as you can do with _labels_. Thus, you can't replace an occurrence of a label with its alias. E.g., the following does not compile:

```dts
/ {
  aliases {
    alias-by-label = &label_a;
  };
  label_a: node_a {
    /* Empty. */
  };
  node_ref {
    // This doesn't work. An alias cannot be used like labels.
    phandle-by-alias = <&alias-by-label>;
  };
};
```

Still wondering why you'd need an _alias_ if you already have labels? Let's have a look at how aliases are used in Zephyr's DTS files. Say, we want to build an application that reads the state of a button. If we look at the nRF52840 development kit, we find the following nodes for the board's buttons:

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`

```dts
/ {
  buttons {
    compatible = "gpio-keys";
    button0: button_0 { /* ... */ };
    button1: button_1 { /* ... */ };
    button2: button_2 { /* ... */ };
    button3: button_3 { /* ... */ };
  };
};
```

In our application, we could refer to `button_0` via its full path `/buttons/button_0`, or using its label `button0`. Let's say we want to run the same application on a different board, e.g., STM's Nucleo-C031C6. After all, Zephyr's promise is that switching boards should be easily doable, right? Let's have a look at its board's DTS file:

`zephyr/boards/st/nucleo_c031c6/nucleo_c031c6.dts`

```dts
/ {
  gpio_keys {
    compatible = "gpio-keys";
    user_button: button { /* ... */ };
  };
};
```

So, our STM board has only one button, which has the path `/gpio_keys/button` and the label `user_button` - both incompatible with the references we'd use for our nRF development kit. Notice that `user_button` is a perfectly fine label for the only available button on the board.

However, if we'd like to use this button in our application, we'd now have to change our sources - or even worse - adapt the DTS files. Instead of doing this, we can use _aliases_ - and since buttons are commonly used throughout Zephyr's example applications, the corresponding alias, in our case `sw0`, already exists:

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`

```dts
/ {
  aliases {
    led0 = &led0;
    /* ... */
    pwm-led0 = &pwm_led0;
    sw0 = &button0;
    /* ... */
  };
};
```

`zephyr/boards/st/nucleo_c031c6/nucleo_c031c6.dts`

```dts
/ {
  aliases {
    led0 = &green_led_4;
    pwm-led0 = &green_pwm_led;
    sw0 = &user_button;
    /* ... */
  };
};
```

> **Note:** In case the aliases don't exist in the board DTS files, you could use overlay files - just like we already did in our examples. We'll see this again in the next article.

As you can see, there are also other examples where labels are not consistent. Instead, _aliases_ are used. We could change our application to get the node using the commonly available alias `sw0`, and it'll work with both boards.


### `/chosen`

Now what about the `/chosen` node? If you've been following along, or if you've just had another look at the DTS file of the nRF52840 development kit, then you might find that some of the `/chosen` nodes look an awful lot like what you find in `/aliases`, just with a different property name format:

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`

```dts
/ {
  chosen {
    zephyr,console = &uart0;
    zephyr,shell-uart = &uart0;
    zephyr,uart-mcumgr = &uart0;
    zephyr,bt-mon-uart = &uart0;
    zephyr,bt-c2h-uart = &uart0;
    zephyr,sram = &sram0;
    zephyr,flash = &flash0;
    zephyr,code-partition = &slot0_partition;
    zephyr,ieee802154 = &ieee802154;
  };
};
```

So what's the difference between a property in `/chosen` and in `/aliases`? Let's first look at the definition of the `/chosen` node in the [DTSpec](https://www.devicetree.org/specifications/):

> The `/chosen` node does not represent a real device in the system but describes parameters chosen or specified by the system firmware at run time. It shall be a child of the root node. [[DTSpec]](https://www.devicetree.org/specifications/)

The first sentence can be a bit misleading: It doesn't mean that we cannot refer to "real devices" using `/chosen` properties, it simply means that a device defined as a `/chosen` property is always a _reference_. Thus, in short, `/chosen` contains a list of _system parameters_.

> **Note:** In Zephyr, `/chosen` is only used at build-time. There is no run-time feature.

According to the [DTSpec](https://www.devicetree.org/specifications/), technically, `/chosen` properties are not restricted to the `path` type. The following are acceptable `/chosen` properties according to the specification, and Zephyr's DTS generator does indeed accept them as input:

```dts
/ {
  chosen {
    chosen-by-label = &label_a;
    chosen-by-path = &{/node_a};
    chosen-as-string = "/node_a";
    chosen-foo = "bar";
    chosen-bar = <0xF00>;
    chosen-invalid = "/invalid/path/is/a/string";
  };
  label_a: node_a {
    /* Empty. */
  };
};
```

At the time of writing, Zephyr uses `/chosen` properties exclusively for references to other _nodes_ and therefore the `/chosen` node only contains properties of the type `path`. Also, the `DT_CHOSEN` macro in the Devicetree API is only used to retrieve node identifiers. You can find a list of all Zephyr-specific `/chosen` nodes [in the official documentation](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-chosen-nodes).

So when would you use `/aliases` and when `/chosen` properties? If you want to specify a _node_ that is independent of the nodes in a Devicetree, you should use an _alias_ rather than a chosen property. `/chosen` is used to specify global configuration options and properties that affect the system as a whole. In Zephyr, `/chosen` is typically only used for [Zephyr-specific parameters](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-chosen-nodes) and not for application-specific configuration options.

Also, think twice when considering adding `/chosen` properties - for some _configuration options_, [Kconfig](https://docs.zephyrproject.org/latest/build/kconfig/index.html#configuration-system-kconfig) is probably better suited. Zephyr's official documentation has a dedicated page on [Devicetree vs. Kconfig](https://docs.zephyrproject.org/latest/build/dts/dt-vs-kconfig.html), check it out!
