---
id: "ethu-driver-begin-end-inference-callbacks"
type: "concept"
domain: "edge-ai"
title: "Driver: Begin/End inference callbacks"
summary: "The driver provides weak hooks that applications can override to receive inference begin and end callbacks:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/driver/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/driver/src/main.md#begin-end-inference-callbacks"
license: "Apache-2.0"
mode: "V"
---

The driver provides weak hooks that applications can override to receive
inference begin and end callbacks:

```c
void ethosu_inference_begin(struct ethosu_driver *drv, void *user_arg);
void ethosu_inference_end(struct ethosu_driver *drv, void *user_arg);
```

The `user_arg` passed to
ethosu_invoke_v3() or
ethosu_invoke_async() is forwarded to both
callbacks. For example:

```c
void my_function() {
    // ...
    struct my_data data = {...};
    int result = ethosu_invoke_v3(drv,
                                  custom_data_ptr,
                                  custom_data_size,
                                  base_addr,
                                  base_addr_size,
                                  num_base_addr,
                                  (void *)&data);
    // ...
}

void ethosu_inference_begin(struct ethosu_driver *drv, void *user_arg) {
        struct my_data *data = (struct my_data*) user_arg;
        // use drv and data here
}

void ethosu_inference_end(struct ethosu_driver *drv, void *user_arg) {
        struct my_data *data = (struct my_data*) user_arg;
        // use drv and data here
}
```

For a practical use of these callbacks, see the PMU example.
