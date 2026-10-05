---
id: "alp-advanced-soc-generating-bitstream"
type: "concept"
domain: "project"
title: "Design an AXI-Lite peripheral to control GPIOs: Generate the bitstream and write your application using Vitis IDE"
summary: "In this section you will generate the bitstream for this project and write a C program to toggle the LEDs using the Xilinx Vitis IDE tools ."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/advanced_soc/generating_bitstream.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/advanced_soc/generating_bitstream/"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this section you will generate the bitstream for this project and write a C program to toggle the LEDs using the Xilinx Vitis IDE tools .

1. Under the “Sources” tab on the left, expand the “Design Sources” folder, right-click the design1.bd file, choose the “Create HDL Wrapper” and select all default options. 

    (figure: Screenshot of Vivado Sources panel showing the right-click context menu on design1.bd with Create HDL Wrapper option highlighted, which generates the top-level Verilog wrapper needed for synthesis) 

    *Figure 3.1. Creating HDL Wrapper*

2. Save any other changes and click “Generate Bitstream” on the left and click “Ok” for all pop-ups. This process takes some time. Once the process is done, select “Open Hardware Manager”:

    (figure: Screenshot of Vivado Bitstream Generation Completed dialog showing the Open Hardware Manager option selected, which you use to program the FPGA with the generated bitstream file) 

    *Figure 3.2. Generating bitstream and uploading to board*

3. Connect the board and make sure the jumper (JP3) above the red LED on the Zybo board is in JTAG mode. Then, in Vivado, click “Auto Connect” in the Hardware Manager as shown below:

    (figure: Screenshot of Vivado Hardware Manager showing the Auto Connect button which detects and connects to the Zybo board via JTAG for programming) 

    *Figure 3.3. Connecting the board*

4. Right-click on the board, select “Program Device” as shown below and click “Program” on the pop-up window. 

    (figure: Screenshot of Vivado Hardware Manager showing the right-click context menu on the detected FPGA device with Program Device option highlighted to upload the bitstream to the Zybo board) 

    *Figure 3.4. Programming the board*

5. Once the board is programmed, the green LED labeled “LD12” should light up on the board. Click “File” on the main menu bar and select “Export” -> “Export Hardware” and click “Next” on the pop-up window. Choose the following option on the next page:

    (figure: Screenshot of Vivado Export Hardware dialog showing the Include bitstream option selected, which packages the hardware design and bitstream into an XSA file for use in Vitis IDE software development) 

    *Figure 3.5. Exporting hardware and bitstream file* 

6. Choose the “export to” location as the project folder and save the file. Then click “Finish”. Next, click “Tools” on the main menu bar and select “Launch Vitis IDE”. Choose the same project folder as your workspace. Click “File” -> “New” -> “Application Project”.

    (figure: Screenshot of Vitis IDE showing the File menu with New > Application Project option selected to create a new embedded software project for the Cortex-A9 processor) 

    *Figure 3.6. Creating a new application project*

7. Select the “Create a new platform from hardware (XSA)” tab and click browse to select the XSA file you saved earlier:

    (figure: Screenshot of Vitis New Application Project wizard showing the Create a new platform from hardware (XSA) option with a browse button to select the exported hardware description file containing the FPGA design and processor configuration) 

    *Figure 3.7. Adding the XSA file*

8. Click next and give a name (e.g. led_system) to the application project. Click “Next” until you reach the following page and choose “Empty Application(C)” and click “Finish”:

    (figure: Creating an empty C Application) 

    *Figure 3.8. Creating an empty C Application*


9. Then right-click the “src” folder within the application project you created and add a new file called “main.c”. 

    (figure: Adding a main.c file) 

    *Figure 3.9. Adding a main.c file*

10. Add the following code to the file and save all your changes:

    ```
    volatile unsigned int value;
    int main(){
        while(1){
            value = *(unsigned int*)0x43c00000;
            *(unsigned int*)0x43c00004 = value;
        }
    }
    ```

11. From the address tab in Vivado, observe that the switches are located at the address “0x43c00000”. All switches together are read as 4 bits with sw[3] being the MSB (most significant bit) and sw[0] as the LSB (least significant bit). If a switch is turned on then it's corresponding bit will be 1, else it will be 0. Store the positions of the switches into a variable called “value” and write that into the address of the LEDs “0x43c00004” so that the LEDs mirror the On/Off state of the switches.

12. Right-click the application project in the explorer tab, select “Build Project” and ensure that the build is successful. Then right click again and select “Run As” and then “1 Launch Hardware” to upload everything to the board.

    (figure: Running the program on the board.) 

    *Figure 3.10. Running the program on the board.*

13. Once this is done, you should be able to toggle the LEDs using the switches.
