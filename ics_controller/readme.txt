Instalation instructions.

the following packages are needed:

pip3 install -U nfcpy
sudo apt install python3-smbus


reconfigure of raspbian image:
    Run sudo raspi-config.
    Use the down arrow to select 9 Advanced Options
    Arrow down to A7 I2C.
    Select yes when it asks you to enable I2C
    Also select yes when it tasks about automatically loading the kernel module.
    Use the right arrow to select the <Finish> button.
    Select yes when it asks to reboot.

    Do the same for enabling SPI