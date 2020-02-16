MARS.py
=======

You can download Mars Photos from Curiosity Rover! 

**MARS.py** is a simple tool that lets you download photos.

Usage:
-----

``usage: mars.py [-h] -d DEST -s SOL``

``Download NASA Curiosity Rover Photos``

``optional arguments:``

``  -h, --help            show this help message and exit``

``  -d DEST, --dest DEST  Download Directory``
  
``  -s SOL, --sol SOL     Mars SOL Day(s)``

Examples:
--------
* For only a SOL download:
```shell script
$ python mars.py -d ~/Photos/MARS -s 2000
```
* For multi SOL download:
```shell script
$ python mars.py -d ~/Photos/MARS -s 2000-2001
```
 
[What is SOL?](https://www.giss.nasa.gov/tools/mars24/help/notes.html)