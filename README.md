## MARS.py

You can download Curosity Photos from MARS! 

**MARS.py** is a simple tool that lets you download photos.

### Usage:

>usage: mars.py [-h] -d DEST -s SOL

>Download NASA Curiosity Photos

>optional arguments:
>  -h, --help            show this help message and exit
>  -d DEST, --dest DEST  Download Directory
>  -s SOL, --sol SOL     Mars SOL Day(s)

### Examples:

For only a SOL download:

*$ python2.7 mars.py -d /home/vader/Photos/MARS -s 1800* 

For multi SOL download:

*$ python2.7 mars.py -d /home/vader/Photos/MARS -s 1800-1819*

**What is SOL?** 
[Here](https://www.giss.nasa.gov/tools/mars24/help/notes.html)