import smbus, time

class I2C(object):
        """An I squared C (I2C) device to communicate with using the RPi"""
        def __init__(self, address=0x04):
                self.address = address
                self.bus = smbus.SMBus(1)
                #the time required for the slave to evaluate data
                self.response_time = 0.04
        def writeNumber(self, value):
                self.bus.write_byte(self.address, value)
                #this delay gives time for the device to respond
                #any value < 0.04 will cause the arduino to freeze up
                #a value of 0 can be used if readNumber is not called immediately after writeNumber
                time.sleep(self.response_time)
                return -1
        def readNumber(self):
                rec = 0
                while not rec:
                        try:
                                number = self.bus.read_byte(self.address)
                                rec = 1
                        except IOError:
                                rec = 0
                return number
        def setNoDelay(self):
                """sets the sleep time to 0. Makes writeNumber() non-blocking"""
                self.response_time = 0
