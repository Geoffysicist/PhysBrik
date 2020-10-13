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
        self.spectrum = ()
        self.proximity = ()
        self.update()

        sensors.append(self)

    def update(self):
        """updates all the sensor values
        """
        self.acceleration = (rn.randrange(16), rn.randrange(16), rn.randrange(16))
        self.gyro = (rn.randrange(255), rn.randrange(255), rn.randrange(255))
        self.magnetic = (rn.randrange(255), rn.randrange(255), rn.randrange(255))
        self.color_data = (rn.randrange(255), rn.randrange(255), rn.randrange(255),rn.randrange(255))
        self.proximity = rn.randrange(100)

class Service(object):
    """Creates a mock service for debugging off the microcontroller.
    """

    def __init__(self, likes_spam=False):
        self.name = "Mock_Service"
        self.connected = False
        self.measurement_period = 1000
        self.acceleration = ()
        self.gyro = ()
        self.magnetic = ()
        self.intensity = 0
        self.spectrum = ()
        self.proximity = ()
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
        
  
