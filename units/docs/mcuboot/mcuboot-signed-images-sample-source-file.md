---
id: "mcuboot-signed-images-sample-source-file"
type: "concept"
domain: "boot-update"
title: "signed images: Sample source file"
summary: "const struct bootutil_key bootutil_keys[] = { [0] = { .key = image_sign_pub_der, .len = &image_sign_pub_der_len, } };"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/signed_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/signed_images.md#sample-source-file"
license: "Apache-2.0"
mode: "V"
---

This exports the keys.

    #include <bootutil/sign_key.h>

    #include "image_sign_pub.c.import"

    const struct bootutil_key bootutil_keys[] = {
        [0] = {
            .key = image_sign_pub_der,
            .len = &image_sign_pub_der_len,
        }
    };

    const int bootutil_key_cnt = sizeof(bootutil_keys) / sizeof(bootutil_keys[0]);
