# YoloV8 Pi 5
 Running Yolo V8 in Raspberry Pi V8 
 - As of 2024, this solution worked for me in running Yolov8 in Raspberry Pi 5.

 ## Install x64 OS in Raspberry Pi
 - [Navigate to the site and install the right lattest OS.][def]

 <img width="587" alt="image" src="https://github.com/AronAyub/Jetson-Nano-OBject-Detection---Yolo-V8/assets/55284959/89e72700-9598-463b-8b32-7b8f2e44ccf6">

## Install OpenCv in your machine.
- For exclusive Python users, use the method 1 below

```
pip3 install opencv-contrib-python
```
or 

```
pip3 install opencv-python
```
- Method 2, for python and c++ installations.

```
# only C++
sudo apt-get install libopencv-dev
# need Python also?
$ sudo apt-get install python3-opencv
```


[def]: https://www.raspberrypi.com/software/operating-systems/