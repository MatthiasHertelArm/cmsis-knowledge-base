---
id: "spec-package-devices-family-element-package-devices-family-processor"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../processor"
summary: "Specifies attributes of the device processor. The element can occur on various levels. The attributes add-up over the different levels (family -> subFamily -> device). Elements of multi-processor devices can be associated with a specific processor using the attribute \\elem{Pname}."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Specifies attributes of the device processor. The element can occur on various levels. The attributes add-up over the different
levels (family -> subFamily -> device). Elements of multi-processor devices can be associated with a specific processor using
the attribute \elem{Pname}. If the information is relevant to all processors, no processor must be specified in \elem{Pname}.

**Example** **1**
```
<package>
  ...
  <devices>
    <family Dfamily="K20 Series" Dvendor="NXP:11">
      <processor Dcore="Cortex-M4" DcoreVersion="r0p1"/>
      <!-- ******************************  MK20DN128xxx5  ****************************** -->
      <device Dname="MK20DN128xxx5">
        <processor Dfpu="0" Dmpu="0" Dendian="Little-endian" Dclock="50000000"/>
      </device>
      ...
    </family>
  </devices>
  ...
</package>
```

**Example** **2**
```
<device name="MCIMX7D">
  ...
  <processor Dcore="Cortex-A7" DcoreVersion="r0p5" Pname="Cortex-A7" Punits="2" />
  <processor Dcore="Cortex-M4" DcoreVersion="r0p1" Pname="Cortex-M4"/>
  ...
  <debug   Pname="Cortex-A7" Punit="0" svd="SVD/iMX7D_A7.svd" __dp="0" __ap="1" address="0x80070000"/> 
  <debug   Pname="Cortex-A7" Punit="1" svd="SVD/iMX7D_A7.svd" __dp="0" __ap="1" address="0x80072000"/>
  <debug   Pname="Cortex-M4"           svd="SVD/iMX7D_M4.svd" __dp="0" __ap="4"/>
  ...
</device>
```


 



  | 
    Parents | 
    Element Chain | 
  

  | 
    family | 
    element_family | 
  

  | 
    subFamily | 
    element_subFamily | 
  

  | 
    device | 
    element_device | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Pname | 
    Processor identifier. This attribute **is mandatory for devices that embed multiple processors**. 
	      Each processor needs a unique identifier and must be used consistently in the **Pname** attribute of the elements within the scope of the current device family section.
        Only alphabetical characters, decimal digits, '-' and '_' are allowed.
     | 
    RestrictedString | 
    required for all multi-core devices | 
  

  | 
    Punits | 
    Specifies the number of processor units in a symmetric multi-processor core (MPCore). Defaults to single-core CPU (`1`) when left empty. | 
    InstancesType | 
    required for all multi-core devices | 
  

  | 
    Dcore | 
    Specifies the processor core. Use predefined values as listed in the table Device Cores. | 
    DcoreEnum | 
    required | 
  

  | 
    Dfpu | 
    Specifies whether a hardware Floating Point Unit is present in the processor.  Use predefined values as listed in the table Device FPU. | 
    DfpuEnum | 
    required | 
  

  | 
    Dmpu | 
    Specifies whether an Arm-based Memory Protection Unit is present in the processor. Do not use this in case of custom MPUs. Use predefined values as listed in the table Device MPU. | 
    DmpuEnum | 
    required | 
  

  | 
    Dtz | 
    Specifies whether an Armv8-M based device implements TrustZone. Use predefined values as listed in the table Device TZ. | 
    DtzEnum | 
    required for ARMv8-M based devices | 
  

  | 
    Ddsp | 
    Specifies whether a device supports the DSP instructions set. Use predefined values as listed in the table Device DSP. | 
    DdspEnum | 
    required | 
  

  | 
    Dmve | 
    Specifies whether a device supports the M-Profile Vector instruction set extension. Use predefined values as listed in the table Device MVE. | 
    DmveEnum | 
    required for ARMv8.1-M based devices | 
  

  | 
    Dcdecp | 
    Specifies whether a device implements Custom Datapath Extension Coprocessors and which coprocessor interfaces can be used. See (**CDE**). Possible values are explained in Custom Datapath Extensions. | 
    DcdecpEnum | 
    required for ARMv8.1-M based devices with CDE support | 
  

  | 
    Dpacbti | 
    Specifies whether a device implements Pointer Authentication/Branch Target Identification (PAC/BTI) instructions. Possible values are explained in Device PAC/BTI. | 
    DpacbtiEnum | 
    required for ARMv8.1-M based devices with PAC/BTI support | 
  

  | 
    Dendian | 
    Specifies the endianess of the processor. Use predefined values as listed in the table Endinaness. | 
    DendianEnum | 
    required | 
  

  | 
    Dclock | 
    Specifies the max clock frequency of the processor subsystem | 
    xs:unsignedInt | 
    required | 
  

  | 
    DcoreVersion | 
    Hardware revision of the processor core | 
    xs:string | 
    required | 
  



**Note:** While the different attributes can be spreaded over the family levels, they add-up and at the leaf (device level), a
complete set of attributes should be present (at least Dcore, Dfpu, Dmpu, Ddsp, Dendian, Dclock, and DcoreVersion). Adding-up
means that you can overwrite previous attributes on the next level. For example, if you have a subFamily that has a general
Dclock of 50000000 (50 Mhz), you can still specify for one of the subFamily members a different Dclock (such as 66000000).


 		

 **Table: Device Vendors**

The table lists predefined values representing device vendors. The list is extended from time to time (on request by new vendors). 
Contact cmsis@arm.com to ask for an extension. These values can be used in the elements:
- element_board_mountedDevice 
- element_accept
- element_require
- element_deny
- element_example_board
- element_board_compatibleDevice
- element_gen_select
- element_part 



  | 
    Dvendor | 
    Description | 
    Web Link | 
  

  | 
    NO_VENDOR:0 | 
    No Vendor | 
     | 
  

  | 
    3PEAK:177 | 
    3PEAK | 
    https://www.3peakic.com.cn/ | 
  

  | 
    ABOV Semiconductor:126 | 
    ABOV Semiconductor | 
    http://www.abov.co.kr/en/ | 
  

  | 
    Active-Semi:140 | 
    Active-Semi | 
    http://www.active-semi.com | 
  

  | 
    Alif Semiconductor:165 | 
    Alif Semiconductor | 
    http://www.alifsemi.com | 
  

  | 
    Ambiq Micro:120 | 
    Ambiq Micro | 
    http://www.ambiqmicro.com | 
  

  | 
    Amiccom:147 | 
    Amiccom | 
    http://www.amiccom.com.tw | 
  

  | 
    Analog Devices:1 | 
    Analog Devices | 
    http://www.analog.com | 
  

  | 
    APEXMIC:153 | 
    Apex Microeletronics Co., Ltd. | 
    http://www.apexmic.com | 
  

  | 
    ARM:82 | 
    ARM Ltd. | 
    http://www.arm.com | 
  

  | 
    ArmChina:160 | 
    Arm China | 
    http://www.armchina.com | 
  

  | 
    ArteryTek:143 | 
    ArteryTek | 
    http://www.arterytek.com | 
  

  | 
    Atmel:3 | 
    Atmel Corporation (now Microchip) | 
    http://www.microchip.com | 
  

  | 
    Autochips:150 | 
    Autochips Inc. | 
    http://www.autochips.com/index_en.aspx | 
  

  | 
    BOYAMICRO:182 | 
    BOYAMICRO | 
    https://www.boyamicro.com | 
  

  | 
    BrainChip:168 | 
    BrainChip Inc | 
    https://brainchipinc.com | 
  

  | 
    Cmsemicon:161 | 
    Cmsemicon | 
    http://www.mcu.com.cn | 
  

  | 
    CSR:118 | 
    CSR | 
    http://www.csr.com | 
  

  | 
    Cypress:19 | 
    Cypress Semiconductor | 
    http://www.cypress.com | 
  

  | 
    Dialog Semiconductor:113 | 
    Dialog Semiconductor | 
    http://www.dialog-semiconductor.com | 
  

  | 
    ELAN:162 | 
    ELAN | 
    http://www.emc.com.tw | 
  

  | 
    Elmos Semiconductor AG:138 | 
    Elmos Semiconductor AG | 
    http://www.elmos.com | 
  

  | 
    ESMT:190 | 
    Elite Semiconductor Microelectronics Technology Inc. | 
    https://www.esmt.com.tw/en | 
  

  | 
    e-peas:167 | 
	e-peas semicondcutors | 
	https://e-peas.com | 
  

  | 
    EtaCompute:157 | 
	Eta Compute Inc. | 
	https://www.etacompute.com | 
  

  | 
    FMD:169 | 
    FMD | 
    https://www.fremontmicro.com/ | 
  

  | 
    FMSH:159 | 
    Shanghai Fudan Microelectronics Group Co., Ltd | 
    http://www.fmsh.com | 
  

  | 
    Geehy:163 | 
    Geehy | 
    https://www.geehy.com/ | 
  

  | 
    Generic:5 | 
    Generic: Not a vendor specific device | 
     | 
  

  | 
    Generalplus:151 | 
    Generalplus Technology Inc. | 
    http://www.generalplus.com | 
  

  | 
    GigaDevice:123 | 
    GigaDevice | 
    http://www.gigadevice.com | 
  

  | 
    Goodix:155 | 
    Goodix | 
    https://www.goodix.com | 
  

  | 
    HDSC:145 | 
    HUADA Semiconductor | 
    http://www.hdsc.com.cn | 
  

  | 
    Hilscher:88 | 
    Hilscher Gesellschaft für Systemautomation mbH | 
    http://www.hilscher.com | 
  

  | 
    Himax:178 | 
    Himax Technologies, Inc. | 
    https://www.himax.com.tw/ | 
  

  | 
    Holtek:106 | 
    Holtek Microelectronics | 
    http://www.holtek.com.tw | 
  

  | 
    HrdWyr:188 | 
    HrdWyr | 
    https://www.hrdwyr.com | 
  

  | 
    Infineon:7 | 
    Infineon Technologies | 
    http://www.infineon.com | 
  

  | 
    Jonzic:174 | 
    Shanghai Jonzic Electronic Co., Ltd | 
    http://www.jonzic.cn | 
  

  | 
    LAPIS Technology:10 | 
    LAPIS Technology | 
    http://www.lapis-tech.com | 
  

  | 
    Linear Technolgy:136 | 
    Linear Technolgy | 
    http://www.linear.com/ | 
  

  | 
    Linkedsemi:175 | 
    LinkedSemi Microelectronics (Xiamen) Co., Ltd | 
    https://www.linkedsemi.com/ | 
  

  | 
    Maxim:23 | 
    Maxim Integrated | 
    http://www.maximintegrated.com | 
  

  | 
    MediaTek:129 | 
    MediaTek | 
    http://www.mediatek.com | 
  

  | 
    MegaChips:128 | 
    MegaChips | 
    http://www.megachips.com | 
  

  | 
    Megawin:70 | 
    Megawin | 
    http://www.megawin.com.tw | 
  

  | 
    Microchip:3 | 
    Microchip (previously Atmel) | 
    http://www.microchip.com | 
  

  | 
    Micronas:30 | 
    TDK-Micronas GmbH | 
    https://www.micronas.tdk.com | 
  

  | 
    MicroSemi:112 | 
    Microsemi | 
    http://www.microsemi.com | 
  

  | 
    Milandr:99 | 
    Milandr | 
    http://www.milandr.ru | 
  

  | 
    MindMotion:132 | 
    MindMotion | 
    http://www.mindmotion.com.cn | 
  

  | 
    MinebeaMitsumi:181 | 
    MinebeaMitsumi | 
    http://www.minebeamitsumi.com | 
  

  | 
    Nationstech:184 | 
    Nations Technologies Inc. | 
    https://www.nationstech.com | 
  

  | 
    Nordic Semiconductor:54 | 
    Nordic Semiconductor | 
    http://www.nordicsemi.com | 
  

  | 
    NSING:185 | 
    NSING Technologies Pte. Ltd. | 
    https://www.nsing.com.sg | 
  

  | 
    Nuvoton:18 | 
    Nuvoton Technolgy Corp. | 
    http://www.nuvoton.com | 
  

  | 
    NXP:11 | 
    NXP | 
    http://www.nxp.com | 
  

  | 
    ONSemiconductor:141 | 
    ON Semiconductor | 
    https://www.onsemi.com | 
  

  | 
    Panasonic:131 | 
    Panasonic | 
    http://www.panasonic.com/industrial | 
  

  | 
    Puya:176 | 
    Puya | 
    https://www.puyasemi.com/ | 
  

  | 
    Qorvo:189 | 
    Qorvo | 
    https://www.qorvo.com/ | 
  

  | 
    Realtek Semiconductor:124 | 
    Realtek Semiconductor | 
    http://www.realtek.com | 
  

  | 
    Redpine Signals:125 | 
    Repine Signals | 
    http://www.redpinesignals.com | 
  

  | 
    RelChip:146 | 
    RelChip  | 
    http://www.relchip.com/ | 
  

  | 
    Renesas:117 | 
    Renesas | 
    http://www.renesas.com | 
  

  | 
    ROHM:103 | 
    ROHM | 
    http://www.rohm.com | 
  

  | 
    RPi:170 | 
    Raspberry Pi Foundation | 
    https://www.raspberrypi.org/ | 
  

  | 
    Samsung:47 | 
    Samsung Semiconductor | 
    http://www.samsung.com | 
  

  | 
    SILAN:164 | 
    Hangzhou Silan Microelectronics Co., Ltd. | 
    http://www.silan.com.cn/ | 
  

  | 
    Silergy Corp:139 | 
    Silergy Corporation | 
    http://silergy.com/ | 
  

  | 
    Silicon Labs:21 | 
    Silicon Labs | 
    http://www.silabs.com | 
  

  | 
    Sinemicro:179 | 
    Anhui Sine Microelectronics Co., Ltd | 
    https://www.sinemicro.com | 
  

  | 
    Sinowealth:149 | 
    Sino Wealth Electronic Ltd. | 
    http://www.sinowealth.com | 
  

  | 
    SmartChip:156 | 
    SmartChip | 
     | 
  

  | 
    Socionext:171 | 
    Socionext | 
    https://www.socionext.com | 
  

  | 
    Spansion:100 | 
    Spansion (previously Fujitsu) | 
    http://www.spansion.com | 
  

  | 
    STMicroelectronics:13 | 
    STMicroelectronics | 
    http://www.st.com | 
  

  | 
    Synwit:144 | 
    Synwit Technology Co.,LTD. | 
    http://www.synwit.cn | 
  

  | 
    Texas Instruments:16 | 
    Texas Instruments | 
    http://www.ti.com | 
  

  | 
    ThinkTech:172 | 
    ThinkTech | 
    http://www.ThinkTech.net.cn | 
  

  | 
    Toshiba:92 | 
    Toshiba Semiconductor | 
    http://toshiba.semicon-storage.com | 
  

  | 
    Triad Semiconductor:104 | 
    Triad Semiconductor | 
    http://www.triadsemi.com | 
  

  | 
    Unisoc:152 | 
    Unisoc Communications, Inc. | 
    http://www.unisoc.com | 
  

  | 
    Vorago:137 | 
    Vorago Technologies | 
    http://www.voragotech.com | 
  

  | 
    Watech:183 | 
    Suzhou Watech Electronics Co., Ltd. | 
    https://www.watechelectronics.com/ | 
  

  | 
    Weltrend:148 | 
    Weltrend | 
    http://www.weltrend.com.tw | 
  

  | 
    WIZnet:122 | 
    WIZnet | 
    http://www.wiznet.co.kr | 
  

  | 
    Xiamen PengPai Microelectronics Co. Ltd:166 | 
    Pai IC | 
    https://www.pai-ic.com | 
  

  | 
    XMC:158 | 
    Wuhan Xinxin Semiconductor Manufacturing Co., Ltd. | 
    http://www.xmcwh.com/ | 
  

  | 
    XYD:186 | 
    Xiamen XYDFAB Integrated Circuit Co., Ltd | 
    http://www.xfabsemi.com/ | 
  

  | 
    YTMicro:180 | 
    YTMicro | 
    http://www.ytmicro.com/ | 
  

  | 
    Zilog:89 | 
    Zilog | 
    http://zilog.com/ | 
  




 

 **Table: Algorithm Styles**

The table lists the predefined Flash algorithm style. These values can be used in:
 - element_algorithm, element_board_algorithm



  | 
    style= | 
    Description | 
  

  | 
    Keil | 
    flashAlgorithm as defined by Arm/Keil | 
  

  | 
    IAR | 
    Flash Programming Algorithm as defined by IAR | 
  

  | 
    CMSIS | 
    To be agreed under CMSIS | 
  





 


 **Table: Device Cores**

The table lists available device cores. The list is extended from time to time to reflect new processor cores.
These values can be used in the elements:
- element_accept
- element_require
- element_deny
- element_processor
	


  | 
    Dcore= | 
    Description | 
  

  | 
    Cortex-M0 | 
    Arm Cortex-M0 processor based device | 
  

  | 
    Cortex-M0+ | 
    Arm Cortex-M0+ processor based device | 
  

  | 
    Cortex-M1 | 
    Arm Cortex-M1 processor based device | 
  

  | 
    Cortex-M3 | 
    Arm Cortex-M3 processor based device | 
  

  | 
    Cortex-M4 | 
    Arm Cortex-M4 processor based device | 
  

  | 
    Cortex-M7 | 
    Arm Cortex-M7 processor based device | 
  

  | 
    Cortex-M23 | 
    Arm Cortex-M23 processor based device | 
  

  | 
    Cortex-M33 | 
    Arm Cortex-M33 processor based device | 
  

  | 
    Cortex-M35P | 
    Arm Cortex-M35P processor based device | 
  

  | 
    Cortex-M52 | 
    Arm Cortex-M52 processor based device | 
  

  | 
    Cortex-M55 | 
    Arm Cortex-M55 processor based device | 
  
  
  | 
    Cortex-M85 | 
    Arm Cortex-M85 processor based device | 
  

  | 
    Star-MC1 | 
    ArmChina STAR-MC1 processor based device | 
  

  | 
    Star-MC3 | 
    ArmChina STAR-MC3 processor based device | 
  

  | 
    SC000 | 
    SecurCore SC000 based on technology of Cortex-M0. | 
  

  | 
    SC300 | 
    SecurCore SC300 based on technology of Cortex-M3. | 
  

  | 
    ARMV8MBL | 
    Processor ArmV8MBL compliant with the Armv8-M Baseline Architecture. | 
  

  | 
    ARMV8MML | 
    Processor ArmV8MML compliant with the Armv8-M Mainline Architecture. | 
  

  | 
    ARMV81MML | 
    Processor ArmV81MML compliant with the Armv8.1-M Mainline Architecture. | 
  

  | 
    Cortex-R4 | 
    Arm Cortex-R4 processor based device | 
  

  | 
    Cortex-R5 | 
    Arm Cortex-R5 processor based device | 
  

  | 
    Cortex-R7 | 
    Arm Cortex-R7 processor based device | 
  

  | 
    Cortex-R8 | 
    Arm Cortex-R8 processor based device | 
  

  | 
    Cortex-A5 | 
    Arm Cortex-A5 processor based device | 
  

  | 
    Cortex-A7 | 
    Arm Cortex-A7 processor based device | 
  

  | 
    Cortex-A8 | 
    Arm Cortex-A8 processor based device | 
  

  | 
    Cortex-A9 | 
    Arm Cortex-A9 processor based device | 
  

  | 
    Cortex-A15 | 
    Arm Cortex-A15 processor based device | 
  

  | 
    Cortex-A17 | 
    Arm Cortex-A17 processor based device | 
  

  | 
    Cortex-A32 | 
    Arm Cortex-A32 processor based device | 
  

  | 
    Cortex-A35 | 
    Arm Cortex-A35 processor based device | 
  

  | 
    Cortex-A53 | 
    Arm Cortex-A53 processor based device | 
  

  | 
    Cortex-A57 | 
    Arm Cortex-A57 processor based device | 
  

  | 
    Cortex-A72 | 
    Arm Cortex-A72 processor based device | 
  

  | 
    Cortex-A73 | 
    Arm Cortex-A73 processor based device | 
  

  | 
    * | 
    Device based on any processor | 
  




 


 **Table: Device FPU**

The table lists values that indicate whether a CPU has an Floating Point Unit (FPU).
The tokens can be used in the elements:
- element_accept  
- element_require 
- element_deny  
- element_processor



  | 
    Dfpu= | 
    Description | 
  

  | 
    NO_FPU | 
    Hardware Floating Point Unit not present | 
  

  | 
    FPU | 
    Hardware Floating Point Unit present | 
  

  | 
    SP_FPU | 
    Single Precision Hardware Floating Point Unit present | 
  

  | 
    DP_FPU | 
    Double Precision Hardware Floating Point Unit present | 
  




 

 **Table: Device MPU**

The table shows predefined values that identify whether a CPU has an Arm-based Memory Protection Unit (MPU).
The values can be used in the elements:
- element_accept  
- element_require 
- element_deny  
- element_processor



  | 
    Dmpu= | 
    Description | 
  

  | 
    NO_MPU | 
    No Memory Protection Unit is present | 
  

  | 
    MPU | 
    Memory Protection Unit is present | 
  



**Note:** Do not use Dmpu in case of a custom (non-Arm) MPU.


 

 **Table: Device Trust Zone **

The table shows predefined values that identify whether a CPU implements TrustZone(TZ).
The values can be used in the elements:
- element_accept  
- element_require 
- element_deny  
- element_processor



  | 
    Dtz= | 
    Description | 
  

  | 
    NO_TZ | 
    No TrustZone is present | 
  

  | 
    TZ | 
    TrustZone is present | 
  




 		

 **Table: Software Model Selection **

The table shows predefined values that identify whether an application will run in secure mode.
The values can be used in the elements:
- element_accept  
- element_require 
- element_deny  



  | 
    Dsecure= | 
    Description | 
  

  | 
    Non-secure | 
    Application is built to run in non-secure mode. | 
  

  | 
    Secure | 
    Application is built to run in secure mode. | 
  

  | 
    TZ-disabled | 
    Application is built with TrustZone security disabled. | 
  

  | 
    Secure-only | 
    Application is built to run in secure mode without any provisions to switch to non-secure code nor for non-secure callable entry points. | 
  




 		


 **Table: Device implements DSP Instructions**

The table shows predefined values that identify whether a CPU implements DSP instructions (DSP).
The values can be used in the elements:
- element_accept  
- element_require 
- element_deny  
- element_processor



  | 
    Ddsp= | 
    Description | 
  

  | 
    NO_DSP | 
    No DSP instructions supported | 
  

  | 
    DSP | 
    DSP instructions supported | 
  




 		

 **Table: Device implements M-Profile Vector Extension Instructions**

The table shows predefined values that identify whether a CPU implements MVE instructions (MVE).
The values can be used in the elements:
- element_accept  
- element_require 
- element_deny  
- element_processor



  | 
    Dmve= | 
    Description | 
  

  | 
    NO_MVE | 
    No MVE instructions supported | 
  

  | 
    MVE | 
    Integer MVE instructions supported | 
  

  | 
    FP_MVE | 
    Floating point and Integer MVE instructions supported | 
  




 		

 **Table: Custom Datapath Extensions**

The table lists values representing	Custom Datapath Extensions in a device.
The values can be used in the elements:
- element_accept 
- element_require
- element_deny  
- element_processor



  | 
    Dcdecp= | 
    Description | 
  

  | 
    BitN = 0 | 
    CDE co-processor interface disabled at BitN. | 
  

  | 
    BitN = 1 | 
    CDE co-processor interface enabled at BitN. | 
  



**Examples:**

- Dcdecp=”0xff” enables CDE on all eight co-processor interfaces.
- Dcdecp="0x12" enables CDE on co-processor interfaces 1 and 4.


 </p

 **Table: Pointer Authentication/Branch Target Identification**

The table lists values representing PAC/BTI in a device.
The values can be used in the elements:
- element_accept 
- element_require
- element_deny  
- element_processor



  | 
    DpacbtiEnum= | 
    Description | 
  

  | 
    NO_PACBTI | 
    Non-NOP-space PAC/BTI instruction are not support. | 
  

  | 
    PACBTI | 
    Non-NOP-space PAC/BTI instructions are supported. | 
  




 

 **Table: Endianness**

The table lists values representing	the endianness of a device.
The values can be used in the elements:
- element_accept 
- element_require
- element_deny  
- element_processor



  | 
    Dendian= | 
    Description | 
  

  | 
    Little-endian | 
    The least significant byte of a multi-byte access is located at the specified address. | 
  

  | 
    Big-endian | 
    The most significant byte of a multi-byte access is located at the specified address. | 
  

  | 
    Configurable | 
    The byte ordering of multi-byte accesses is configurable. |
