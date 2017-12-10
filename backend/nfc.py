from threading import Thread
import Adafruit_PN532 as PN532
import binascii
import sys
import time

CS = 8 # pin
MOSI = 10 #
MISO = 9 #
SCLK = 11 #

class Nfc(Thread):

    observers = []

    
    def __init__(self):
        Thread.__init__(self)
        self.onNfcPresent = None
        self.pn532 = PN532.PN532(cs = CS, sclk = SCLK, mosi = MOSI,miso = MISO)
        self.pn532.begin()

        self.pn532.SAM_configuration()

    def run(self):

        while True:
            # Check if a card is available to read.
            uid = self.pn532.read_passive_target()
            # Try again if no card is available.
            if uid is None:
                continue
            print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
            self.onNfcPresent(nfc=uid)
            time.sleep(2)

    def setOnNfcPresentCallback(self,theCallback):
        self.onNfcPresent = theCallback

    

    
        
