
# Real-Time Object Detection with ESP32-Cam

The primary goal of this project is to explore and develop a real-time object detection system using custom neural networks for object classification and recognition. 
Deep Neural Networks (DNNs) have proven to be highly effective in handling large, highdimensional data by mimicking the parallel processing capabilities of the human brain, making them a natural choice for object detection tasks.


**main.py** is the Python Script with has the ComputerVision Pipeline to receive the Live data from the IoT Device through Wifi.

**Custom Local Server** using *HTTP* the live data is being transmitted to the Host (pc) which is later is pushed on the Object Detection Model to classify and visualize

**IoT Device** the is is primarily based on ESP-32 Cam by expressif. 
* It has built-in Wifi 802.11 Wifi 2.4 GHz.
* Blutooth 5.0.
* An Led for indicator.
* 3.7v 500mAh Li-Po battery.
* BMS for over current and over charge protection.

**Device Working** this device is programmed using Arduino IDE, and the Wifi credentials is hardcoded, so if needed to change the Wifi need to reupload the new code with new credentials.



## Project

This is a Final year project for Computer Science Engineering Students from Dr. M.G.R. Educational and Research Institute.

### Team:

**Tharun Kumar S**

**Subesh N R**

**Trivikraman R**

**CSE 2020 - 2024**
## Research Paper

### Real Time Object Detection Using Deep Learning
Tuijin Jishu/Journal of Propulsion Technology

ISSN: 1001-4055

Vol. 44 No. 6 (2023)

**Link** >> [Research Paper](https://propulsiontechjournal.com/index.php/journal/article/view/4933) 


## Demo

To run the project

```bash
  python main.py
```


## Usage/Examples

Clone the respository
```bash
git clone 
```

[or]

Fork the respository



## License

[MIT](https://choosealicense.com/licenses/mit/)

