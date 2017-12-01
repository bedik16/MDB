import nfc
#import ade7878


class Ics:
    nfccontroller = None
    ##smartpicontroller = None
    
    def __init__(self):

        self.nfccontroller = Nfc()
        self.nfccontroller.run()

    