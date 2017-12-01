import smbus
import ade7878_reg as reg

class SmartPi:

    address = 0X00
    bus = smbus.SMBus(0)

    def __init__(self,address):
        self.address = address
        
    def set_address(Self,new_address):
        Self.address = new_address

    def get_voltage(Self):
        volt1 = Self.bus.read.read_byte_data(Self.address,reg.registers['AVRMS'])
        volt1 = Self.bus.read.read_byte_data(Self.address,reg.registers['BVRMS'])
        volt1 = Self.bus.read.read_byte_data(Self.address,reg.registers['CVRMS'])

    def get_current(Self):
        curr1 = Self.bus.read.read_byte_data(Self.address,reg.registers[''])
        curr1 = Self.bus.read.read_byte_data(Self.address,reg.registers[''])
        curr1 = Self.bus.read.read_byte_data(Self.address,reg.registers[''])

