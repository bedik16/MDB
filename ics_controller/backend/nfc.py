from threading import Thread
import Adafruit_PN532 as PN532
import binascii
import sys
import time

CS = 8
MOSI = 10
MISO = 9
SCLK = 11

class Nfc(Thread,):

    observers = []
    pn532 = None  
    
    def __init__(self):
        Thread.__init__(self)
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
            self._notify()
            time.sleep(2)

            # Authenticate block 4 for reading with default key (0xFFFFFFFFFFFF).
            #if not self.pn532.mifare_classic_authenticate_block(uid, 4, PN532.MIFARE_CMD_AUTH_B,
            #                                            [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]):
            #    print('Failed to authenticate block 4!')
            #    continue
            # Read block 4 data.
            #data = self.pn532.mifare_classic_read_block(4)
            #if data is None:
            #    print('Failed to read block 4!')
            #    continue
            # Note that 16 bytes are returned, so only show the first 4 bytes for the block.
            #print('Read block 4: 0x{0}'.format(binascii.hexlify(data[:4])))


    def attach(self,observer):
        self.observers.append(observer)

    def detach(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def _notify(self,*args,**kwargs):
        print('event')
        for observer in self.observers:
            observer.update(*args,**kwargs)

    
        
