# Mechatronic Design and Build
This project aims to design a cross-platform app for MDB class

**Installation:**

1. Update your software into the latest Raspbian Image

       pi@raspberrypi ~ $ sudo apt-get update && sudo apt-get -y upgrade

2. Reboot (not required but always good idea to reboot latest upgrades)

       pi@rasberrypi ~ $ reboot

3. Install the dependencies:

       pi@raspberrypi ~ $ sudo apt-get update
       pi@raspberrypi ~ $ wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
       pi@raspberrypi ~ $ sudo python get-pip.py


4. Install [Cython](http://cython.org/), [Pygments](http://pygments.org/), and [docutils](https://pypi.python.org/pypi/docutils) (this step might take quite a few minutes).

       pi@raspberrypi ~ $ sudo pip install cython pygments docutils

5. Download Kivy and install it

       pi@raspberrypi ~ $ git clone https://github.com/kivy/kivy
       pi@raspberrypi ~ $ cd kivy
       pi@raspberrypi ~/kivy $ python setup.py build
       pi@raspberrypi ~/kivy $ sudo python setup.py install

6. Download and install Kivy Garden

       pi@raspberrypi ~ $ pip install kivy-garden

7. Download and install Kivy Garden Packages

       pi@raspberrypi ~ $ garden install circularlayout
       pi@raspberrypi ~ $ garden install circulardatetimepicker
       
8. To enable touch (if you are working with 7" RPi touch screen), you will need to make a modification to the default Kivy configuration file. To create that file, first run an example: 

       pi@raspberrypi ~/kivy $ python ~/kivy/examples/demo/pictures/main.py

9. Quit the example with `Ctrl+C` and then open the newly-created `config.ini` file for editing:

       pi@raspberrypi ~/kivy $ nano ~/.kivy/config.ini

10. Go into the `[input]` section, remove the lines that are in there and put in:

       mouse = mouse
       mtdev_%(name)s = probesysfs,provider=mtdev
       hid_%(name)s = probesysfs,provider=hidinput

11. Launch the multi touch pictures demo. Tap, drag, pinch, and rotate should all work like a dream:

       pi@raspberrypi ~/kivy $ python ~/kivy/examples/demo/pictures/main.py

12. Type `Control+C` to exit the pictures demo.

13. To run the GUI, clone and change your directory into this repository and type: 

       pi@raspberrypi ~/this/repo/ $ python main.py 

