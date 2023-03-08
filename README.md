# webserial
Display data from serial port on a web page


This can be used to display data from serial port (any data such as from IoT devices ESP32, etc.) on a web page.

This has been tested on Ubuntu Linux.

First install dependencies 

`pip3 install serial`

Give permission to dialout group

`sudo usermod -a -G dialout $USER`


Then open two terminals. On first terminal launch readserial.py

`python3 readserial.py`


On another terminal launch 

`python -m SimpleHTTPServer`
