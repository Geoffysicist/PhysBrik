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
        self.update()

        sensors.append(self)

    def update(self):
        """updates all the sensor values
        """
        self.acceleration = (rn.randrange(16), rn.randrange(16), rn.randrange(16))

class Service(object):
    """Creates a mock service for debugging off the microcontroller.
    """

    def __init__(self, likes_spam=False):
        self.name = "Mock_Service"
        self.connected = False
        self.measurement_period = 1000
        self.acceleration = ()
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
        
  
