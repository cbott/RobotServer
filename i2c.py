import smbus, time

class I2C(object):
        """An I2C device connected to the RPi"""
        def __init__(self, address=0x04): #0x04 is the default address for an arduino
                self.address = address
                self.bus = smbus.SMBus(1)

                self.response_time = 0 #the time required for the slave to evaluate data

        def writeNumber(self, value):
                self.bus.write_byte(self.address, value)
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
        def setDelay(self, t = 0.04):
                """sets the sleep time
                this delay gives time for the device to respond. Any value < 0.04 will cause the arduino to freeze up.
                A value of 0 can be used if readNumber is not called immediately after writeNumber """
                self.response_time = t