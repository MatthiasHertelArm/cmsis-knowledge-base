---
id: "intr-how-to-transition-from-nrf5-sdk-to-5-addressing-post-release-issues"
type: "concept"
domain: "debug"
title: "How to Transition from nRF5 SDK to Zephyr NCS － Lessons from Ultrahuman’s Journey: Behind the Solution / 5\\. Addressing Post-Release Issues"
summary: "Post-release migration of a DFU from an nRF5 SDK-based application to a Zephyr-based application presented significant challenges for iOS and Android users, primarily in managing BLE connections."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-12-11-upgrading-from-nrf5-sdk-to-ncs.md"
doc_source: "https://interrupt.memfault.com/blog/upgrading-from-nrf5-sdk-to-ncs#5-addressing-post-release-issues"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Behind the Solution_

Post-release migration of a DFU from an **nRF5 SDK-based application** to a
**Zephyr-based application** presented significant challenges for iOS and
Android users, primarily in managing BLE connections. The migration required
end-users to unpair their devices and restart their phones to re-establish
connections.

For many Android users, this process was particularly problematic, as some
phones failed to connect even after unpairing and restarting. In such cases,
users were forced to undertake multiple troubleshooting steps, including
toggling Bluetooth, clearing device caches, and sometimes even resetting the
device to factory settings.

These issues were primarily caused by changes in BLE stack handling between the
SDKs, differences in bonding and pairing mechanisms, and inconsistencies in how
Android devices handle BLE caching. Addressing these challenges required
extensive testing, clear user guidance, and improvements to the Zephyr-based
application to ensure smoother reconnection experiences post-migration.

First, to overcome the challenges of BLE connection issues during the migration
from an **nRF5 SDK-based application** to a **Zephyr-based application**, we
implemented a solution that preserved the user’s pairing information across the
transition. This involved migrating a copy of the existing pairing data from the
nRF5 SDK to the Zephyr-based application, ensuring continuity in the bond
between the device and the connected phone.

Next, we leveraged the **Service Changed indication** mechanism to inform the
phone's operating system (iOS and Android) of updates to the BLE GATT services.
This proactive notification forced the phone to refresh its cached data,
preventing connection errors caused by stale BLE attribute caches. By preserving
pairing information and signaling changes in a compliant manner, we
significantly reduced user-facing disruptions, eliminating the need for manual
troubleshooting steps like unpairing, restarting phones, or resetting Bluetooth
settings. This solution improved the migration experience and minimized user
frustration.

To develop the solution, I created a transition firmware based on nRF SDK that
would copy the pairing information and store it in a memory space intended to
remain untouched after the firmware update.

```c
void extract_ltk(uint16_t handle)
{
  const volatile uint32_t *ptr = (const volatile uint32_t *)(0xf7100);
  pm_peer_data_bonding_t bonding_data;
  ret_code_t err_code;
  uint32_t resolved_len = 0;
  uint32_t resolved_len_t = 0;
  pm_peer_id_t peer_id;
  uint32_t peer_count = pm_peer_count();
  if(peer_count>5) peer_count = 0;
  uint8_t per_ltk[16];
  int ret = 0;
  uint32_t erase_address = 0xf7000;
  peer_id = pm_next_peer_id_get(handle);
  err_code = pm_peer_data_bonding_load(handle, &bonding_data);
  if(*ptr != 0xFFFFFFFF)
  {
    memcpy(&per_ltk[0],((uint8_t*)ptr),16);
    ret = memcmp(per_ltk,&bonding_data.peer_ble_id.id_info.irk[0],16);
    if(ret!=0) fstorage_erase_info(erase_address,1);
  }
  else ret = 1;                                       //For safekeeping
  uint32_t total = sizeof(ble_gap_id_key_t)+sizeof(ble_gap_enc_key_t)+1;
  uint8_t aligned_irk[sizeof(ble_gap_id_key_t)] = {0};
  uint8_t aligned_ltk[sizeof(ble_gap_enc_key_t)] = {0};
  memcpy(aligned_keys, &bonding_data.peer_ble_id, sizeof(ble_gap_id_key_t));
  memcpy(aligned_keys+sizeof(ble_gap_id_key_t), &bonding_data.own_ltk, sizeof(ble_gap_enc_key_t));
  resolved_len = sizeof(bonding_data.peer_ble_id)+1;//(sizeof(bonding_data.peer_ble_id)%4);
  if(!err_code && (ret!=0))  {
    nrf_delay_ms(5000);
    fstorage_write_info(pairing_info_addr,&aligned_keys[0],total);
  }
}
```

Then, once the migration update completes, this information is handled in the
Zephyr-based application, as shown below:

```c
void retrieve_pairing_keys(void)
{
  const volatile uint32_t *ptr =
    (const volatile uint32_t
       *)(0xf7100); // Workaround to read back the pairing info from the old SDK
  uint8_t reversed_ltk_ediv[2]; // Array to store reversed bytes
  uint8_t reversed_ltk_val[16];
  uint8_t reversed_ltk_rand[8];
  memcpy(&irk_val[0], ((uint8_t *)ptr), 16);
  memcpy(&keys_addr[0], ((uint8_t *)ptr + 16 + 1), 6);
  memcpy(&ltk_val[0], ((uint8_t *)ptr + 16 + 6 + 1), 16);
  memcpy(&ltk_ediv[0], ((uint8_t *)ptr + 16 + 6 + 16 + 1 + 2), 2);
  memcpy(&ltk_rand[0], ((uint8_t *)ptr + 16 + 6 + 16 + 2 + 1 + 2), 8);

  printk("Successfully copied pairing info from the memory\\n");
}
```

```c
static void pre_shared_bond_set(void)
{
  int err;
  int bond_num = 0;
  struct bt_keys *pairing_info;

  bt_foreach_bond(BT_ID_DEFAULT, bond_cb, &bond_num);

  if (bond_num) {
    return;
  }

  bt_addr_le_t addr = {.type = BT_ADDR_LE_PUBLIC,
           .a.val = {0x43, 0x82, 0x5E, 0xC7, 0xE8, 0xF4}};

  struct bt_ltk ltk = {.val = {0x31, 0x30, 0xca, 0x16, 0x8d, 0x53, 0x73, 0x7c, 0x89, 0xee,
             0x42, 0x58, 0x61, 0x47, 0x03,
             0xb4}, //{0xcb, 0xea, 0xd5, 0xea, 0xe1, 0xab, 0x7c, 0x36, 0x91,
              //0x1b, 0xe7, 0xd3, 0x31, 0xd1, 0xf8, 0xbc},
           .ediv = {0},
           .rand = {0}};

  struct bt_irk irk = {.val = {0xF7, 0xDD, 0x7E, 0xC0, 0xDD, 0x48, 0x69, 0x41, 0x15, 0xF0,
             0x2A, 0x92, 0xA7, 0x1E, 0x27, 0x8A},
           .rpa.val = {0}};

  /**Copying the retrieved values from the memory onto the relevant array to pass the pairing
   * infos*/
  memcpy(&addr.a.val[0], keys_addr, 6);
  memcpy(&irk.val[0], irk_val, 16);
  memcpy(&ltk.val[0], ltk_val, 16);
  memcpy(&ltk.ediv[0], ltk_ediv, 2);
  memcpy(&ltk.rand[0], ltk_rand, 8);

  pairing_info = bt_keys_get_addr(0, &addr);
  if (pairing_info == NULL) {
    printk("Failed to get keyslot\\n");
  }

  memcpy(&pairing_info->periph_ltk, &ltk, sizeof(pairing_info->ltk));
  memcpy(&pairing_info->irk, &irk, sizeof(pairing_info->irk));

  pairing_info->flags = 0;
  pairing_info->enc_size = 16;
  pairing_info->keys = BT_KEYS_IRK | BT_KEYS_PERIPH_LTK;

  unsigned char ff[6] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};
  if (memcmp(keys_addr, ff, 6) != 0) {
    err = bt_keys_store(pairing_info);
    if (err) {
      printk("Failed to store keys (err %d)\\n", err);
    } else {
      printk("Keys stored successfully\\n");
    }
  }
}
```

This completes the transfer of bonding information from the nRF5 SDK-based
application to the Zephyr-based application. However, we still needed to
indicate service changes to ensure seamless transitioning and connectivity. This
was done using the following:

```c
void service_changed_work_handle(struct k_work *item)
{
  int err;
  static struct bt_gatt_indicate_params indicate_params;
  /* Hardcode the attribute handle for SC characteristic from nRF5 SDK application (12 in this
   * case). CONFIG_BT_GATT_ENFORCE_SUBSCRIPTION must be disabled in project configuration to
   * allow the indication to be sent, as the Zephyr host has know way of knowing if the client
   * was subscribed to this characteristic.
   *
   * IMPORTANT: consider if disabling CONFIG_BT_GATT_ENFORCE_SUBSCRIPTION
   * has security implications for your application.
   */
  static struct bt_gatt_attr attr = {.handle = 12};
  static uint16_t sc_range[2];

  sc_range[0] = sys_cpu_to_le16(0x0001);
  sc_range[1] = 0xffff;

  indicate_params.attr = &attr;
  indicate_params.func = sc_indicate_rsp;
  indicate_params.data = &sc_range[0];
  indicate_params.len = sizeof(sc_range);

  err = bt_gatt_indicate(local_connection, &indicate_params);
  if (err) {
    printk("Failed to send SC indication. (err %d)\\n", err);
    notify_service_changed(local_connection);
  }
}
```
