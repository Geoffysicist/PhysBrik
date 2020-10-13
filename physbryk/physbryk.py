"""PhysBryk module.

Base uuid for PhysBryk is a0d1839c-0eaa-5b52-bc84-818888dc7dc5

  Typical usage example:

  foo = SampleClass()
  
  bar = foo.public_method(required_variable, optional_variable=42)
"""

# DEBUG = True
# BOARD = True #flag indicating whether attached to a board.
# BASE_UUID = 'a0d1839c-0eaa-5b52-0000-818888dc7dc5'

# try:
#     import board
# except NotImplementedError:
#     # no board attached so mock sensors, services etc
#     import mock as mk
#     print('No valid board. Using mock sensors and services')
#     BOARD = False


# import adafruit_lsm6ds.lsm6ds33

import random as rn

from adafruit_ble_adafruit.adafruit_service import AdafruitServerAdvertisement

from adafruit_ble.characteristics import Characteristic, StructCharacteristic
from adafruit_ble.characteristics.int import Int32Characteristic, Uint32Characteristic
from adafruit_ble.uuid import VendorUUID
from adafruit_ble.services import Service
from adafruit_ble.attributes import Attribute
from adafruit_ble import BLERadio

from adafruit_ble_adafruit.adafruit_service import AdafruitService
# from adafruit_ble_adafruit.accelerometer_service import AccelerometerService

class IMUService(AdafruitService):  # pylint: disable=too-few-public-methods
    """Accelerometer and Gyroscope values."""

    uuid = AdafruitService.adafruit_service_uuid(0x200)
    acceleration = StructCharacteristic(
        "<fff",
        uuid=AdafruitService.adafruit_service_uuid(0x201),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    """Tuple (x, y, z) float acceleration values, in m/s^2"""

    gyro = StructCharacteristic(
        "<fff",
        uuid=AdafruitService.adafruit_service_uuid(0x202),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    """Tuple (x, y, z) float gyroscope values, in rad/s"""
    measurement_period = AdafruitService.measurement_period_charac()
    """Initially 1000ms."""


class PhysBrykService(Service): # does this have to be a service?
    """Common superclass for all PhysBryk board services."""

    @staticmethod
    def physbryk_service_uuid(n):
        """Generate a VendorUUID which fills in a 16-bit value in the standard
        PhysBryk Service UUID: a0d1839c-0eaa-5b52-nnnn-818888dc7dc5.
        """
        # return VendorUUID("ADAF{:04x}-C332-42A8-93BD-25E905756CB8".format(n))
        return VendorUUID('a0d1{:04x}-0eaa-5b52-bc84-818888dc7dc5'.format(n))

    @classmethod
    def measurement_period_charac(cls, msecs=1000):
        """Create a measurement_period Characteristic for use by a subclass."""
        return Int32Characteristic(
            uuid=cls.physbryk_service_uuid(0x0001),
            properties=(Characteristic.READ | Characteristic.WRITE),
            initial_value=msecs,
        )

    @classmethod
    def service_version_charac(cls, version=1):
        """Create a service_version Characteristic for use by a subclass."""
        return Uint32Characteristic(
            uuid=cls.physbryk_service_uuid(0x0002),
            properties=Characteristic.READ,
            write_perm=Attribute.NO_ACCESS,
            initial_value=version,
        )

class DummyService(AdafruitService):  # pylint: disable=too-few-public-methods
    """Accelerometer values."""

    uuid = AdafruitService.adafruit_service_uuid(0x1000)
    value = StructCharacteristic(
        "<fff",
        uuid=AdafruitService.adafruit_service_uuid(0x1001),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    """Tuple (x, y, z) float acceleration values, in m/s^2"""

    measurement_period = AdafruitService.measurement_period_charac()
    """Initially 1000ms."""

class _DummyService(PhysBrykService):  # pylint: disable=too-few-public-methods
    """Random Data values."""

    uuid = PhysBrykService.physbryk_service_uuid(0x1000)
    value = StructCharacteristic(
        "<fff",
        uuid=PhysBrykService.physbryk_service_uuid(0x1001),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    """Tuple (x, y, z) random values between 1 and 100"""

    measurement_period = PhysBrykService.measurement_period_charac()
    """Initially 1000ms."""

class DummySensor(object):
    """Creates a dummy sensor which generates a tuple of 3 random numbers.
    """

    def __init__(self, likes_spam=False):
        self.name = "Dummy_Sensor"
        self.value = ()
        self.update()

    def update(self):
        """updates all the sensor values
        """
        self.value = (rn.randrange(16), rn.randrange(16), rn.randrange(16))

def main():
    DEBUG = True
    BOARD = True #flag indicating whether attached to a board.

    try:
        import board
    except NotImplementedError:
        # no board attached so mock sensors, services etc
        import mock as mk
        print('No valid board. Using mock sensors and services')
        BOARD = False


    import adafruit_lsm6ds.lsm6ds33
    import time

    dummy_sensor = DummySensor()

    if BOARD: #valid board present
        # Accelerometer and gyro
        lsm6ds33 = adafruit_lsm6ds.lsm6ds33.LSM6DS33(board.I2C())
        
        # Create and initialize the available services.
        imu_svc = IMUService()
        dummy_svc = DummyService()
        ble = BLERadio()
        adv = AdafruitServerAdvertisement()

    else: #use mock sensors and services
        
        # Accelerometer and gyro
        lsm6ds33 = mk.Sensor()

        ble = mk.Service()
        imu_svc = mk.Service()
        dummy_svc = mk.Service()
        adv = mk.Service()


    ble.name = "PhysBryk"
    # accel_svc.measurement_period = 100 # millis

    last_update = 0
    measurement_period = 1000


    while True:
        # Advertise when not connected.
        ble.start_advertising(adv)
        if DEBUG: print('Connecting...')
        while not ble.connected:
            pass
        ble.stop_advertising()
        if DEBUG:
                print('Connected!')
        
        while ble.connected:
            now_msecs = time.monotonic_ns() // 1000000  # pylint: disable=no-member

            if now_msecs - last_update >= measurement_period:
                imu_svc.acceleration = lsm6ds33.acceleration
                imu_svc.gyro = lsm6ds33.gyro
                dummy_svc.value = dummy_sensor.value
                dummy_sensor.update()
                last_update = now_msecs

                if DEBUG:
                    print(f'acceleration: {imu_svc.acceleration}')
                    print(f'dummy: {dummy_svc.value}')
                if not BOARD:
                    for s in mk.sensors: s.update()



if __name__ == "__main__":
    main()

