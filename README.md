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

## Create a Memory Swap

SWAP memory is parts of memory from the RAM (Random Access Memory) that enables an operating system to provide more memory to a running application or process than is available in physical random access memory (RAM). So if the physical memory (RAM) is full, we can use SWAP partition for extra memory resources. It is useful if we have low memory on our machine.

- Stop the SWAP
```
sudo dphys-swapfile swapoff
```
- Modify the SWAP size
```
sudo nano /etc/dphys-swapfile
```
- Create and initialize the file 
```
sudo nano /etc/dphys-swapfile
```
- Edit the line in MBs

```
CONF_SWAPSIZE=2048
```
-  Create and initialize the file

```
sudo dphys-swapfile setup
```
- Start the SWAP
```
sudo dphys-swapfile swapon
```


## Install ultralytics.
- [Visit the site below for ultralytics][def2]
- Whenever you deploy ultralytics you will get errors because
- [Official Site](def4)
- Whenever you deploy ultralytics you will get errors because:
    - There are specific requirements for torch and torchvision for the ultralytics to work.
    - The temporary solution below worked for me:
    
    * Please run the command below:

#### Method 1

```
pip uninstall torch torchvision
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.
```
#### Temporary Solution that works as well.
 
 

### Install ultralytics 
```
pip install ultralytics
```

## Test Ultralytics


 - Download these files from the official Ultralytics website. We shall use them for the testing.()

 <img width="512" alt="image" src="https://github.com/AronAyub/Jetson-Nano-OBject-Detection---Yolo-V8/assets/55284959/bc78ab30-c80c-4c68-9e64-7987f868b81c">


## Testing the model

See the results i got:

```
image 1/1 /home/pi/Desktop/objectdetection/image test2.png: 448x640 12 persons, 1 bicycle, 12 cars, 1 bus, 1 truck, 10 traffic lights, 1 handbag, 2782.8ms
Speed: 8.4ms preprocess, 2782.8ms inference, 2.3ms postprocess per image at shape (1, 3, 448, 640)
```



[def]: https://www.raspberrypi.com/software/operating-systems/
[def2]: https://github.com/ultralytics/ultralytics
[def4]: https://github.com/ultralytics/ultralytics/tree/main/examples
