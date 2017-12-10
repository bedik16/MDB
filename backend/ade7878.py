import smbus
import ade7878_reg as reg

class SmartPi:

    address = 0X00
    bus = smbus.SMBus(0)

    def __init__(self,address):
        self.address = address
            
    def set_address(self,new_address):
        self.address = new_address
        
    def resertEnergy(self):
        pass
    def getEnergyUse(self):
        pass
    def getCurrentPower(self):
        pass

    def get_voltage(self):
        volt1 = self.bus.read.read_byte_data(self.address,reg.registers[ 0xC1])
        volt2 = self.bus.read.read_byte_data(self.address,reg.registers[ 0xC3])
        volt3 = self.bus.read.read_byte_data(self.address,reg.registers[ 0xC5])
        return (volt1,volt2,volt3)

    def get_current(self):
        curr1 = self.bus.read.read_byte_data(self.address,reg.registers[ 0xC0])
        curr2 = self.bus.read.read_byte_data(self.address,reg.registers[ 0xC2])
        curr3 = self.bus.read.read_byte_data(self.address,reg.registers[ 0xC4])
        return (curr1,curr3,curr3)

