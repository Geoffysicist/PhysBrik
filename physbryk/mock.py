"""PhysBryk mock module.

Creates mock sensors and services for debugging when no board attached

  Typical usage example:

  try:
    import board
  except ModuleNotFoundError:
    # no board attached so mock sensors etc
    import mock
"""

import random as rn

sensors = []

class Sensor(object):
    """Creates a mock sensor for debugging off the microcontroller.
    """

    def __init__(self, likes_spam=False):
        self.name = "Mock_Sensor"
        self.acceleration = ()
        self.gyro = ()
        self.magnetic = ()
        self.intensity = 0
        self.color_data = ()
        self.proximity = ()
        self.value = 0 # used for he battery sensor
        
        self.update()

        sensors.append(self)

    def update(self):
        """updates all the sensor values
        """
        self.acceleration = (rn.randrange(16), rn.randrange(16), rn.randrange(16))
        self.gyro = (rn.randrange(255), rn.randrange(255), rn.randrange(255))
        self.magnetic = (rn.randrange(255), rn.randrange(255), rn.randrange(255))
        self.intensity = rn.randrange(255)
        self.color_data = (rn.randrange(65535), rn.randrange(65535), rn.randrange(65535),rn.randrange(65535))
        self.proximity = rn.randrange(100)
        self.value = rn.randrange(65535)

class Service(object):
    """Creates a mock service for debugging off the microcontroller.
    """

    def __init__(self):
        self.name = "Mock_Service"
        self.connected = False
        self.measurement_period = 1000
        self.acceleration = ()
        self.gyro = ()
        self.magnetic = ()
        self.intensity = 0.0
        self.color_data = ()
        # self.spectrum = ()
        self.proximity = ()
        self.value = 0
        self.update()

    def update(self):
        """updates all the service values
        """
        pass
  
    def start_advertising(self, adv):
        """mock method
        """
        self.connected = True
  
    def stop_advertising(self):
        """mock method
        """
        
    @classmethod 
    def get_voltage(cls, battery_sensor):
        """Calculates the voltage from the reading of the on board battery sensor."""
        return (battery_sensor.value * 3.3) / 65536 * 2

    def get_lux(self):
        """Calculate ambient light values"""
        #   This only uses RGB ... how can we integrate clear or calculate lux
        #   based exclusively on clear since this might be more reliable?
        r, g, b, c = self.color_data
        lux = (-0.32466 * r) + (1.57837 * g) + (-0.73191 * b)
        print(f"lux {lux}")
        return lux

    def get_spectrum(self):
        """Return the R G B values as a tuple"""
        r, g, b, c = self.color_data
        return (r, g, b)
