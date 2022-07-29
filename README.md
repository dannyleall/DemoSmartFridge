# DemoSmartFridge
This is a miniature smart fridge system that utilizes OpenCV to identify when an item is missing inside of a refrigerator. Once it recognizes an item is missing, it will use Selenium to automate the process of placing an order for that specific missing item. Lastly, it will automatically shoot an email to the user notifying them of its purchase.<br>
Some files and functions are purposely left out to avoid forking. These files aim to demonstrate the necessary active knowledge of machine learning algorithms to successfully complete an actual smart fridge.<br><br>


## Hardware Components
1. Raspberry Pi 4.
  a. Broadcom BCM2711, Quad-core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz.
  b. 4GB of SDRAM.
  c. 32GB SD card for hard disk memory.

2. Raspberry Pi 4 Camera IR-CUT Night Vision Camera Module.
  a. 5MP OV5647 sensor, 3.6mm adjustable Focal Length, and 2pcs LED Flashlight.<br>
  
![image](https://user-images.githubusercontent.com/92603066/181682724-c98c3d7d-9b04-4bb4-962d-07ffe630de9a.png)<br><br><br>

## Software Components
  1. Python, version: 3.7.3.
  2. OpenCV module for Python, version: 4.5.4-dev.
    a. yolo.weights, yolo.cgf, and coco.names for configuring the YOLO algorithm in OpenCV’s deep neural network [3].
  3. Email, SMTPlib, Time, and Picamera modules for Python (included with interpreter).
  4. Selenium module for Python, version: 3.14.1.
  5. Raspberry Pi OS (Raspbian), version: 10 (buster).
  6. Thony Python IDE (included with Raspbian).
  <br><br><br>
  
  
## Sample Run With Images
### Set Up For Capture
Here is a visual of how the test example was run by pointing the Raspberry Pi camera towards the desired object, in this case, a banana.

![image](https://user-images.githubusercontent.com/92603066/181682859-85bd0381-6885-408e-9ce3-1610f73c81de.png)<br><br><br>

### Successful Object Identification
This is the visual of the output as a result of the snapshot captured by the Raspberry Pi camera in the first image.<br>

![image](https://user-images.githubusercontent.com/92603066/181683068-0002cd8e-3c2f-44a9-9561-4b0ffad55b4d.png)<br><br><br>
  
## Reference
[1] A. Farhadi, J. Redmon, “Yolo v3: An incremental Improvement,” arXiv [Online]. Available: https://pjreddie.com/darknet/yolo/.
