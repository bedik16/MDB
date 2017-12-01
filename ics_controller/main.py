from backend.nfc import Nfc
import time

def main():

    #test = Nfc()
    Nfc().start()
    while True:
        print('main')
        time.sleep(1)
       

if __name__ == "__main__":
     main()